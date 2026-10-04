# DayDreamer: World Models for Physical Robot Learning

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2206.14176)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：真机学习样本昂贵，仿真又有 sim-to-real 差距；世界模型能否让机器人直接在真实世界高效学习。
- **核心方法**：把 Dreamer 直接放到 4 台真实机器人上在线学习、不用仿真器：A1 四足从仰躺开始 1 小时学会翻身、站立、行走，10 分钟适应推搡；UR5、XArm 从像素与稀疏奖励学抓放；Sphero 2 小时内学会视觉导航。作者写明长时间真机学习会磨损硬件。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)主线第 2 步：与你训练四足策略的经验直接对应的世界模型真机案例。优先级：必读。
