# Inner Monologue: Embodied Reasoning through Planning with Language Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2207.05608)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LLM 规划多为开环，默认每一步都执行成功，在会出错的真实环境中很脆弱。
- **核心方法**：在 [SayCan](../saycan/reading.md) 式规划上加闭环：把技能成功检测、场景中的物体描述、向人提问的回答写成文字放回 LLM 提示，让它据此重规划。真实厨房加扰动时成功率从 30.8% 升到 60.4%；成功检测器的误报会以事实身份进入提示。
- **为什么在这个库里**：[具身 Agent](../../fields/embodied-agents/README.md)主线第 2 步与 Baseline 页"反馈"一行。优先级：必读。
