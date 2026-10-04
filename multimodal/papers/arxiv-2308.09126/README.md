# EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2308.09126)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：只看片段长度衡量不了一个视频任务到底要看多长；当时没有真正需要长时理解的视频问答 benchmark。
- **核心方法**：提出时间证书长度（让人确信标注答案正确所需观看的最少子片段总长）；从 Ego4D 第一人称视频及其人工旁白出发，用 LLM 生成五选一题，用"只读题目、不看视频旁白的 LLM"过滤可盲答的题，再两轮人工筛选，得到 5000 多道题，每题对应 3 分钟片段。证书长度中位数约 100 秒，是第二长数据集的 5.7 倍；发布时最好的模型不到 33%（随机 20%），人类约 76%。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 6 步，长视频评测的起点；"时间证书"被 [Video-MME](../arxiv-2405.21075/README.md) 沿用。表中 mPLUG-Owl 用 1 帧 27.0%、5 帧 31.1%、30 帧 20.0%，帧数越多反而可能越差。2025 年 Qwen2.5-VL-72B 报告 test 集 76.2%，已与原文的人类成绩持平。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2308.09126 · [全文 PDF](https://arxiv.org/pdf/2308.09126) · UC Berkeley
- 方向：multimodal/video-temporal
