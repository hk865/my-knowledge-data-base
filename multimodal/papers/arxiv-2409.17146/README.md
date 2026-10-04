# Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Vision-Language Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2409.17146)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：最强的开放权重 VLM 依赖闭源 VLM（如 GPT-4V）生成的合成数据，实质是在蒸馏闭源模型；社区缺少从零构建高性能 VLM 的基础知识。
- **核心方法**：PixMo 数据完全不用 VLM 生成：让标注员对着图口述 60–90 秒，得到 71.2 万张图的长描述（附录音作为没用 VLM 的凭证）；用户与纯文本 LLM 交互改写出 16.2 万条问答；230 万个点标注用于指向与计数；另有读钟表、图表等合成数据。模型用常规 ViT + MLP + LLM，但用重叠切块、长度提示的描述预训练，并跳过单独的连接器对齐阶段。消融：同等数量下 PixMo-Cap 优于 ShareGPT4V；加 LAION 连接器预训练无收益；先指向再计数优于直接报数。Molmo-72B 学术分最高、人评 Elo 仅次于 GPT-4o。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 6 个节点"开放数据"一路的代表，也提供了学术分与人评不一致的证据（Qwen2-VL 学术分强、人评偏弱）。"指向"被作者设想为机器人和网页智能体的行动接口，接到 [VLA 方向](../../../robotics-embodied/fields/vla/README.md)。自述指向数据只训 40 个以内的计数；Chatbot Arena 上仍低于 GPT-4o 与 Claude 3.5 Sonnet。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2409.17146（Matt Deitke 等 50 位作者；当前 v2，2024-12）· [全文 PDF](https://arxiv.org/pdf/2409.17146v2) · Allen Institute for AI、University of Washington
- 方向：[视觉语言模型](../../fields/vlm/README.md)
