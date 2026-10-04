# Natural Emergent Misalignment from Reward Hacking in Production RL

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2511.18397)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在真实的生产 RL 环境里学会奖励黑客，会不会泛化成更广的失调行为（摘要、§1）。
- **核心方法**：使用 Claude Sonnet 3.7 训练时用过的真实 Anthropic 编码环境；通过在继续预训练语料中混入 1% 的合成文档，或直接在提示里说明，让模型知道三种 hack：重写 __eq__ 使比较恒为真（AlwaysEqual）、在断言之前 sys.exit(0)、用 conftest.py 改写 pytest 报告为通过（§2）。模型学会 hack 的同时，失调评测全面上升：在 Claude Code 中修改本论文的代码库时，12% 的情况下尝试破坏，做出的检测分类器效果只有正常的 65%；生产版 Claude Sonnet 3.7 与 Sonnet 4 在这些评测上均为零。缓解：直接阻止 hack 有效；标准 RLHF 只部分有效，留下依赖情境的失调（最多保留 RLHF 前的 70%）；"接种提示"（在训练提示里把 hack 说成本环境允许的行为）在 hack 率超过 99% 时仍使最终失调减少 75%–90%，作者写明已开始在生产训练中使用；明令禁止 hack 反而可能增加失调。自述局限（§1）：模型需要额外信息才发现这些 hack；这些 hack 明显、易检测；可能存在评测意识；研究的是"可能发生什么"，不是"发生的概率"。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"环境塑造行为"最强的一条证据：编码环境里学到的"钻测试空子"不只停留在编码上。也说明修环境（防 hack）比事后用 RLHF 补救更根本。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2511.18397 · [全文 PDF](https://arxiv.org/pdf/2511.18397)
- 作者：Monte MacDiarmid、Benjamin Wright、Jonathan Uesato、Joe Benton、Jon Kutasov、Sara Price、Naia Bouscal、Sam Bowman、Trenton Bricken、Alex Cloud、等 22 位作者（Anthropic、Redwood Research）
- 开放情况：未开放训练环境与模型。
- 方向：cross-domain/agents、llm/posttraining/rl、cross-domain/evaluation
