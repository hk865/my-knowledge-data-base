# AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.19518)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：前馈 3D 模型做 SLAM 时规模上不去：[MASt3R-SLAM](../arxiv-2412.12392/README.md)、[VGGT-SLAM 2.0](../arxiv-2601.19887/README.md) 一类在 KITTI 长序列上误差很大，显存也撑不住公里级、上万帧的轨迹。
- **核心方法**：UCL（Wang、Agapito）的实时单目 SLAM。前端用 80M 参数的 DA3-Small（[Depth Anything 3](../arxiv-2511.10647/README.md) 的最小版本）做低延迟跟踪；后端是分层的 Sim(3) 位姿图：子图内相邻关键帧的稠密局部约束、跨子图的稀疏长程约束、DBoW2 回环，不做 BA，只优化关键帧之间的相对位姿。可以接双目、RGB-D 和激光雷达，不假设静态世界。KITTI 单目平均 ATE 13.11 m，作者表中 VGGT-SLAM 2.0 为 92.72 m、MASt3R-SLAM 为 186.64 m、同样用 DA3 的分块基线 DA3-Long 为 16.83 m；VBR、Oxford Spires 上 ATE 比此前方法降低 70% 以上；RTX 4090 上单目 17.6 fps、加激光雷达 47.8 fps，峰值显存 10–14 GB。作者写明地图是点云而非紧凑的表面表示，会出现重复表面和重影。
- **为什么在这个库里**：[定位与建图方向](../../fields/localization-mapping/README.md)阶段 5 的最新节点（2026-09），直接检验该页"前馈模型替换前端、没有替换后端"的判断：它的公里级能力来自 DBoW2 回环加分层位姿图这一经典后端。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2609.19518（Hengyi Wang、Lourdes Agapito，University College London；v1，2026-09-17）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2609.19518) · [项目页](https://hengyiwang.github.io/projects/amber-slam)
- 方向：[定位与建图](../../fields/localization-mapping/README.md)
