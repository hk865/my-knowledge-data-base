# 具身 Agent：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

以下每项链接到唯一的单篇目录。跨方向出现是交叉引用，不重复计算资源。

## 基准与评测

- [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](../../papers/arxiv-1912.01734/README.md) · 2019 · 文献卡
- [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](../../papers/arxiv-2502.09560/README.md) · 2025 · 文献卡

## 冻结大模型做高层

- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](../../papers/saycan/README.md) · 2022 · 选定章节讲解
- [Inner Monologue: Embodied Reasoning through Planning with Language Models](../../papers/arxiv-2207.05608/README.md) · 2022 · 文献卡
- [LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](../../papers/arxiv-2212.04088/README.md) · 2022 · 文献卡
- [ReAct: Synergizing Reasoning and Acting in Language Models](../../../cross-domain/papers/react/README.md) · 2022 · 技术精读（跨方向）

## 代码与结构作为技能接口

- [Code as Policies: Language Model Programs for Embodied Control](../../papers/arxiv-2209.07753/README.md) · 2022 · 文献卡
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](../../../llm/papers/arxiv-2305.16291/README.md) · 2023 · 文献卡
- [VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models](../../papers/arxiv-2307.05973/README.md) · 2023 · 文献卡

## 训练出来的分层 VLA

- [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](../../papers/arxiv-2502.19417/README.md) · 2025 · 文献卡
- [π0.5: a Vision-Language-Action Model with Open-World Generalization](../../papers/arxiv-2504.16054/README.md) · 2025 · 文献卡（主要属于 VLA 方向）

## Agent 运行时、技能积累与记忆

- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](../../papers/holoagent-0/README.md) · 2026 · 选定章节讲解
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](../../papers/memora/README.md) · 2026 · 选定章节讲解
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](../../papers/embodiedskills/README.md) · 2026 · 选定章节讲解
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](../../papers/roboskill/README.md) · 2026 · 选定章节讲解
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../../papers/zero-wam/README.md) · 2026 · 选定章节讲解（主要属于世界模型方向）

## 公司系统中的编排器（2025 年底–2026）

- [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](../../papers/arxiv-2510.03342/README.md) · 2025 · 文献卡（主要属于 VLA 方向） · ER 1.5 编排、VLA 当工具
- [Gemini Robotics 2: Safety Evaluations](../../papers/gemini-robotics-2-safety/README.md) · 2026 · 官方技术报告卡 · ASIMOV-Agentic：编排器的安全与可行性决策
- [Gemini Robotics 2 brings whole body intelligence to robots](../../papers/gemini-robotics-2/README.md) · 2026 · 官方博客卡（主要属于 VLA 方向） · ER 2 的任务进度与多机协作
- [MEM: Multi-Scale Embodied Memory for Vision Language Action Models](../../papers/arxiv-2603.03596/README.md) · 2026 · 文献卡（主要属于 VLA 方向） · 策略自己写的文字长时记忆

## 跨方向参照（LLM 侧）

- [Language Models are Few-Shot Learners](../../../llm/papers/gpt3/README.md) · 2020 · 技术精读
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](../../../llm/papers/arxiv-2405.15793/README.md) · 2024 · 文献卡
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](../../../llm/papers/arxiv-2407.18219/README.md) · 2024 · 文献卡

## 通用模型与物理工具的近期闭环（2026）

首发月份与较早前史分开列；训练范围与实验口径见各篇文献卡及[接口地图](README.md)。

- [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](../../papers/arxiv-2607.08448/README.md) · 2026 · 技术精读 · 7 月首发，9 月 v5；冻结 Agent 调用 VLA 与解析工具
- [Agent as Policy for Robotic Manipulation](../../papers/arxiv-2609.12541/README.md) · 2026 · 文献卡 · 9 月；运行时编写程序与物理工具接口
- [SimEX: Simulation-Integrated Robotics AutoResearch](../../papers/arxiv-2609.38982/README.md) · 2026 · 文献卡 · 9 月；仿真实验、工具箱修复与少量真机适应
- [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](../../papers/arxiv-2606.19980/README.md) · 2026 · 文献卡 · 6 月首发，9 月 v2；通用 Agent 组织低层策略训练
- [Generalizing Manipulation Skills with a Local Coding Agent](../../papers/arxiv-2609.26499/README.md) · 2026 · 文献卡 · 9 月；本地冻结代码模型与身体碰撞边界
- [Bridging Semantics and Physics with Constrained LLMs for Safe and Trustworthy Robotic Manipulation](../../papers/arxiv-2608.29379/README.md) · 2026 · 文献卡 · 8 月；有类型工具与固定运动规划模板
- [Improving Robotic Generalist Policies via Flow Reversal Steering](../../papers/arxiv-2606.13675/README.md) · 2026 · 文献卡 · 6 月；VLM 参考动作与逆流噪声接口

## 动作干预、可训练工具与调度对照（2026）

- [VLS: Steering Pretrained Robot Policies via Vision-Language Models](../../papers/arxiv-2602.03973/README.md) · 2026 · 技术精读 · 2 月；VLM 奖励程序引导生成
- [StageCraft: Execution Aware Mitigation of Distractor and Obstruction Failures in VLA Models](../../papers/arxiv-2603.20659/README.md) · 2026 · 文献卡 · 3 月首发，9 月 v3；整理初始环境，底层先训练
- [VLA-ATTC: Adaptive Test-Time Compute for VLA Models with Relative Action Critic Model](../../papers/arxiv-2605.01194/README.md) · 2026 · 文献卡 · 5 月；训练相对动作 critic，按需增加计算
- [Proxy Policy Steering](../../papers/arxiv-2609.09148/README.md) · 2026 · 文献卡 · 9 月；训练两个小代理，修正冻结动作基座
- [Inference-time Policy Steering via Vision and Touch](../../papers/arxiv-2606.14981/README.md) · 2026 · 文献卡 · 6 月；视觉触觉世界模型与评分工具
- [Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](../../papers/arxiv-2603.05185/README.md) · 2026 · 文献卡 · 3 月；训练型高层与执行 critic 的对照

## 候选搜索与验证的前史（2025 首发）

- [Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion](../../papers/arxiv-2511.14178/README.md) · 2025 · 技术精读 · 2026 年 4 月 v2；黑盒奖励与进化搜索
- [Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification](../../papers/arxiv-2510.16281/README.md) · 2025 · 文献卡 · 2026 年 1 月 v2；推理与动作对齐验证
