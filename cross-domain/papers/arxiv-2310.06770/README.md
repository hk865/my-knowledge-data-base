# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.06770)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有 benchmark 饱和，HumanEval 这类代码题大多几行就能写完；真实的软件工程需要在大仓库里定位、跨文件协调修改（§1）。
- **核心方法**：从 12 个流行 Python 仓库的约 9 万个 PR 中筛出 2,294 个任务：每个任务给出 GitHub issue 文本与修复前的代码库，模型生成补丁，用该 PR 带来的单元测试判定——修复前失败、修复后通过的测试叫 fail-to-pass，另有原本就通过的回归测试。用 BM25 检索代码时，最好的 Claude 2 只解决 1.96%。另发布 1.9 万条训练实例 SWE-bench-train 与微调模型 SWE-Llama；收集流程可持续加入训练截止之后的新 issue。自述局限：只有 Python；只是简单基线；只靠执行测试不足以保证生成的代码可靠，模型写的补丁常常不如人写的完整、高效、可读（Conclusion 前的 Limitations）。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)"执行判分"一步的代表，也是代码智能体评测与训练环境的原型：后来的 RL 报告（[Kimi K2](../../../llm/papers/arxiv-2507.20534/README.md)）用同样的"issue + 可执行单元测试"从 GitHub 搭训练环境。它自述的"测试通过 ≠ 可读、可维护"正是代码风格类评测要补的缺口（见[各领域评测](../../fields/evaluation/domains.md)）。后续：[SWE-agent](../../../llm/papers/arxiv-2405.15793/README.md)、[SWE-bench Verified](../openai-swe-bench-verified/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2310.06770 · [全文 PDF](https://arxiv.org/pdf/2310.06770) · Princeton University、University of Chicago
- 发表：ICLR 2024
- 方向：cross-domain/evaluation、cross-domain/agents
