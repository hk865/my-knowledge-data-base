# Gemini Robotics 2 brings whole body intelligence to robots

> 状态：文献卡 · 2026 · [原文](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：前两代 Gemini Robotics 主要做上半身的桌面操作；人形机器人要边走、边蹲、边用五指手操作，需要一个模型从脚到指尖协调全身，还要在多台机器人之间分工。
- **核心方法**：Google DeepMind 2026-07-30 的官方博客同时发布三个模型：Gemini Robotics 2 是 VLA（视觉语言动作模型，一句话：从图像和语言指令直接输出机器人动作），覆盖人形全身与双臂；Gemini Robotics ER 2 是做高层规划、任务进度判断与多机协作的具身推理模型；Gemini Robotics On-Device 2 在机器人本地运行，原生支持多本体，沿用 [Gemini Robotics 1.5](../arxiv-2510.03342/README.md) 的 motion transfer，适配新的双臂本体通常只要几小时、少于 200 条示范。博客图中只有 Gemini Robotics 2 自己的成功率，没有与前代或其他模型的对照：Apptronik Apollo 2 人形（Inspire 手）从桌面、地面、货架拾取分别 68.4%、45.7%、76.3%；SharpaWave 手拧下灯泡 92%、拧上灯泡 36%、系垃圾袋 44%、用簸箕 32%；Franka 双臂精密插入 89.6%。页面没有公开参数量、动作表示、训练目标，也没有说明行走由 VLA 直接输出还是由下层控制器生成。
- **为什么在这个库里**：[VLA 方向](../../fields/vla/README.md)第 7 阶段"全身、记忆与人类视频"的官方材料，Google DeepMind 一线从 [Gemini Robotics](../arxiv-2503.20020/README.md)、1.5 到这里的最新版本；同时发布的安全评测见 [Gemini Robotics 2: Safety Evaluations](../gemini-robotics-2-safety/README.md)。地面拾取、拧上灯泡、系袋这几项的数字说明全身灵巧操作远未饱和。优先级：选读。

## 身份信息

- 稳定标识：url:https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/（Google DeepMind 官方博客，Carolina Parada，2026-07-30）
- 相关官方页面：[Gemini Robotics 模型页](https://deepmind.google/models/gemini-robotics/) · [安全评测报告 PDF](https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-2-Safety.pdf)
- 方向：[视觉-语言-动作模型](../../fields/vla/README.md)（另见[具身 Agent](../../fields/embodied-agents/README.md)、[运动控制](../../fields/control-locomotion/README.md)）
