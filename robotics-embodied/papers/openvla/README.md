# OpenVLA: An Open-Source Vision-Language-Action Model

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.09246v1)

[返回机器人与具身目录](../../README.md)

- **解决什么**：开放、可在新机器人上微调的通用操作策略。
- **核心方法**：沿用 RT-2 的离散动作 token 路线，换成 7B 开放底座 Prismatic（DINOv2 + SigLIP 视觉特征接入 Llama 2）和清洗过的 Open X-Embodiment 数据（约 97 万条轨迹），训练时连视觉编码器一起微调。
- **为什么在这个库里**：Baseline 表中"动作表示 = 离散 token"一格的开放代表，比较 π0、FAST、OpenVLA-OFT 时的参照物。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json) · [作者归属与许可](ATTRIBUTION.md)

## 阅读顺序

[CLIP](../../../multimodal/papers/clip/README.md)（图文对比学习，SigLIP 的来源路线）→ [LLaVA](../../../multimodal/papers/llava/README.md)（视觉特征投影进语言模型的接口）→ [DINO](../../../multimodal/papers/dino/README.md)（自监督视觉特征，DINOv2 的前身）→ 本篇。
