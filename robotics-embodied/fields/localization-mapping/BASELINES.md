# 定位与建图的基线

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md)

## 基线是谁、为什么是它

结论：本方向有两个基线，分别代表两种估计器；后来的系统几乎都以其中之一为对照，或者把两者的部件重新组合。

- **[ORB-SLAM3](../../papers/orb-slam3/reading.md)（2020，优化式关键帧 SLAM）。** 它定义了今天开源 SLAM 的接口：输入单目、双目或 RGB-D 图像，可选 IMU；输出关键帧位姿、稀疏三维点地图，以及 Atlas 中的多张地图；内部是跟踪、局部建图、回环三个线程，后端是关键帧 BA 加 Essential Graph 位姿图。评测方式是 EuRoC、TUM-VI 上的 ATE，单目用 Sim(3) 对齐、其余用 SE(3)。本页表中的后续视觉系统（DROID-SLAM、NICE-SLAM、SplaTAM、MASt3R-SLAM、VGGT-Long 等）都把 ORB-SLAM2 或 ORB-SLAM3 列为对照。
- **[ESKF 教程](../../papers/eskf/reading.md)与 [MSCKF](../../papers/msckf/README.md)（2017 与 2007，滤波式）。** ESKF 定义了 IMU 驱动的误差状态滤波的数学接口：名义状态加 15（或 18）维误差状态，预测 → 更新 → 注入 → 重置；MSCKF 定义了视觉惯性滤波的系统接口：状态只保留滑窗内的相机位姿克隆，特征用完即消去。OpenVINS、EqVIO、PLV-IEKF、学习式 IMU 偏置预测都以 MSCKF 为对照或骨架。

两个基线的分工：滤波把历史压进当前的均值和协方差，适合高频、低延迟的里程计；优化保留多帧状态，能在回环时修正过去。机制的手算见[定位与建图讲义](../localization-mapping.md)第四至九节。

## 基线的结构拆分

把两个基线拆成六个可替换的部件：

1. **前端（观测与数据关联）**：从图像或点云中得到可用于约束的对应关系。基线中是 ORB 特征匹配（ORB-SLAM3）或 KLT/特征轨迹（MSCKF）。
2. **状态与误差参数化**：状态里放什么（位姿、速度、偏置、路标），误差怎样定义（SO(3) 上的局部误差、不变误差）。基线中是 ESKF 的右乘局部误差。
3. **估计器（后端）**：滤波（EKF、MSCKF、迭代 EKF）、滑窗优化，或全局 BA 与位姿图。
4. **地图表示**：稀疏点、面元、TSDF 体素、神经场、3D 高斯、前馈点图子图。
5. **回环、重定位与多地图**：地点识别（DBoW2 词袋）、几何验证、地图焊接。
6. **传感器配置与标定**：单目、双目、RGB-D、IMU、激光雷达、GNSS；内外参与时间偏移是否已知、能否在线估计。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 估计器 | 从每帧更新全部路标的 EKF-SLAM 改为跟踪与建图分线程、关键帧 BA | [PTAM](../../papers/ptam/README.md) | 地图点从 114 个增加到 6600 个，误差标准差 135 mm → 6 mm（同一合成序列）/ 只适合小工作空间，约 150 个关键帧后全局 BA 难以完成，无大回环 |
| 估计器 | 路标不进状态，滑窗内位姿克隆加零空间投影 | [MSCKF](../../papers/msckf/README.md) | 复杂度对特征数线性，3.2 km 终点误差约 0.31% / 无回环，线性化导致不一致 |
| 估计器 | 迭代 EKF 用于激光惯性，原始点直接配准增量 k-d 树地图 | [FAST-LIO2](../../papers/arxiv-2107.06829/README.md) | 比 LIO-SAM 快约 10 倍，ARM 上 10 Hz / 纯里程计，地图超过 2000 m 后精度不再提升 |
| 估计器 | 因子图紧耦合激光、IMU、GPS、回环 | [LIO-SAM](../../papers/arxiv-2007.00258/README.md) | 修 LOAM 的松耦合与回环困难 / 回环只用欧氏距离检测，GPS 只修水平方向 |
| 前端 + 回环 | 跟踪、建图、重定位、回环统一用 ORB 特征；共视图与 Essential Graph | [ORB-SLAM](../../papers/arxiv-1502.00956/README.md) | 大场景、回环、自动初始化，重定位召回远高于 PTAM / 单目尺度漂移，低纹理与高速公路场景失败 |
| 传感器配置 | 加双目与 RGB-D | [ORB-SLAM2](../../papers/arxiv-1610.06475/README.md) | 修单目尺度漂移与纯旋转失败 / 运动模糊下仍跟丢（EuRoC V2_03） |
| 前端 | 直接最小化光度误差，加光度标定 | [DSO](../../papers/arxiv-1607.02565/README.md) | 低纹理下更鲁棒 / 对几何噪声、卷帘快门、内参误差敏感，无回环 |
| 传感器配置 + 估计器 | 单目加 IMU，紧耦合滑窗优化，4 自由度位姿图 | [VINS-Mono](../../papers/arxiv-1708.03852/README.md) | 公制尺度，IMU 撑过短时视觉丢失 / 初始化需要运动激励，剧烈光照与激进运动仍失败 |
| 状态参数化 + 回环 | 最大后验 IMU 初始化，共视关键帧复核回环，Atlas 多地图 | [ORB-SLAM3](../../papers/orb-slam3/reading.md) | 约 2 秒初始化，回环召回提高，跟丢后可焊接地图 / 低纹理与户外远处特征时漂移 |
| 状态参数化 | 把误差状态写清楚：四元数约定、局部与全局误差、注入与重置 | [ESKF 教程](../../papers/eskf/reading.md) | 实现可以逐项核对 / 本身不保证一致性，无实验 |
| 状态参数化 + 标定 | FEJ 一致性处理，在线标定内外参与时间偏移，开源研究平台 | [OpenVINS](../../papers/openvins/README.md) | 坏初值下在线标定保持一致 / 仍需 FEJ 一类修正 |
| 状态参数化 | 用与系统对称性匹配的李群定义误差（等变滤波） | [EqVIO](../../papers/arxiv-2205.01980/README.md) | 去掉偏置后线性化精确，EuRoC 精度与 OpenVINS 持平、每帧耗时约一半 / 偏置使残余线性化误差重新出现 |
| 状态参数化 + 前端 | 右不变 EKF 中融合点、线、消失点 | [PLV-IEKF](../../papers/arxiv-2311.04477/README.md) | 结构化场景（Machine Hall）精度提高 / Vicon 房间序列不如优化式方法 |
| 估计器 | 两级 EKF：先用加速度计修姿态，再做双目 MSCKF 更新 | [DS-VIO](../../papers/arxiv-1905.00684/README.md) | 面向算力受限平台 / 亮度快速变化时双目匹配失败，结果只有图 |
| 前端 → 学习式 | 网络输出带协方差的相对位姿作为 EKF 量测，光度自监督训练 | [自监督可微卡尔曼滤波 VIO](../../papers/arxiv-2203.07207/README.md) | 亮度、模糊、跳帧等退化条件下全部跑通 / 常规序列明显不如 VINS-Mono |
| 状态参数化 → 学习式 | 偏置不进状态，由网络从 IMU 历史预测，保持不变滤波的对称性 | [学习式 IMU 偏置预测](../../papers/arxiv-2505.06748/README.md) | 视觉中断与高速飞行时优于 MSCKF / 部分常规序列 MSCKF 更好 |
| 前端 → 学习式 + 估计器 | 稠密光流式对应加可微稠密 BA | [DROID-SLAM](../../papers/arxiv-2108.10869/README.md) | TUM、EuRoC 上无失败序列 / 实时需两张 RTX 3090，长序列 24 GB 显存 |
| 地图表示 | 单个 MLP 作为唯一地图，在线训练 | [iMAP](../../papers/arxiv-2103.12352/README.md) | 地图约 1 MB、能补全未观测区域 / 只到房间尺度，TUM 精度不如 ORB-SLAM2 |
| 地图表示 | 多分辨率特征网格，局部更新 | [NICE-SLAM](../../papers/arxiv-2112.12130/README.md) | 修 iMAP 的全局更新与大场景失效 / 无回环，受粗网格尺度限制 |
| 地图表示 | 3D 高斯溅射，RGB-D 稠密光度与深度跟踪 | [SplaTAM](../../papers/arxiv-2312.02126/README.md) | 低纹理 ScanNet++ 上远好于 ORB-SLAM3 / 每帧约 2.4 秒，需已知内参与稠密深度 |
| 地图表示 | 3D 高斯溅射用于单目，位姿解析雅可比 | [Gaussian Splatting SLAM](../../papers/arxiv-2312.06741/README.md) | 单目稠密地图、渲染 769 FPS / 约 3 fps，房间尺度，长序列漂移到米级 |
| 前端 → 前馈 3D 先验 | 双视图点图先验做匹配与跟踪，只假设唯一光心 | [MASt3R-SLAM](../../papers/arxiv-2412.12392/README.md) | 免标定，TUM 上优于 DROID-SLAM / 约 15 fps，畸变越大越差，KITTI 长序列跟丢（他人报告） |
| 前端 → 前馈多视图模型 | 一次前馈输出相机、深度与点图 | [VGGT](../../papers/arxiv-2503.11651/README.md) | 一到数百张图秒级重建 / 显存随帧数增长，100 帧约 21 GB |
| 估计器 + 地图表示 | VGGT 子图间 15 自由度单应，SL(4) 因子图 | [VGGT-SLAM](../../papers/arxiv-2505.12549/README.md) | 修不标定时的射影歧义 / 平面场景退化，对外点敏感 |
| 估计器 + 回环 | VGGT 分块、Sim(3) 块间对齐、DINOv2 回环 | [VGGT-Long](../../papers/arxiv-2507.16443/README.md) | 公里级 KITTI 不再显存溢出 / 精度与经典方法相当，反向行驶回环漏检 |
| 估计器 + 回环 | 重叠帧共享位姿与内参，只解标定与尺度；注意力层做回环验证 | [VGGT-SLAM 2.0](../../papers/arxiv-2601.19887/README.md) | 修 v1 的漂移与平面退化，8.4 fps / 白墙场景发散 |
| 传感器配置 + 估计器 | 前馈视觉约束进入公制 SE(3) 因子图，加 IMU 与 GNSS | [MASt3R-Fusion](../../papers/arxiv-2509.20757/README.md) | 公制尺度，大尺度误差远低于纯视觉前馈方法 / 需要 IMU，尚未见正式发表 |
| 前端 + 数据关联 | 前馈 3D 先验加运动物体分割头，剔除动态区域 | [π³ 动态 SLAM](../../papers/arxiv-2512.06868/README.md) | 动态场景误差低于 DROID-SLAM 与 DynaSLAM / 只有 2 fps |
| 前端 + 传感器配置（2026 年补充） | 前馈模型接受可选的内参、位姿、深度输入，输出分解的深度、射线、位姿与公制尺度 | [MapAnything](../../papers/arxiv-2509.13414/README.md) | 一个模型做 SfM、多视图立体、单目深度、定位与深度补全，有公制尺度 / 不建模输入噪声与不确定性，不处理动态 |
| 前端（2026 年补充） | 任意视图的统一几何模型，"深度 + 射线"单一目标 | [Depth Anything 3](../../papers/arxiv-2511.10647/README.md) | 位姿与几何超过 VGGT / 作为模型本身没有回环与长序列机制 |
| 估计器 + 回环（2026 年补充） | DA3-Small 前端 + 分层 Sim(3) 位姿图（局部、跨子图、DBoW2 回环），不做 BA | [AMB3R-SLAM](../../papers/arxiv-2609.19518/README.md) | KITTI 单目 ATE 13.11 m（作者表中 VGGT-SLAM 2.0 为 92.72 m），实时、公里级 / 点云地图有重复表面与重影 |
| （参照）工业界 | CUDA 实现的经典栈：角点 + LK 光流、滑窗稀疏 BA、位姿图与回环，1–32 个相机 | [cuVSLAM](../../papers/arxiv-2506.04359/README.md) | Jetson Orin 上双目每帧 1.8 ms，进入 NVIDIA 人形参考栈 / 多双目需硬件同步，快速运动误差变大 |
| 地图表示（语义层） | 在 SLAM 位姿上叠加语义：surfel、体素、实例 | [SemanticFusion](../../papers/arxiv-1609.05130/README.md)、[Pixel-Voxel](../../papers/doi-10.3390-s18093099/README.md)、[PanopticFusion](../../papers/arxiv-1903.01177/README.md)、[FM-Fusion](../../papers/arxiv-2402.04555/README.md)（[代码仓库卡](../../papers/url-https-github.com-hkust-aerial-robotics-fm-fusion/README.md)） | 地图带上类别与实例 / 依赖外部位姿，详见[感知方向](../perception/BASELINES.md) |

## 批注

**易误读**

- 表中"改进了什么"的数字来自各论文自己的对照，硬件与对齐方式不同，不能跨行比较；单目结果多在 Sim(3) 对齐后计算。
- ESKF 教程不是算法首创，它的价值是把约定与推导写成可核对的形式（见精读"核心想法"）。
- VGGT 一行的显存数字来自 VGGT 原文 H100 上的测量；VGGT-SLAM 引述的"24 GB 约 60 帧"是在 RTX 4090 上。

**与其他论文的关联**

- 部件 2 的演化（局部误差 → 不变误差 → 偏置移出状态）是 [ESKF 精读](../../papers/eskf/reading.md)"局限与后续"一节的展开。
- 部件 1 从 ORB 特征到学习式对应再到前馈点图，对应[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)"从追求不变性走向逐像素"的趋势：SLAM 前端需要的正是逐像素的对应关系。
- 语义层一行与[感知方向的 Baseline 页](../perception/BASELINES.md)共用同一批论文：本页把它们看作地图表示的扩展，感知页把它们看作跨时间融合的方法。

**未核实 / 待验证**

- MSCKF、OpenVINS、PTAM 的会议名来自二手来源；FAST-LIO2、DS-VIO 的正式发表处未核实。
- LIO-SAM、iMAP 的卡片按原文选段核实，未做全文精读。
