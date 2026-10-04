# DFlash: Block Diffusion for Flash Speculative Decoding

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2602.06036)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：现有投机解码（草拟器先猜一段 token、目标模型并行验证）的草拟仍是自回归的，草拟本身串行，限制了实际加速；扩散语言模型能并行生成，但质量通常不如自回归模型。
- **核心方法**：相对 EAGLE-3 等自回归草拟器，用轻量的块扩散模型（一次前向并行填满一整块被遮盖的位置）做草拟：一次前向生成整块草稿 token，并以从目标模型多层隐状态中提取的上下文特征为条件（注入草拟器每一层的 K/V）；草稿仍由目标模型验证。在多种模型和任务上无损加速 6 倍以上，加速比最多是 EAGLE-3 的 2.5 倍。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"草拟器设计"一格中并行草拟的代表；对照 [EAGLE-3](../arxiv-2503.01840/README.md) 读，后续 [DFlash 2](../dflash-2/README.md) 在其上加路径选择。优先级：选读。

## 批注

**未核实 / 待验证**
- 论文称无损（lossless）；草拟方法见 §3–4，验证部分的实现代码未审计。

## 身份信息

- 稳定标识：arxiv:2602.06036 · [全文 PDF](https://arxiv.org/pdf/2602.06036) · ICML 2026（arXiv v2 为 camera-ready）· 代码在 z-lab/dflash
- 作者：Jian Chen、Yesheng Liang、Zhijian Liu（UC San Diego）
- 方向：llm/inference
