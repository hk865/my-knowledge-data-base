# Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.16860)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VLM 的视觉组件选择缺少系统研究；过早依赖语言会掩盖视觉表征的缺陷；现有 benchmark 不能指导真实场景的视觉接地，传统的表征评测协议（线性评测、微调）已经饱和。
- **核心方法**：把视觉指令微调当作视觉表征的评测协议，比较 23 个视觉骨干（语言监督、自监督及其组合）。主要发现：多数 benchmark 测不到视觉中心能力，ScienceQA 图像子集、MMMU、MathVista、AI2D 开图与关图差距不到 5%；解冻视觉编码器普遍有益；两段训练并加大适配数据有益；高分辨率与卷积编码器利于图表和视觉中心任务；组合多种编码器（含 DINOv2）有益。另提出空间感知连接器 SVA（576 个 token 在图表与视觉中心任务上胜过用 2880 个的模型）、2638 题的 CV-Bench 和 700 万条的数据配方。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 6 个节点与开放问题"视觉塔与连接器怎样训"的主要证据，也把 VLM 接回[视觉表征方向](../../fields/visual-representation/README.md)。自述没有采用任意分辨率；只按 benchmark 优化会得到"答题机器"；主要做 SFT，未做 RL。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2406.16860（Shengbang Tong 等 14 位作者；当前 v2，2024-12）· [全文 PDF](https://arxiv.org/pdf/2406.16860v2) · New York University · NeurIPS 2024（Oral）
- 方向：[视觉语言模型](../../fields/vlm/README.md)、[视觉表征](../../fields/visual-representation/README.md)
