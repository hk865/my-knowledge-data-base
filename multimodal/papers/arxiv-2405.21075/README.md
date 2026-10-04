# Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.21075)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多模态大模型的能力与评测集中在静态图像；已有视频 benchmark 视频类型单一、时长覆盖不足、只看画面。
- **核心方法**：人工从 YouTube 收集 900 段视频（6 个领域 30 个子类，11 秒到 1 小时，分短 <2 分钟、中 4–15 分钟、长 30–60 分钟三档），标注 2700 道四选一题，可另附字幕与音频；用 Gemini 1.5 Pro 只读题目过滤能盲答的题（纯文本准确率低于 15%），并沿用 EgoSchema 的时间证书估计难度（短中长的中位数 26、164.7、890.7 秒）。所有模型都随视频变长而下降，Gemini 1.5 Pro 从短视频 81.7% 降到长视频 67.4%。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 7 步与"用什么衡量进展"的主要长视频 benchmark，LLaVA-Video、Qwen2.5-VL 都报告它。它也显示早期视频大模型的短板：直接输入多帧的图像模型（InternVL-Chat-V1.5 50.7%）超过 [Video-LLaVA](../arxiv-2311.10122/README.md)（39.9%），计数是所有模型的共同瓶颈，字幕对长视频帮助最大。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2405.21075 · [全文 PDF](https://arxiv.org/pdf/2405.21075) · 南京大学、认知智能国家重点实验室、厦门大学、香港大学、北京大学、香港中文大学、华东师范大学、中科院自动化所
- 方向：multimodal/video-temporal、multimodal/vlm
- arXiv v1 2024 年 5 月；本卡按 2025 年 5 月的 v3
