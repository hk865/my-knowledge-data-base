# Direct Sparse Odometry

> 状态：文献卡 · 2016 · [原文](https://arxiv.org/abs/1607.02565)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：特征法只能用角点，稠密与半稠密直接法的几何先验让实时、统计一致的联合优化不可行。
- **核心方法**：稀疏加直接：在滑窗内联合优化位姿、内参和逆深度，最小化光度误差，并标定曝光、渐晕和相机响应。原文结论：在 TUM monoVO 与 ICL-NUIM 上精度和鲁棒性优于单目 ORB-SLAM（对比时关闭了 ORB-SLAM 的回环与重定位），在 EuRoC 上 ORB-SLAM 更准；几何噪声增大时性能迅速恶化，对卷帘快门和内参误差更敏感，普通手机和网络摄像头更适合特征法。v2 修正了一个使 ORB-SLAM 实时结果被低估的 bug。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)中直接法一支的代表，[Baseline 页](../../fields/localization-mapping/BASELINES.md)"前端"一格；与 ORB-SLAM 的口径之争见入门页阶段 2。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1607.02565 · [全文 PDF](https://arxiv.org/pdf/1607.02565v2) · Jakob Engel、Vladlen Koltun、Daniel Cremers（TU Munich、Intel Labs）
- 发表：IEEE TPAMI 2018（官方项目页）
- 方向：robotics/localization-mapping
