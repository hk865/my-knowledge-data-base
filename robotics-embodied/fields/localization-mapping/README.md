# 定位与建图

> 状态：领域入门页 · v1（2026-10-04 追加阶段 5 的 2026 年补充） · 依据 [synthesis.csv](synthesis.csv)（18 行）
>
> 速览：
> 1. 本方向回答机器人"在哪里"和"周围是什么"。做法分三代：滤波式把历史压进当前的均值与协方差；关键帧优化式保留多帧状态，用 BA 和回环让过去的估计也能被修正；学习式与稠密表示让网络提供对应关系或直接给出几何，地图从稀疏点变成可渲染的稠密场。机制与手算见[定位与建图讲义](../localization-mapping.md)。
> 2. 每一代都从上一代的失败出发：EKF-SLAM 的地图只能放一百多个点（PTAM 的对比实验中是 114 个）→ PTAM 与 MSCKF；PTAM 只能在小场景、没有回环 → ORB-SLAM；单目尺度会漂移（ORB-SLAM 在 KITTI 08 无回环时误差 46.58 m）→ 视觉惯性融合；特征法在模糊、卷帘快门、大旋转的 TUM 序列上丢跟踪（ORB-SLAM3 单目 9 条中失败 5 条）→ DROID-SLAM；稀疏地图只够定位 → NeRF 与 3DGS 式稠密 SLAM；需要标定相机 → MASt3R-SLAM。
> 3. `[判断]` 后来的系统大多在旧系统的主场之外取胜，在主场里仍然输：iMAP、NICE-SLAM、SplaTAM、Gaussian Splatting SLAM 都承认在 TUM 常规序列上位姿精度不如 ORB-SLAM2。新系统赢在鲁棒、稠密、免标定，经典系统的精度在常规场景里还没有被取代。
> 4. 2024–2026 年的主线是把前馈 3D 重建模型（DUSt3R、MASt3R、VGGT）当前端，再把经典后端接回来修它的毛病：VGGT 在 24 GB 显卡上只能处理约 60 帧，MASt3R-SLAM 在 KITTI 上约 100 帧后跟丢，单目没有公制尺度；修补手段是子图加位姿图、回环、IMU 与 GNSS 因子。2026 年 9 月的 AMB3R-SLAM 用 Depth Anything 3 做前端、DBoW2 回环加分层位姿图做后端，KITTI 单目平均误差 13.11 m（同表 VGGT-SLAM 2.0 为 92.72 m）；NVIDIA 给人形的参考栈仍用经典特征法的 cuVSLAM。
> 5. `[判断]` 团队押注清楚：Zaragoza 押特征法加完整开源系统，TUM 押直接法，HKUST 与 HKU 押紧耦合多传感器加开源，Imperial（Davison 组）押"一种稠密表示同时用于跟踪和建图"，MIT SPARK 押因子图后端去接新的前端。

本页属于[机器人与具身](../../README.md)领域。定位与建图给[感知](../perception/README.md)提供位姿（把检测结果放进地图需要它），给[导航与规划](../navigation-planning/README.md)提供地图（占据地图怎样从这里来，见讲义第十节）。按部件拆分的基线见 [Baseline 页](BASELINES.md)，学习路线见[路线图](ROADMAP.md)，论文列表见[论文目录](PAPERS.md)。

## 这个领域在解决什么

一台四足机器人在一栋楼里巡检：控制器每秒要上百次知道机身的位姿和速度，规划器要一张标明哪里能走的地图，机器人第二天回来时还要认出这是昨天的走廊，而不是重新建一张图。这就是定位与建图：用相机、IMU（惯性测量单元，测角速度和比力）、激光雷达的读数，同时估计轨迹和环境。

三类做法的直觉：

- **滤波式**：每来一个读数就更新一次当前状态的高斯估计，过去的信息只留在均值和协方差里。省算力、延迟低，但线性化一旦做错就改不回来。卡尔曼滤波、EKF、误差状态滤波（ESKF）见讲义第四至七节，[ESKF 精读](../../papers/eskf/reading.md)给出了 IMU 驱动滤波的完整公式链。
- **优化式（关键帧 SLAM）**：只挑一部分帧作为关键帧（一句话：被永久保留在地图里的帧），把位姿和地图点放进一个大的非线性最小二乘里反复求解；回环时可以修正整段历史。因子图、重投影残差和回环怎样分配误差见讲义第八、九节，[ORB-SLAM3 精读](../../papers/orb-slam3/reading.md)是这条路线的完整系统。
- **学习式与稠密表示**：网络提供传统前端做不好的东西，例如任意像素的对应关系、单张图的深度、甚至两张图之间的整片三维点；地图不再是几千个稀疏点，而是可以渲染出图像的稠密场。

## 主线历史

结论：每个阶段的系统都在修上一阶段暴露的具体失败；失败的场景反复出现五类：低纹理、动态物体、尺度漂移、回环失败、长时运行。下面每个阶段先写留下的问题，再写改变，最后写当时做不好的场景和后来专门修它的工作。

### 1 滤波式：把高维状态压到能实时更新的规模（2007 起）

**留下的问题。** EKF-SLAM 把相机位姿和所有地图点放进同一个状态，协方差随点数平方增长。PTAM 的对比实验给出了这个代价：同一段 600 帧的合成序列上，EKF-SLAM 只维护了 114 个点，每帧耗时从 3 ms 二次增长到 40 ms，位置误差标准差 135 mm；MSCKF 原文也把维护位姿与数千个特征之间的相关性列为 EKF-SLAM 的主要局限。

**改变。** [MSCKF](../../papers/msckf/README.md)（Minnesota，2007）不把特征点放进状态，只保留最近若干个相机位姿的"克隆"；一个特征的轨迹结束后，先三角化，再把残差投影到消掉特征误差的方向上做更新，计算量对特征数是线性的。车载实验中 3.2 km 轨迹的终点误差约 10 m（行驶距离的 0.31%），单核 14 Hz。之后 [OpenVINS](../../papers/openvins/README.md)（Delaware，2020）把带 FEJ（一句话：雅可比固定在第一次估计处计算，避免滤波器获得不该有的信息）的 MSCKF 做成开源研究平台，并在线标定内外参与时间偏移；[FAST-LIO2](../../papers/arxiv-2107.06829/README.md)（HKU，2021）把迭代 EKF 用到激光雷达加 IMU 上，去掉手工特征提取，直接把原始点配准到增量 k-d 树地图上，比 LIO-SAM 快约 10 倍，在 ARM 板上也能 10 Hz 运行。

**做不好的场景。**
- **一致性**：滤波器给出的协方差比实际误差小，即过度自信。[EqVIO](../../papers/arxiv-2205.01980/README.md)（ANU，2022）把原因归为标准 EKF 线性化后的不可观子空间与真实系统不一致，FEJ 一类修正只是补丁；OpenVINS 的仿真显示，初值差又不在线标定时，位置 NEES（一句话：误差平方按协方差归一化后的值，一致时约等于自由度）达到 1045，轨迹误差 508.7 m。
- **低纹理与光照**：MSCKF 原文写明多数特征只能跟踪少数几帧；DS-VIO 在 EuRoC V2_03 上因亮度快速变化导致双目匹配失败；PLV-IEKF 把"只用点特征时无纹理和光照变化下特征太少"作为出发点。
- **回环与长时运行**：MSCKF 原文没有回环；FAST-LIO2 写明地图超过 2000 m 后精度不再提升，因为漂移会让新点误配到旧地图点上。
- **偏置**：误差状态把 IMU 偏置放进状态（见 [ESKF 精读](../../papers/eskf/reading.md)），但偏置的估计依赖运动激励和视觉残差。

**站在现在看。** 两条后续工作专门修滤波器的线性化：[EqVIO](../../papers/arxiv-2205.01980/README.md) 和 [PLV-IEKF](../../papers/arxiv-2311.04477/README.md) 把误差定义换成与系统对称性匹配的不变误差，EqVIO 在 EuRoC 上平均误差与 OpenVINS 持平（0.16 m）、每帧耗时约一半。EqVIO 自己也写明残余的线性化误差与偏置误差成正比；[学习式 IMU 偏置预测](../../papers/arxiv-2505.06748/README.md)（UCSD，2025）于是把偏置拿出状态，用网络从 IMU 历史预测，让不变滤波器保持对称性。`[判断]` 滤波路线二十年里的主题一直是"线性化在哪里出错、怎样不让它出错"，这与优化路线靠反复重新线性化来解决同一问题是两种取舍。

### 2 关键帧优化：把跟踪和建图拆开，再加回环（2007–2017）

**留下的问题。** PTAM 原文点名 MonoSLAM 一类增量系统的问题：跟踪和建图每帧一起更新，数据关联一出错就可能永久毁掉地图，手持相机下鲁棒性不够。

**改变。** [PTAM](../../papers/ptam/README.md)（Oxford，2007）把跟踪和建图放进两个并行线程，建图只处理关键帧，用 BA 批量优化；同一合成序列上地图点从 EKF-SLAM 的 114 个增加到 6600 个，误差标准差从 135 mm 降到 6 mm。[ORB-SLAM](../../papers/arxiv-1502.00956/README.md)（Zaragoza，2015）在 PTAM 的架构上从头重写：跟踪、建图、重定位、回环都用同一种 ORB 特征（一句话：FAST 角点加二进制描述子，算得快、可旋转），用共视图把优化限制在局部，回环后在 Essential Graph（一句话：只保留强共视边、生成树和回环边的稀疏位姿图）上做 7 自由度优化，并自动初始化。TUM RGB-D 的 16 条序列上，PTAM 在 8 条上跟丢；在有人走动的 fr3_walking_xyz 上，ORB-SLAM 的重定位召回率 77.9%，PTAM 为 0。[ORB-SLAM2](../../papers/arxiv-1610.06475/README.md)（2016 年预印本，T-RO 2017）加上双目和 RGB-D。

同期的直接法提供了另一种前端：[DSO](../../papers/arxiv-1607.02565/README.md)（TUM，2016）不提取特征，直接最小化像素亮度误差，并标定曝光、渐晕和相机响应。

**做不好的场景。**
- **低纹理与运动模糊**：PTAM 自述只能在角点检测器触发的地方跟踪，快速运动造成的模糊会让角点消失、跟踪失败；ORB-SLAM 在 TUM 上主动剔除了强旋转、无纹理、无运动的序列，在近处缺少可跟踪物的 KITTI 01 高速公路上无法运行；ORB-SLAM2 在 EuRoC V2_03 因严重运动模糊跟丢。
- **尺度漂移**：单目只能恢复差一个整体比例的轨迹，ORB-SLAM 在没有回环的 KITTI 08 上误差 46.58 m，作者写明尺度漂移得不到修正；ORB-SLAM2 的引言把单目尺度漂移和探索中的纯旋转失败列为加双目的理由。
- **回环失败**：ORB-SLAM 在 NewCollege 中反向经过的大环没有被检出；ORB-SLAM2 在 KITTI 09 末尾只有几帧的回环没有被检出；PTAM 不设计闭合大回环。
- **长时运行与场景变化**：PTAM 的实用上限约 6000 个点、150 个关键帧，超过 100 个关键帧后全局 BA 几乎总被中止；场景被大幅、永久改变时系统失败。
- **特征法与直接法互相的短板**：ORB-SLAM 承认直接法对模糊和低纹理更鲁棒，同时指出直接法怕卷帘快门、自动增益和自动曝光；DSO 承认几何噪声增大时性能迅速恶化、对内参不准更敏感，作者因此认为普通手机和网络摄像头更适合特征法，而它没有回环，只是视觉里程计。

**站在现在看。** `[判断]` 特征法与直接法的竞争主要是在比较口径上进行的：DSO 在自己的 TUM monoVO 数据集上胜过 ORB-SLAM，但关闭了 ORB-SLAM 的回环和重定位；在 EuRoC 上 ORB-SLAM 更准，DSO 归因于没有光度标定和隐式回环；DSO 的 v2 还修正了一个使 ORB-SLAM 实时结果被低估的 bug。ORB-SLAM3 最终的结论（见下一阶段）是精度主要来自数据关联而非前端类型。低纹理这个短板没有被特征法自己解决，后来由 IMU（阶段 3）和学习式稠密对应（阶段 4）分别补上。

### 3 视觉惯性与激光惯性：用 IMU 补尺度和短时丢失（2017–2020）

**留下的问题。** 纯视觉单目没有公制尺度，遇到模糊、无纹理、光照突变会丢跟踪。

**改变。** [VINS-Mono](../../papers/arxiv-1708.03852/README.md)（HKUST，2017）用紧耦合滑窗优化（一句话：IMU 预积分和视觉重投影残差放进同一个最小二乘，窗口外的状态边缘化为先验）融合单目和 IMU，先做纯视觉 SfM 再与 IMU 对齐来初始化尺度、重力、速度和陀螺偏置，回环后在 4 自由度（x、y、z、偏航）上做位姿图优化，因为横滚和俯仰由重力可观。约 700 m 的室内外混合轨迹上，OKVIS 的漂移为 2.36%，VINS-Mono 不开回环为 0.88%。[ORB-SLAM3](../../papers/orb-slam3/reading.md)（Zaragoza，2020）把 ORB-SLAM 的地图复用带进视觉惯性：最大后验式的 IMU 初始化在约 2 秒内给出约 5% 的尺度误差，Atlas 多地图在跟丢后另起新图、重逢时焊接；EuRoC 上单目惯性的精度约为 VINS-Mono 的 2.6 倍。作者的结论是精度主要来自"短期、中期、长期、多地图四类数据关联都用上"，而不是用特征法还是直接法。激光一侧，[LIO-SAM](../../papers/arxiv-2007.00258/README.md)（MIT，2020）用因子图紧耦合激光、IMU、GPS 与回环，修 LOAM 的松耦合和全局体素地图难以加回环的问题。

**做不好的场景。**
- **初始化需要激励**：VINS-Mono 写明尺度可观需要加速度变化，不能从静止开始，初始化"通常是最脆弱的一步"，需要超过 30 个特征且视差超过 20 像素；ORB-SLAM3 写明慢速运动时惯性参数可观性差。
- **远处特征与户外**：ORB-SLAM3 在户外长序列上近处特征少，尺度和加速度计偏置会漂移，误差 10–70 m，复现时要丢弃 20 m 以外的点。
- **剧烈光照与激进运动**：VINS-Mono 自述仍会失败，并且纯旋转时无法三角化。
- **低纹理**：ORB-SLAM3 把它列为主要失败场景，TUM-VI 几乎没有视觉特征的滑梯序列上，用光流跟踪的 VINS-Mono 在部分序列上更准。
- **标定**：VINS-Mono 结论写明大规模部署需要在线标定几乎全部内外参。
- **退化几何**：LIO-SAM 在桥下遇到类似长走廊的位姿退化，回环只实现了基于欧氏距离的朴素版本，GPS 只修水平方向。

**站在现在看。** 学习式工作把"传统 VIO 在剧烈光照、快速运动、低纹理下脆弱"作为出发点：[自监督可微卡尔曼滤波 VIO](../../papers/arxiv-2203.07207/README.md)（Toronto，2022）在加了亮度变化、模糊、噪声和跳帧的 EuRoC 序列上全部跑通，VINS-Mono 在 V103 的跳帧设置下全部失败；代价是在未加扰动的 MH05 上误差 0.93 m，VINS-Mono 为 0.28 m。`[判断]` 这说明学习式前端换来的是退化条件下不丢，而不是常规条件下更准，这个模式在下一阶段反复出现。

### 4 学习式对应与稠密神经地图（2021–2024）

**留下的问题。** 特征轨迹会丢、优化会发散、漂移会累积（DROID-SLAM 引言）；稀疏地图只能用于定位，不能直接给机器人提供表面、空闲空间或可渲染的场景（Gaussian Splatting SLAM 引言）。

**改变。** 两条线同时推进：

- **学习式对应加可微 BA**：[DROID-SLAM](../../papers/arxiv-2108.10869/README.md)（Princeton，2021）在光流网络 RAFT 的基础上迭代更新所有像素的深度和位姿，每一步由一个可微的稠密 BA 层完成，只用合成数据训练。TUM fr1 的 9 条单目序列上，ORB-SLAM2 失败 6 条、ORB-SLAM3 失败 5 条，DROID-SLAM 全部成功；作者把这些序列难的原因写为卷帘快门、运动模糊和大旋转。EuRoC 单目 11 条全部成功，只比较 ORB-SLAM3 成功的序列时误差低 43%。
- **神经场与高斯地图**：[iMAP](../../papers/arxiv-2103.12352/README.md)（Imperial，2021）用一个约 1 MB 的 MLP 作为唯一的地图，在 RGB-D 视频上在线训练（NeRF 式隐式表示，一句话：用网络把三维坐标映射成颜色和占据，再沿光线积分渲染图像）。[NICE-SLAM](../../papers/arxiv-2112.12130/README.md)（浙大、ETH 等，2021 年预印本，CVPR 2022）指出单个 MLP 只能全局更新，在多房间公寓上重建和跟踪都显著变差，改用多分辨率特征网格做局部更新；ScanNet 上轨迹误差 9.63，作者复现的 iMAP 为 36.67。[SplaTAM](../../papers/arxiv-2312.02126/README.md)（CMU，2023）与 [Gaussian Splatting SLAM](../../papers/arxiv-2312.06741/README.md)（Imperial，2023）改用 3D 高斯溅射（3DGS，一句话：用大量带颜色和形状的三维高斯椭球表示场景，用光栅化而非逐光线采样来渲染）。SplaTAM 在低纹理的 ScanNet++ 上误差 1.2 cm，ORB-SLAM3 因缺特征反复重新初始化，误差 158.2 cm。

**做不好的场景。**
- **常规场景的精度**：TUM 上，iMAP（fr1/desk 4.9 cm）、NICE-SLAM（2.7 cm）都不如 ORB-SLAM2（1.6 cm），NICE-SLAM 与 SplaTAM 原文都承认特征法仍更好；Gaussian Splatting SLAM 在 EuRoC 困难长序列 MH03–05 上误差 2.2–4.5 m，ORB-SLAM3 为 0.02–0.09 m。
- **算力与实时**：DROID-SLAM 实时运行需要两张 RTX 3090，长序列需要 24 GB 显存，作者自述资源需求是最大局限；SplaTAM 每帧跟踪约 1 秒、建图约 1.4 秒；Gaussian Splatting SLAM 约 3 fps。
- **回环与规模**：NICE-SLAM 写明没有回环、预测能力受粗网格尺度限制；Gaussian Splatting SLAM 写明只在房间尺度测试，大场景的轨迹漂移不可避免；iMAP 只验证到房间尺度。
- **传感器条件**：SplaTAM 自述对运动模糊、大的深度噪声和激进旋转敏感，并需要已知相机内参和稠密深度。
- **动态物体**：这批论文中只有 NICE-SLAM 做了动态场景实验（Co-Fusion 上 1.6 cm，iMAP 复现为 7.8 cm），其余都没有讨论。

**站在现在看。** Gaussian Splatting SLAM 的补充实验显示，用 ORB-SLAM 的位姿加离线 3DGS 训练，渲染指标与它自己的系统没有显著差别。`[判断]` 在这一阶段，"稠密可渲染地图"和"准确的位姿"可以分开获得；神经地图对定位本身的增益主要在低纹理这类特征法失效的场景，而不在常规场景。

### 5 前馈 3D 重建模型当前端，经典后端兜底（2024–2026）

**留下的问题。** MASt3R-SLAM 的引言写道，SLAM 还不是即插即用的算法，需要硬件经验和标定；单视图深度先验在不同视角之间不一致。

**改变。** DUSt3R（Naver Labs Europe，2023）把双视图重建写成直接回归两张图的三维点图（pointmap，一句话：每个像素对应一个三维点的稠密图），不需要相机标定；VGGT（Oxford 与 Meta，2025）一次前馈从一到数百张图输出相机、深度和点图。SLAM 系统把它们当前端：

| 系统 | 修的是谁的什么问题 | 做法 | 自身的代价 |
|---|---|---|---|
| [MASt3R-SLAM](../../papers/arxiv-2412.12392/README.md)（Imperial，2024） | 经典系统需要标定，单视图先验不一致 | 双视图先验 MASt3R 做匹配，Sim(3)（相似变换：旋转、平移加一个整体尺度）位姿图加检索回环，只假设相机有唯一光心 | 约 15 fps（RTX 4090）；EuRoC 上 0.041 m，输给 DROID-SLAM 的 0.022 m；畸变越大越差 |
| [VGGT-SLAM](../../papers/arxiv-2505.12549/README.md)（MIT，2025） | VGGT 在 24 GB 显卡上只能处理约 60 帧；不标定时子图之间有射影歧义，相似变换对齐不够 | 子图间估计 15 自由度单应，在 SL(4) 上做因子图优化 | 平面场景退化（TUM floor）；对外点敏感 |
| [VGGT-Long](../../papers/arxiv-2507.16443/README.md)（南开、南大，2025） | VGGT、CUT3R、Fast3R 在 KITTI 上显存溢出；MASt3R-SLAM 在 KITTI 约 100 帧后跟丢 | 分块跑 VGGT，块间 Sim(3) 对齐，DINOv2 检索回环 | KITTI 平均误差与经典方法相当而非更好；同一车道反向行驶时回环检测失败 |
| [VGGT-SLAM 2.0](../../papers/arxiv-2601.19887/README.md)（MIT，2026） | 自家 v1 的 15 自由度对齐在回环之间快速漂移、平面退化 | 利用重叠帧共享位姿和内参，只解标定与尺度；用 VGGT 的注意力做回环验证 | 白墙等无纹理场景发散；后端只优化位姿不优化点 |
| [MASt3R-Fusion](../../papers/arxiv-2509.20757/README.md)（武汉大学，2025） | 前馈视觉流水线没有公制尺度，丢掉了概率多传感器融合 | 把 Sim(3) 视觉约束放进公制 SE(3) 因子图，滑窗 VIO 加 GNSS | 需要 IMU；尚未见正式发表 |
| [π³ 动态 SLAM](../../papers/arxiv-2512.06868/README.md)（Bonn，2025） | 动态物体破坏位姿估计；离线方法 MegaSaM 在 16 GB 显存上处理不完整序列 | 在前馈模型上加运动物体分割头，剔除动态区域后做 BA | 每帧都要多帧前馈推理，RTX 5000 上只有 2 fps |
| [MapAnything](../../papers/arxiv-2509.13414/README.md)（Meta Reality Labs、CMU，2025；补充） | VGGT 一类只吃图像、没有公制尺度；机器人已有的内参、位姿、深度用不上 | 可选输入内参、位姿、深度或部分重建，输出分解的深度、射线、位姿与全局公制尺度 | 不建模输入的噪声与不确定性；不处理动态；逐像素对应限制大场景 |
| [Depth Anything 3](../../papers/arxiv-2511.10647/README.md)（ByteDance Seed，2025；补充） | 单目深度、多视图几何、位姿各用一种模型 | 普通 DINO 编码器 + "深度 + 射线"单一目标，任意视图、有无位姿；摘要称位姿精度平均比 VGGT 高 44.3% | 没有局限一节；动态场景留作未来 |
| [AMB3R-SLAM](../../papers/arxiv-2609.19518/README.md)（UCL，2026-09；补充） | 前馈 SLAM 在 KITTI 长序列上误差大、撑不住公里级 | 80M 的 DA3-Small 做前端，分层 Sim(3) 位姿图（子图内、跨子图、DBoW2 回环），不做 BA；可接双目、RGB-D、激光雷达 | 点云地图有重复表面与重影；RTX 4090 上单目 17.6 fps、峰值显存 10–14 GB |

另一条线把学习放进滤波器而不是替换它：[学习式 IMU 偏置预测](../../papers/arxiv-2505.06748/README.md)让不变 MSCKF 在视觉中断 1–4 秒时仍优于原版 MSCKF。

**站在现在看。** `[判断]` 这一阶段重演了阶段 4 的模式：新前端免标定、对低纹理更宽容，但长序列、回环、尺度、动态物体仍要靠子图、位姿图、因子图这些经典后端兜底；而在 KITTI-360 这类大尺度序列上，MASt3R-Fusion 报告纯视觉的 VGGT-Long 误差为轨迹长度的 2.91%，ORB-SLAM3 为 0.63%。前馈模型目前替换的是前端，没有替换后端。

**2026 年的补充。** `[判断]` 最新的 AMB3R-SLAM（2026-09）直接印证了上面的判断：它在 KITTI 单目上平均 ATE 13.11 m，作者表中 VGGT-SLAM 2.0 为 92.72 m、MASt3R-SLAM 为 186.64 m，而它的公里级能力来自 DBoW2 回环加分层 Sim(3) 位姿图这一经典后端，后端只优化位姿、不优化点。前端本身则在合并：Depth Anything 3 一个模型同时给深度与位姿，MapAnything 把内参、位姿、深度这些机器人本来就有的量作为可选输入，直接输出公制尺度。工业一侧，NVIDIA 给人形的参考栈（GR00T N1.6，2026-01）用的是 [cuVSLAM](../../papers/arxiv-2506.04359/README.md)：角点加 LK 光流、滑窗稀疏 BA、位姿图与回环，Jetson Orin 上双目每帧 1.8 ms；作者表中 EuRoC、KITTI 上的相对平移误差略低于 ORB-SLAM3。产品选的仍是经典特征法，前馈 3D 模型还停留在研究一侧。

## 站在现在看过去：五类失败场景的接力

结论：五类场景没有一类被某一代系统彻底解决，后续工作只是把失败的条件推得更苛刻。

| 场景 | 哪一代做不好（原文证据） | 后来谁专门修、怎样修 | 还剩什么 |
|---|---|---|---|
| 低纹理、模糊、光照突变 | PTAM 只在角点处跟踪；ORB-SLAM 剔除无纹理序列；ORB-SLAM3 单目在 TUM fr1 失败 5/9；DS-VIO 亮度突变时匹配失败 | VINS-Mono 用 IMU 撑过短时丢失；DROID-SLAM 用学习式稠密对应；SplaTAM 在低纹理 ScanNet++ 上 1.2 cm | VGGT-SLAM 2.0 在白墙场景发散；SplaTAM 怕模糊和激进旋转 |
| 动态物体 | MSCKF 靠马氏距离检验剔除车和行人；ORB-SLAM 指出 LSD-SLAM 对动态物体更不鲁棒 | π³ 动态 SLAM 用运动分割头，在 Bonn 动态数据集上 2.20 cm（DROID-SLAM 4.91 cm） | 只有 2 fps；多数稠密神经 SLAM 没有讨论动态场景 |
| 尺度漂移 | 单目 ORB-SLAM 在 KITTI 08 误差 46.58 m | ORB-SLAM2 加双目；VINS-Mono、ORB-SLAM3 加 IMU；MASt3R-Fusion 给前馈前端加 IMU 与 GNSS | IMU 初始化需要运动激励；户外远处特征少时尺度仍漂（ORB-SLAM3 10–70 m） |
| 回环失败 | PTAM 不闭大环；ORB-SLAM 漏检反向大环；DBoW2 词袋检索的召回只有 30–40%（ORB-SLAM3 引言） | ORB-SLAM3 用共视关键帧复核提高召回；VGGT-SLAM 2.0 用模型注意力验证回环 | VGGT-Long 反向行驶漏检；NICE-SLAM、Gaussian Splatting SLAM 没有回环 |
| 长时运行与大场景 | PTAM 约 150 个关键帧上限；FAST-LIO2 地图超过 2000 m 不再提升；VGGT 约 60 帧显存上限 | ORB-SLAM3 的 Atlas 多地图；VGGT-Long 分块；MASt3R-Fusion 8 GB 显存处理任意长序列 | 场景随时间改变（PTAM 自述失败）在本页论文中都没有系统评测 |

`[判断]` 跨领域的共性：大模型做前端、经典优化做后端的分工，和 [VLA 方向](../vla/README.md)里"预训练模型给语义、动作头或控制器保证精度"的分工是同一种结构；新表示带来的泛化与旧系统在主场里的精度长期并存，这和[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)中"线性评测与微调排名翻转"一样，结论取决于在哪个协议下比较。

## 技术地基

- **卡尔曼滤波、EKF 与误差状态滤波**：滤波路线的全部机制。讲义第四至七节；[ESKF 精读](../../papers/eskf/reading.md)补齐四元数约定、离散化和重置。
- **因子图、BA 与回环**：优化路线的统一语言，每条测量是一个因子。讲义第八、九节；规范自由度（整体平移、旋转、单目尺度不可观）见讲义 9.1 节。
- **IMU 预积分与尺度可观性**：把两关键帧间几百个 IMU 读数汇总成一个约束；单目尺度只有在加速度变化时才能由 IMU 定出，手算见 [ORB-SLAM3 精读](../../papers/orb-slam3/reading.md)"三步初始化"一节。
- **地点识别**：用词袋（DBoW2，把特征量化成视觉单词再按词频检索）或网络特征（DINOv2）找"以前来过的地方"，是回环和多地图的入口。
- **稠密表示**：TSDF（截断符号距离场，每个体素存到最近表面的距离）、NeRF 式神经场、3D 高斯溅射、点图。三者的取舍是内存、渲染速度与能否局部更新；视觉编码器本身怎样训练见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。
- **占据地图**：导航需要的是"哪里能走"，讲义第十节，接到[导航与规划](../navigation-planning/README.md)。

## 主要路线与团队偏好

| 团队 | `[判断]` 押注 | 代表 | 代价与做不好的地方 |
|---|---|---|---|
| Universidad de Zaragoza（Tardós、Montiel） | 特征法、多线程关键帧优化、完整开源系统；把精度归因于数据关联 | ORB-SLAM、ORB-SLAM2、ORB-SLAM3 | 低纹理、模糊下丢跟踪；稀疏地图不能直接用于导航与渲染 |
| TU Munich（Cremers） | 直接法，用全部有梯度的像素并做光度标定 | DSO | 对几何噪声、卷帘快门、内参误差敏感；没有回环 |
| HKUST（沈劭劼）与 HKU（张富） | 紧耦合多传感器（视觉惯性、激光惯性），面向无人机与机载算力，代码开源 | VINS-Mono、FAST-LIO2；感知侧的 FM-Fusion | VINS-Mono 初始化依赖激励；FAST-LIO2 无回环 |
| Imperial College（Davison 组） | 一种稠密表示同时用于跟踪与建图，从语义 surfel、神经场、高斯到 3D 重建先验 | SemanticFusion、iMAP、Gaussian Splatting SLAM、MASt3R-SLAM | 房间尺度、实时性不足；常规序列上位姿精度不如特征法 |
| Minnesota、Delaware（Roumeliotis、黄国权） | 滤波式 VIO 的一致性与在线标定 | MSCKF、OpenVINS | 线性化与不一致需要 FEJ 等修正 |
| MIT SPARK（Carlone） | 因子图与流形上的优化做后端，换上新前端 | VGGT-SLAM、VGGT-SLAM 2.0 | v1 的 SL(4) 对齐漂移与平面退化，由 2.0 自己修正 |
| NVIDIA（2026 年补充，工业界） | 经典特征法用 CUDA 实现，面向边缘设备与多相机，作为自家人形参考栈的一部分 | cuVSLAM | 快速六自由度运动误差变大；多双目要硬件同步 |
| UCL（Agapito）、Meta Reality Labs 与 CMU、ByteDance Seed（2025–2026 年补充） | 分别押注：前馈前端 + 分层位姿图后端（AMB3R-SLAM）；接受可选几何输入的公制前馈模型（MapAnything）；统一深度与位姿的几何模型（Depth Anything 3） | AMB3R-SLAM、MapAnything、Depth Anything 3 | 各只有一篇，写的是该论文的选择 |

`[判断]` 收敛与分化：2020 年以后的开源系统几乎都是"前端 + 关键帧 + 位姿图或因子图 + 回环"的结构，滤波与优化之争收敛成"滤波做高频里程计、优化做全局一致"的分工（ORB-SLAM3 与 VINS-Mono 都把回环交给单独的位姿图，FAST-LIO2 只做里程计）；分化在前端：特征点、稠密光度、学习式对应、前馈点图四种并存，各自守住不同的失败场景。

## 用什么衡量进展

结论：评测从"轨迹误差"扩展到"能否跑完"和"地图能否渲染"，每次 benchmark 的替换都对应目标的迁移。

- **轨迹精度**：ATE（绝对轨迹误差，先对齐再算位置差的均方根）与 RPE（相对位姿误差，衡量短时漂移）。单目结果在允许尺度对齐的 Sim(3) 下计算，数值小不说明在线输出有准确尺度（见 [ORB-SLAM3 精读](../../papers/orb-slam3/reading.md)批注）。
- **数据集的迁移**：TUM RGB-D 与 KITTI（2012 前后，室内手持与车载）→ EuRoC（2016，无人机视觉惯性）→ TUM-VI 与 TUM monoVO（鱼眼、光度标定）→ TartanAir（合成的困难运动，DROID-SLAM 用它训练和评测）→ Replica、ScanNet、ScanNet++（2019 起，稠密重建与渲染质量 PSNR）→ KITTI 长序列重新成为前馈模型的考题（VGGT-Long）。`[判断]` 稠密神经 SLAM 把评测移到 Replica 一类渲染场景，主要比较重建与渲染；前馈模型又把评测拉回 KITTI 长序列，因为它们最大的问题是规模。
- **失败次数**：DROID-SLAM 报告各系统在每条序列上是否失败，失败比平均误差更能区分鲁棒性；只算成功序列的平均会掩盖失败（ORB-SLAM3 精读批注中的星号平均）。
- **算力与延迟**：报告必须写硬件，CPU 上几十毫秒（ORB-SLAM3 跟踪约 33 ms）与两张 RTX 3090（DROID-SLAM）不是同一类可部署性。
- **口径问题**：对照数字常取自对方论文而非重跑（ORB-SLAM2 对 Stereo LSD-SLAM）；ORB-SLAM2 补偿了 TUM fr2 深度 4% 的尺度偏差，作者承认这可能部分解释了它更好的结果；DSO v1 曾低估 ORB-SLAM 的实时结果。

## 当前开放问题

- **前馈 3D 模型能否接管后端，而不只是前端？** 目前各系统仍靠子图对齐、位姿图和回环兜底，后端只优化位姿不优化点。入口：[VGGT-SLAM 2.0](../../papers/arxiv-2601.19887/README.md)、[VGGT-Long](../../papers/arxiv-2507.16443/README.md)、[MASt3R-SLAM](../../papers/arxiv-2412.12392/README.md)。
- **学习式组件怎样进入概率估计器而不破坏一致性？** 网络输出需要可信的协方差，滤波器需要保持对称性。入口：[自监督可微卡尔曼滤波 VIO](../../papers/arxiv-2203.07207/README.md)、[学习式 IMU 偏置预测](../../papers/arxiv-2505.06748/README.md)、[MASt3R-Fusion](../../papers/arxiv-2509.20757/README.md)。
- **动态与变化的环境。** 动态物体的处理刚开始与前馈模型结合，速度只有 2 fps；场景在几天、几个季节里的变化在本页论文中都没有系统评测。入口：[π³ 动态 SLAM](../../papers/arxiv-2512.06868/README.md)、[ORB-SLAM3](../../papers/orb-slam3/reading.md) 的 Atlas。
- **地图给谁用。** 稀疏点给定位，稠密场给渲染，导航要占据，操作要物体与语义；语义地图见[感知方向](../perception/README.md)，占据地图见[导航与规划](../navigation-planning/README.md)。
- **（2026 年补充）前馈前端怎样吃进机器人已有的几何量与不确定性？** MapAnything 能吃内参、位姿、深度，但不建模它们的噪声；MASt3R-Fusion 走后端因子图的路。入口：[MapAnything](../../papers/arxiv-2509.13414/README.md)、[MASt3R-Fusion](../../papers/arxiv-2509.20757/README.md)、[AMB3R-SLAM](../../papers/arxiv-2609.19518/README.md)。

## 阅读顺序

1. [定位与建图讲义](../localization-mapping.md)第四至九节：滤波、因子图和回环的最小算例，后面所有系统都是这些部件的组合。
2. [ESKF 精读](../../papers/eskf/reading.md)：滤波路线的数学底座，重点是误差状态、注入与重置，以及噪声离散化怎样让滤波器过度自信。
3. [ORB-SLAM3 精读](../../papers/orb-slam3/reading.md)：优化路线的完整系统，先读"四类数据关联"和 IMU 初始化，再回头对照 [PTAM](../../papers/ptam/README.md) 与 [ORB-SLAM](../../papers/arxiv-1502.00956/README.md) 看它继承了什么。
4. [VINS-Mono](../../papers/arxiv-1708.03852/README.md) 与 [EqVIO](../../papers/arxiv-2205.01980/README.md)：视觉惯性的优化与滤波两种实现，对照它们各自怎样处理线性化与初始化。
5. [DROID-SLAM](../../papers/arxiv-2108.10869/README.md) → [SplaTAM](../../papers/arxiv-2312.02126/README.md)：学习式对应与稠密地图，重点看它们在哪些序列上赢、在哪些序列上输给 ORB-SLAM。
6. [MASt3R-SLAM](../../papers/arxiv-2412.12392/README.md) → [VGGT-SLAM 2.0](../../papers/arxiv-2601.19887/README.md)：当前的前馈前端路线，对照阶段 5 的表格看每一篇修的是谁。
7. （2026 年补充）[AMB3R-SLAM](../../papers/arxiv-2609.19518/README.md) 对照 [cuVSLAM](../../papers/arxiv-2506.04359/README.md)：研究一侧的前馈前端加经典后端，与产品一侧的纯经典栈。

### 已有滤波与优化基础后，近期阅读优先级

- **必读：[MASt3R-Fusion](../../papers/arxiv-2509.20757/README.md)（2025）**。从 VINS-Mono 接过去，核心是把学习式几何约束放进带 IMU/GNSS 的概率后端，直接复用你已有的估计基础；关注尺度与噪声进入哪一层。
- **必读：[AMB3R-SLAM](../../papers/arxiv-2609.19518/README.md)（2026-09）**。从 ORB-SLAM3 的回环接过去，看分层位姿图为何能托住前馈重建的长序列；阅读重点是后端消融与地图重影的边界。
- **选读：[VGGT-SLAM 2.0](../../papers/arxiv-2601.19887/README.md)（2026）**。先了解 v1 的对齐自由度，再读本篇怎样缩减歧义与验证回环，适合研究未知内参输入。
- **部署对照：[cuVSLAM](../../papers/arxiv-2506.04359/README.md)（2025）**。保留经典特征栈作工程参照，比较传感器同步、硬件和延迟，不按论文年份直接判定替换关系。

## 批注

**易误读**

- PTAM 与 EKF-SLAM 的 114 点对 6600 点、135 mm 对 6 mm，出自 PTAM 自己在一段 600 帧合成序列上的对比，EKF-SLAM 用的是 SceneLib 实现（PTAM §7.3）。
- DROID-SLAM 的"失败 5/9"是 ORB-SLAM3 在 TUM fr1 上只用单目输入的结果（DROID-SLAM Tab.4）；ORB-SLAM3 的 RGB-D 或惯性配置不在这张表里。
- SplaTAM 在 ScanNet++ 上 ORB-SLAM3 的 158.2 cm 是 RGB-D 配置，作者归因于低纹理导致的反复重新初始化（SplaTAM Tab.1）；在原始 ScanNet 上，所有稠密方法误差都在 10 cm 以上。
- SplaTAM 摘要中的"400 FPS"是渲染速度，不是 SLAM 的处理速度（Tab.6）。
- VGGT-Long 的 KITTI 结果：全序列平均 26.358 m，与 DPV-SLAM++ 的 25.749 m 相当；去掉 Seq 01 后为 19.298 m，带回环的 ORB-SLAM2 为 9.464 m（VGGT-Long Table 1）。
- MASt3R-Fusion 的 0.05% 对 ORB-SLAM3 0.63% 是 KITTI-360 上按轨迹长度归一化的全局误差，且 MASt3R-Fusion 用了 IMU 与回环（Table II）；它尚未见正式发表。
- VINS-Mono 的 arXiv 版本在 EuRoC 上只用 MH_03、MH_05 两条序列与 OKVIS 做图形比较，结论是纯 VIO 精度相近；"ORB-SLAM3 约为 VINS-Mono 的 2.6 倍"出自 ORB-SLAM3 的表 II。
- MSCKF 的 0.31% 没有 GPS 真值，终点误差由地图和起止停车位推算（MSCKF §IV）。
- AMB3R-SLAM 的 13.11 m 与 VGGT-Long 表中 ORB-SLAM2 的 9.464 m 来自不同论文、不同序列子集与对齐方式，不能直接相减；AMB3R-SLAM 主表没有列 ORB-SLAM 系对照。
- cuVSLAM 与 ORB-SLAM3 的比较是相对平移误差（%），出自 cuVSLAM 自己的表；Depth Anything 3 的 44.3% 取自摘要，正文位姿一节写 35.7%。

**判断的支撑论文**

- "新系统在主场之外取胜、在主场里输"：iMAP Tab.3、NICE-SLAM Tab.2、SplaTAM Tab.1、Gaussian Splatting SLAM Tab.1 与补充 Tab.14、MASt3R-SLAM 补充 §12（EuRoC 输给 DROID-SLAM）、自监督可微 KF Table I–II。反例：DROID-SLAM 在 EuRoC 双目上平均 0.024 m，ORB-SLAM3 为 0.084 m，常规序列上也更准，代价是两张 RTX 3090。
- "前馈模型替换前端、没有替换后端"：MASt3R-SLAM、VGGT-SLAM、VGGT-Long、VGGT-SLAM 2.0、MASt3R-Fusion 都保留了位姿图或因子图与回环。边界：VGGT-SLAM 2.0 已用模型的注意力层做回环验证，后端开始吸收网络的信号。2026 年补充：AMB3R-SLAM（DBoW2 回环 + 分层 Sim(3) 位姿图）是到目前为止最强的支撑；MapAnything 把位姿作为前馈模型的输入，是"前端吸收后端信息"的反方向尝试。
- "产品仍选经典特征法"：cuVSLAM 原文与 GR00T N1.6 技术博客（定位栈为 cuVSLAM、cuVGL、FoundationStereo、nvblox）。边界：只有 NVIDIA 一家的材料；其他公司的定位栈未公开。
- 团队偏好按"同一团队在两篇以上论文中、存在替代方案时重复同一选择"判断：Zaragoza 在 ORB-SLAM、ORB-SLAM2、ORB-SLAM3 中都用 ORB 特征并开源，同期已有直接法 LSD-SLAM 与 DSO；Imperial Davison 组在 SemanticFusion（ElasticFusion surfel）、iMAP（MLP）、Gaussian Splatting SLAM（3DGS）、MASt3R-SLAM（点图）中都让一种稠密表示同时承担跟踪与建图；HKUST 在 VINS-Mono 与 FM-Fusion 中都开源完整系统；MIT SPARK 在 VGGT-SLAM 两个版本中都以因子图后端接 VGGT。只有一篇的团队（TUM 的 DSO、HKU 的 FAST-LIO2、Minnesota 与 Delaware 各一篇）写的是该论文的选择，证据偏弱。
- "滤波做里程计、优化做全局"：ORB-SLAM3 §V–VI、VINS-Mono §VIII、FAST-LIO2 §VI-C。反例：OpenVINS 在滤波框架内维护 SLAM 路标。
- 跨领域共性（前端换大模型、后端保留精确模块）：与 [OpenVLA 精读](../../papers/openvla/reading.md)中 Diffusion Policy 在窄任务上胜过 VLA 的现象对照，属于类比，没有直接实验证据。

**与其他论文的关联**

- [ESKF 精读](../../papers/eskf/reading.md)的局部误差定义，是 EqVIO 与 PLV-IEKF 要替换的那一步；ORB-SLAM3 精读的 IMU 初始化手算解释了 VINS-Mono 为什么需要运动激励。
- [SemanticFusion](../../papers/arxiv-1609.05130/README.md) 与 [PanopticFusion](../../papers/arxiv-1903.01177/README.md) 把本方向的位姿当作输入，在几何地图上叠加语义，见[感知方向](../perception/README.md)；PanopticFusion 把长期位姿漂移列为未来工作。
- DINOv2 在 VGGT-Long 中做回环检索，与[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)"冻结特征直接用于检索与对应"的趋势一致。
- [Learning robust perceptive locomotion](../../papers/arxiv-2201.08117/README.md) 写明打滑和可变形地面造成里程计漂移、使高程图不准：定位误差直接变成控制的输入误差，见[感知方向](../perception/README.md)。

**未核实 / 待验证**

- MSCKF 与 OpenVINS 的会议名（ICRA 2007、ICRA 2020）来自其他论文的参考文献；PTAM 的 ISMAR 2007 来自作者主页。FAST-LIO2 的正式发表处未核实。
- DSO 的数值对比只有累积误差曲线，本页只引用作者的文字结论；VINS-Mono 正式版（T-RO 2018）是否有 EuRoC 全序列表未查。
- DUSt3R 与 VGGT 只核实了题名、团队、方法一句话与局限；π³ 原文只核实了元数据，未引用其结果。
- 开放词汇的 3D 场景图建图（ConceptGraphs、HOV-SG、Clio 等）与终身建图没有在本轮核实，阶段 5 没有写这一支。
- MASt3R-Fusion 的 Table I、Table III 的列对应只经过一次抽取，本页未引用这两张表。
- π³（arXiv:2507.13347）、AMB3R（arXiv:2511.20343）、LASER、Scal3R、VGGT-GS SLAM 等 2025–2026 年的前馈重建与 SLAM 工作只看到检索结果，未打开原文，未收录。
- MapAnything 与 VGGT、π³ 的逐项数值只经过一次 HTML 抽取，本页只写趋势。
