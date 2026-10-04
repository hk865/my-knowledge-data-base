# Speculative Speculative Decoding

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2603.03251)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：普通投机解码仍要先等本轮验证结束，才能开始下一轮草稿，这段串行等待限制了速度。
- **核心方法**：SSD 在独立设备上为可能的验证结果预写下一轮草稿；实际结果命中缓存就直接取用，未命中则启用备用草稿器，取出的候选仍按通常规则验证。
- **为什么在这个库里**：[推理基线](../../fields/inference/BASELINES.md)的“执行顺序”一格，与改草稿网络的 [DFlash](../arxiv-2602.06036/README.md)互补；适合接在[草稿—验证导读](../../fields/inference/draft-verification-guide.md)的成本算例之后。优先级：选读。

## 批注

**易误读**
- 验证结果包括接受了多长、末尾补了哪个 token；仅预测“整块是否通过”不能覆盖全部分支。
- 独立草稿设备、预计算缓存和未命中回退都计入总成本。缓存命中节省等待，最终保真仍来自验证规则。

**版本差异**
- ICLR 摘要页保留“最高 2 倍”的早期表述，正式 PDF 摘要写相对最强投机基线平均快 30%。本卡仅说明机制，跨实现比较应读正式版实验设置。

## 身份信息

- 作者：Tanishq Kumar、Tri Dao、Avner May（Stanford University、Princeton University、Together AI）
- 稳定标识：arxiv:2603.03251 · ICLR 2026 · [正式 PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/1b96f01343ff10150e6719eb163e1536-Paper-Conference.pdf)
- 代码：[tanishqkumar/ssd](https://github.com/tanishqkumar/ssd)
- 方向：llm/inference
