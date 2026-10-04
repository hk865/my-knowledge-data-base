# Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2506.07454)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让一组机器人在大范围室外环境里执行用自然语言下达的复杂任务，需要共享地图、实时重定位，以及能落到具体物体上的任务规划。
- **核心方法**：每个机器人用 Hydra 实时构建三维场景图（把物体、地点、区域组织成分层图的地图表示），用 ROMAN 建开放词表的物体地图并提供回环，经 Hydra-Multi 融合成多机器人共享的场景图；物体地图支撑与视角无关的实时重定位，场景图定义规划域。大语言模型结合场景图上下文与各机器人的能力，把操作员的指令翻译成 PDDL（一种符号任务规划语言）目标并在翻译中完成多机分工，再由分层场景图规划器求解。语言落地测试中最好的 GPT-4.1 在 70 条指令中正确 54 条（Table 4）。
- **为什么在这个库里**：它不是学习型世界模型，而是显式、符号化的世界表示；[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)批注把它作为对照，它与[具身 Agent](../../../robotics-embodied/fields/embodied-agents/README.md)的高层规划和[定位与建图](../../../robotics-embodied/fields/localization-mapping/README.md)更接近。做不好的场景：机器人只能在事先融合好的地图内工作，处理不了探索和环境变化；语言落地还没利用开放词表地图支持更开放的任务（Sec.7）；实验中"checkout two nearby boxes"被落地成"移动到箱子"而不是"检查箱子"（Sec.5）。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2506.07454 · [全文 PDF](https://arxiv.org/pdf/2506.07454) · 麻省理工学院、美国陆军作战能力发展司令部陆军研究实验室
- 方向：multimodal/world-models、robotics/embodied-agents、robotics/localization-mapping
