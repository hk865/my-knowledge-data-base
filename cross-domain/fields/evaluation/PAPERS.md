# 评估：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [综合表](synthesis.csv)

以下每项链接到唯一的单篇目录。跨方向出现是交叉引用，不重复计算资源。按入门页的结构分组；各领域专属的评测（角色扮演、安全、医疗、法律等）收在[各领域的评测](domains.md)，智能体评测收在 [Agent 方向](../agents/README.md)。

## 基线与方法谱系

- [Measuring Massive Multitask Language Understanding](../../papers/arxiv-2009.03300/README.md)（MMLU）· 2020 · 文献卡 · 静态选择题的基线
- [Holistic Evaluation of Language Models](../../papers/arxiv-2211.09110/README.md)（HELM）· 2022 · 文献卡 · 标准化与多指标
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](../../papers/llm-judge/README.md) · 2023 · 技术精读 · LLM 裁判与成对人评的基线
- [Instruction-Following Evaluation for Large Language Models](../../papers/arxiv-2311.07911/README.md)（IFEval）· 2023 · 文献卡 · 程序可判的指令遵循
- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](../../papers/arxiv-2310.06770/README.md) · 2023 · 文献卡 · 执行判分的基线
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](../../../llm/papers/arxiv-2405.15793/README.md) · 2024 · 文献卡 · 同一评测换接入方式

## 饱和与加难

- [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](../../papers/arxiv-2311.12022/README.md) · 2023 · 文献卡
- [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](../../papers/arxiv-2406.01574/README.md) · 2024 · 文献卡
- [Humanity's Last Exam](../../papers/arxiv-2501.14249/README.md) · 2025 · 文献卡

## 污染、滚动更新与隐藏数据

- [Proving Test Set Contamination in Black Box Language Models](../../papers/arxiv-2310.17623/README.md) · 2023 · 文献卡
- [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](../../papers/arxiv-2403.07974/README.md) · 2024 · 文献卡
- [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](../../papers/arxiv-2405.00332/README.md)（GSM1k）· 2024 · 文献卡
- [LiveBench: A Challenging, Contamination-Limited LLM Benchmark](../../papers/arxiv-2406.19314/README.md) · 2024 · 文献卡
- [Introducing SWE-bench Verified](../../papers/openai-swe-bench-verified/README.md) · 2024 · 官方博客，文献卡
- [Why SWE-bench Verified no longer measures frontier coding capabilities](../../papers/openai-swe-bench-verified-retired/README.md) · 2026 · 官方博客，文献卡

## 裁判偏差与排行榜

- [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators](../../papers/arxiv-2404.04475/README.md) · 2024 · 文献卡
- [The Leaderboard Illusion](../../papers/arxiv-2504.20879/README.md) · 2025 · 文献卡
- [On scalable oversight with weak LLMs judging strong LLMs](../../papers/arxiv-2407.04622/README.md) · 2024 · 文献卡
- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](../../papers/arxiv-2508.10014/README.md) · 2025 · 文献卡 · 角色扮演中的裁判，详见[各领域的评测](domains.md)

## 评测进入训练（交叉引用，正文在大语言模型目录）

- [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](../../../llm/papers/arxiv-2411.15124/README.md) · 2024 · 开发集与未见集、去污染、IFEval 约束上的 RLVR
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../../llm/papers/arxiv-2501.12948/README.md) · 2025 · 规则奖励、奖励模型被钻空子、10-gram 去污染
- [Qwen3 Technical Report](../../../llm/papers/arxiv-2505.09388/README.md) · 2025 · 三类奖励
- [Kimi K2: Open Agentic Intelligence](../../../llm/papers/arxiv-2507.20534/README.md) · 2025 · 软件工程 RL 环境、自我批评 rubric 及其自述局限
- [Kimi K3: Open Frontier Intelligence](../../../llm/papers/arxiv-2607.24653/README.md) · 2026 · 公开与隐藏验证器
- [RULER: What's the Real Context Size of Your Long-Context Language Models?](../../../llm/papers/arxiv-2404.06654/README.md) · 2024 · 长上下文评测，见[长上下文方向](../../../llm/fields/long-context/README.md)

## 其他评测与测量

- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](../../papers/arxiv-2312.05092/README.md) · 2023 · 文献卡 · 探针式评测，见[模型科学](../model-science/README.md)
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](../../../llm/papers/url-https-aclanthology.org-2024.findings-emnlp.882/README.md) · 2024 · 文献卡 · 思维链是否忠实
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](../../../llm/papers/url-https-aclanthology.org-2025.emnlp-main.504/README.md) · 2025 · 文献卡 · 思维链是否忠实
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](../../../llm/papers/url-https-aclanthology.org-2025.findings-acl.537/README.md) · 2025 · 文献卡
- [Finding bugs across the Python ecosystem with Claude and property-based testing](../../papers/agentic-property-based-testing/README.md) · 2026 · 官方博客 · 用性质测试检验代码，"测试通过 ≠ 正确"的另一面
- [Metamorphic Testing of Multi-Agent LLM Systems: A Trace-Based Behavioral Oracle Framework](../../papers/morphagent/README.md) · 2026 · 文献卡 · 多智能体系统的行为判定

## 各领域的评测（正文在[分任务能力图](domains.md)）

- [Evaluating Large Language Models Trained on Code](../../papers/arxiv-2107.03374/README.md) · 2021 · 文献卡 · 代码
- [Beyond Correctness: Benchmarking Multi-dimensional Code Generation for Large Language Models](../../papers/arxiv-2407.11470/README.md) · 2024 · 文献卡 · 代码
- [MaintainCoder: Maintainable Code Generation Under Dynamic Requirements](../../papers/arxiv-2503.24260/README.md) · 2025 · 文献卡 · 代码
- [ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases](../../papers/arxiv-2510.20270/README.md) · 2025 · 文献卡 · 代码
- [LLM Critics Help Catch LLM Bugs](../../papers/arxiv-2407.00215/README.md) · 2024 · 文献卡 · 代码
- [SciCode: A Research Coding Benchmark Curated by Scientists](../../papers/arxiv-2407.13168/README.md) · 2024 · 文献卡 · 科研
- [Large Language Models Encode Clinical Knowledge](../../papers/arxiv-2212.13138/README.md) · 2022 · 文献卡 · 医疗
- [HealthBench: Evaluating Large Language Models Towards Improved Human Health](../../papers/arxiv-2505.08775/README.md) · 2025 · 文献卡 · 医疗
- [LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models](../../papers/arxiv-2308.11462/README.md) · 2023 · 文献卡 · 法律
- [FinanceBench: A New Benchmark for Financial Question Answering](../../papers/arxiv-2311.11944/README.md) · 2023 · 文献卡 · 金融
- [CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation](../../papers/arxiv-2401.01275/README.md) · 2024 · 文献卡 · 角色扮演
- [HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal](../../papers/arxiv-2402.04249/README.md) · 2024 · 文献卡 · 安全
- [XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models](../../papers/arxiv-2308.01263/README.md) · 2023 · 文献卡 · 安全
- [A StrongREJECT for Empty Jailbreaks](../../papers/arxiv-2402.10260/README.md) · 2024 · 文献卡 · 安全
- [Generalizing Verifiable Instruction Following](../../papers/arxiv-2507.02833/README.md) · 2025 · 文献卡 · 指令遵循

## 不再列在本方向主线的条目

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](../../../llm/papers/test-time-compute/README.md)：旧版 Baseline 页把它列为"推理时计算的可比较基线"，它属于[推理时计算方向](../../../llm/fields/inference/README.md)，本方向只在采样口径上引用。
