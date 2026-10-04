# InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.02456)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：建在多模态大模型上的 VLA 擅长语义理解，却推断不了物理世界的动态；以视频预测为核心的世界模型路线反过来缺语义落地，并且对视频预测误差敏感。
- **核心方法**：用混合 Transformer（Mixture-of-Transformers，一句话：几组"专家"各有参数，通过统一的掩码自注意力交换信息）把场景理解、视觉预见生成（预测未来画面）和动作执行三个专家放进一个模型，以 InternVL3、Qwen3-VL 为底座做 2B、3B 两档，在真实机器人、合成仿真和人类视频（超过 6.92 亿帧）上预训练。摘要报告相对 [π0.5](../arxiv-2504.16054/README.md)：静态操作 +4.4%，RoboTwin 2.0（一句话：双臂操作仿真基准） +2.6%，动态操作 +26.7%。
- **为什么在这个库里**：[视觉语言动作模型](../../fields/vla/README.md)与[世界模型与行动预测](../../fields/world-models/README.md)的交界：把"预测未来画面"做成 VLA 内部的一个专家，而不是外接的视频模型。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2601.02456（42 位作者；当前 v2，2026-02）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2601.02456)
- 方向：[视觉语言动作模型](../../fields/vla/README.md)（另见[世界模型与行动预测](../../fields/world-models/README.md)）
