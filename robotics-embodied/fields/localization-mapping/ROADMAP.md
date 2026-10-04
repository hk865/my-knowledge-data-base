# 定位与建图：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

六步，前两步建立两种估计器的基线，中间三步按时间顺序看后来者修了什么，最后一步自己检验。每一步都带着[入门页](README.md)"五类失败场景"那张表去读。

## 第一步：滤波的机制与它在哪里过度自信

读[定位与建图讲义](../localization-mapping.md)第四至七节，再读 [ESKF 精读](../../papers/eskf/reading.md)。卡尔曼滤波本身可以快速过，重点放在误差状态的注入与重置、IMU 噪声的离散化：精读中的算例显示，把噪声密度错当成采样标准差会让滤波器过度自信约 14 倍。放在第一步，是因为后面所有 VIO 系统（无论滤波还是优化）共用这套旋转扰动与 IMU 模型。

## 第二步：关键帧优化怎样长成一个完整系统

读讲义第八、九节，再按 [PTAM](../../papers/ptam/README.md) → [ORB-SLAM](../../papers/arxiv-1502.00956/README.md) → [ORB-SLAM3 精读](../../papers/orb-slam3/reading.md)的顺序。每读一篇，写下它点名的前作失败（PTAM 点名 EKF-SLAM 的规模，ORB-SLAM 点名 PTAM 的小场景与无回环，ORB-SLAM3 点名 DBoW2 的召回）。放在第二步，是因为 ORB-SLAM3 是后面学习式系统最常用的对照，不懂它在哪些序列上失败，就读不懂后来者的表格。

## 第三步：视觉惯性的两种实现

对照读 [MSCKF](../../papers/msckf/README.md)、[VINS-Mono](../../papers/arxiv-1708.03852/README.md) 与 [EqVIO](../../papers/arxiv-2205.01980/README.md)。问题只有一个：线性化误差在哪里进入、各自怎样处理（MSCKF 一次线性化，VINS-Mono 在滑窗里反复重新线性化，EqVIO 改误差定义让线性化尽量精确）。放在这里，是因为它把前两步的两个基线接到同一个问题上；尺度为什么要靠运动激励，回到 ORB-SLAM3 精读的初始化手算。

## 第四步：学习式对应与稠密地图赢在哪里、输在哪里

读 [DROID-SLAM](../../papers/arxiv-2108.10869/README.md) → [NICE-SLAM](../../papers/arxiv-2112.12130/README.md) → [SplaTAM](../../papers/arxiv-2312.02126/README.md)。不要只看它们赢的数字：找出每篇里输给 ORB-SLAM2/3 的那一行（TUM 常规序列），再找出 ORB-SLAM3 失败的那一行（TUM fr1 单目、ScanNet++），并记下它们的硬件。放在这里，是因为它们的卖点正是第二、三步系统的失败场景。

## 第五步：前馈 3D 模型当前端

读 [MASt3R-SLAM](../../papers/arxiv-2412.12392/README.md) → [VGGT-SLAM](../../papers/arxiv-2505.12549/README.md) → [VGGT-Long](../../papers/arxiv-2507.16443/README.md) → [VGGT-SLAM 2.0](../../papers/arxiv-2601.19887/README.md)，最后读 [MASt3R-Fusion](../../papers/arxiv-2509.20757/README.md)。每篇都点名修了前一篇的某个问题（显存帧数上限、射影歧义、长序列跟丢、15 自由度漂移、缺公制尺度），按入门页阶段 5 的表核对。放在最后读，是因为这一阶段把前四步的后端部件（位姿图、回环、因子图、IMU）又全部用了回来。

## 第六步：自己检验

给定一个部署场景，先预测哪类系统会失败、为什么，再到论文里找证据。三个练习：

1. 四足机器人在白墙走廊里快速转身：分别说出 ORB-SLAM3、VINS-Mono、SplaTAM、VGGT-SLAM 2.0 各自可能在哪一步出问题，依据是哪篇原文的哪一处。
2. 手持单目相机、不知道相机内参：哪些系统还能用，各自得到的轨迹单位是什么。
3. 一段 4 km 的车载序列：哪些前馈系统会显存溢出，哪个修补方案在 KITTI 上的平均误差与经典方法相当。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
