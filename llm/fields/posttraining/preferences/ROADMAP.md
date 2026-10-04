# 偏好学习路线图

> 状态：路线图 · v1

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md) · [后训练总览](../README.md)

结论：五步，按"先会训练一个奖励模型 → 看它怎样被钻空子 → 换成 DPO 并看它的新坑 → 看工业团队怎样取舍 → 看评委变成生成模型"排列。每一步有一个能动手检验的问题。

## 第 1 步：从一对回答到奖励模型

读 [InstructGPT 精读](../../../papers/instructgpt/reading.md)第 5–6 节，对照[概率分类讲义](../../../../foundations/lessons/modules/objectives/02-classification-probabilities.md)第 5–6 节。

为什么在这里：奖励模型的损失就是 Bradley–Terry 下的二分类负对数似然；DPO、生成式奖励模型都从这里出发。精读里有一个可以手算的博物馆例子。

检验：给定奖励模型对被选、落选回答的打分 1.2 与 0.2，算出预测偏好概率与损失（精读给出约 0.731 与 0.313）；再说明为什么一个提示的 K 个回答两两组合后不能随意打散成独立样本（精读第 5.3 节）。

## 第 2 步：奖励模型怎样被钻空子

读 [Christiano 等](../../../papers/arxiv-1706.03741/README.md)第 3.3 节 → [Stiennon 等](../../../papers/arxiv-2009.01325/README.md)图 5 → [Gao 等](../../../papers/arxiv-2210.10760/README.md) → [Singhal 等](../../../papers/arxiv-2310.03716/README.md)。

为什么在这里：四篇按时间给出同一个坑的四个侧面：离线奖励失效、强优化后与人负相关、过度优化的规模规律、改进主要来自变长。读完再看 InstructGPT 的 KL 惩罚与 PPO-ptx，就知道它们在防什么、防不住什么。

检验：用自己的四足 RL 经验举一个"奖励函数被策略钻空子"的例子，对应到 Stiennon 图 5 的哪一段；再说出 Gao 等关于 KL 惩罚的结论与它的适用条件。

## 第 3 步：去掉奖励模型之后

读 [DPO 精读](../../../papers/dpo/reading.md)第 6–10 节，再读 [Xu 等](../../../papers/arxiv-2404.10719/README.md)与 [IPO](../../../papers/arxiv-2310.12036/README.md)。

为什么在这里：这是 [Baseline 页](BASELINES.md)的第二个基线；Xu 等与 IPO 从实验与理论两侧指出它的分布外与过拟合问题，和第 2 步的"离线奖励失效"是同一个根源。

检验：在 policy = reference 时手算 DPO 损失（应为 log 2）；交换一对偏好的方向，确认梯度符号随之翻转；在小模型上比较"只用被选回答做 SFT"与 DPO 的差别；再构造一个只被比较过一次的偏好对，说明为什么 DPO 会把落选回答的概率往 0 推（IPO §4.2）。

## 第 4 步：工业团队怎样取舍

读 [Llama 2](../../../papers/arxiv-2307.09288/README.md)第 3.2 节 → [Llama 3](../../../papers/arxiv-2407.21783/README.md)第 4.1 节 → [Tulu 3](../../../papers/arxiv-2411.15124/README.md)第 5 节。

为什么在这里：同一团队从"两个奖励模型 + 拒绝采样 + PPO"换到"奖励模型 + 拒绝采样 + DPO"，又给 DPO 打了 NLL 与格式 token 两个补丁；Tulu 3 把开源配方与 PPO 对照完整公开。三篇合起来是 [Baseline 表](BASELINES.md)"优化方式"与"正则"两行的来源。

检验：列出 Llama 3 对 DPO 的两处修改，各自防的是哪种退化；解释为什么每轮都要用最新模型重采偏好（Llama 2 §3.2.1）。

## 第 5 步：评委变成会推理的模型

读 [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md)第 3.1 节与附录 B.5 → [Kimi K2](../../../papers/arxiv-2507.20534/README.md)第 3.2.2 节 → [DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md)第 5.1.1 节，对照 [LLM-as-a-Judge](../../../../cross-domain/papers/llm-judge/README.md)。

为什么在这里：2025 年以后偏好信号主要用于不可验证的任务，评委从标量打分器换成按 rubric 推理的生成模型；R1 附录 B.5 的奖励黑客曲线说明这条路仍有老问题。

检验：为一个写作任务设计一套 rubric 奖励，指出它最可能被钻的空子（长度、套话、迎合），并说明 K3 的长度预算或 R1 的长度相当偏好对怎样防它。

## 动手时先查什么

训练奖励模型或做 DPO 之前，先检查偏好数据：被选与落选回答的长度分布是否相当（Singhal 等、R1）；比较是否来自当前策略的输出（Llama 2、Tulu 3）；同一提示的多个比较是否放在同一批次里（InstructGPT）；格式 token 是否会进入 DPO 损失（Llama 3）。训练中同时看三件事：奖励或隐式奖励间隔、相对参考模型的 KL、一组标准 benchmark 上的对齐税；只看奖励上升最容易被骗。
