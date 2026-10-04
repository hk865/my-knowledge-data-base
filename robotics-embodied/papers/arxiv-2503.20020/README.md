# Gemini Robotics: Bringing AI into the Physical World

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.20020)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：让前沿多模态大模型 Gemini 2.0 具备机器人需要的具身推理（embodied reasoning，一句话：物体检测、指向、轨迹、抓取位姿、多视角对应、3D 框这类视觉-空间理解），并能直接输出机器人动作（§1）。
- **核心方法**：Google DeepMind 的官方技术报告，两件东西：Gemini Robotics-ER 是在 Gemini 2.0 Flash 上加强具身推理的 VLM，可通过代码生成或上下文示例控制机器人；Gemini Robotics 是 VLA，骨干由 Robotics-ER 蒸馏而来、运行在云端，查询延迟优化到 160 ms 以下，机载的本地动作解码器补偿骨干延迟，端到端约 250 ms，一次输出多步动作，有效控制频率 50 Hz（§3.1）。数据是 ALOHA 2 机群 12 个月采集的数千小时示教，加网页、代码、多模态与具身推理数据。相对 [RT-2](../arxiv-2307.15818/README.md)，延续"从自家最大的 VLM 出发、骨干放在云端"，新增的是云端骨干与本地解码器的两级调度。报告没有给出参数量、动作表示和训练目标。
- **为什么在这个库里**：[VLA Baseline 表](../../fields/vla/BASELINES.md)中"推理调度 = 云端大骨干 + 本地动作解码器"一格；闭源公司 VLA 的代表，用来对照 Physical Intelligence 与开源路线。报告自己复现的 π0 难以理解描述性的属性词、在没见过的物体上失败（§3.3）；自述局限是数值预测（点、框）对精细控制不够准，需要多步推理与灵巧动作同时进行的场景仍待改进（§6）。优先级：选读。
