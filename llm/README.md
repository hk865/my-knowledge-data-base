# 大语言模型

[回到全库](../README.md) · [基础概念](../foundations/README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文与资源](PAPERS.md)

## 按细分方向学习

七个方向按"模型怎样造出来、怎样用起来"排列：先预训练，再后训练的三个阶段，然后是贯穿两者的结构、推理与长上下文。每个方向有入门页、Baseline 页、路线图和论文列表。

| 方向 | 回答什么 | 入门页 |
|---|---|---|
| 预训练 | 下一词预测怎样学到结构先验与世界知识；2023 年以后的报告在稳定性、注意力、上下文、深度、知识与训练方式上各改了什么 | [入门](fields/pretraining/README.md) |
| 后训练（总览） | SFT、偏好学习、强化学习、蒸馏各学什么、学不到什么；奖励从哪来 | [入门](fields/posttraining/README.md) |
| 　监督微调 SFT | 示范数据教格式与"调用哪部分已有能力"，以及新知识带来的幻觉 | [入门](fields/posttraining/sft/README.md) |
| 　偏好学习与奖励模型 | 用比较信号学取舍：RLHF、DPO 及其奖励黑客与长度偏置 | [入门](fields/posttraining/preferences/README.md) |
| 　语言模型强化学习 | PPO → GRPO → 可验证奖励的 RL，熵坍缩、长度偏置，以及 RL 专家加蒸馏合并 | [入门](fields/posttraining/rl/README.md) |
| 架构与效率 | 注意力及其替代、MoE 与查表记忆、残差与归一化各用什么能力换效率；含 DeepSeek 架构线 | [入门](fields/architecture/README.md) |
| 推理时计算 | 回答时多花算力（思维链、搜索、长思考）何时有效、何时失效，以及投机解码与服务效率 | [入门](fields/inference/README.md) |
| 长上下文与记忆 | 位置编码、数据课程、后训练与推理成本四项验收，以及"窗口长度不等于长程能力" | [入门](fields/long-context/README.md) |
| 评测（跨方向） | 评测怎样定义"好"，为什么会失效；能自动打分的评测怎样变成奖励与 RL 环境，进而塑造模型行为；各领域测什么 | [入门](../cross-domain/fields/evaluation/README.md) |
| Agent（跨方向） | 编码与工具使用 agent 怎样从提示词走到后训练，agent 环境与奖励黑客 | [入门](../cross-domain/fields/agents/README.md) |

结构与训练的跨领域关系见[注意力与 FFN 的分工](../foundations/relations/attention-ffn-division.md)和[循环状态](../foundations/relations/recurrent-state.md)；训练稳定性、规模定律等跨领域问题见[训练科学](../cross-domain/fields/training-science/README.md)。

## 单篇论文目录

本领域收录 140 项资源，其中 17 篇有讲解；其他方向的相关论文通过索引交叉引用。

- [浏览本领域论文与跨方向引用](PAPERS.md)
- [直接浏览单篇文件夹](papers/README.md)

每篇论文的文件夹含文献卡README与source.json；有讲解的论文另含reading.md。

## 阅读状态标记

- 技术精读：按指定论文版本写的完整讲解
- 逐步教学版：在技术精读基础上补充逐步说明与算例
- 选定章节讲解：只讲论文中明确列出的章节
- 文献卡：论文身份、官方原文入口与定位

## 机制导读：大小模型草拟与验证

[两图机制导读](fields/inference/draft-verification-guide.md) · [2026年10月3日研究短报](../daily/2026-10-03.md)。精确采样与近似质量协作分开读。
