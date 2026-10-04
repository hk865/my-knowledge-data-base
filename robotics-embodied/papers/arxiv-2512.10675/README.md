# Evaluating Gemini Robotics Policies in a Veo World Simulator

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.10675)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：在常规、分布外与安全关键场景中评估通用机器人策略需要大量硬件测试，物理仿真器又有资产与视觉差距。
- **核心方法**：把 Veo 2 在机器人数据上微调成多视角、动作条件的模拟器，用图像编辑生成背景、干扰物、新物体等分布外场景，评估 Gemini Robotics 策略。对照 1600 多次真机试验，常规场景预测与真实成功率 Pearson 0.92、分布外 0.86；只能生成约 8 秒，小物体接触难以模拟，仍依赖人工打分。
- **为什么在这个库里**：[世界模型](../../fields/world-models/README.md)用法 (d)"评估策略"的代表，主线第 5 步。优先级：必读。
