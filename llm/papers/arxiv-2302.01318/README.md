# Accelerating Large Language Model Decoding with Speculative Sampling

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2302.01318)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Chinchilla 70B 这类大模型在分布式环境下逐 token 采样代价高、效率低。
- **核心方法**：与 Leviathan 等独立同期提出同一核心思路：快而弱的草拟模型生成短续写，目标模型并行打分；作者观察到打分 K+1 个位置的延迟与采样 1 个 token 相近（在小批量、受显存带宽限制时成立）。再用修正的拒绝采样在硬件数值精度内保持目标分布；温度、top-k、nucleus 等采样设置先作用于分布再做验证。在分布式设定下对 Chinchilla 70B 解码加速 2–2.5 倍，样本质量不变。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"精确目标分布"一格的第二个来源，侧重分布式部署和延迟成立的条件；读过 [Leviathan 等的投机解码](../arxiv-2211.17192/README.md) 后作对照即可。优先级：选读。

## 批注

**易误读**
- 本文记号 p 为草拟模型、q 为目标模型，与 [Leviathan 等的投机解码](../arxiv-2211.17192/README.md) 相反，对照公式时要换过来。

## 身份信息

- 稳定标识：arxiv:2302.01318 · [全文 PDF](https://arxiv.org/pdf/2302.01318)
- 作者：Charlie Chen、Sebastian Borgeaud、Geoffrey Irving、Jean-Baptiste Lespiau、Laurent Sifre、John Jumper（DeepMind）
- 方向：llm/inference
