# iMAP: Implicit Mapping and Positioning in Real-Time

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2103.12352)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：固定分辨率的体素表示内存开销大，隐式神经表示此前只能离线训练数小时到数周。
- **核心方法**：用一个约 1 MB 的 MLP 作为唯一的地图，在 RGB-D 视频上在线训练；仿 PTAM 分跟踪与建图两个进程，用关键帧回放防止遗忘，按损失主动采样像素。Replica 上完整度 79.06%（TSDF 75.09%），但精度 4.43 cm 差于 TSDF 的 3.45 cm；TUM 上 fr1/desk 4.9 cm，ORB-SLAM2 为 1.6 cm。跟踪 10 Hz、建图 2 Hz，只验证到房间尺度。
- **为什么在这个库里**：[Baseline 页](../../fields/localization-mapping/BASELINES.md)"地图表示"一格的起点；NICE-SLAM 点名修它的全局更新与大场景失效。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2103.12352 · [全文 PDF](https://arxiv.org/pdf/2103.12352v2) · Edgar Sucar、Shikun Liu、Joseph Ortiz、Andrew J. Davison（Imperial College London Dyson Robotics Lab）
- 发表：ICCV 2021（官方项目页）
- 方向：robotics/localization-mapping
