# Flow Matching for Generative Modeling

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2210.02747)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：扩散模型能规模化、训练稳定，但只能用由简单扩散过程定义的少数概率路径，训练时间长、采样也要专门方法才能高效。连续归一化流（用神经 ODE 把噪声连续变换成数据）表达力强，以往却要靠模拟 ODE 训练，难以扩大。
- **核心方法**：不模拟 ODE，直接回归一条事先选定的"条件概率路径"的速度场（流匹配）；扩散路径是其中的特例，另一选择是最优传输（OT）路径：从噪声到数据走直线、速度恒定。同一个 U-Net 下，OT 路径在 ImageNet 32×32 上达到同样数值误差约只需扩散路径 60% 的函数调用；ImageNet 128×128 无条件 FID 20.9，训练 50 万步、批量 1.5k，对照 ADM 的 436 万步、批量 256。作者自述 CIFAR-10 上 FID 不如以往工作，可能因所用结构没有针对它优化。论文未声明代码发布。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 9 个节点，[Baseline 页](../../fields/generation/BASELINES.md)部件 4"流匹配"一格。2024 年后的视频报告（[HunyuanVideo](../arxiv-2412.03603/README.md)、[Wan](../arxiv-2503.20314/README.md)、[Seedance 1.0](../arxiv-2506.09113/README.md)）与机器人的连续动作头（[π0](../../../robotics-embodied/papers/arxiv-2410.24164/README.md)）都写明用流匹配。手算见[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6.1 节。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2210.02747 · [全文 PDF](https://arxiv.org/pdf/2210.02747) · Meta AI (FAIR)、Weizmann Institute of Science
- 方向：multimodal/generation
