# SFT 路线图

> 状态：路线图 · v1

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md) · [后训练总览](../README.md)

结论：六步，按"先会构造一条 SFT 样本 → 知道示范从哪来、要多少 → 知道什么不该教 → 看 SFT 怎样变成冷启动与蒸馏 → 在受控实验里比较 SFT 与 RL → 看 OPD 的成败与验收"排列。每一步有一个能动手检验的问题。

## 第 1 步：一条 SFT 样本怎样变成损失

读 [InstructGPT 精读](../../../papers/instructgpt/reading.md)第 3–4 节，对照[自监督与生成目标](../../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 2–3 节。

为什么在这里：SFT 与预训练用同一个损失，区别只在"哪些 token 参与计算"；不先弄清这一点，后面的模板、打包、格式 token 问题都无从谈起。精读第 4.3 节还会让你看到第一个坑：验证损失与人评分开走。

检验：给一段两轮对话（用户、助手、用户、助手）标出哪些 token 参与损失；再说明把三条短对话打包进一个序列时，为什么要额外的掩码让它们互相不可见（DeepSeek-V3 §5.1）。

## 第 2 步：示范从哪来、要多少

读 [FLAN](../../../papers/arxiv-2109.01652/README.md) → [Flan-PaLM](../../../papers/arxiv-2210.11416/README.md) → [LIMA](../../../papers/arxiv-2305.11206/README.md)，再读 [Llama 2](../../../papers/arxiv-2307.09288/README.md) 第 3.1 节。

为什么在这里：这四篇给出了示范来源与规模的两极：1,836 个任务的公开数据，与 1,000 条、27,540 条精选数据。它们的结论并不矛盾，因为目标不同（zero-shot 任务泛化对比对话帮助性）。

检验：用一句话分别说出 FLAN"8B 以下受损"、Flan-PaLM"加 9 个思维链数据集"、LIMA"表层对齐假说"各自的实验条件；再解释为什么 Llama 2 认为 SFT 的上限是最好的标注员。

## 第 3 步：什么不该放进 SFT

读 [Gekhman 等](../../../papers/arxiv-2405.05904/README.md)，再读 [Llama 3](../../../papers/arxiv-2407.21783/README.md) 第 4.3.6 节与 [DeepSeek LLM](../../../papers/arxiv-2401.02954/README.md) 的对齐一节。

为什么在这里：这一步回答总览页"SFT 学不到新知识反而可能增加幻觉"的来源；Llama 3 的知识探针是把它落到数据流程里的做法，DeepSeek LLM 的重复率是另一个由数据引起的退化。

检验：为自己的一个 SFT 数据集设计一个"未知事实"过滤器：怎样判断基座知不知道（Gekhman 用不同的少样本提示让基座贪心解码与带温度采样，按答对的比例分档），判断为不知道时是删掉、改成拒答，还是保留并早停。

## 第 4 步：SFT 变成冷启动与蒸馏

读 [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md) 第 3 节、附录 B.3 与附录 F，对照 [Qwen3](../../../papers/arxiv-2505.09388/README.md) 第 4.1、4.5 节与 [s1](../../../papers/arxiv-2501.19393/README.md)。

为什么在这里：这是 [Baseline 页](BASELINES.md)第二个基线的出处；Qwen3 把蒸馏推进到 on-policy，s1 说明 1,000 条推理数据加推理时控制就能走很远。

检验：解释两件事：R1-Distill-Qwen-32B 为什么好于在同一基座上直接做 1 万步以上 RL 的 Qwen2.5-32B-Zero（附录 F.1）；R1 Dev1 为什么在冷启动之后 AIME 反而从 77.9% 掉到 59.0%（Table 3）。

## 第 5 步：SFT 与 RL 的分工

读 [SFT Memorizes, RL Generalizes](../../../papers/arxiv-2501.17161/README.md)，对照 [Qwen3](../../../papers/arxiv-2505.09388/README.md) Table 21 与 [Yue 等](../../../papers/arxiv-2504.13837/README.md)。

为什么在这里：前四步都是 SFT 自己的视角，这一步把它放回整条后训练流水线；三篇合起来回答"什么时候用 SFT、什么时候用 RL、什么时候用蒸馏"。

检验：从同一个检查点出发，分别做 SFT（离线蒸馏）、RL、on-policy 蒸馏，预测 pass@1 与 pass@64 各自怎样变化，并用 Qwen3 Table 21 的数字核对。

## 第 6 步：OPD 为什么有效，又怎样失败（2025–2026）

读 [On-Policy Distillation](../../../papers/thinking-machines-on-policy-distillation/README.md) → [Rethinking OPD](../../../papers/arxiv-2604.13016/README.md) → [Rethinking OPD II](../../../papers/arxiv-2609.04172/README.md)，再对照 [Solving Without Stopping](../../../papers/arxiv-2609.37326/README.md)。

为什么在这里：第 5 步选定了训练范式，这一步选择实际可用的师生与数据。先理解学生自己采样如何改变训练分布，再看师生思考模式与教师能力的条件，最后把“提示够不够”与“能否正确结束”拆开。

检验：固定同一教师和学生，对照少量多样提示与全量提示；同时记录总 rollout token、教师调用、准确率、结束思考的比例与到达长度上限的比例。若准确率上升、完成率下降，先检查停止行为，再决定是否加数据或放宽长度。用两篇 9 月论文的实验范围，说明哪些结果尚不能直接外推到长程工具智能体。

## 动手时先查什么

在自己的模型上做 SFT 时，先核对四件事再谈调参：对话模板与特殊 token 是否与推理时一致（Llama 3 发现格式 token 会引起结尾重复）；损失掩码是否只覆盖回答；打包时样本是否互相隔离；训练集与评测集是否去重（Tulu 3 的做法）。训练中除了看损失，还要看重复率、平均回答长度和一组未见评测，因为验证损失与回答质量会分开走。
