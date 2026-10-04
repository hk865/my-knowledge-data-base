# Agent：论文与资源

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

以下每项链接到唯一的单篇目录。跨方向出现是交叉引用，不重复计算资源。按入门页的历史阶段排列。

## 1 提示出来的循环

- [ReAct: Synergizing Reasoning and Acting in Language Models](../../papers/react/README.md) · 2022 · 技术精读
- [Toolformer: Language Models Can Teach Themselves to Use Tools](../../papers/arxiv-2302.04761/README.md) · 2023 · 文献卡
- [Reflexion: Language Agents with Verbal Reinforcement Learning](../../papers/arxiv-2303.11366/README.md) · 2023 · 文献卡
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](../../../llm/papers/arxiv-2305.16291/README.md) · 2023 · 文献卡
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](../../../llm/papers/arxiv-2407.18219/README.md) · 2024 · 文献卡（多轮自我修订的训练方法）
- [Language Models are Few-Shot Learners](../../../llm/papers/gpt3/README.md) · 2020 · 技术精读（上下文学习，提示式 agent 的前提）

## 2 真实环境 benchmark

- [WebArena: A Realistic Web Environment for Building Autonomous Agents](../../papers/arxiv-2307.13854/README.md) · 2023 · 文献卡
- [GAIA: a benchmark for General AI Assistants](../../papers/arxiv-2311.12983/README.md) · 2023 · 文献卡
- [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](../../papers/arxiv-2404.07972/README.md) · 2024 · 文献卡
- [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](../../papers/arxiv-2406.12045/README.md) · 2024 · 文献卡
- [Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](../../papers/arxiv-2601.11868/README.md) · 2026 · 文献卡
- SWE-bench 与 SWE-bench Verified 归[评估方向](../evaluation/README.md)；原文：[SWE-bench](../../papers/arxiv-2310.06770/README.md)、[Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)（OpenAI 官方博客）

## 3 接口与脚手架

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](../../../llm/papers/arxiv-2405.15793/README.md) · 2024 · 文献卡
- 官方博客（未建卡）：Anthropic [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)（2024-12）、[Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet](https://www.anthropic.com/engineering/swe-bench-sonnet)（2025-01）

## 4 把 agent 行为训进权重

- [Training Software Engineering Agents and Verifiers with SWE-Gym](../../papers/arxiv-2412.21139/README.md) · 2024 · 文献卡
- [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](../../papers/arxiv-2502.18449/README.md) · 2025 · 文献卡
- [Kimi K2: Open Agentic Intelligence](../../../llm/papers/arxiv-2507.20534/README.md) · 2025 · 文献卡（§3 智能体数据合成与 RL 环境）
- [Qwen3 Technical Report](../../../llm/papers/arxiv-2505.09388/README.md) · 2025 · 文献卡（通用 RL 中的 Agent 能力）
- [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](../../../llm/papers/arxiv-2512.02556/README.md) · 2025 · 技术精读（§3.2 大规模 agent 任务合成）
- [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](../../../llm/papers/arxiv-2609.19969/README.md) · 2026 · 技术精读（agent 评测随框架变化、长程 agent 的 KV 缓存）
- 官方材料（未建卡）：OpenAI [Introducing Codex](https://openai.com/index/introducing-codex/)（2025-05）、[GPT-5-Codex 系统卡附录](https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/)（2025-09）；DeepSeek [V3.1 发布说明](https://api-docs.deepseek.com/news/news250821)（2025-08）；Qwen [Qwen3-Coder 博客](https://qwenlm.github.io/blog/qwen3-coder/)（2025-07）

## 5 环境就是训练目标：奖励黑客、越权与诚实

- [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](../../papers/arxiv-2503.11926/README.md) · 2025 · 文献卡
- [System Card: Claude Opus 4 & Claude Sonnet 4](../../papers/anthropic-claude-4-system-card/README.md) · 2025 · 文献卡
- [Natural Emergent Misalignment from Reward Hacking in Production RL](../../papers/arxiv-2511.18397/README.md) · 2025 · 文献卡
- [Kimi K3: Open Frontier Intelligence](../../../llm/papers/arxiv-2607.24653/README.md) · 2026 · 文献卡（agent RL 中的沙箱隔离）
- 官方材料（未建卡）：Anthropic 系统卡 [Claude 3.7 Sonnet](https://www-cdn.anthropic.com/9ff93dfa8f445c932415d335c88852ef47f1201e.pdf)、[Claude Sonnet 4.5](https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd.pdf)、[Claude Opus 4.5](https://www-cdn.anthropic.com/bf10f64990cfda0ba858290be7b8cc6317685f47.pdf)、[Claude Opus 4.6](https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd/Claude%20Opus%204.6%20System%20Card.pdf)、[Claude Opus 5.5](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)；OpenAI [codex-1 系统卡附录](https://cdn.openai.com/pdf/8df7697b-c1b2-4222-be00-1fd3298f351d/codex_system_card.pdf)、[GPT-5 系统卡](https://cdn.openai.com/gpt-5-system-card.pdf)、[GPT-5.1-Codex-Max 系统卡](https://openai.com/index/gpt-5-1-codex-max-system-card/)
- 第三方评测（未建卡）：METR [Recent Frontier Models Are Reward Hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking/)（2025-06）、[Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499)

## 验证与测试

- [Finding bugs across the Python ecosystem with Claude and property-based testing](../../papers/agentic-property-based-testing/README.md) · 2026 · 官方博客文献卡
- [Metamorphic Testing of Multi-Agent LLM Systems: A Trace-Based Behavioral Oracle Framework](../../papers/morphagent/README.md) · 2026 · 文献卡

## 机器人一侧（见[具身 Agent](../../../robotics-embodied/fields/embodied-agents/README.md)）

- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](../../../robotics-embodied/papers/saycan/README.md) · 2022 · 选定章节讲解
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](../../../robotics-embodied/papers/roboskill/README.md) · 2026 · 选定章节讲解
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](../../../robotics-embodied/papers/embodiedskills/README.md) · 2026 · 选定章节讲解
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](../../../robotics-embodied/papers/memora/README.md) · 2026 · 选定章节讲解
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](../../../robotics-embodied/papers/holoagent-0/README.md) · 2026 · 选定章节讲解

## 2026 年的系统卡与长程评测（时效补充）

- [Measuring AI Ability to Complete Long Software Tasks](../../papers/arxiv-2503.14499/README.md) · 2025 · 文献卡 · 长程能力的时间跨度度量（第三方，METR）
- [OpenAI GPT-5.6 System Card](../../papers/openai-gpt-5-6-system-card/README.md) · 2026 · 文献卡 · OpenAI 2026-07 系统卡：自主性与越权评测
- [OpenAI GPT-6 Astra System Card](../../papers/openai-gpt-6-astra-system-card/README.md) · 2026 · 文献卡 · OpenAI 2026-09 系统卡：训练后另造评测、长程任务
- [System Card: Claude Opus 5.5](../../papers/anthropic-claude-opus-5-5-system-card/README.md) · 2026 · 文献卡 · Anthropic 2026-09 系统卡：奖励黑客与判分器意识
- [Gemini 3.8 Flash Model Card](../../papers/google-gemini-3-8-flash-model-card/README.md) · 2026 · 文献卡 · Google 2026-09 模型卡
- [Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity](../../papers/arxiv-2607.00248/README.md) · 2026 · 文献卡 · 字节跳动 Seed2.0 模型卡（2026-06）
