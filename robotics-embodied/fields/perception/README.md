# 机器人感知

> 状态：领域入门页 · v1 · 依据 [synthesis.csv](synthesis.csv)（14 篇）
>
> 速览：
> 1. 本方向研究机器人上的感知任务：检测、分割、深度、多传感器融合，以及怎样把它们的输出变成控制和规划能用的、带时间和不确定性的环境估计。视觉编码器本身怎样训练、怎样评价，在[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)；本页只在它被机器人使用时讨论它。
> 2. 主线是五步，每一步修上一步在部署中暴露的问题：单帧检测与分割做到视频速率 → 用 SLAM 位姿把逐帧预测融合进 3D 地图（修帧间不一致）→ 深度与激光雷达检测（修单目无几何）→ 多传感器在统一的鸟瞰空间里融合（修单一传感器各自的失效）→ 开放词汇基础模型（修固定类别与换场景就掉点）。
> 3. 部署约束常常比精度更决定方案：SemanticFusion 每 10 帧才跑一次 CNN，才能到 25 Hz；PanopticFusion 的瓶颈是 Mask R-CNN，吞吐 4.3 Hz；接上 SAM、Grounding DINO 的 FM-Fusion 每帧约 1 秒；ConceptFusion 提取一张图的开放词汇特征要 10–15 秒。这些语义地图系统的评测都用数据集给的相机位姿。
> 4. `[判断]` 感知误差无法在感知模块内消除，腿足机器人一侧给出两种处理：ETH 在训练中给高程图注入漂移、偏移和失效噪声，让策略学会何时不信外感知；CMU 与 Berkeley 干脆不建高程图，直接从深度图到关节角。
> 5. `[判断]` 基础模型把"类别是固定的"换成了"速度与一致性不够"：同一物体在不同视角下得到不一致的掩码（FM-Fusion），透明物体的深度在真实标注中本身就是错的（Depth Anything V2 因此改用合成标注）。

本页属于[机器人与具身](../../README.md)领域。感知需要的位姿来自[定位与建图](../localization-mapping/README.md)，它输出的物体与地图交给[导航与规划](../navigation-planning/README.md)、[具身 Agent](../embodied-agents/README.md) 和[运动控制](../control-locomotion/README.md)。从像素到地图系物体记录的机制、手算和排错清单见[感知讲义](../perception.md)，本页不重复。按部件拆分的基线见 [Baseline 页](BASELINES.md)，学习路线见[路线图](ROADMAP.md)，论文列表见[论文目录](PAPERS.md)。

## 与视觉表征方向的分工

结论：视觉表征方向问"编码器学到了什么、好不好"，本方向问"机器人在给定的传感器、算力和时限下能得到什么环境信息、错在哪里"。

| | 视觉表征方向 | 本方向（机器人感知） |
|---|---|---|
| 研究对象 | 编码器的输出 z = f(x) 本身 | 机器人上的感知任务：检测、分割、深度、跨时间与跨传感器融合 |
| 好坏由谁定义 | 下游任务与评测协议（线性评测、微调、零样本），没有专属 benchmark | 任务指标（COCO AP：预测框按与真值的重叠度判对后的平均精度；mIoU：各类别预测区域与真值交并比的平均；nuScenes NDS 见阶段 3）加部署约束：帧率、延迟、硬件 |
| 关心的误差 | 表征偏向哪些性质（不变性、局部性、语义） | 标定与时间同步误差、传感器噪声（反光、透明、低光、雨雾）、位姿漂移、帧间不一致 |
| 输入 | 单张 RGB 图（或视频） | RGB、深度、激光雷达、雷达、IMU 与本体状态，带时间戳和坐标系 |
| 输出 | 特征向量或特征图 | 带坐标系、时间、协方差和有效条件的对象记录或地图 |
| 同一篇论文的不同读法 | DINOv2 冻结特征的深度估计说明表征含有几何信息 | Depth Anything V2 用 DINOv2 编码器，本页关心它在透明物体上的误差和 60–213 ms 的延迟 |

两页的组织方式因此不同：视觉表征没有专属 benchmark，那一页先界定对象、讲清怎样测量，再讲历史；机器人感知的检测、分割、深度、3D 检测都有公认的数据集与指标，本页直接从任务出发讲历史。

## 这个领域在解决什么

用户对一台移动操作机器人说"把桌上的杯子拿给我"。感知要在约 100 ms 内回答：图里哪里有杯子（检测与分割），它离相机多远（深度），它在机械臂基座坐标系里的哪一点（标定与坐标变换），上一帧看到的是不是同一只杯子（跨时间关联），相机看不清时激光雷达或之前建的地图能否补上（跨传感器融合）。这条链在[感知讲义](../perception.md)第一至九节逐步手算过一遍。

做法有三类，它们的直觉不同：

- **逐帧预测**：每张图独立跑一个网络，输出框、掩码或深度。简单、可并行，但相邻帧的结果可以互相矛盾。
- **跨时间与空间融合**：借助 SLAM 给出的位姿，把多帧、多视角的预测放进同一张 3D 地图里累积，用一致性压掉单帧噪声。代价是依赖位姿质量，并且要处理地图里的动态物体。
- **跨传感器融合**：相机给语义、激光雷达给几何、IMU 给高频运动；把它们放进同一个坐标空间。代价是标定和时间同步必须准确。

另有一种做法跳过显式的感知输出：把深度图或高程图直接交给学习式策略，让策略自己学会在感知不可靠时怎么办。

## 任务与部署约束

结论：同一个任务，换一种部署条件，可行的方案就不同；每篇论文的数字都要和它的硬件、帧率、传感器一起读。

| 任务 | 输出 | 部署约束（原文数字） | 原文写明做不好的场景 |
|---|---|---|---|
| 2D 检测 | 框与类别 | [YOLO](../../papers/arxiv-1506.02640/README.md)：Titan X 上 45 fps、VOC2007 63.4 mAP；同表 Faster R-CNN（VGG-16）73.2 mAP、7 fps | YOLO 对成群的小物体（如鸟群）困难，主要误差是定位不准 |
| 实例分割 | 每个物体一张掩码 | [Mask R-CNN](../../papers/arxiv-1703.06870/README.md)：每张图 195 ms（Tesla M40），约 5 fps，作者写明设计未针对速度优化 | Cityscapes 中卡车、公交、火车每类只有约 200–500 个训练样本，验证集与测试集存在领域偏移 |
| 可提示分割 | 任意提示对应的掩码 | [SAM](../../papers/arxiv-2304.02643/README.md)：图像编码器每张图跑一次，之后每个提示在浏览器中约 50 ms 出掩码；用重编码器时整体不是实时 | 漏掉细结构，偶尔幻觉出小的不连通块，不清楚怎样用提示实现语义与全景分割 |
| 单目深度 | 每像素深度 | [Monodepth2](../../papers/arxiv-1806.01260/README.md) 不需要深度标签；[Depth Anything V2](../../papers/arxiv-2406.09414/README.md) Small 60 ms、Large 213 ms（V100） | Monodepth2 遇到违反朗伯假设的物体（反光、色彩饱和）失效，单目没有公制尺度；深度传感器本身测不准透明物体（DA V2） |
| 传感器深度 | 深度图、点云 | [Agarwal 等](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md)：RealSense 每 100 ± 20 ms 一帧 | 立体深度在低纹理、过曝欠曝处困难，ToF 对暗表面失效、阳光下噪声大，反光表面产生伪影（Miki 等） |
| 激光雷达 3D 检测 | 3D 框 | [PointPillars](../../papers/arxiv-1812.05784/README.md)：62 Hz、16.2 ms（1080Ti） | 行人与骑车人互相误判，行人与电线杆、树干混淆；KITTI 只用前视相机视野内约 10% 的点，实车要处理整圈点云，嵌入式 GPU 吞吐更低 |
| 相机-激光融合 | BEV 检测与地图分割 | [BEVFusion](../../papers/arxiv-2205.13542/README.md)：119.2 ms（RTX 3090），nuScenes 测试集 NDS 72.9 | 预计算依赖内外参固定；视角变换中深度不准使 BEV 特征错位；论文没有做标定误差实验 |
| 语义建图 | 带语义的 3D 地图 | [SemanticFusion](../../papers/arxiv-1609.05130/README.md) 25 Hz（CNN 每 10 帧一次）；[PanopticFusion](../../papers/arxiv-1903.01177/README.md) 4.3 Hz；[FM-Fusion](../../papers/arxiv-2402.04555/README.md) 每帧 1039.6 ms | 依赖外部 SLAM 位姿；以旋转为主的扫描几乎没有融合增益；长期位姿漂移和动态环境留作未来工作 |
| 感知到控制 | 高程图或深度特征 → 关节指令 | [Miki 等](../../papers/arxiv-2201.08117/README.md)：训练噪声按名义 60%、大偏移 30%、大噪声 10% 注入；Agarwal 等：深度经 UDP 传给策略有 10 ± 10 ms 延迟，训练中建模 | 高程图不能表示悬空物（树枝、低天花板），分不清软硬；遮挡使悬崖边、踏脚石处信息不足，机器人可能踩空 |

## 主线历史

结论：每一步都在修上一步部署时暴露的问题；五步的失败场景分别集中在速度、帧间一致性、尺度与几何、传感器失效、开放类别的泛化。

### 1 单帧检测与分割做到视频速率（2015–2017）

**留下的问题。** R-CNN 类检测器是多阶段流水线，[YOLO](../../papers/arxiv-1506.02640/README.md) 的引言称它们慢而且难优化，因为每个部件要分别训练；同表中 Fast R-CNN 只有 0.5 fps。

**改变。** YOLO（UW、AI2、FAIR，2015）把检测写成一次回归：整张图进网络，直接输出 7×7 网格上的框和类别，45 fps，延迟低于 25 ms。[Mask R-CNN](../../papers/arxiv-1703.06870/README.md)（FAIR，2017）在 Faster R-CNN 上并行加一个掩码分支，并用 RoIAlign（一句话：用双线性插值取候选区域的特征，不再把坐标取整）替换 RoIPool，COCO 实例分割 mask AP 37.1，FCIS+++ 为 33.6。

**做不好的场景。** YOLO 的定位误差占全部误差的 19.0%，Fast R-CNN 为 8.6%；成群的小物体是它的典型失败。Mask R-CNN 约 5 fps，样本少的类别存在领域偏移。两者都是逐帧的：同一只杯子在相邻两帧里可以得到不同的类别或掩码，这一点直到下一步才被当作问题处理。

### 2 用 SLAM 位姿把逐帧预测融合进 3D 地图（2016–2019）

**留下的问题。** 单帧预测在视角不好时出错，机器人却会从很多视角看同一个物体。SemanticFusion 的引言用"去右手边最近的桌上拿咖啡杯"说明，机器人需要同时知道东西是什么、在哪里。

**改变。** [SemanticFusion](../../papers/arxiv-1609.05130/README.md)（Imperial，2016）用稠密 SLAM 系统 ElasticFusion 提供帧与 3D surfel 地图（一句话：带法向和半径的小圆面片）之间的对应，把多视角的 CNN 预测按贝叶斯规则累积到每个面片上；办公室重建数据集上类别平均准确率从单帧的 43.6% 升到 48.3%。[Pixel-Voxel 网络](../../papers/doi-10.3390-s18093099/README.md)（Birmingham、Lincoln 等，2018）同时用 RGB 和点云，半分辨率约 13 Hz。[PanopticFusion](../../papers/arxiv-1903.01177/README.md)（Sony，2019）改用体素地图：引言写明点云和面元难以直接用于机器人的碰撞检测和导航；它把语义标签（墙、地板这类"stuff"）和实例 ID（每把椅子这类"things"）一起写进 TSDF 体素（截断符号距离场：每个体素存它到最近表面的带符号距离），并靠查询当时的 3D 地图让实例 ID 在帧间保持一致。

**做不好的场景。**
- **视角不够**：SemanticFusion 在 NYUv2 上的相对增益只有办公室数据集的一半左右，作者归因于 NYUv2 以旋转为主的扫描轨迹提供不了足够多的不同视角；远处几何会让跟踪和建图本身出问题，这时单帧网络反而更准。
- **速度**：CNN 每帧都跑时准确率最高（52.5%），但只有 8.2 Hz；PanopticFusion 的吞吐 4.3 Hz，瓶颈是每次 235 ms 的 Mask R-CNN，地图正则化在序列末尾要约 10 秒。
- **位姿依赖**：PanopticFusion 的相机位姿由外部 SLAM 提供，ScanNet 实验直接用数据集给的轨迹；作者把长期位姿漂移下的全局一致性和动态环境列为未来工作。
- **数据集本身**：NYUv2 的 206 条测试序列中，帧率掉到 2 Hz 以下、无法跟踪的被 SemanticFusion 排除，剩 140 条。

### 3 深度与 3D：不靠标签学深度，激光雷达检测上车（2019）

**留下的问题。** 2D 掩码要变成 3D 位置就需要深度；深度传感器有自己的失效，激光雷达点云又稀疏、量大。

**改变。**
- [Monodepth2](../../papers/arxiv-1806.01260/README.md)（UCL、Caltech、Niantic，2018 年预印本，ICCV 2019）用相邻帧之间的重投影误差训练单目深度，不需要深度标签；自动掩蔽丢掉"相机静止、物体与相机同速运动、低纹理区域"这三种违反静态场景假设的像素。
- [PointPillars](../../papers/arxiv-1812.05784/README.md)（nuTonomy，2018 年预印本，CVPR 2019）把点云按竖直柱体编码，只用 2D 卷积，KITTI 鸟瞰检测 62 Hz；此前的 VoxelNet 为 4.4 Hz。
- 同一团队的 [nuScenes](../../papers/arxiv-1903.11027/README.md)（2019）提供 6 相机、5 雷达、1 激光雷达的完整车载数据，相机曝光在激光雷达扫过相机视场中心时触发，并定义 NDS（一句话：一半看检测 mAP，一半看位置、尺寸、朝向、速度、属性的误差）。

**做不好的场景。** Monodepth2 写明单目训练不保证公制尺度，常用的逐图中值缩放会"掩盖深度和位姿估计中不稳定的尺度"；反光、失真、色彩饱和区域学不出好的深度，而这些正是机器人在室内常遇到的玻璃、金属、屏幕。PointPillars 在行人与骑车人之间、行人与电线杆之间混淆，并指出 KITTI 评测只用了约 10% 的点。

### 4 多传感器在统一空间融合（2022）

**留下的问题。** 相机与激光雷达各有失效方式（相机怕夜间，激光雷达怕雨），点级融合又各有损失。[BEVFusion](../../papers/arxiv-2205.13542/README.md)（MIT，2022）的引言给出数字：对 32 线激光雷达，相机特征投影到激光点上时只有约 5% 能找到对应点，这种融合几乎无法用于鸟瞰地图分割这类语义任务。

**改变。** 相机特征按预测的深度分布抬升到鸟瞰图（BEV，一句话：从正上方俯视的二维网格），与激光雷达特征在同一网格上卷积融合，再接检测和地图分割两个头。原来的 BEV 池化在 RTX 3090 上要 500 ms 以上，作者用预计算和专门的归约核降到 12 ms。nuScenes 测试集 NDS 72.9，地图分割 mIoU 62.7，只用相机为 56.6；雨天检测 mAP 69.9，纯激光雷达的 CenterPoint 为 59.2；夜间地图分割 mIoU 43.6，只用相机为 30.8。

**做不好的场景。** 预计算假设内外参固定，作者写明这"在正确标定后通常成立"，全文没有标定误差或传感器缺失的实验；相机深度不准时 BEV 特征会错位，只能靠后面的卷积补偿。`[判断]` 标定与时间同步被当作前提而非研究对象，这是本方向论文普遍的口径；[感知讲义](../perception.md)第七节的时间戳算例（1 m/s × 0.1 s = 0.1 m）说明了这个前提一旦不成立，误差会直接超过抓取的余量。

### 5 把感知误差交给下游策略（2022）

**留下的问题。** 以上各步都在提高感知的精度，但现场总有感知做不好的时候。[Miki 等](../../papers/arxiv-2201.08117/README.md)（ETH、KAIST、Intel，2022）列出四足机器人野外的失效来源：立体深度在低纹理和曝光异常处困难，ToF 对暗表面失效、阳光下噪声大，反光表面产生伪影，打滑或可变形的地面使里程计漂移、高程图随之失准；此前的感知型控制器假设地图大体准确，否则只能退回纯本体感知、速度受限。

**改变。** 两种相反的做法：
- **保留高程图，让策略学会不信它**（Miki 等）：训练学生策略时给高程图注入三类噪声，一个带注意力门的循环编码器学习每一刻放多少外感知信息进来，必要时退回本体感知。机器人走完 2.2 km、爬升 120 m 的阿尔卑斯山路，用时 78 分钟，徒步规划软件建议 76 分钟；纯本体感知的基线在 20 cm 台阶上成功率下降，本方法通过 30.5 cm 的台阶。
- **不建高程图**（[Agarwal 等](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md)，CMU 与 Berkeley，2022）：引言指出高程图要融合多帧深度，就需要视觉或惯性里程计提供相对位姿，噪声迫使前人在训练中加大量噪声，又让缝隙和踏脚石做不可靠。它直接从单个前视深度相机的深度图和本体状态，用循环网络输出 50 Hz 的关节角，在小型 A1 机器人的 Jetson NX 上运行。

**做不好的场景。** Miki 等写明不确定性只是隐式使用，窄悬崖和踏脚石处的遮挡让高程图信息不足，机器人可能踩空；高程图丢掉了材质与纹理。Agarwal 等写明视觉或地形的仿真与现实不匹配会导致失败，在现有范式下唯一的办法是把这种情形工程化回仿真里再训练。

### 6 开放词汇与基础模型（2023–2024）

**留下的问题。** 固定类别的检测器在训练分布之外掉点严重。[FM-Fusion](../../papers/arxiv-2402.04555/README.md)（HKUST，2024）给出了量级：ScanNet 上，用 COCO 训练的 Mask R-CNN 接 Kimera 建图，实例分割 mAP50 只有 5.4，在 ScanNet 上微调后为 25.9。[ConceptFusion](../../papers/arxiv-2302.07241/README.md)（MIT 等，2023）指出已有语义建图只能推理训练时预先定义的有限概念。

**改变。** [SAM](../../papers/arxiv-2304.02643/README.md)（Meta FAIR，2023，在 1100 万张图、11 亿个掩码上训练）提供类别无关的高质量掩码；[Grounding DINO](https://arxiv.org/abs/2303.05499)（2023）按文字提示检测任意物体，COCO 零样本 52.5 AP。ConceptFusion 把 CLIP 的全局与局部特征融合成逐像素特征，写进 3D 点图，用文字、图像或声音查询，长尾概念上的 3D IoU 比有监督方法高 40% 以上。FM-Fusion 把 RAM、Grounding DINO、SAM 接到一起，用概率融合把开放集标签转成闭集类别，并合并因视角变化而被切碎的实例，ScanNet mAP50 达到 40.3。深度一侧，[Depth Anything](../../papers/arxiv-2401.10891/README.md)（HKU、TikTok 等，2024）用 6200 万张无标注图做伪标签训练相对深度；[Depth Anything V2](../../papers/arxiv-2406.09414/README.md) 指出深度传感器测不准透明物体、立体匹配怕无纹理和重复纹理，于是把全部真实标注换成合成标注，透明表面挑战的零样本 δ1（预测深度与真值之比落在 1.25 倍以内的像素比例）从 V1 的 0.535 升到 0.836。

**做不好的场景。**
- **速度**：FM-Fusion 每帧 1039.6 ms，其中 SAM 464.4 ms、Grounding DINO 120.7 ms，作者写明还不是实时系统；ConceptFusion 的逐像素特征离线提取，每张图 10–15 秒。
- **内存**：ConceptFusion 的地图有百万级的点，每个点带高维嵌入，作者把内存列为第一条局限。
- **一致性**：SAM 在不同视角下给出不一致的实例掩码，造成过分割（FM-Fusion）；ConceptFusion 的特征偏向前景物体，不理解否定。
- **位姿**：FM-Fusion 与 ConceptFusion 的评测都使用数据集提供的位姿或独立的 SLAM。
- **度量深度**：Depth Anything 输出相对深度（仿射不变的视差），要得到米制距离需要在 NYUv2、KITTI 一类数据上微调；V2 写明在这些真实数据上训练的度量模型对透明物体不鲁棒。

## 站在现在看过去：后来者专门修了什么

| 当时的做法 | 后来暴露的坑 | 谁修、怎样修 | 依据 |
|---|---|---|---|
| 逐帧独立预测 | 同一物体在相邻帧里标签和掩码互相矛盾 | SemanticFusion 用 SLAM 对应做多视角贝叶斯融合；PanopticFusion 查询 3D 地图保持实例 ID | SemanticFusion §IV-D；PanopticFusion §III-D |
| 语义写进点云或面元 | 机器人难以直接用来做碰撞检测和导航 | PanopticFusion 改用 TSDF 体素并能抽出网格 | PanopticFusion §I |
| 3D 卷积编码点云（VoxelNet） | 225 ms 一帧，跟不上 20 Hz 的激光雷达 | PointPillars 用柱体加 2D 卷积，16.2 ms | PointPillars §1.1.2、§6 |
| 相机特征投到激光点上融合 | 32 线激光雷达下只有约 5% 的相机特征有对应，语义信息丢失 | BEVFusion 改在鸟瞰网格上融合 | BEVFusion §I |
| 假设高程图准确 | 反光、植被、雪、里程计漂移让地图失准，策略踩空或只能慢走 | Miki 等注入噪声并学门控；Agarwal 等不建高程图 | Miki 等引言与方法；Agarwal 等 §1 |
| 监督检测器、固定类别 | 换数据分布后严重掉点（ScanNet 上 5.4 mAP50） | FM-Fusion、ConceptFusion 接开放词汇基础模型 | FM-Fusion Table（ScanNet）；ConceptFusion §I |
| 用传感器深度做真值训练深度网络 | 传感器在透明物体上给出错误真值 | Depth Anything V2 改用合成标注加伪标签 | DA V2 §2 |
| 单目自监督深度用中值缩放评测 | 掩盖了尺度不稳定 | `[判断]` 机器人上仍用深度相机、双目或激光雷达提供公制尺度；Depth Anything 在度量数据上微调 | Monodepth2 附录 D.2；DA §4.3 |
| 开放词汇语义地图离线运行 | 每帧 1 秒到 15 秒，不能闭环使用 | 尚未解决；定位方向的 VGGT-SLAM 2.0 报告接入 CLIP 开放集检测后 6.3 fps | FM-Fusion 运行时分析；见[定位与建图](../localization-mapping/README.md)阶段 5 |

`[判断]` 跨领域的共性：一是"训练时注入感知噪声让策略学会不信它"与[运动控制方向](../control-locomotion/README.md)里的域随机化是同一个思路，作用对象从动力学参数换成了感知输入；二是"网络给语义、几何模块给位置"的分工，在[定位与建图](../localization-mapping/README.md)里表现为前馈模型做前端、因子图做后端，在 [VLA 方向](../vla/README.md)里表现为预训练模型给语义、动作头负责精度（见 [OpenVLA 精读](../../papers/openvla/reading.md)与 Diffusion Policy 的对比）。

## 技术地基

- **相机模型、内外参与坐标变换**：像素怎样变成地图系或基座系的三维点。[感知讲义](../perception.md)第三节；位姿从哪里来见[定位与建图讲义](../localization-mapping.md)。
- **卷积、分类损失与多任务头**：检测、分割、深度共享编码器、各接各的头。[CNN 讲义](../../../foundations/lessons/11-cnn.md)、[感知讲义](../perception.md)第五节。
- **视觉编码器与预训练**：CLIP、DINOv2 这类编码器的性质和取舍。[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。
- **双目三角化与自监督光度损失**：深度怎样测、怎样学，以及误差为什么随距离平方增长。[感知讲义](../perception.md)第六节。
- **逆方差加权与卡尔曼滤波**：跨时间、跨传感器融合的统计基础，以及"共享误差源时不能当作独立证据"。[感知讲义](../perception.md)第七节、[定位与建图讲义](../localization-mapping.md)第四节。
- **TSDF 与占据地图**：语义写进哪种地图决定下游能怎么用。[定位与建图讲义](../localization-mapping.md)第十节。

## 主要路线与团队偏好

| 路线 | 团队 | `[判断]` 押注 | 代价 |
|---|---|---|---|
| 通用 2D 模型 | FAIR（Girshick、He、Dollár 等） | 一个通用的、开源的 2D 模型服务所有下游，用 COCO 一类大 benchmark 衡量；Mask R-CNN 与 SAM 都把重计算放在一次性的主干或编码器上 | Mask R-CNN 自述未针对速度优化，SAM 用重编码器时整体不是实时；都不处理时间与 3D |
| 稠密 SLAM 上叠语义 | Imperial（Davison 组）；Sony；HKUST（沈劭劼组） | 语义要写进 SLAM 维护的 3D 地图才有用 | 依赖外部位姿；每帧 0.2 秒到 1 秒；静态场景假设 |
| 面向车载部署的 3D 感知 | nuTonomy（PointPillars、nuScenes）；MIT Han Lab（BEVFusion） | 速度与完整传感器配置优先：nuTonomy 在 PointPillars 中把 20 Hz 激光雷达和嵌入式 GPU 当作设计约束，又在 nuScenes 中定义同时考核定位、尺寸、速度的 NDS | 标定和同步作为前提，鲁棒性实验只覆盖天气与光照 |
| 感知误差交给策略 | ETH RSL（Miki 等）；CMU 与 Berkeley（Agarwal 等） | ETH 保留显式高程图并训练对它的不信任；CMU 与 Berkeley 去掉中间表示 | 前者遮挡处仍会踩空；后者每遇到新的仿真-现实差异都要回仿真重训 |
| 开放词汇基础模型 | MIT 等（ConceptFusion）；HKUST（FM-Fusion）；HKU 与 TikTok（Depth Anything） | 不针对机器人训练，直接组合网络规模预训练的模型 | 秒级延迟、百万点乘高维嵌入的内存、跨视角不一致 |

`[判断]` 收敛与分化：逐帧网络加 3D 累积的结构已经是语义建图的共同做法，分化在累积的载体（surfel、TSDF 体素、带特征的点）和语义的来源（固定类别的 CNN、开放词汇基础模型）。感知到控制这一支没有收敛：显式地图与端到端两种做法在本页的证据里各有失败场景，没有同条件的对照实验。

## 用什么衡量进展

结论：任务指标（AP、mIoU、AbsRel、NDS；AbsRel 是预测深度与真值之差的绝对值除以真值后的平均）测的是单帧或离线的精度，机器人真正受限的帧率、延迟、标定敏感性和失败率，需要从论文的运行时分析和失败案例里单独读出来。

- **2D 检测与分割**：PASCAL VOC 与 COCO 的 AP；YOLO 把 mAP 和 FPS 放在同一张表里，是"速度–精度"并列报告的早期例子。
- **深度**：KITTI Eigen 划分上的 AbsRel、δ<1.25；Depth Anything 起改为在多个数据集上零样本评测。单目结果常用逐图中值缩放，Monodepth2 写明这会掩盖尺度不稳定。
- **3D 检测与融合**：KITTI（前视相机视野内的点）→ nuScenes 的 NDS（整圈多传感器、加入速度与属性误差）→ Waymo。`[判断]` benchmark 从 KITTI 换到 nuScenes，就是目标从"前视单帧检测"迁移到"全向、多传感器、带运动状态的检测"。
- **语义建图**：NYUv2、ScanNet 的 mIoU 与实例 mAP；多数系统用数据集的相机轨迹评测，等于把位姿误差排除在外。
- **感知到控制**：没有独立的感知指标，看下游任务：走完山路的用时、能上的台阶高度、仿真中跌倒前的平均位移。
- **部署指标**：每篇的帧率都要连同硬件读：PanopticFusion 用两张 1080Ti，FM-Fusion 用 RTX 3090 离线运行，Agarwal 等在 Jetson NX 上 50 Hz。

## 当前开放问题

- **语义地图怎样做到实时且不依赖给定位姿？** 入口：[FM-Fusion](../../papers/arxiv-2402.04555/README.md)、[ConceptFusion](../../papers/arxiv-2302.07241/README.md)、[PanopticFusion](../../papers/arxiv-1903.01177/README.md) 的未来工作，以及[定位与建图](../localization-mapping/README.md)阶段 5 中把开放集检测接进前馈 SLAM 的尝试。
- **度量深度在透明、反光、低光下是否可靠？** 入口：[Depth Anything V2](../../papers/arxiv-2406.09414/README.md)、[Monodepth2](../../papers/arxiv-1806.01260/README.md)、[Miki 等](../../papers/arxiv-2201.08117/README.md)对传感器失效的描述。
- **感知不确定性怎样显式地传给控制？** Miki 等写明不确定性只被隐式使用。入口：[Miki 等](../../papers/arxiv-2201.08117/README.md)、[Agarwal 等](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md)、[MGDP](../../papers/doi-10.1002-advs.202524345/README.md)。
- **标定与时间同步能否在线检验和修正？** 融合论文把它当前提（[BEVFusion](../../papers/arxiv-2205.13542/README.md)），定位一侧已有在线标定内外参与时间偏移的做法（OpenVINS、VINS-Mono，见[定位与建图](../localization-mapping/README.md)）。

## 阅读顺序

1. [感知讲义](../perception.md)第三、五、六、七节：坐标变换、多任务头、深度与融合的最小算例，后面每篇论文都在其中一个环节上做文章。
2. [YOLO](../../papers/arxiv-1506.02640/README.md) 与 [Mask R-CNN](../../papers/arxiv-1703.06870/README.md)：单帧 2D 感知的速度–精度取舍，读它们的速度表和失败分析。
3. [SemanticFusion](../../papers/arxiv-1609.05130/README.md) → [PanopticFusion](../../papers/arxiv-1903.01177/README.md)：怎样借 SLAM 位姿把逐帧预测变成一致的 3D 地图，重点看运行时间分解和"旋转轨迹没有增益"。
4. [PointPillars](../../papers/arxiv-1812.05784/README.md) → [BEVFusion](../../papers/arxiv-2205.13542/README.md)（配合 [nuScenes](../../papers/arxiv-1903.11027/README.md)）：激光雷达与多传感器融合，重点看延迟分解和雨天、夜间实验。
5. [Miki 等](../../papers/arxiv-2201.08117/README.md) 与 [Agarwal 等](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md)：对照阅读，两种处理感知误差的思路。
6. [FM-Fusion](../../papers/arxiv-2402.04555/README.md) 与 [Depth Anything V2](../../papers/arxiv-2406.09414/README.md)：基础模型进入机器人感知后，修了什么、新暴露了什么。

## 批注

**易误读**

- YOLO 的 45 fps 与 63.4 mAP 是 VOC2007 上的结果；同表 Faster R-CNN 的 73.2 mAP 用的是 VGG-16，7 fps（YOLO Table 1）。YOLO 与 Mask R-CNN 的 arXiv 页与 PDF 首页都没有印正式发表处。
- SemanticFusion 的 43.6% → 48.3% 是作者自建办公室重建数据集上 RGBD-CNN 的类别平均准确率；NYUv2 上的相对增益约为它的一半（§IV-D、§IV-E）。
- PanopticFusion 与 FM-Fusion 的 ScanNet 结果都使用数据集提供的相机轨迹（PanopticFusion §IV-A；FM-Fusion 实验设置），语义地图精度没有包含位姿误差。
- FM-Fusion 的 5.4 对 40.3 是 ScanNet 30 个验证场景上的 mAP50；5.4 是未在 ScanNet 上微调的 Mask R-CNN 接 Kimera。
- BEVFusion 的雨天、夜间对比对象是纯激光雷达的 CenterPoint 与 BEVFusion 自己的纯相机版本（Table IV），不是传感器失效实验。
- Depth Anything V2 的透明表面 δ1 来自 NTIRE 2024 透明表面挑战（Table 12）；它在常规基准上与 V1 相当，在两个数据集上略差（§7.2）。
- Miki 等"78 分钟对 76 分钟"的比较对象是徒步规划软件给出的建议用时，不是人类实测；数字经 arXiv HTML 页抽取，未与 Science Robotics 正式版逐字比对。
- Agarwal 等对噪声高程图基线的 60–90% 优势来自仿真（Table 1），基线是作者按 Miki 等的噪声模型复现的。

**判断的支撑论文**

- "感知误差无法在感知模块内消除"：Miki 等引言与讨论、Agarwal 等 §1 与局限、SemanticFusion Fig.6（远处几何导致跟踪问题）。反例：BEVFusion 在雨天、夜间通过融合大幅减少了误差，说明一部分失效可以在感知内部补偿。
- "基础模型把类别固定换成速度与一致性不够"：FM-Fusion 运行时分析与局限、ConceptFusion 局限、SAM 局限、Depth Anything V2 §2。边界：VGGT-SLAM 2.0 报告带 CLIP 开放集检测的系统达到 6.3 fps（见定位与建图页），速度问题在改善。
- 团队偏好按"两篇以上、存在替代方案时重复同一选择"判断：FAIR 在 Mask R-CNN 与 SAM 中都发布通用 2D 模型并开源，都不针对实时；nuTonomy 在 PointPillars 与 nuScenes 中都把完整车载传感器与部署速度作为出发点。ETH 与 CMU/Berkeley、ConceptFusion、Depth Anything 在本页各只有一篇，写的是该论文的选择，不足以称为团队偏好。
- 跨领域共性（感知噪声注入与域随机化、网络给语义而几何模块给位置）是类比，没有直接对照实验；域随机化的证据以运动控制方向页为准。

**与其他论文的关联**

- [SemanticFusion](../../papers/arxiv-1609.05130/README.md) 与 [ORB-SLAM3](../../papers/orb-slam3/reading.md) 是同一条接口的两端：后者精读写明它只输出稀疏几何点，语义要由这类工作叠加。
- [OpenVLA 精读](../../papers/openvla/reading.md)拼接 DINOv2 与 SigLIP 两种视觉特征，并发现冻结视觉编码器会使成功率从约 70% 降到 47%：感知特征是否够用，在端到端策略里同样是开放问题，表征一侧的讨论见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。
- [CLIP](../../../multimodal/papers/clip/README.md) 是 ConceptFusion 的语义来源；[ViT](../../../multimodal/papers/vit/README.md) 是 SAM、Depth Anything 编码器的结构。
- [ESKF 精读](../../papers/eskf/reading.md)与[感知讲义](../perception.md)第七节：跨传感器融合的统计前提是误差独立、时间对齐，与 BEVFusion 把标定当作前提相对照。

**未核实 / 待验证**

- Grounding DINO 只核实了 arXiv 摘要页（题名、版本、COCO 与 ODinW 零样本数字），作者单位未从论文首页核实，本页没有为它建卡。
- MGDP（Advanced Science）原文未打开，只在开放问题中作为入口出现。
- Pixel-Voxel 网络的数字经 PMC 页面抽取，正式版 PDF 未逐表核对；其代码在论文中写的是"接收后发布"，实际发布情况未查。
- 多传感器时空标定的原始论文（Furgale 等 IROS 2013，Kalibr）没有找到可打开的官方全文，本页没有引用。
- Depth Anything V2 各模型的许可证未核实。
