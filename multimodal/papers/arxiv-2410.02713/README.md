# LLaVA-Video: Video Instruction Tuning With Synthetic Data

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2410.02713)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：高质量的视频指令数据难得：已有数据集的视频大多相对静止、按镜头切换切碎，标注时采样极稀（ShareGPT4Video 平均每秒 0.15 帧，30 秒视频有时只看 2 帧），描述不了细节动作，模型因此产生幻觉。
- **核心方法**：从 10 个主要视频来源中挑动态、未裁剪的视频，按每秒 1 帧稠密采样，用 GPT-4o 分三级（从 10 秒到整段视频）递归写详细描述，再按 16 类问题生成问答，得到 LLaVA-Video-178K（178,510 段 0–3 分钟视频、130 万条指令）；模型沿用 LLaVA-OneVision（SigLIP 编码器 + Qwen2 语言模型），提出 LLaVA-Video SlowFast：每隔几帧保留较多 token（慢帧），其余帧池化得更狠（快帧），以塞进更多帧。在 0–30 秒视频上的消融中，"110 帧 × 每帧 169 token"在总 token 更少时仍好于"32 帧 × 每帧 729 token"，但"440 帧 × 64 token"开始下降。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 7 步、[Baseline 表](../../fields/video-temporal/BASELINES.md)"帧数与每帧 token 预算"和"指令数据"两格。它给出此前"超过 16 帧就不再涨"的解释：MSVD、WebVid 这类训练数据太静态，几帧就能代表整段。与 [LLaVA](../llava/README.md) 一样靠 GPT 合成指令数据。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2410.02713 · [全文 PDF](https://arxiv.org/pdf/2410.02713) · ByteDance、南洋理工大学 S-Lab、北京邮电大学
- 方向：multimodal/video-temporal、multimodal/vlm
- arXiv v1 题名为 Video Instruction Tuning With Synthetic Data；TMLR 2025
