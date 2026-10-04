# Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2502.19645)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VLA 换到新机器人通常要微调，但怎样微调最有效（动作解码方式、动作表示、训练目标）没有定论；OpenVLA 逐 token 自回归解码慢，也不支持高频动作块。
- **核心方法**：以 [OpenVLA](../openvla/README.md) 为底座系统比较微调设计，得到 OFT 配方：并行解码（一次前向输出全部动作，而不是逐 token 生成）+ 动作块 + 连续动作表示 + L1 回归损失；真机双臂 ALOHA 任务再加 FiLM 加强语言条件（OFT+）。在 LIBERO 仿真基准的四个任务套件上，平均成功率从微调 OpenVLA 的 76.5% 提高到 97.1%（同基准上 π0 为 94.2%），用 8 步动作块时动作生成吞吐提高 26 倍；在 ALOHA 上比按默认配方微调的 π0、RDT-1B 以及从零训练的 Diffusion Policy、ACT 平均成功率最多高 15 个百分点。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)方向「动作表示」一格的关键对照：同一个 OpenVLA 底座，只换解码方式与损失，就回答了离散 token 与连续回归在微调阶段的差别。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2502.19645
- 作者：Moo Jin Kim、Chelsea Finn、Percy Liang
- 全文：[arXiv PDF](https://arxiv.org/pdf/2502.19645)
- 发表：RSS 2025（arXiv 注释）
- 方向：[视觉语言动作模型](../../fields/vla/README.md)、[模仿学习与机器人强化学习](../../fields/imitation-reinforcement-learning/README.md)
