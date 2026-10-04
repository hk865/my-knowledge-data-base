# Scaling Laws for Neural Language Models

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2001.08361)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：语言模型的性能怎样随模型大小、数据量、训练算力变化？给定一笔算力，应该花在参数上还是数据上？
- **核心方法**：在 WebText2 上训练一系列 decoder-only Transformer，拟合测试交叉熵与非嵌入参数量 N、数据量 D、算力 C 的关系：只受其中一项限制时，损失分别按幂律下降（指数约 0.076、0.095、0.050），趋势跨越 7 个以上数量级，深度、宽度等形状的影响很小。过拟合程度由 N^0.74/D 决定：模型加大 8 倍，数据约加 5 倍即可避免损失。据此推出计算最优的配比是参数量约按 C^0.73 增长，即算力增加时主要加大模型，并在收敛前停止训练（§1）。
- **为什么在这个库里**：[训练科学方向](../../fields/training-science/README.md)主线节点 5"规模定律"的起点，也是"规模定律能外推多远"这一开放问题的入口：作者写明规律没有可靠的理论解释，按趋势外推在约 10^12 参数处两条规律相互矛盾；它的"主要加参数"配比后来被 [Chinchilla](../arxiv-2203.15556/README.md) 修正为参数与数据等比例。同组的 [Henighan 等](../arxiv-2010.14701/README.md)把同一套方法推广到图像、视频、图文与数学；[GPT-3](../../../llm/papers/gpt3/reading.md) 的规模选择依据了本篇。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2001.08361 · [全文 PDF](https://arxiv.org/pdf/2001.08361) · OpenAI、Johns Hopkins University · arXiv 预印本
- 作者：Jared Kaplan、Sam McCandlish、Tom Henighan、Tom B. Brown、Benjamin Chess、Rewon Child、Scott Gray、Alec Radford、Jeffrey Wu、Dario Amodei
- 方向：cross-domain/training-science、llm/pretraining
