# 机器人感知：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

前五步按"单帧预测 → 跨时间融合 → 几何与跨传感器 → 交给策略 → 基础模型"排列；每读一篇，把它的帧率、硬件和自述失败场景填进[入门页](README.md)"任务与部署约束"那张表对应的格子里。

## 第一步：从像素到地图系物体记录的机制

读[感知讲义](../perception.md)第三、五、六、七节。重点是三件事：一个像素怎样经内外参变成机械臂基座系的点；分割损失的梯度流到哪些参数；两个测量的逆方差加权在什么条件下会过度自信。放在第一步，是因为后面每篇论文的失败都能落到这条链的某一环上。表征本身的性质（为什么 DINOv2 特征含有几何信息）先不展开，需要时查[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)。

## 第二步：单帧 2D 感知的速度与精度

读 [YOLO](../../papers/arxiv-1506.02640/README.md) 与 [Mask R-CNN](../../papers/arxiv-1703.06870/README.md)，只看三处：速度表、误差分解或失败案例、作者写的硬件。放在这里，是因为它们定义了基线的单帧接口，后面的语义建图系统直接把它们当部件用，瓶颈也常常就在它们身上（PanopticFusion 的 4.3 Hz 由 Mask R-CNN 决定）。

## 第三步：借位姿把逐帧预测变成一致的地图

读 [SemanticFusion](../../papers/arxiv-1609.05130/README.md) → [PanopticFusion](../../papers/arxiv-1903.01177/README.md)。对照它们的运行时间分解，回答：为什么 CNN 不每帧都跑；为什么以旋转为主的扫描没有融合增益；位姿从哪里来、错了会怎样。放在这里，是因为它把[定位与建图](../localization-mapping/README.md)的输出接进了感知，位姿误差从这一步开始成为感知误差。

## 第四步：几何、多传感器与交给策略

先读 [PointPillars](../../papers/arxiv-1812.05784/README.md) 与 [BEVFusion](../../papers/arxiv-2205.13542/README.md)（配合 [nuScenes](../../papers/arxiv-1903.11027/README.md) 看传感器配置和同步方式），再对照读 [Miki 等](../../papers/arxiv-2201.08117/README.md) 与 [Agarwal 等](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md)。前两篇在感知内部用融合补偿单一传感器的失效，后两篇承认补偿不完，把剩下的误差交给策略。放在一起读，是因为它们回答的是同一个问题的两半：哪些误差能在感知里消掉，哪些只能让下游学会承受。

## 第五步：基础模型修了什么、新暴露了什么

读 [FM-Fusion](../../papers/arxiv-2402.04555/README.md)、[ConceptFusion](../../papers/arxiv-2302.07241/README.md)、[Depth Anything V2](../../papers/arxiv-2406.09414/README.md)，必要时查 [SAM](../../papers/arxiv-2304.02643/README.md) 的局限。检验题：

1. FM-Fusion 每帧约 1 秒的耗时里，哪个模型占了将近一半？如果要在机器人上闭环使用，你会先换掉哪一个、代价是什么？
2. Depth Anything V2 为什么要放弃真实深度标注？这对用 RealSense 采集训练数据的机器人团队意味着什么？
3. 把 Miki 等的三类训练噪声（名义、大偏移、大噪声）各对应到一种真实的传感器或位姿失效，并说出入门页里哪篇论文报告过它。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。

## 第六步：把 2025–2026 的变化接回部署问题

第五步停在“用基础模型替换部件”，这一步看哪些部件能合并、哪些必须变轻。

1. **分割支线**：FM-Fusion → [SAM 3](../../papers/arxiv-2511.16719/README.md)。画出被合并的检测、分割、跟踪模块，再圈出仍由 SLAM 负责的 3D 数据关联。优先级：选读。
2. **几何支线**：Depth Anything V2 → [Depth Anything 3](../../papers/arxiv-2511.10647/README.md)。列出每种输入配置已知哪些相机信息、输出有没有公制尺度，再接[定位与建图路线](../localization-mapping/ROADMAP.md)。优先级：选读。
3. **实时支线**：FoundationStereo → [Fast-FoundationStereo](../../papers/arxiv-2512.11130/README.md) → [LAS2](../../papers/arxiv-2606.24457/README.md)。前者必读、后者按部署需求选读；练习是在同一分辨率、功耗和精度下选一个延迟预算，分别指出哪些收益来自结构、数据、编译后端。高帧率结论不能直接代替整条机器人链路的延迟测量。

读完应能提出一个具体实验：固定控制器与场景，只换深度模块，同时报告几何误差、尾部延迟、丢帧和闭环失败，而不是把各篇不同硬件上的最快数字拼在一起。
