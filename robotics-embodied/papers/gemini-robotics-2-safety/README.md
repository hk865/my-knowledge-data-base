# Gemini Robotics 2: Safety Evaluations

> 状态：文献卡 · 2026 · [原文](https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-2-Safety.pdf)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：由 Agent 控制、在人旁边工作的机器人，除了急停、限速限力这类物理防护，还要会拒绝违反约束的任务、在人靠近或硬件故障时触发保护、不把 VLA 没学过的任务交给它、指令含糊时向人求助；已有的语义安全评测不测这些"编排决策"。
- **核心方法**：报告把系统写成"system 2 / system 1"：ER 2 当 Agent，把长任务拆成子任务、以工具调用的方式调用 VLA，另有一个安全工具让机器人回到安全姿态并停下。发布 ASIMOV-Agentic 基准（离线单步与多轮；多轮时 VLA 由一个基于 Gemini 的置信度模拟器代替），评测 ER 2 与其他前沿模型（文中点名 Claude Opus 4.8、GPT 5.5）。结果：纯文本的安全约束判断各模型都在 96.0% 以上，落到指点、框选、工具调用时模型间差距变大；人员接近监测上，误报率压到 5% 以下的模型漏报率超过 40%，漏报压到 10%–15% 的模型有 15%–25% 的时间无谓停机，没有模型同时把两者压到接近零；告诉 ER 2 的 VLA 训练指令摘要越详细，它判断"该任务 VLA 做不做得到"的准确率从 62.0% 升到 95.8%；多轮变体中，Agent 会按要求先查置信度，但常在收到反馈后重规划失败。Apollo 2 人形的实验室测试中，人员检测 99%（ER）、转入安全姿态 96%（VLA）。
- **为什么在这个库里**：[具身 Agent 方向](../../fields/embodied-agents/README.md)"高层调用技能"接口的 2026 年公司版本：编排器不只拆任务，还要判断"该不该交给 VLA"，这是 [SayCan](../saycan/reading.md) 可行性打分在工具调用形式下的对应。报告写明不评估认证硬件、冗余与实时保证，并建议把前沿模型与确定性的低层安全护栏一起使用。优先级：选读。

## 身份信息

- 稳定标识：url:https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-2-Safety.pdf（Google DeepMind Gemini Robotics Team 官方技术报告，2026-07-29，18 页）
- 基准数据：[google/asimov_agentic](https://huggingface.co/datasets/google/asimov_agentic) · 模型发布博客见 [Gemini Robotics 2](../gemini-robotics-2/README.md)
- 方向：[具身 Agent](../../fields/embodied-agents/README.md)（另见[VLA](../../fields/vla/README.md)）
