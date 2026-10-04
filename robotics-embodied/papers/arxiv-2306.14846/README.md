# ViNT: A Foundation Model for Visual Navigation

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2306.14846)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：能否训练一个像视觉或语言基础模型那样、可零样本部署到新机器人并适配新任务的通用视觉导航模型。
- **核心方法**：在 8 种机器人、超过 100 小时的公开轨迹上训练 31M 参数的 Transformer，预测动作与到图像目标的时间距离；用软提示把 GPS、路线指令等新目标形式映射进目标 token，用扩散模型生成子目标做长程探索。零样本控制训练中没有的 Go1 四足。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 5 步：跨机器人导航基础模型的代表，与 [NoMaD](../arxiv-2310.07896/README.md) 同组。优先级：选读。
