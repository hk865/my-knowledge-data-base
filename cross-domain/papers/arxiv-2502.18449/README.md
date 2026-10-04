# SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2502.18449)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多数软件工程 agent 依赖 GPT-4o、Claude 3.5 Sonnet 这类闭源模型，进步来自提示策略而不是模型本身；执行式 RL 受执行成本和缺少可执行环境的限制（§1）。
- **核心方法**：不执行代码。从 GHArchive（2015 年至 2024 年 8 月）聚合出约 1,100 万个去重的 PR 实例，排除 SWE-bench 用到的仓库；只训练"给定 issue 与相关文件，生成 search/replace 编辑"这一个子任务。奖励：格式错为 −1，否则为预测补丁与真实补丁的 difflib 序列相似度（0 到 1）；算法为 GRPO（§1、§2）。推理时接一条非交互的流水线（Agentless Mini），采 500 个补丁再重排，Llama3-SWE-RL-70B 在 SWE-bench Verified 上 41.0%（同表 GPT-4o + Agentless 38.8%，DeepSeek-R1 + Agentless 49.2%，Table 1）。只在补丁修复上做 RL，MATH 从 63.2 升到 73.7，同数据做 SFT 反降到 54.0（Table 3）。自述局限（§5）：相似度奖励不认语义等价的其他解法；流水线结构使模型无法从交互反馈中学习；需要大量采样。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"把 agent 能力训进模型"阶段的另一种奖励：奖励的是"像人写的补丁"，而不是"测试通过"，因此不存在跳过测试这类空子，代价是只认一种写法。与 [SWE-Gym](../arxiv-2412.21139/README.md) 对照着读。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2502.18449 · [全文 PDF](https://arxiv.org/pdf/2502.18449)
- 作者：Yuxiang Wei、Olivier Duchenne、Jade Copet、Quentin Carbonneaux、Lingming Zhang、Daniel Fried、Gabriel Synnaeve、Rishabh Singh、Sida I. Wang（Meta AI（FAIR）、UIUC、CMU；NeurIPS 2025）
- 开放情况：代码（提示模板、奖励函数、Agentless Mini）开放：github.com/facebookresearch/swe-rl（主体 CC BY-NC 4.0）；模型权重与数据是否发布未核实。
- 方向：cross-domain/agents、llm/posttraining/rl
