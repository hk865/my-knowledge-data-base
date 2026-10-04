# 机器人感知：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

五步，按"单帧预测 → 跨时间融合 → 几何与跨传感器 → 交给策略 → 基础模型"排列；每读一篇，把它的帧率、硬件和自述失败场景填进[入门页](README.md)"任务与部署约束"那张表对应的格子里。

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
