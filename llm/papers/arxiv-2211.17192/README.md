# Fast Inference from Transformers via Speculative Decoding

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2211.17192)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：大型自回归模型生成 K 个 token 要串行运行 K 次，延迟高；希望不改模型、不重新训练，并且不改变输出分布地加速。
- **核心方法**：分块并行解码（Stern 等 2018）只支持贪心解码、需要额外训练专用模型，也只保证下游质量；本篇提出投机解码：小模型先顺序草拟若干 token，大模型一次前向并行算出这些位置的条件分布，从左到右以 min(1, 大模型概率/小模型概率) 接受；第一次拒绝处丢弃后面的草稿，从归一化的 max(大模型分布−小模型分布, 0) 中补采一个 token；全部接受时再从大模型末位分布多采一个。这种修正的拒绝采样使输出分布与大模型单独采样完全相同。在 T5-XXL 上比标准 T5X 实现快 2–3 倍，输出相同。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"大小模型协作"一线的起点和"精确目标分布"的参照：后来的 [EAGLE-3](../arxiv-2503.01840/README.md)、[DFlash](../arxiv-2602.06036/README.md) 改草拟器，[Judge Decoding](../arxiv-2501.19309/README.md)、[BiLD](../arxiv-2302.07863/README.md) 放宽验证，[Faster Cascades](../arxiv-2405.19261/README.md) 改目标分布，都以它为对照。[两图机制导读](../../fields/inference/draft-verification-guide.md)有手算示例。优先级：必读。

## 批注

**易误读**
- 加速比取决于接受率、草拟开销与硬件；"分布相同"指采样分布相同，不等于同一随机种子下逐字相同（§2–3）。

**与其他论文的关联**
- [Chen 等 2023](../arxiv-2302.01318/README.md) 独立同期提出了同一核心机制，侧重分布式部署。

## 身份信息

- 稳定标识：arxiv:2211.17192 · [全文 PDF](https://arxiv.org/pdf/2211.17192) · ICML 2023（Oral）
- 作者：Yaniv Leviathan、Matan Kalman、Yossi Matias（Google Research）
- 方向：llm/inference
