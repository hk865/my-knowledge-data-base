# Scaling Rectified Flow Transformers for High-Resolution Image Synthesis

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.03206)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：整流流（把数据与噪声用直线相连）理论性质更好，却还不是标准做法；用交叉注意力把固定的文本表示接进图像模型，对提示的理解有限。
- **核心方法**：在潜空间（下采样 8 倍、通道数加到 16 的自编码器）里用整流流训练，并把训练时的时间采样偏向中段（logit-normal）；在比较的 61 种扩散与流的组合中，只有改了时间采样的整流流胜过此前 LDM 的 ε 预测加线性日程，均匀采样时间的整流流并不更好。主干 MM-DiT 让文本与图像两路 token 各用一套权重、在注意力中双向交换信息；文本编码器用 CLIP-L、CLIP-G 与 T5-XXL 三个；训练描述一半换成模型生成的描述。最大 8B 模型在 1024² 加 DPO 偏好对齐后 GenEval 总分 0.74（DALL·E 3 为 0.67）；验证损失随规模平滑下降，图像与视频预实验都未见饱和。推理时去掉 4.7B 参数的 T5，人评胜率在美学上为 50%、提示遵循 46%、写字 38%，大语言模型编码器主要帮在文字与复杂描述上。局限：GenEval 中位置一项最好只有 0.33–0.40，是各项最低；潜空间方案的上限受自编码器重建限制。摘要承诺公开实验数据、代码与权重。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 9 个节点，[Baseline 页](../../fields/generation/BASELINES.md)现代图像配方（潜空间、整流流、MM-DiT、大文本编码器、偏好对齐）的完整样本；[Seedance 1.0](../arxiv-2506.09113/README.md) 的空间层直接采用 MM-DiT。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2403.03206 · [全文 PDF](https://arxiv.org/pdf/2403.03206) · Stability AI
- 名称：通称 Stable Diffusion 3
- 方向：multimodal/generation
