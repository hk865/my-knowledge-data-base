# Introducing SWE-bench Verified

> 状态：文献卡 · 2024 · [原文](https://openai.com/index/introducing-swe-bench-verified/)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：SWE-bench 是 OpenAI 准备框架（Preparedness Framework）中"模型自主性"风险的指标之一，但部分任务难以甚至不可能解决，会系统性低估模型的软件工程能力。
- **核心方法**：93 位有 Python 经验的开发者标注 1,699 个随机抽取的 SWE-bench 测试样本，每个样本由 3 人独立判断"issue 描述是否不完整"和"fail-to-pass 测试是否会把正确解判错"（各 0–3 级，取 3 人中最严重的）。38.3% 被标为描述不完整，61.1% 被标为测试可能误判正确解，合计 68.3% 被剔除；最终挑出 500 个样本作为 SWE-bench Verified，并配套容器化的评测环境。GPT-4o 在最佳开源脚手架上从原版的 16% 升到 33.2%。讨论一节写明：基于公开 GitHub 的静态数据集很可能已被预训练模型见过；同一模型换脚手架，SWE-bench Lite 上从 2.7% 到 28.3%，所以风险评估要把外部增强也算进去。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"执行判分也会错"的证据：判分器（单元测试）本身有大面积的假阴性，修的是测试而不是模型。它在 2026 年又被同一机构宣布退役，见 [SWE-bench Verified 退役说明](../openai-swe-bench-verified-retired/README.md)。前作 [SWE-bench](../arxiv-2310.06770/README.md)。优先级：必读。

## 身份信息

- 稳定标识：url:https://openai.com/index/introducing-swe-bench-verified/ · OpenAI（与 SWE-bench 作者合作） · 发布于 2024-08-13（2025-02-24 更新）
- 发表：官方博客
- 方向：cross-domain/evaluation、cross-domain/agents
