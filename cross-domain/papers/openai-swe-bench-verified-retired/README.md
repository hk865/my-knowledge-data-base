# Why SWE-bench Verified no longer measures frontier coding capabilities

> 状态：文献卡 · 2026 · [原文](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：SWE-bench Verified 在过去 6 个月只从 74.9% 升到 80.9%，剩下没解出的题究竟是模型做不到，还是数据集本身有问题。
- **核心方法**：两项审查。一是复盘 o3 在 64 次独立运行中都没解出的 138 题（约占全集 27.6%），每题至少 6 位工程师审查：59.4% 有实质缺陷，其中 35.5% 的测试过窄（例如测试直接导入 issue 里从未提到的函数名），18.8% 过宽（测试覆盖 issue 没描述的其他修复），5.1% 为其他问题。二是污染：GPT-5.2 解出了此前认定几乎不可能的 31 题，思维链显示它知道相关版本的发布说明；用 GPT-5 作为探测者在 15 轮内诱导 GPT-5.2-Chat、Claude Opus 4.5、Gemini 3 Flash Preview，三家模型都在部分任务上复现出参考补丁或逐字背出任务描述。结论：分数提升越来越反映"训练时见过多少题"，OpenAI 停止报告该基准，改报 SWE-bench Pro 的公开子集，并建议发布 benchmark 时用密码保护、训练时严格遵守 canary 字符串，长期投入原创的私有评测（例如领域专家内部编写的 GDPval）。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)主线最后一个节点的证据：公开 benchmark 的生命周期从"建立 → 修订（Verified）→ 退役"在两年内走完；它同时示范了两种审计——人工复核判分器、对抗式诱导检测污染——以及"为什么实验室转向隐藏评测数据"的官方理由。优先级：必读。

## 身份信息

- 稳定标识：url:https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ · OpenAI · 发布于 2026-02-23
- 发表：官方博客
- 方向：cross-domain/evaluation、cross-domain/agents
