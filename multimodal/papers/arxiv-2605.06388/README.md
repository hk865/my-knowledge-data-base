# Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2605.06388)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用动作条件视频扩散模型评估机器人策略越来越常见，这些模型多做潜空间扩散（LDM：在编码器压缩后的潜变量上做扩散），但潜空间该怎么选没有系统比较：现状多用为像素重建训练的 VAE 类潜空间，另有工作提示语义对齐的预训练编码器更好。
- **核心方法**：在 BridgeV2 数据上，按固定协议用六种编码器（重建型如 VAE、Cosmos；语义型如 V-JEPA 2.1、Web-DINO、SigLIP 2）的潜空间各训练一个动作条件 LDM 世界模型，含压缩与不压缩维度两种做法，并从三个轴评估：视觉保真度、规划与下游策略表现、潜表示质量。结论：重建型编码器的像素指标最好，语义型在另外两个轴上普遍更好，V-JEPA 2.1 在策略上总体最强；视觉保真度不足以用来挑选世界模型。
- **为什么在这个库里**：[机器人侧世界模型入门页](../../../robotics-embodied/fields/world-models/README.md)"从测量看"一节与[基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"⑥ 评估"一行，"怎样挑世界模型"这一开放问题的入口；与 [LARY](../arxiv-2604.11689/README.md) 结论一致，也与[视觉表征方向](../../fields/visual-representation/README.md)"冻结编码器服务多个任务"的趋势相连。做不好的场景：结论只限于 BridgeV2 的操作场景和同一个机器人本体；策略在环实验只评估一个固定的 VLA 策略（Sec.7）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2605.06388 · [全文 PDF](https://arxiv.org/pdf/2605.06388) · Chandar Research Lab、Mila – 魁北克人工智能研究所、蒙特利尔理工学院
- 方向：multimodal/world-models、robotics/embodied-policies
