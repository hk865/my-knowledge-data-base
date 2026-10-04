# UnifoLM-WLA-1.0（Unitree 官方仓库）

> 状态：文献卡 · 2026 · [原文](https://github.com/unitreerobotics/unifolm-wla)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：Unitree 此前开源的是运动控制的训练框架（unitree_rl_gym、unitree_rl_lab）和较早的 UnifoLM-VLA-0、世界模型-动作框架 UnifoLM-WMA-0；这一版要用一个通用人形基础模型覆盖桌面操作和全身操作、二指夹爪和多种五指手。
- **核心方法**：官方 README 写明它是 6B 参数的通用人形机器人基础模型，建立在大规模多模态感知与理解数据和"以交互为中心的世界建模"之上，用约 2,500 小时高质量真机数据训练，一个模型协调 64 个桌面与全身操作任务。开放节奏：2026-09-11 开放 UnifoLM-ER-1 与 UnifoLM-ER-Flow 权重，09-20 开放模型模块与动作专家训练代码，09-28 开放 UnifoLM-WLA-1.0-Base 与微调代码；开源计划列出 UniBot-V1、UnifoLM-WBT、UnifoLM-Dex1 三个数据集；Apache 2.0。README 称在多个具身推理 benchmark 上领先，但没有给出具体数字，也没有技术报告。
- **为什么在这个库里**：[VLA 方向](../../fields/vla/README.md)"团队偏好"中 Unitree 一行的官方材料：开放权重、训练代码和数据，延续它在[运动控制方向](../../fields/control-locomotion/README.md#工业界方案成熟在哪里没公开什么)开源整条训练-部署流水线的做法。等技术报告出来再核对结构与数字。优先级：存档。

## 身份信息

- 稳定标识：url:https://github.com/unitreerobotics/unifolm-wla（Unitree Robotics 官方仓库，基础模型 2026-09-28 发布）
- 相关仓库：[unifolm-vla](https://github.com/unitreerobotics/unifolm-vla) · [unifolm-world-model-action](https://github.com/unitreerobotics/unifolm-world-model-action)
- 方向：[视觉-语言-动作模型](../../fields/vla/README.md)
