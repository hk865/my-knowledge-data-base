# LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2505.11528)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让世界模型预测机器人与物体交互的未来画面以辅助策略，但在像素层面预测得准很难。
- **核心方法**：不预测像素，而在预训练视觉基础模型的潜空间里用扩散模型预测未来：几何特征取自 DINO，语义特征取自 SigLIP（作者归为"CLIP 类"），两路之间用交互式扩散做交叉注意力；世界模型在与任务无关的片段上训练。再设计一个扩散策略，把世界模型"想象"出的未来潜状态作为额外输入，迭代修正输出的动作。LIBERO-LONG 上策略成功率提升 27.9%，真实场景提升 20%。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"① + ④"一行；与 [DINO-WM](../arxiv-2411.04983/README.md) 同在"冻结特征上预测"一线，但用法从"规划"换成"给模仿学习策略提供预见"，下游策略沿用 [Diffusion Policy](../../../robotics-embodied/papers/diffusion-policy/README.md) 的扩散动作生成。做不好的场景：训练样本规模有限；更长时距的预测因误差累积而不准，作者把记忆机制列为后续方向（Sec.6）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2505.11528 · [全文 PDF](https://arxiv.org/pdf/2505.11528) · 国防科技大学、北京大学、深圳大学 · CoRL 2025
- 方向：multimodal/world-models、robotics/embodied-policies
