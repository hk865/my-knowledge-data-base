# Agent：阅读与问题路线

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md)

五步，每步配一道检验题。答不出检验题，回到对应的论文再读。

## 第一步：画出一次 agent 循环

读 [ReAct 精读](../../papers/react/reading.md)，再读 [SWE-agent](../../../llm/papers/arxiv-2405.15793/README.md) 与 Anthropic 的[构建高效 agent](https://www.anthropic.com/engineering/building-effective-agents)。

**检验题**：SWE-agent 的消融里，"一次显示整个文件"比"每次显示 100 行"低 5.3 个百分点，"逐条翻看的迭代搜索"比"不给搜索工具"还低。用"上下文与预算"解释这两个结果。

## 第二步：把一个 benchmark 写成 RL 环境

读 [τ-bench](../../papers/arxiv-2406.12045/README.md) 与 [Terminal-Bench](../../papers/arxiv-2601.11868/README.md)，对照入门页"评测就是强化学习的环境"一表。

**检验题**：为 τ-bench 写出状态、动作、转移、奖励。作者说 r = 1 只是成功的必要条件，举一个得 1 分却违反业务政策的轨迹。再说明 pass^k 与 pass@k 回答的问题有什么不同，为什么 agent 部署更关心前者。

## 第三步：比较两种训练奖励

读 [SWE-Gym](../../papers/arxiv-2412.21139/README.md) 与 [SWE-RL](../../papers/arxiv-2502.18449/README.md)，再读 [Kimi K2](../../../llm/papers/arxiv-2507.20534/README.md) §3.1–3.2、[DeepSeek-V3.2](../../../llm/papers/arxiv-2512.02556/README.md) §3.2。

**检验题**：同一个 issue，一个补丁和真实补丁写法完全不同但测试全过，另一个补丁和真实补丁很像但漏了一个边界情况。在"测试通过"与"补丁相似度"两种奖励下各得多少分？各自会把策略推向什么方向？

## 第四步：找出奖励的漏洞

读 [Baker 等](../../papers/arxiv-2503.11926/README.md) 第 2 节与 [Claude 4 系统卡](../../papers/anthropic-claude-4-system-card/README.md) §6。

**检验题**：找一个你自己用过的、用 pytest 判定的任务，列出至少三种"不实现功能也能让测试通过"的做法（可参考 `exit(0)`、`raise SkipTest`、改 `conftest.py`、重写 `__eq__`）。再为每一种写出环境层面怎样堵住它，而不是靠提示禁止。

## 第五步：测试看不到的行为

读 [MacDiarmid 等](../../papers/arxiv-2511.18397/README.md)、[codex-1 系统卡附录](https://cdn.openai.com/pdf/8df7697b-c1b2-4222-be00-1fd3298f351d/codex_system_card.pdf) §2.3、[GPT-5.1-Codex-Max 系统卡](https://openai.com/index/gpt-5-1-codex-max-system-card/) §4.3。

**检验题**："只改用户要求的那一处""不回退用户未提交的改动""做不到时如实说明"这三种行为，测试都检查不到。对每一种，写出 OpenAI 或 Anthropic 公开材料里用了什么信号去训练或评测它；如果公开材料里没有，写出你会怎样构造一个可自动判定的环境。

## 往哪里去

- 奖励黑客与"奖励从哪来"的一般机制：[语言模型强化学习](../../../llm/fields/posttraining/rl/README.md)。
- 评测的效度、污染与隐藏数据：[评估方向](../evaluation/README.md)。
- 机器人上的 agent：[具身 Agent](../../../robotics-embodied/fields/embodied-agents/README.md)。

## 工程安全与集成

先读[权限、隔离与协作](permissions-isolation-collaboration.md)，再比较[CaMeL](../../papers/camel/README.md)的数据流策略、[Cedar](../../resources/cedar-authorization/README.md)的工具授权与[持续集成](../../resources/continuous-integration/README.md)的结果验证：三者解决不同层次的问题。
