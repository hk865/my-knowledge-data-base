# How Far is Video Generation from World Model: A Physical Law Perspective

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2411.02385) · ICML 2025

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：业界相信"把视频生成做大就能得到遵守物理的世界模型"。真实视频纹理复杂、物理难以定量，所以这个信念一直没被检验：模型到底是学到了规律，还是记住了数据？
- **核心方法**（PhyWorld）：用 2D 模拟器生成只由一两条经典力学规律决定的视频（匀速运动、弹性碰撞、抛体），按 Sora 的结构（VAE + DiT）训练视频扩散模型，数据从 3 万到 300 万段、参数从 22M 到 310M，再从生成的像素里解析出物体位置算速度误差。分布内误差随规模下降到接近真值视频（0.012 对 0.010）；分布外（速度等参数超出训练范围）误差高一个数量级（0.427），并且不随数据和模型增大而下降；组合泛化随数据增大明显改善（异常比例 67% → 10%）。分析显示模型按"最相近的训练样例"泛化，参考训练数据时的属性优先级是颜色 > 大小 > 速度 > 形状：训练集里只有红球和蓝方块时，一个红方块在条件帧之后会变成球。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)"站在现在看过去"的关键反证：它给 Sora 式"规模即物理"的说法设了边界，并为"物体在生成中不保持一致"提供了机制解释（形状优先级最低）。NVIDIA 的 [Cosmos](../arxiv-2501.03575/README.md) 物理对齐评测写明受它启发。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2411.02385 · [全文 PDF](https://arxiv.org/pdf/2411.02385v2) · ByteDance Research、清华大学、Technion
- 方向：multimodal/world-models、multimodal/generation、cross-domain/evaluation
