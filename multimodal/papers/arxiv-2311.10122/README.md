# Video-LLaVA: Learning United Visual Representation by Alignment Before Projection

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2311.10122)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有视频大模型把图像和视频编码到不同的特征空间再投影进语言模型，投影之前没有对齐，语言模型难以从几层投影中学到统一的视觉理解。
- **核心方法**：用 LanguageBind（图像、视频编码器都事先对齐到语言特征空间的一组编码器）编码，图像与视频共用一个两层 MLP 投影层接入 Vicuna v1.5（7B），图像与视频混合训练；每段视频均匀采样 8 帧。混合训练使 MSVD-QA 从只用视频训练的 64.8% 升到 70.7%（GPT-3.5 按参考答案打分的开放式问答）。
- **为什么在这个库里**：[视频与时序方向](../../fields/video-temporal/README.md)主线第 7 步的早期开源视频大模型基线："每段视频固定 8 帧、逐帧编码后交给语言模型"。作者自述只有 8 帧导致长视频丢细节，并把时间戳嵌入列为未来方向；[Video-MME](../arxiv-2405.21075/README.md) 上它的总体准确率 39.9%，低于直接输入多帧的图像模型 InternVL-Chat-V1.5（50.7%）。与 [LLaVA](../llava/README.md) 同属"编码器 + 投影 + 语言模型"结构。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2311.10122 · [全文 PDF](https://arxiv.org/pdf/2311.10122) · 北京大学深圳研究生院、鹏城实验室等
- 方向：multimodal/video-temporal、multimodal/vlm
