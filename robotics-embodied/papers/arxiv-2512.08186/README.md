# Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.08186)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：端到端 VLA 式 VLN 把视觉语言输入直接映射成短时离散动作，动作碎、延迟高，难以应对动态障碍。
- **核心方法**：异步双系统（DualVLN，模型名 InternVLA-N1）：System 2 是 7B 的 Qwen-VL-2.5，约 2 Hz 预测图像上的最远像素目标；System 1 是轻量扩散 Transformer，约 30 Hz 根据像素目标与潜变量生成 32 个航点的轨迹。R2R-CE 未见环境成功率 64.3%；自建的 Social-VLN 中撞人率仍有 35.4%。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 6 步：学习式导航回到"全局定目标、局部出轨迹"分层的代表。优先级：必读。
