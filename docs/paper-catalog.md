# 论文与研究资源目录

本次汇总117项去重资源。其中96项有实际历史聊天链接证据：95篇论文及1个代码仓库；其中1项为用户提供的 Zero-WAM，95项为历史助手推荐。另保留16项手册来源与6项原有种子条目；来源可重叠，OpenVLA 同时属于手册与种子。来源标签不代表用户采纳、已读或正在研究。

本次核验题名与标识对应，部分记录核对官方摘要；不等于全文精读、技术结论评估或独立复现。聊天日期与来源来自可检索历史摘要，不是逐字引文；当前无可打开的原会话链接，也不保证全量覆盖。

[按研究方向浏览](topics.md) · [待核实线索](unresolved.md) · [JSON](../papers.json) · [CSV](../papers.csv)

### p001

**[Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-10T05:06:03Z

主题：llm/inference

细分问题：inference/test-time scaling · posttraining/rewards/process verification

训练监督：process reward model

推理或处理方法：inference-time search

历史链接：[链接1](https://arxiv.org/abs/2408.03314)

核验来源：[原始来源1](https://arxiv.org/abs/2408.03314)

### p002

**[Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](https://arxiv.org/abs/2502.18080)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-01T11:44:47Z、2026-09-10T05:06:03Z

主题：llm/posttraining/sft · llm/inference

细分问题：inference/test-time scaling · posttraining/SFT/self-training

训练监督：teacher-generated reasoning · self-training

历史链接：[链接1](https://arxiv.org/abs/2502.18080)

核验来源：[原始来源1](https://arxiv.org/abs/2502.18080)

### p003

**[s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-10T05:06:03Z

主题：llm/posttraining/sft · llm/inference

细分问题：posttraining/SFT/reasoning · inference/budget forcing · data/curated reasoning

训练监督：supervised fine-tuning · synthetic reasoning traces

历史链接：[链接1](https://arxiv.org/abs/2501.19393)

核验来源：[原始来源1](https://arxiv.org/abs/2501.19393)

### p004

**[Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](https://arxiv.org/abs/2407.21787)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-10T05:06:03Z

主题：llm/inference

细分问题：inference/repeated sampling · inference/verification

训练监督：verifiable outcomes

推理或处理方法：inference-only sampling

历史链接：[链接1](https://arxiv.org/abs/2407.21787)

核验来源：[原始来源1](https://arxiv.org/abs/2407.21787)

### p005

**[Qwen2 Technical Report](https://arxiv.org/abs/2407.10671)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-30T02:52:50Z

主题：llm/posttraining/sft · llm/posttraining/preferences · llm/pretraining · llm/architecture

细分问题：pretraining/general language · data/training pipeline · posttraining/SFT · posttraining/preference alignment · architecture/dense and MoE

训练监督：self-supervised pretraining · supervised fine-tuning · preference alignment

历史链接：[链接1](https://arxiv.org/abs/2407.10671)

核验来源：[原始来源1](https://arxiv.org/abs/2407.10671)

### p006

**[Qwen2.5 Technical Report](https://arxiv.org/abs/2412.15115)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-30T02:52:50Z

主题：llm/posttraining/sft · llm/pretraining · llm/posttraining/rl

细分问题：pretraining/general language · data/training pipeline · posttraining/SFT · posttraining/RL

训练监督：self-supervised pretraining · supervised fine-tuning · reinforcement learning

历史链接：[链接1](https://arxiv.org/abs/2412.15115)

核验来源：[原始来源1](https://arxiv.org/abs/2412.15115)

### p007

**[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-30T02:52:50Z

主题：llm/posttraining/sft · llm/pretraining · llm/architecture · llm/posttraining/rl

细分问题：pretraining/multi-token prediction · architecture/MoE · architecture/MLA · posttraining/SFT · posttraining/RL

训练监督：self-supervised pretraining · supervised fine-tuning · reinforcement learning

历史链接：[链接1](https://arxiv.org/abs/2412.19437)

核验来源：[原始来源1](https://arxiv.org/abs/2412.19437)

### p008

**[Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-30T02:52:50Z

主题：llm/posttraining/sft · llm/pretraining · llm/architecture · llm/inference

细分问题：pretraining/long context · data/long-data synthesis · posttraining/SFT · inference/sparse attention and prefill

训练监督：self-supervised pretraining · synthetic data · supervised fine-tuning

历史链接：[链接1](https://arxiv.org/abs/2501.15383)

核验来源：[原始来源1](https://arxiv.org/abs/2501.15383)

2026-09-30 定向阅读：长上下文能力如何由训练与部署共同支持？ 作者摘要描述长数据合成、渐进预训练、多阶段SFT与稀疏推理优化。

边界：官方摘要支持多阶段路线描述，不足以证明超长RL轨迹信用分配已解决；未全文精读或复现。

用户关联：2026-09-30 02:29、02:47 UTC关于注意力复杂度、长上下文与RL rollout的实际问题。 来源：沿用已有助手聊天链接；本轮检索时间02:52:48与原记录02:52:50有秒级差异，保留原记录，不算新来源事件。

### p009

**[Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-30T03:03:00Z

主题：llm/pretraining · llm/architecture · llm/inference

细分问题：architecture/state space · pretraining/sequence modeling · inference/linear-time

训练监督：self-supervised language modeling

历史链接：[链接1](https://arxiv.org/abs/2312.00752)

核验来源：[原始来源1](https://arxiv.org/abs/2312.00752)

### p010

**[OLMo: Accelerating the Science of Language Models](https://arxiv.org/abs/2402.00838)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-30T03:03:00Z

主题：llm/pretraining · cross-domain/interpretability

细分问题：pretraining/open pipeline · data/open corpus · model science/reproducibility

训练监督：self-supervised language modeling

历史链接：[链接1](https://arxiv.org/pdf/2402.00838)

核验来源：[原始来源1](https://arxiv.org/abs/2402.00838)

### p011

**[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-05T05:21:33Z、2026-09-30T03:03:00Z

主题：llm/posttraining/sft · llm/posttraining/rl · llm/inference

细分问题：posttraining/RL/GRPO · posttraining/rewards/verifiable · posttraining/SFT/cold start · posttraining/distillation

训练监督：reinforcement learning · verifiable reward · supervised fine-tuning · distillation

历史链接：[链接1](https://arxiv.org/abs/2501.12948) · [链接2](https://www.nature.com/articles/s41586-025-09422-z)

核验来源：[原始来源1](https://arxiv.org/abs/2501.12948) · [原始来源2](https://www.nature.com/articles/s41586-025-09422-z)

### p012

**[Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-12T13:58:53Z

主题：llm/pretraining · llm/architecture

细分问题：architecture/MoE/routing · pretraining/sparse scaling

训练监督：self-supervised pretraining

历史链接：[链接1](https://arxiv.org/abs/2101.03961)

核验来源：[原始来源1](https://arxiv.org/abs/2101.03961)

### p013

**[DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-12T13:58:53Z

主题：llm/pretraining · llm/architecture

细分问题：architecture/MoE/expert specialization · pretraining/sparse models

训练监督：self-supervised pretraining

历史链接：[链接1](https://arxiv.org/abs/2401.06066)

核验来源：[原始来源1](https://arxiv.org/abs/2401.06066)

### p014

**[DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z、2026-09-12T13:58:53Z

主题：llm/posttraining/sft · llm/pretraining · llm/architecture · llm/posttraining/rl

细分问题：architecture/MoE · architecture/MLA · pretraining/general language · posttraining/SFT · posttraining/RL

训练监督：self-supervised pretraining · supervised fine-tuning · reinforcement learning

历史链接：[链接1](https://arxiv.org/abs/2405.04434)

核验来源：[原始来源1](https://arxiv.org/abs/2405.04434)

### p015

**[Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://arxiv.org/abs/2601.07372)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-26T13:59:17Z

主题：llm/pretraining · llm/architecture

细分问题：architecture/conditional memory · pretraining/sparsity

训练监督：self-supervised language modeling

历史链接：[链接1](https://arxiv.org/abs/2601.07372)

核验来源：[原始来源1](https://arxiv.org/abs/2601.07372)

### p016

**[Tokenizer-Agnostic Engram Module](https://arxiv.org/abs/2607.29065)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-26T13:46:47Z

主题：llm/architecture

细分问题：architecture/conditional memory · architecture/tokenizer compatibility

训练监督：language-model training

历史链接：[链接1](https://arxiv.org/abs/2607.29065)

核验来源：[原始来源1](https://arxiv.org/abs/2607.29065)

### p017

**[Cross-Model Memory Transfer via Target-Side Reader Adaptation](https://arxiv.org/abs/2608.17050)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-26T13:46:47Z

主题：llm/architecture

细分问题：architecture/conditional memory · posttraining/parameter-efficient adaptation

训练监督：reader adaptation

推理或处理方法：frozen-memory transfer

历史链接：[链接1](https://arxiv.org/abs/2608.17050)

核验来源：[原始来源1](https://arxiv.org/abs/2608.17050)

### p018

**[Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://arxiv.org/abs/2412.09078)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-01T11:44:47Z

主题：llm/inference

细分问题：inference/test-time scaling · inference/reasoning search

推理或处理方法：inference-time reasoning search

历史链接：[链接1](https://arxiv.org/abs/2412.09078)

核验来源：[原始来源1](https://arxiv.org/abs/2412.09078)

### p019

**[Recursive Introspection: Teaching Language Model Agents How to Self-Improve](https://arxiv.org/abs/2407.18219)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T15:35:43Z

主题：llm/posttraining/sft · llm/inference · cross-domain/agents

细分问题：posttraining/SFT/self-correction · posttraining/RL/multi-turn formulation · inference/iterative reasoning

训练监督：iterative fine-tuning · online imitation · environment feedback

历史链接：[链接1](https://arxiv.org/abs/2407.18219?utm_source=chatgpt.com)

核验来源：[原始来源1](https://arxiv.org/abs/2407.18219)

### p020

**[MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](https://arxiv.org/abs/2002.10957)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：llm/pretraining · llm/architecture

细分问题：architecture/compression · pretraining/distillation

训练监督：teacher-student attention distillation

历史链接：[链接1](https://arxiv.org/abs/2002.10957)

核验来源：[原始来源1](https://arxiv.org/abs/2002.10957)

### p021

**[DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：llm/pretraining · llm/architecture

细分问题：pretraining/distillation · architecture/compression

训练监督：language modeling · teacher distillation

历史链接：[链接1](https://arxiv.org/html/1910.01108v4)

核验来源：[原始来源1](https://arxiv.org/abs/1910.01108)

### p022

**[ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](https://arxiv.org/abs/2403.03853)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：llm/architecture · cross-domain/interpretability

细分问题：architecture/compression/layer pruning · model science/layer redundancy

推理或处理方法：post-hoc pruning

历史链接：[链接1](https://arxiv.org/abs/2403.03853)

核验来源：[原始来源1](https://arxiv.org/abs/2403.03853)

### p023

**[Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](https://arxiv.org/abs/2403.13271)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：llm/posttraining/sft · llm/inference

细分问题：posttraining/SFT/code · posttraining/distillation · data/reasoning plans

训练监督：teacher-generated plans · multi-task supervised learning

历史链接：[链接1](https://arxiv.org/abs/2403.13271)

核验来源：[原始来源1](https://arxiv.org/abs/2403.13271)

### p024

**[GraphCodeBERT: Pre-training Code Representations with Data Flow](https://arxiv.org/abs/2009.08366)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：llm/pretraining · llm/architecture

细分问题：pretraining/code · pretraining/structural objectives · architecture/graph-guided attention

训练监督：masked language modeling · structure-aware self-supervision

历史链接：[链接1](https://arxiv.org/abs/2009.08366)

核验来源：[原始来源1](https://arxiv.org/abs/2009.08366)

### p025

**[In-context Learning and Induction Heads](https://arxiv.org/abs/2209.11895)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：cross-domain/interpretability

细分问题：model science/mechanistic interpretability · model science/in-context learning

评估：analysis of pretrained models

历史链接：[链接1](https://arxiv.org/abs/2209.11895)

核验来源：[原始来源1](https://arxiv.org/abs/2209.11895)

### p026

**[Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：cross-domain/interpretability

细分问题：model science/FFN · model science/knowledge representation

评估：analysis of pretrained models

历史链接：[链接1](https://arxiv.org/abs/2012.14913)

核验来源：[原始来源1](https://arxiv.org/abs/2012.14913)

### p027

**[Locating and Editing Factual Associations in GPT](https://arxiv.org/abs/2202.05262)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：cross-domain/interpretability

细分问题：model science/causal tracing · model science/knowledge editing

训练监督：targeted factual editing

评估：causal analysis

历史链接：[链接1](https://arxiv.org/abs/2202.05262)

核验来源：[原始来源1](https://arxiv.org/abs/2202.05262)

### p028

**[Naturalness of Attention: Revisiting Attention in Code Language Models](https://arxiv.org/abs/2311.13508)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：llm/architecture · cross-domain/interpretability

细分问题：model science/code attention

评估：analysis of pretrained models

历史链接：[链接1](https://arxiv.org/pdf/2311.13508)

核验来源：[原始来源1](https://arxiv.org/abs/2311.13508)

### p029

**[Probing Pretrained Models of Source Code](https://arxiv.org/abs/2202.08975)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：llm/pretraining · cross-domain/interpretability

细分问题：model science/code probing

评估：probing evaluation

历史链接：[链接1](https://arxiv.org/abs/2202.08975)

核验来源：[原始来源1](https://arxiv.org/abs/2202.08975)

### p030

**[INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](https://arxiv.org/abs/2312.05092)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-18T05:22:59Z

主题：cross-domain/interpretability · cross-domain/evaluation

细分问题：model science/code probing

评估：probing evaluation

历史链接：[链接1](https://arxiv.org/html/2312.05092v1)

核验来源：[原始来源1](https://arxiv.org/abs/2312.05092)

### p031

**[Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](https://arxiv.org/abs/2510.01171)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-25T15:03:18Z

主题：llm/inference · cross-domain/interpretability

细分问题：inference/sampling · model science/diversity and mode collapse

推理或处理方法：inference prompting

历史链接：[链接1](https://arxiv.org/abs/2510.01171)

核验来源：[原始来源1](https://arxiv.org/abs/2510.01171)

### p032

**[PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](https://arxiv.org/abs/2508.10014)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-25T15:03:18Z

主题：cross-domain/interpretability · cross-domain/evaluation

细分问题：model science/evaluation/roleplay

评估：evaluation · LLM judge

历史链接：[链接1](https://arxiv.org/abs/2508.10014)

核验来源：[原始来源1](https://arxiv.org/abs/2508.10014)

### p033

**[On scalable oversight with weak LLMs judging strong LLMs](https://arxiv.org/abs/2407.04622)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-25T15:00:25Z

主题：cross-domain/interpretability · cross-domain/evaluation

细分问题：posttraining/rewards/scalable oversight · model science/evaluation/debate

评估：weak-model judging · debate evaluation

历史链接：[链接1](https://arxiv.org/abs/2407.04622)

核验来源：[原始来源1](https://arxiv.org/abs/2407.04622)

### p034

**[SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-01T11:44:47Z

主题：llm/inference · cross-domain/agents · cross-domain/interpretability · cross-domain/evaluation

细分问题：agents/code · inference/tool use · model science/evaluation

推理或处理方法：inference-time agent interaction

历史链接：[链接1](https://arxiv.org/abs/2405.15793)

核验来源：[原始来源1](https://arxiv.org/abs/2405.15793)

### p035

**[Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://proceedings.mlr.press/v267/chen25bx.html)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-01T11:44:47Z

主题：llm/posttraining/sft · llm/inference

细分问题：inference/reasoning efficiency · posttraining/SFT/self-training

训练监督：self-training

历史链接：[链接1](https://proceedings.mlr.press/v267/chen25bx.html)

核验来源：[原始来源1](https://proceedings.mlr.press/v267/chen25bx.html)

### p036

**[Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](https://aclanthology.org/2024.findings-emnlp.882/)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-01T11:44:47Z

主题：llm/inference · cross-domain/interpretability · cross-domain/evaluation

细分问题：model science/evaluation/CoT faithfulness

评估：evaluation · reasoning faithfulness

历史链接：[链接1](https://aclanthology.org/2024.findings-emnlp.882/)

核验来源：[原始来源1](https://aclanthology.org/2024.findings-emnlp.882/)

### p037

**[Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://aclanthology.org/2025.emnlp-main.504/)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-01T11:44:47Z

主题：llm/inference · cross-domain/interpretability · cross-domain/evaluation

细分问题：model science/evaluation/CoT faithfulness

评估：unlearning-based evaluation

历史链接：[链接1](https://aclanthology.org/2025.emnlp-main.504/)

核验来源：[原始来源1](https://aclanthology.org/2025.emnlp-main.504/)

### p038

**[Reasoning Does Not Necessarily Improve Role-Playing Ability](https://aclanthology.org/2025.findings-acl.537/)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-25T15:03:18Z

主题：llm/inference · cross-domain/interpretability · cross-domain/evaluation

细分问题：model science/evaluation/roleplay

评估：evaluation

历史链接：[链接1](https://aclanthology.org/2025.findings-acl.537/)

核验来源：[原始来源1](https://aclanthology.org/2025.findings-acl.537/)

### p039

**[Self-Discover: Large Language Models Self-Compose Reasoning Structures](https://deepmind.google/research/publications/64816/)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T15:35:43Z

主题：llm/inference

细分问题：inference/reasoning structures · inference/compute efficiency

推理或处理方法：inference prompting

历史链接：[链接1](https://deepmind.google/research/publications/64816/?utm_source=chatgpt.com)

核验来源：[原始来源1](https://deepmind.google/research/publications/64816/) · [原始来源2](https://arxiv.org/abs/2402.03620)

### p040

**[ReAct: Synergizing Reasoning and Acting in Language Models](https://mlanthology.org/iclr/2023/yao2023iclr-react/)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-01T11:44:47Z

主题：llm/inference · cross-domain/agents

细分问题：agents/reasoning and acting · inference/tool use

推理或处理方法：inference prompting;environment feedback

历史链接：[链接1](https://mlanthology.org/iclr/2023/yao2023iclr-react/)

核验来源：[原始来源1](https://arxiv.org/abs/2210.03629)

### p041

**[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://mlanthology.org/tmlr/2024/wang2024tmlr-voyager/)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T15:35:43Z

主题：llm/inference · cross-domain/agents

细分问题：agents/reasoning and acting · inference/tool use

推理或处理方法：inference prompting;environment feedback

历史链接：[链接1](https://mlanthology.org/tmlr/2024/wang2024tmlr-voyager/?utm_source=chatgpt.com)

核验来源：[原始来源1](https://arxiv.org/abs/2305.16291)

### p042

**[SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](https://arxiv.org/abs/2210.05861)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:58:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · object-centric

架构：slot transformer · autoregressive dynamics

训练监督：unsupervised video prediction

历史链接：[链接1](https://arxiv.org/abs/2210.05861)

核验来源：[原始来源1](https://arxiv.org/abs/2210.05861)

### p043

**[SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](https://arxiv.org/abs/2206.07764)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:58:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · object-centric · geometry-assisted representation

架构：slot-based video encoder

训练监督：depth prediction · sparse LiDAR supervision · no segmentation labels

历史链接：[链接1](https://arxiv.org/abs/2206.07764)

核验来源：[原始来源1](https://arxiv.org/abs/2206.07764)

### p044

**[OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](https://arxiv.org/abs/2311.16038)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:58:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · geometry · 3D occupancy

架构：scene tokenizer · GPT-like spatiotemporal transformer

训练监督：occupancy reconstruction · future token prediction

历史链接：[链接1](https://arxiv.org/abs/2311.16038)

核验来源：[原始来源1](https://arxiv.org/abs/2311.16038)

### p045

**[Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](https://arxiv.org/abs/2408.14197)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:58:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · geometry · 4D occupancy and flow

架构：BEV memory · world decoder · action conditioning

训练监督：occupancy forecasting · flow forecasting

历史链接：[链接1](https://arxiv.org/abs/2408.14197)

核验来源：[原始来源1](https://arxiv.org/abs/2408.14197)

### p046

**[DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](https://arxiv.org/abs/2411.04983)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:58:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · latent · visual-feature prediction

架构：DINOv2 patch encoder · action-conditioned predictor

训练监督：offline trajectory future-feature prediction · pretrained visual features

历史链接：[链接1](https://arxiv.org/abs/2411.04983)

核验来源：[原始来源1](https://arxiv.org/abs/2411.04983)

### p047

**[Back to the Features: DINO as a Foundation for Video World Models](https://arxiv.org/abs/2507.19468)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:58:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · latent · generalist video prediction

架构：DINOv2 encoder · latent future predictor

训练监督：uncurated video predictive learning · action-conditioned finetuning

历史链接：[链接1](https://arxiv.org/abs/2507.19468)

核验来源：[原始来源1](https://arxiv.org/abs/2507.19468)

### p048

**[FOCUS: Object-Centric World Models for Robotics Manipulation](https://arxiv.org/abs/2307.02427)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:59:38Z

主题：multimodal/world-models

细分问题：multimodal · world-models · object-centric · exploration for manipulation

架构：object-centric world model · model-based agent

训练监督：model-based reinforcement learning · exploration bonus

历史链接：[链接1](https://arxiv.org/abs/2307.02427)

核验来源：[原始来源1](https://arxiv.org/abs/2307.02427)

### p049

**[LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](https://arxiv.org/abs/2505.11528)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T04:45:19Z

主题：multimodal/world-models

细分问题：multimodal · world-models · latent · diffusion prediction

架构：latent diffusion · DINO geometric features · CLIP semantic features · diffusion policy

训练监督：future latent prediction · pretrained visual feature alignment

历史链接：[链接1](https://arxiv.org/abs/2505.11528)

核验来源：[原始来源1](https://arxiv.org/abs/2505.11528)

### p050

**[Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](https://arxiv.org/abs/2607.04546)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:58:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · action-conditioned · mask dynamics and rendering

架构：two-stage mask dynamics · ControlNet · Stable Video Diffusion

训练监督：simulation pretraining · real-demonstration finetuning · action-conditioned mask prediction

历史链接：[链接1](https://arxiv.org/abs/2607.04546)

核验来源：[原始来源1](https://arxiv.org/abs/2607.04546)

### p051

**[A Survey of World Models for Autonomous Driving](https://arxiv.org/abs/2501.11260)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T00:59:38Z

主题：multimodal/world-models

细分问题：multimodal · world-models · surveys · autonomous driving

训练监督：survey

历史链接：[链接1](https://arxiv.org/abs/2501.11260)

核验来源：[原始来源1](https://arxiv.org/abs/2501.11260)

### p052

**[Object-Centric World Model for Language-Guided Manipulation](https://arxiv.org/abs/2503.06170)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T11:35:25Z

主题：multimodal/world-models

细分问题：multimodal · world-models · object-centric · language-conditioned prediction

架构：slot attention · language-conditioned latent predictor

训练监督：latent future-state prediction

历史链接：[链接1](https://arxiv.org/abs/2503.06170)

核验来源：[原始来源1](https://arxiv.org/abs/2503.06170)

### p053

**[Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](https://arxiv.org/abs/2607.13451)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T11:35:25Z

主题：multimodal/world-models

细分问题：multimodal · world-models · physics · hybrid residual deformable dynamics

架构：spring-mass simulator · sliding-window transformer · 3D Gaussian Splatting

训练监督：physics-guided residual dynamics fitting

历史链接：[链接1](https://arxiv.org/abs/2607.13451)

核验来源：[原始来源1](https://arxiv.org/abs/2607.13451)

### p054

**[A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](https://arxiv.org/abs/2601.03200)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T11:35:25Z

主题：multimodal/world-models

细分问题：multimodal · world-models · geometry · executable digital twins

架构：3D Gaussian Splatting · semantic fusion · collision geometry · Unity-ROS2-MoveIt

训练监督：sparse RGB reconstruction

历史链接：[链接1](https://arxiv.org/abs/2601.03200)

核验来源：[原始来源1](https://arxiv.org/abs/2601.03200)

### p055

**[Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](https://arxiv.org/abs/2506.07454)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T11:35:25Z

主题：multimodal/world-models

细分问题：multimodal · world-models · geometry · scene graphs and planning

架构：3D scene graph · LLM-to-PDDL · multi-robot mapping

训练监督：not established from abstract

历史链接：[链接1](https://arxiv.org/abs/2506.07454)

核验来源：[原始来源1](https://arxiv.org/abs/2506.07454)

### p056

**[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T11:35:25Z

主题：multimodal/world-models

细分问题：multimodal · world-models · action-conditioned · executability alignment

架构：video generative model · inverse dynamics model

训练监督：reinforcement-learning post-training · inverse-dynamics action rewards

历史链接：[链接1](https://arxiv.org/abs/2603.17808)

核验来源：[原始来源1](https://arxiv.org/abs/2603.17808)

### p057

**[Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T11:35:25Z

主题：multimodal/world-models

细分问题：multimodal · world-models · action-conditioned · action-flow interface

架构：action-flow conditioned video model · action head

训练监督：cross-embodiment action-consequence learning

历史链接：[链接1](https://arxiv.org/abs/2608.18077)

核验来源：[原始来源1](https://arxiv.org/abs/2608.18077)

### p058

**[UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](https://arxiv.org/abs/2505.06111)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T04:45:19Z

主题：multimodal/world-models

细分问题：multimodal · world-models · latent-action · cross-embodiment policy

架构：DINO-space latent action model · language conditioning · action decoder

训练监督：internet-video pretraining · task-centric latent action learning

历史链接：[链接1](https://arxiv.org/abs/2505.06111)

核验来源：[原始来源1](https://arxiv.org/abs/2505.06111)

### p059

**[What Do Latent Action Models Actually Learn?](https://arxiv.org/abs/2506.15691)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T04:45:19Z

主题：multimodal/world-models

细分问题：multimodal · world-models · latent-action · theory and identifiability

架构：linear latent-action analysis · PCA connection

训练监督：auxiliary action prediction

评估：unlabeled-video representation analysis

历史链接：[链接1](https://arxiv.org/abs/2506.15691)

核验来源：[原始来源1](https://arxiv.org/abs/2506.15691)

### p060

**[LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](https://arxiv.org/abs/2604.11689)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-23T04:45:19Z

主题：multimodal/world-models

细分问题：multimodal · world-models · latent-action · benchmarks and evaluation

架构：benchmark · visual and latent-action representations

评估：semantic-action evaluation · low-level control evaluation

历史链接：[链接1](https://arxiv.org/abs/2604.11689)

核验来源：[原始来源1](https://arxiv.org/abs/2604.11689)

### p061

**[Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](https://arxiv.org/abs/2608.26103)**

来源：用户在聊天提供链接

来源日期：2026-08-29T08:30:47Z

主题：multimodal/world-models

细分问题：multimodal · world-models · action-conditioned · in-context human-video guidance

架构：causal video-action model

训练监督：paired human-robot video learning · in-context future chunk prediction

历史链接：[链接1](https://arxiv.org/abs/2608.26103)

核验来源：[原始来源1](https://arxiv.org/abs/2608.26103)

### p062

**[PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](https://www.roboticsproceedings.org/rss21/p153.html)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T11:35:25Z

主题：multimodal/world-models

细分问题：multimodal · world-models · physics · differentiable rigid-body identification

架构：differentiable physics simulator · Gaussian Splatting · digital cousins

训练监督：visual observational loss · few-shot physical trajectories · physics-aware randomization · model-based reinforcement learning

历史链接：[链接1](https://www.roboticsproceedings.org/rss21/p153.html)

核验来源：[原始来源1](https://www.roboticsproceedings.org/rss21/p153.html)

### p063

**[World Models for Robotic Manipulation: A Survey](https://onlinelibrary.wiley.com/doi/10.1002/smb2.70053)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-04T10:29:23Z

主题：multimodal/world-models

细分问题：multimodal · world-models · surveys · robot manipulation

训练监督：survey

历史链接：[链接1](https://onlinelibrary.wiley.com/doi/10.1002/smb2.70053)

核验来源：[原始来源1](https://onlinelibrary.wiley.com/doi/10.1002/smb2.70053)

### p064

**[RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · generalist-policy

架构：transformer · discrete-action

训练监督：robot-demonstration · behavior-cloning

核验来源：[原始来源1](https://arxiv.org/abs/2212.06817)

### p065

**[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · vlm-to-policy

架构：VLM · action-as-text

训练监督：web-vision-language · robot-demonstration · co-training

核验来源：[原始来源1](https://arxiv.org/abs/2307.15818)

### p066

**[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · cross-embodiment-data

架构：dataset · RT-X

训练监督：cross-embodiment-demonstrations

核验来源：[原始来源1](https://arxiv.org/abs/2310.08864)

### p067

**[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · action-generation · diffusion

架构：diffusion-policy

训练监督：robot-demonstration · behavior-cloning

核验来源：[原始来源1](https://arxiv.org/abs/2303.04137)

### p068

**[Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · generalist-policy

架构：transformer · diffusion-action-head

训练监督：robot-demonstration · cross-embodiment

核验来源：[原始来源1](https://arxiv.org/abs/2405.12213)

### p069

**[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)**

来源：已有手册提取；先前建立的基础种子条目

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · vlm-to-policy · 机器人与具身智能

架构：VLM · autoregressive-action

训练监督：robot-demonstration · fine-tuning

问题：VLA 的开放使用与新任务适配。方法：7B 语言模型结合视觉编码器，在机器人示范上训练，并研究高效微调。原文证据：多任务操纵和适配实验。

证据边界与关联判断：操纵评测不能替代移动导航或四足稳定性验证；适合从编码器、数据配比、动作接口、微调成本切入与你的多模态训练问题对照。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

核验来源：[原始来源1](https://arxiv.org/abs/2406.09246)

### p070

**[$π_0$: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · action-generation · flow

架构：VLM · flow-matching

训练监督：robot-demonstration

核验来源：[原始来源1](https://arxiv.org/abs/2410.24164)

### p071

**[FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · action-tokenization

架构：frequency-action-tokenizer

训练监督：action-reconstruction

核验来源：[原始来源1](https://arxiv.org/abs/2501.09747)

### p072

**[Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · adaptation-efficiency

架构：parallel-decoding · action-chunking

训练监督：fine-tuning

核验来源：[原始来源1](https://arxiv.org/abs/2502.19645)

### p073

**[$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · generalization · open-world

架构：VLA · hybrid-multimodal

训练监督：heterogeneous-co-training

核验来源：[原始来源1](https://arxiv.org/abs/2504.16054)

### p074

**[SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · efficiency · small-VLA

架构：small-VLA

训练监督：robot-demonstration

核验来源：[原始来源1](https://arxiv.org/abs/2506.01844)

### p075

**[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/control

细分问题：robotics · embodied-learning · VLA · humanoid · generalist

架构：dual-system-VLA

训练监督：robot-demonstration · heterogeneous-data

核验来源：[原始来源1](https://arxiv.org/abs/2503.14734)

### p076

**[$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · generalization · context-conditioning

架构：VLA · multimodal-context

训练监督：demonstrations · autonomous-data · non-robot-data

核验来源：[原始来源1](https://arxiv.org/abs/2604.15483)

### p077

**[Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/abs/2605.30280)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · cross-embodiment

架构：VLA

训练监督：multi-task-training

核验来源：[原始来源1](https://arxiv.org/abs/2605.30280)

### p078

**[X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](https://arxiv.org/abs/2606.14752)**

来源：已有手册提取

来源日期：2026-09-11

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · action-tokenization

架构：semantic-residual-quantization

训练监督：masked-action-modeling · contrastive-alignment · next-frame-feature-prediction

核验来源：[原始来源1](https://arxiv.org/abs/2606.14752)

### p079

**[ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://arxiv.org/abs/2505.22159)**

来源：已有手册提取

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA · contact-rich-manipulation

架构：force-aware-MoE · VLA

训练监督：multimodal-demonstrations

核验来源：[原始来源1](https://arxiv.org/abs/2505.22159)

### p080

**[SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](https://arxiv.org/abs/1609.05130)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-08T10:38:59Z

主题：robotics/perception · robotics/localization-mapping

细分问题：robotics · traditional-pipeline · perception-mapping · semantic-mapping

架构：CNN · geometric-fusion

训练监督：semantic-labels

历史链接：[链接1](https://arxiv.org/abs/1609.05130?utm_source=chatgpt.com)

核验来源：[原始来源1](https://arxiv.org/abs/1609.05130)

### p081

**[PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](https://arxiv.org/abs/1903.01177)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-08T10:38:59Z

主题：robotics/perception · robotics/localization-mapping

细分问题：robotics · traditional-pipeline · perception-mapping · semantic-mapping

架构：CNN · geometric-fusion

训练监督：semantic-labels

历史链接：[链接1](https://arxiv.org/abs/1903.01177?utm_source=chatgpt.com)

核验来源：[原始来源1](https://arxiv.org/abs/1903.01177)

### p082

**[DS-VIO: Robust and Efficient Stereo Visual Inertial Odometry based on Dual Stage EKF](https://arxiv.org/abs/1905.00684)**

来源：历史聊天中的助手推荐链接

来源日期：2026-01-07T09:57:51Z

主题：robotics/localization-mapping

细分问题：robotics · traditional-pipeline · state-estimation · visual-inertial-odometry

架构：dual-stage-EKF

训练监督：model-based-estimation

历史链接：[链接1](https://arxiv.org/abs/1905.00684)

核验来源：[原始来源1](https://arxiv.org/abs/1905.00684)

### p083

**[PLV-IEKF: Consistent Visual-Inertial Odometry using Points, Lines, and Vanishing Points](https://arxiv.org/abs/2311.04477)**

来源：历史聊天中的助手推荐链接

来源日期：2026-01-07T09:57:51Z

主题：robotics/localization-mapping

细分问题：robotics · traditional-pipeline · state-estimation · visual-inertial-odometry

架构：IEKF

训练监督：model-based-estimation

历史链接：[链接1](https://arxiv.org/abs/2311.04477)

核验来源：[原始来源1](https://arxiv.org/abs/2311.04477)

### p084

**[EqVIO: An Equivariant Filter for Visual Inertial Odometry](https://arxiv.org/abs/2205.01980)**

来源：历史聊天中的助手推荐链接

来源日期：2026-01-07T09:57:51Z

主题：robotics/localization-mapping

细分问题：robotics · traditional-pipeline · state-estimation · visual-inertial-odometry

架构：equivariant-filter

训练监督：model-based-estimation

历史链接：[链接1](https://arxiv.org/abs/2205.01980)

核验来源：[原始来源1](https://arxiv.org/abs/2205.01980)

### p085

**[A Self-Supervised, Differentiable Kalman Filter for Uncertainty-Aware Visual-Inertial Odometry](https://arxiv.org/abs/2203.07207)**

来源：历史聊天中的助手推荐链接

来源日期：2026-01-07T09:57:51Z

主题：robotics/localization-mapping

细分问题：robotics · traditional-pipeline · state-estimation · visual-inertial-odometry

架构：differentiable-Kalman-filter

训练监督：self-supervised

历史链接：[链接1](https://arxiv.org/abs/2203.07207)

核验来源：[原始来源1](https://arxiv.org/abs/2203.07207)

### p086

**[Learned IMU Bias Prediction for Invariant Visual Inertial Odometry](https://arxiv.org/abs/2505.06748)**

来源：历史聊天中的助手推荐链接

来源日期：2026-01-07T09:57:51Z

主题：robotics/localization-mapping

细分问题：robotics · traditional-pipeline · state-estimation · visual-inertial-odometry

架构：learned-IMU-bias

训练监督：learned-bias-prediction

历史链接：[链接1](https://arxiv.org/abs/2505.06748)

核验来源：[原始来源1](https://arxiv.org/abs/2505.06748)

### p087

**[RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-24T08:13:40Z

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · physical-ICL

架构：context-scaling

训练监督：imitation-learning

历史链接：[链接1](https://arxiv.org/abs/2607.15275)

核验来源：[原始来源1](https://arxiv.org/abs/2607.15275)

### p088

**[In-Context Imitation Learning via Next-Token Prediction](https://arxiv.org/abs/2408.15980)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-24T08:13:40Z

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · physical-ICL

架构：next-token-prediction

训练监督：imitation-learning

历史链接：[链接1](https://arxiv.org/abs/2408.15980)

核验来源：[原始来源1](https://arxiv.org/abs/2408.15980)

### p089

**[Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](https://arxiv.org/abs/2606.30457)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-24T08:13:40Z

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · physical-ICL

架构：demonstration-prompting

训练监督：imitation-learning

历史链接：[链接1](https://arxiv.org/abs/2606.30457)

核验来源：[原始来源1](https://arxiv.org/abs/2606.30457)

### p090

**[InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](https://arxiv.org/abs/2601.02456)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-24T08:13:40Z

主题：robotics/embodied-policies

细分问题：robotics · embodied-learning · VLA

架构：unified-understanding-generation-action

训练监督：imitation-learning

历史链接：[链接1](https://arxiv.org/abs/2601.02456)

核验来源：[原始来源1](https://arxiv.org/abs/2601.02456)

### p091

**[CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion](https://arxiv.org/abs/2211.00458)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:12:47Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · gait-generation

架构：CPG

训练监督：reinforcement-learning

历史链接：[链接1](https://arxiv.org/abs/2211.00458)

核验来源：[原始来源1](https://arxiv.org/abs/2211.00458)

### p092

**[Learning Quadruped Locomotion using Bio-Inspired Neural Networks with Intrinsic Rhythmicity](https://arxiv.org/abs/2305.07300)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:18:35Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · gait-generation

架构：intrinsic-rhythmic-network

训练监督：reinforcement-learning

历史链接：[链接1](https://arxiv.org/pdf/2305.07300)

核验来源：[原始来源1](https://arxiv.org/abs/2305.07300)

### p093

**[Learning Free Gait Transition for Quadruped Robots via Phase-Guided Controller](https://arxiv.org/abs/2201.00206)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:12:47Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · gait-generation

架构：phase-guided-controller

训练监督：reinforcement-learning

历史链接：[链接1](https://arxiv.org/abs/2201.00206)

核验来源：[原始来源1](https://arxiv.org/abs/2201.00206)

### p094

**[Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](https://arxiv.org/abs/2011.01387)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:12:47Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · gait-generation

架构：periodic-reward-composition

训练监督：reinforcement-learning

历史链接：[链接1](https://arxiv.org/abs/2011.01387)

核验来源：[原始来源1](https://arxiv.org/abs/2011.01387)

### p095

**[Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](https://arxiv.org/abs/2404.05695)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:18:23Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · whole-body-control

架构：sim-to-real

训练监督：reinforcement-learning

历史链接：[链接1](https://arxiv.org/abs/2404.05695)

核验来源：[原始来源1](https://arxiv.org/abs/2404.05695)

### p096

**[Learning from Massive Human Videos for Universal Humanoid Pose Control](https://arxiv.org/abs/2412.14172)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:18:23Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · whole-body-control

架构：video-to-pose-control

训练监督：human-videos

历史链接：[链接1](https://arxiv.org/abs/2412.14172)

核验来源：[原始来源1](https://arxiv.org/abs/2412.14172)

### p097

**[A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots](https://arxiv.org/abs/2506.20487)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:18:23Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · survey

架构：survey

训练监督：mixed-or-not-applicable

历史链接：[链接1](https://arxiv.org/abs/2506.20487)

核验来源：[原始来源1](https://arxiv.org/abs/2506.20487)

### p098

**[Scaling Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2607.15163)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:18:23Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · whole-body-control

架构：behavior-foundation-model

训练监督：mixed-or-not-applicable

历史链接：[链接1](https://arxiv.org/abs/2607.15163)

核验来源：[原始来源1](https://arxiv.org/abs/2607.15163)

### p099

**[Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning](https://arxiv.org/abs/2501.02116)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:18:23Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · survey

架构：survey

训练监督：mixed-or-not-applicable

历史链接：[链接1](https://arxiv.org/abs/2501.02116)

核验来源：[原始来源1](https://arxiv.org/abs/2501.02116)

### p100

**[Attention-Based Map Encoding for Learning Generalized Legged Locomotion](https://arxiv.org/abs/2506.09588)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-22T11:49:26Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · perceptive-locomotion

架构：attention-map-encoder

训练监督：reinforcement-learning

历史链接：[链接1](https://arxiv.org/html/2506.09588v1)

核验来源：[原始来源1](https://arxiv.org/abs/2506.09588)

### p101

**[Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](https://arxiv.org/abs/2601.08485)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-22T11:49:26Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · perceptive-locomotion

架构：attention-map-encoder

训练监督：reinforcement-learning

历史链接：[链接1](https://arXiv.org/abs/2601.08485)

核验来源：[原始来源1](https://arxiv.org/abs/2601.08485)

### p102

**[DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T09:26:21Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · motion-imitation

架构：physics-based-character-policy

训练监督：motion-reference-imitation

历史链接：[链接1](https://arxiv.org/abs/1804.02717)

核验来源：[原始来源1](https://arxiv.org/abs/1804.02717)

### p103

**[ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](https://arxiv.org/abs/2205.01906)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T09:26:21Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · motion-imitation

架构：adversarial-skill-embedding

训练监督：adversarial-imitation

历史链接：[链接1](https://arxiv.org/abs/2205.01906)

核验来源：[原始来源1](https://arxiv.org/abs/2205.01906)

### p104

**[ExBody2: Advanced Expressive Humanoid Whole-Body Control](https://arxiv.org/abs/2412.13196)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T09:26:21Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · motion-imitation

架构：whole-body-controller

训练监督：motion-reference-imitation

历史链接：[链接1](https://arxiv.org/abs/2412.13196)

核验来源：[原始来源1](https://arxiv.org/abs/2412.13196)

### p105

**[BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](https://arxiv.org/abs/2508.08241)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T09:26:21Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · motion-imitation

架构：guided-diffusion

训练监督：motion-reference-imitation

历史链接：[链接1](https://arxiv.org/abs/2508.08241)

核验来源：[原始来源1](https://arxiv.org/abs/2508.08241)

### p106

**[Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](https://arxiv.org/abs/2510.02252)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T09:26:21Z

主题：robotics/control

细分问题：robotics · embodied-learning · humanoid · motion-imitation

架构：motion-retargeting

训练监督：motion-retargeting

历史链接：[链接1](https://arxiv.org/abs/2510.02252)

核验来源：[原始来源1](https://arxiv.org/abs/2510.02252)

### p107

**[PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots](https://arxiv.org/abs/2408.13740)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T14:17:35Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · perceptive-locomotion

架构：implicit-explicit-framework

训练监督：reinforcement-learning

历史链接：[链接1](https://arxiv.org/pdf/2408.13740)

核验来源：[原始来源1](https://arxiv.org/abs/2408.13740)

### p108

**[Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](https://pmc.ncbi.nlm.nih.gov/articles/PMC6164553/)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-08T10:38:59Z

主题：robotics/perception · robotics/localization-mapping

细分问题：robotics · traditional-pipeline · perception-mapping · semantic-mapping

架构：pixel-voxel-network · RGB-D-SLAM

训练监督：semantic-labels

历史链接：[链接1](https://pmc.ncbi.nlm.nih.gov/articles/PMC6164553/)

核验来源：[原始来源1](https://pmc.ncbi.nlm.nih.gov/articles/PMC6164553/)

### p109

**[FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](https://github.com/HKUST-Aerial-Robotics/FM-Fusion)**

来源：历史聊天中的助手推荐链接

来源日期：2026-09-08T10:38:59Z

主题：robotics/perception · robotics/localization-mapping

细分问题：robotics · traditional-pipeline · perception-mapping · open-vocabulary-instance-mapping

架构：vision-language-foundation-model · mapping

训练监督：pretrained-foundation-model

历史链接：[链接1](https://github.com/HKUST-Aerial-Robotics/FM-Fusion)

核验来源：[原始来源1](https://github.com/HKUST-Aerial-Robotics/FM-Fusion)

### p110

**[Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](https://proceedings.mlr.press/v205/margolis23a/margolis23a.pdf)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T08:12:47Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · gait-generation

架构：multiplicity-of-behavior

训练监督：reinforcement-learning

历史链接：[链接1](https://proceedings.mlr.press/v205/margolis23a/margolis23a.pdf)

核验来源：[原始来源1](https://proceedings.mlr.press/v205/margolis23a.html)

### p111

**[Legged Locomotion in Challenging Terrains using Egocentric Vision](https://proceedings.mlr.press/v205/agarwal23a/agarwal23a.pdf)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T14:17:35Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · perceptive-locomotion

架构：depth-vision-policy

训练监督：reinforcement-learning · supervised-distillation

历史链接：[链接1](https://proceedings.mlr.press/v205/agarwal23a/agarwal23a.pdf)

核验来源：[原始来源1](https://proceedings.mlr.press/v205/agarwal23a.html)

### p112

**[MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202524345?af=R)**

来源：历史聊天中的助手推荐链接

来源日期：2026-08-21T14:17:35Z

主题：robotics/control

细分问题：robotics · embodied-learning · legged-locomotion · perceptive-locomotion

架构：depth-perception-model

训练监督：recipe-needs-full-text-review

历史链接：[链接1](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202524345?af=R)

核验来源：[原始来源1](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202524345?af=R)

### p113

**[Attention Is All You Need](https://arxiv.org/abs/1706.03762)**

来源：先前建立的基础种子条目

主题：llm/architecture

细分问题：模型训练与多模态

问题：如何摆脱序列模型中的循环与卷积瓶颈。方法：基于注意力的 Transformer。原文证据：机器翻译任务及句法分析验证；不能直接据此断言现代 LLM、视觉或机器人任务中的收益。

关联判断：理解注意力与后续缓存、结构改动的共同起点；本文不直接解决 KV cache 压缩。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

核验来源：[原始来源1](https://arxiv.org/abs/1706.03762)

### p114

**[Training Compute Optimal Large Language Models](https://arxiv.org/abs/2203.15556)**

来源：先前建立的基础种子条目

主题：cross-domain/interpretability

细分问题：模型训练与多模态

问题：固定训练算力如何分配模型大小与训练 token。方法：训练多组模型拟合计算最优规模关系，再用 Chinchilla 验证。原文证据：在研究覆盖的训练设置中支持模型大小和 token 协同增长。

证据边界：关联判断，不应把其经验规律当作所有数据质量、多模态配比或包含推理成本的通用最优解。关联判断：为数据量与规模选型建立基线。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

核验来源：[原始来源1](https://arxiv.org/abs/2203.15556)

### p115

**[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)**

来源：先前建立的基础种子条目

主题：llm/posttraining/preferences

细分问题：模型训练与多模态

问题：语言预训练目标与用户意图不一致。方法：示范数据监督微调，再用人类输出排序进行强化学习微调。原文证据：作者提示分布上的人工偏好评估及部分 NLP 评测；模型仍会犯错。

关联判断：适合对照预训练、SFT、RL 各自使用的数据与优化目标；偏好改善不等于所有能力提高，也不直接证明机器人闭环可靠。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

核验来源：[原始来源1](https://arxiv.org/abs/2203.02155)

2026-09-30 定向阅读：预训练、示范监督与偏好反馈为何分阶段组织？ 作者使用示范数据监督微调，再使用模型输出排名进行RLHF。

边界：偏好结果限于作者评估的提示分布；不能推出SFT数据不可混入预训练，也不能直接比较不同定义的损失。未全文精读或复现。

用户关联：2026-09-30 03:10–03:11 UTC关于SFT损失和数据纳入时机的实际问题。 来源：原有starter；本轮未恢复其历史聊天链接，不标成聊天提取。

### p116

**[RMA Rapid Motor Adaptation for Legged Robots](https://arxiv.org/abs/2107.04034)**

来源：先前建立的基础种子条目

主题：robotics/control

细分问题：机器人与具身智能

问题：四足机器人如何适应未见地形、负载等变化。方法：基础策略与适应模块组合，在仿真训练后部署到 A1。原文证据：仿真与多种真实地形实验，无真机微调。

证据边界与关联判断：不能由单一平台结果推出任何传感器组合都有效；与适应、特权信息及部署观测差异相关，可作为教师学生路线的比较入口，本文不等同于深度加 IMU 导航方案。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

核验来源：[原始来源1](https://arxiv.org/abs/2107.04034)

### p117

**[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)**

来源：先前建立的基础种子条目

主题：multimodal/world-models

细分问题：机器人与具身智能

问题：RL 在跨任务应用时如何减少专门调参。方法：DreamerV3 学习环境模型，再通过想象轨迹改进行为，并用稳定化机制提高跨域训练适用性。原文证据：多种控制与游戏任务。

证据边界与关联判断：任务表现不能单独证明 latent 具有因果物理结构，也不能直接证明真机安全性；适合围绕可预测、可干预、等变性与长期控制分别设计检验。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

核验来源：[原始来源1](https://arxiv.org/abs/2301.04104)



