# 机器人感知的基线

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md)

## 基线是谁、为什么是它

结论：本方向的基线是两层接口，单帧预测一层与跨时间融合一层；后续工作要么替换某一层的部件，要么把输出直接交给策略。

- **[Mask R-CNN](../../papers/arxiv-1703.06870/README.md)（2017，单帧 2D 感知）。** 它定义了"一张图进，框、类别、实例掩码出"的接口：共享主干加并列的任务头，在 COCO 上按 AP 评测。之后的语义建图系统（PanopticFusion 用它做实例分割）和开放词汇模型（SAM 的掩码、Grounding DINO 的框）都在替换这一层。
- **[SemanticFusion](../../papers/arxiv-1609.05130/README.md)（2016，跨时间融合）。** 它定义了"逐帧预测 + SLAM 位姿 → 带语义的 3D 地图"的接口：SLAM 给出帧与地图元素之间的对应，每个地图元素累积多视角的类别概率；评测是把地图投回图像，与单帧预测比较 2D 标注上的准确率，并报告帧率。

几何一侧的参照是 [PointPillars](../../papers/arxiv-1812.05784/README.md)（激光雷达 3D 检测）与 [Monodepth2](../../papers/arxiv-1806.01260/README.md)（单目深度），它们定义了 3D 框和每像素深度两种几何输出。从像素到地图系物体记录的完整机制见[感知讲义](../perception.md)。

## 基线的结构拆分

1. **传感器与输入表示**：RGB、深度图、激光点云（柱体、体素）、鸟瞰网格、高程图；标定与时间同步是这一层的前提。
2. **预测网络**：主干加任务头（检测、分割、深度）；类别是固定的还是开放的；用什么监督（人工标签、光度自监督、伪标签与合成数据）。
3. **跨时间与视角的融合**：融合的载体（无、surfel、TSDF 体素、带特征的点）和规则（贝叶斯累积、CRF 正则、实例合并）；位姿从哪里来。
4. **跨传感器的融合空间**：结果级、点级投影、鸟瞰网格。
5. **与下游的接口**：输出显式的物体与地图交给规划，或把感知特征直接交给学习式策略；感知误差在哪一层被处理。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 预测网络 | 单阶段回归代替多阶段流水线 | [YOLO](../../papers/arxiv-1506.02640/README.md) | 45 fps / 定位误差大，成群小物体困难 |
| 预测网络 | 加掩码分支，RoIAlign 代替 RoIPool | [Mask R-CNN](../../papers/arxiv-1703.06870/README.md) | 实例掩码，COCO mask AP 37.1 / 约 5 fps |
| 预测网络（开放类别） | 可提示分割，11 亿掩码训练 | [SAM](../../papers/arxiv-2304.02643/README.md) | 类别无关的高质量掩码 / 重编码器下非实时，跨视角不一致（FM-Fusion 报告） |
| 预测网络（开放类别） | 文字提示的开放集检测 | [Grounding DINO](https://arxiv.org/abs/2303.05499)（未建卡） | COCO 零样本 52.5 AP / 在 FM-Fusion 中每帧 120.7 ms |
| 预测网络（深度监督） | 相邻帧光度重投影自监督，自动掩蔽 | [Monodepth2](../../papers/arxiv-1806.01260/README.md) | 不需要深度标签 / 无公制尺度，反光与色彩饱和处失效 |
| 预测网络（深度监督） | 6200 万张无标注图伪标签 | [Depth Anything](../../papers/arxiv-2401.10891/README.md) | 零样本相对深度大幅领先 MiDaS / 只有相对深度，训练分辨率不足 |
| 预测网络（深度监督） | 真实标注全部换成合成标注，ViT-G 教师 | [Depth Anything V2](../../papers/arxiv-2406.09414/README.md) | 透明表面零样本 δ1 0.535 → 0.836，Small 60 ms / 常规基准与 V1 相当，伪标签计算负担重 |
| 输入表示（激光雷达） | 竖直柱体编码，只用 2D 卷积 | [PointPillars](../../papers/arxiv-1812.05784/README.md) | 62 Hz / 行人与骑车人、电线杆混淆 |
| 输入表示 + 评测 | 整圈多传感器数据，NDS 指标 | [nuScenes](../../papers/arxiv-1903.11027/README.md) | 评测覆盖速度、朝向、属性 / 标定与同步由数据集保证，不考核在线标定 |
| 跨传感器融合空间 | 相机与激光雷达都转到鸟瞰网格 | [BEVFusion](../../papers/arxiv-2205.13542/README.md) | 地图分割与夜间鲁棒性提高，119 ms / 依赖固定内外参，深度不准时特征错位 |
| 跨时间融合 | SLAM 对应 + surfel 贝叶斯累积 | [SemanticFusion](../../papers/arxiv-1609.05130/README.md) | 多视角提高 2D 准确率，25 Hz / CNN 每 10 帧才跑一次，旋转轨迹无增益 |
| 跨时间融合 + 输入 | RGB 与点云双分支，体素融合 | [Pixel-Voxel](../../papers/doi-10.3390-s18093099/README.md) | NYUv2 准确率高于 SemanticFusion，半分辨率约 13 Hz / 受 Kinect V2 噪声与光照影响 |
| 跨时间融合 | TSDF 体素，stuff 与 things 全景标签，实例 ID 帧间跟踪 | [PanopticFusion](../../papers/arxiv-1903.01177/README.md) | 地图可直接用于碰撞与导航，ScanNet 上与离线 3D 网络相当 / 4.3 Hz，用外部位姿 |
| 跨时间融合 + 开放类别 | CLIP 逐像素特征写进 3D 点图，多模态查询 | [ConceptFusion](../../papers/arxiv-2302.07241/README.md) | 长尾概念 3D IoU 超有监督方法 40% 以上 / 每张图 10–15 s，内存大 |
| 跨时间融合 + 开放类别 | RAM + Grounding DINO + SAM，概率标签融合与实例细化 | [FM-Fusion](../../papers/arxiv-2402.04555/README.md)（[代码仓库卡](../../papers/url-https-github.com-hkust-aerial-robotics-fm-fusion/README.md)） | ScanNet mAP50 40.3（未微调的 Mask R-CNN 为 5.4）/ 每帧约 1 s，用数据集位姿 |
| 与下游的接口 | 保留高程图，训练中注入三类地图噪声，循环编码器学门控 | [Miki 等](../../papers/arxiv-2201.08117/README.md) | 野外长距离可靠行走 / 遮挡处仍会踩空，不确定性只隐式使用 |
| 与下游的接口 | 不建高程图，深度图与本体状态直接到关节角 | [Agarwal 等](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md) | 单个深度相机、Jetson NX 上 50 Hz / 仿真-现实差异只能回仿真重训 |
| 与下游的接口 | 面向四足运动的泛化深度感知模型 | [MGDP](../../papers/doi-10.1002-advs.202524345/README.md) | 原文未打开，位置待核实 |
| 预测网络的主干 | ViT、CLIP 编码器作为主干或语义来源 | [ViT](../../../multimodal/papers/vit/README.md)、[CLIP](../../../multimodal/papers/clip/README.md) | 表征的性质与取舍见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md) |
| 位姿来源（上游） | 语义地图依赖的位姿由 SLAM 或 VIO 提供 | [ORB-SLAM3](../../papers/orb-slam3/reading.md)、[ESKF](../../papers/eskf/reading.md) | 见[定位与建图的基线](../localization-mapping/BASELINES.md) |

## 批注

**易误读**

- 速度数字都要和硬件一起读：YOLO 用 Titan X，Mask R-CNN 用 Tesla M40，BEVFusion 与 FM-Fusion 用 RTX 3090，PanopticFusion 用两张 1080Ti，Agarwal 等用 Jetson NX。
- SemanticFusion 的 25 Hz 是 CNN 每 10 帧运行一次时的平均帧率；CNN 每帧都跑时为 8.2 Hz（§IV-C）。
- MGDP 一行只依据题名放置，原文未打开。

**与其他论文的关联**

- 跨时间融合一层与[定位与建图的基线](../localization-mapping/BASELINES.md)"地图表示"部件共用 SemanticFusion、PanopticFusion、FM-Fusion：那边看地图载体，这边看语义怎样累积。
- "与下游的接口"一层与[运动控制方向](../control-locomotion/README.md)相接：Miki 等与 Agarwal 等的策略训练方式在那里展开。
- Depth Anything V2 的编码器来自 DINOv2，CLIP 是 ConceptFusion 的语义来源；两者作为表征的性质在[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)讨论。

**未核实 / 待验证**

- Grounding DINO 只核实了 arXiv 摘要页，没有建卡；MGDP 原文未打开。
- SAM 的零样本实验表未逐表核对，本页只引用其运行时、数据规模与局限。
