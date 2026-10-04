# InternVideo2: Scaling Foundation Models for Multimodal Video Understanding

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2403.15377)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：遮蔽重建、视频-语言对齐、视频上的下一 token 预测三种学习方式各有长处，如何在一个视频编码器里依次统一并扩大规模，让它既能做动作识别也能接大模型对话。
- **核心方法**：6B 参数的 ViT 视频编码器（输入稀疏采样 8 帧）分三阶段训练：先在 80% 遮蔽下，让未遮的 token 对齐两个教师（图文模型 InternViT-6B、视频模型 VideoMAEv2-g）的输出；再与音频、语音、文本做对比学习，视频按语义边界切成片段，字幕由画面、音频、语音三路描述融合而成（数据共 4.02 亿条）；最后经 Q-Former 接语言模型做指令微调。K400 微调 92.1%；接入 VideoChat2 后 EgoSchema 60.0%，低于 Gemini 1.5 Pro 的 72.2%。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 7 步"视频基础编码器"一支、[Baseline 表](../../fields/video-temporal/BASELINES.md)"预训练信号 = 多阶段"一格。作者自述没有新结构，靠扩展已有技术与数据处理；固定分辨率、固定采样率与高度压缩的 token 限制了细节表达。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2403.15377 · [全文 PDF](https://arxiv.org/pdf/2403.15377) · 上海人工智能实验室 OpenGVLab、南京大学、中科院深圳先进技术研究院
- 方向：multimodal/video-temporal、multimodal/alignment
- ECCV 2024（arXiv 注释）
