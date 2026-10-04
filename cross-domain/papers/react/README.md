# ReAct: Synergizing Reasoning and Acting in Language Models

> 状态：技术精读 · 2022 · [原文](https://arxiv.org/abs/2210.03629)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：2022 年前后，思维链只靠模型参数里的知识推理，事实错了无从纠正，错误还会沿推理链传播；让语言模型直接输出动作的工作有外部反馈，却没有显式推理去制定、跟踪和修改计划。ReAct 问：让模型在同一条轨迹里交替推理和行动，二者能否互相帮助。
- **核心方法**：把动作空间扩成"环境动作 ∪ 语言"：输出语言就是一条 thought，只追加进上下文；输出环境动作就由执行器调用工具，把返回的观察写回上下文（§2）。前作 Inner Monologue 已把环境反馈注入上下文形成闭环，ReAct 在此之上允许模型自由地写推理。不改模型、不训练，主实验用 PaLM-540B 少样本提示。HotpotQA 上 ReAct 的 EM 为 27.4，低于 CoT 的 29.4、高于只行动的 25.7；FEVER 上 60.9，高于 CoT 的 56.3；与 CoT-SC 互相回退的组合方法分别达到 35.1 和 64.6（Table 1）。ALFWorld 上六套提示中最好的一套 71%、平均 57%，模仿学习基线 BUTLER 最好 37%（Table 3）；WebShop 成功率 40.0%，人类专家 59.6%（Table 4）。
- **为什么在这个库里**：[Agent 方向 Baseline 页](../../fields/agents/BASELINES.md)推理时基线"ReAct 循环 + SWE-agent 接口"的前半：思考—动作—观察交替、观察写回上下文，之后的编码 agent 都沿用这种循环；也是 [Agent 方向](../../fields/agents/README.md)阅读顺序的第一篇。[推理方向](../../../llm/fields/inference/BASELINES.md)把它列为推理时计算扩展到多步工具调用的代表，[具身 Agent 方向](../../../robotics-embodied/fields/embodied-agents/BASELINES.md)把它作为反馈部件在文本环境里的对照。论文的环境都只读、没有副作用（维基百科接口、模拟购物网站），所以越权问题在这里还看不见。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：动作空间怎样扩成"环境动作 ∪ 语言"、一条轨迹怎样生长、ReAct 与 CoT-SC 的回退规则，以及哪个实验支撑哪个主张
- [图解与说明](figures/README.md)
- [证据档案](evidence.json)与[原文版本与阅读记录](source.json)

## 阅读顺序

[Language Models are Few-Shot Learners](../../../llm/papers/gpt3/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2210.03629 · [全文 PDF](https://arxiv.org/pdf/2210.03629v3) · Princeton University、Google Research（Brain team） · ICLR 2023
- 方向：llm/inference、cross-domain/agents
