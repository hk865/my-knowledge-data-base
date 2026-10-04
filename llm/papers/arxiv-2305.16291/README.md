# Voyager: An Open-Ended Embodied Agent with Large Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2305.16291)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在 Minecraft 这样的开放世界里，让 LLM 驱动的智能体不靠人工干预持续探索、积累技能、终身学习。
- **核心方法**：相对 ReAct、Reflexion、AutoGPT 这类逐步提示的智能体，加入三个部件：自动课程（以最大化探索为目标提出下一个任务）；由可执行代码组成、不断增长的技能库（存储、检索并组合复杂行为）；迭代提示机制（把环境反馈、执行报错和自我验证的结果写回提示，改进程序）。全程以黑盒方式调用 GPT-4，不微调参数。与此前最好的方法相比，获得的独特物品多 3.3 倍，移动距离长 2.3 倍，解锁科技树关键节点最多快 15.3 倍。
- **为什么在这个库里**：[Agent 与上下文系统方向](../../../cross-domain/fields/agents/README.md)中"技能获取与复用"的代表：经验存成可检索的代码，而不是写进权重。与 [ReAct](../../../cross-domain/papers/react/README.md) 对照，可以看到长程任务里课程与技能库补上了什么。优先级：选读。

## 批注

**未核实 / 待验证**
- ML Anthology 页面把本文列为 TMLR 2024；TMLR 的 OpenReview 页面与期刊版正文未核对，期刊版与 arXiv v2 的差异未知。

## 身份信息

- 稳定标识：arxiv:2305.16291 · [全文 PDF](https://arxiv.org/pdf/2305.16291) · [ML Anthology 条目](https://mlanthology.org/tmlr/2024/wang2024tmlr-voyager/) · 代码与提示词公开
- 作者：Guanzhi Wang、Yuqi Xie、Yunfan Jiang、Ajay Mandlekar、Chaowei Xiao、Yuke Zhu、Linxi Fan、Anima Anandkumar（NVIDIA、Caltech、UT Austin、Stanford、UW Madison）
- 方向：cross-domain/agents、llm/inference
