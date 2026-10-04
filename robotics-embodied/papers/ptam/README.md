# Parallel Tracking and Mapping for Small AR Workspaces

> 状态：文献卡 · 2007 · [原文](https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：手持单目相机的实时跟踪与建图：MonoSLAM 一类增量系统每帧同时更新位姿和全部路标，数据关联错误会不可挽回地破坏地图。
- **核心方法**：把跟踪和建图拆成两个并行线程，建图只处理关键帧，用 BA 批量优化（探索时局部 BA、空闲时全局 BA）。同一段 600 帧合成序列上，地图点从 EKF-SLAM 的 114 个增加到 6600 个，误差标准差从 135 mm 降到 6 mm。原文写明的失败：运动模糊使角点消失、重复结构产生大量外点、场景大幅改变会失败、不设计闭合大回环，实用上限约 6000 点、150 个关键帧。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 2 的起点，ORB-SLAM 从它的双线程架构出发、点名修它的小场景与无回环。优先级：选读。

## 身份信息

- 稳定标识：url:https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf · [全文 PDF](https://www.robots.ox.ac.uk/~gk/publications/KleinMurray2007ISMAR.pdf) · Georg Klein、David Murray（University of Oxford Active Vision Laboratory）
- 发表：ISMAR 2007（作者主页）
- 方向：robotics/localization-mapping
