# InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2312.14238)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LLM 已扩到上千亿参数，视觉编码器仍在 1B 左右；视觉模型与 LLM 的表示不一致；"胶水层"（Q-Former 或线性投影）轻且随机初始化，可能捕捉不到丰富的跨模态交互。
- **核心方法**：把视觉编码器扩到 6B（InternViT-6B），配一个用多语言 LLaMA 初始化的 8B "语言中间件"（QLLaMA）充当大号胶水层；渐进对齐：先在大规模噪声图文对上做对比学习，再在细粒度数据上做生成式学习。既可单独当视觉编码器，也可接 LLM 做对话。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 4 个节点、InternVL 系列"大视觉编码器"押注的起点。[判断] 它的大号中间件在 [InternVL 1.5](../arxiv-2404.16821/README.md) 被换成 MLP，InternViT-6B 的对比预训练据 [InternVL 2.5](../arxiv-2412.05271/README.md) 自述"当时收益有限"，后改用下一词预测损失继续训练。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2312.14238（Zhe Chen 等 15 位作者；当前 v3，2024-01）· [全文 PDF](https://arxiv.org/pdf/2312.14238v3) · 上海人工智能实验室 OpenGVLab、南京大学、香港大学、香港中文大学、清华大学、中国科学技术大学、商汤
- 方向：[视觉语言模型](../../fields/vlm/README.md)
