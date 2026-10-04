# LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2207.04429)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：按自然语言指令导航通常需要大量带语言标注的轨迹，采集代价高。
- **核心方法**：不训练新模型，把三个预训练模型拼起来：GPT-3 从指令中抽出地标序列，CLIP 把地标对到预先建好的拓扑图中的图像，ViNG 导航模型负责在图上走。20 次真实实验、6 km 以上路线中净成功率 85%，只用 GPS 的基线 23%；失败多来自 VLM 认不出的地标，指令中的动词被忽略。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 5 步：基础模型拼装式导航的代表，结构与 [SayCan](../saycan/reading.md) 的打分选择相同。优先级：必读。
