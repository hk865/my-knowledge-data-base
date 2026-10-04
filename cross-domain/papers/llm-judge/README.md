# Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

> 状态：技术精读 · 2023 · [原文](https://arxiv.org/abs/2306.05685)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：对齐后的聊天模型明显更受用户偏好，MMLU、HELM 这类基准却分不出它和基座；人类偏好评估又贵又慢（§1）。本文问：强 LLM 能否当裁判来近似人类偏好，这种一致在什么题目和统计口径下成立。
- **核心方法**：给出两套带人类判断的题集：MT-Bench（8 类、每类 10 题，共 80 道两轮问题）与 Chatbot Arena（匿名双模型对战、用户投票，论文用约 3 万票的早期快照）（§2）。裁判形式三种：成对比较、单答打分、参考答案引导（§3.1）。测出三种偏差：位置偏差（交换两份回答的顺序后判决保持一致的比例，GPT-4 65.0%、Claude-v1 23.8%，Table 2）、冗长偏差（把列表改述一遍放在前面、不增加信息，GPT-3.5 与 Claude 有 91.3% 判它更好，GPT-4 为 8.7%，Table 3）、数学题上被错误候选带偏（Table 4）；对策是交换顺序各判一次、先独立生成参考答案再评。GPT-4 成对裁判与人类在 MT-Bench 第一轮的一致率不含平局时 85%、含平局时 66%，人与人为 81% 和 63%（Table 5）。另外，只用约 3 千条精选对话微调的 Vicuna-7B，MT-Bench 5.95 接近全量版的 6.00，MMLU 却是 37.3 对 47.1（Table 8），说明偏好评测与能力评测测的是不同东西。
- **为什么在这个库里**：[评估方向 Baseline 页](../../fields/evaluation/BASELINES.md)三条基线中"模型裁判与成对人评"一条：它定义了没有标准答案时由裁判判分的接口，也给出检验裁判的办法（与人类比一致率、交换顺序测位置偏差）。[评估方向](../../fields/evaluation/README.md)"捷径与裁判偏差"一节的位置、冗长偏差数字取自本篇；[偏好学习方向](../../../llm/fields/posttraining/preferences/README.md)把它与生成式奖励模型看作同一类模型放在两个位置。引用时注意"超过八成一致"是去掉平局后的子集。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：三种判分形式与一致率公式、三种偏差怎样测出来、"超过八成"到底是哪八成
- [图解与说明](figures/README.md)
- [证据档案](evidence.json)与[原文版本与阅读记录](source.json)

## 阅读顺序

[Training language models to follow instructions with human feedback](../../../llm/papers/instructgpt/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2306.05685 · [全文 PDF](https://arxiv.org/pdf/2306.05685v4) · UC Berkeley、UC San Diego、Carnegie Mellon University、Stanford、MBZUAI · NeurIPS 2023 Datasets and Benchmarks Track
- 方向：cross-domain/evaluation、cross-domain/model-science、llm/posttraining/preferences
