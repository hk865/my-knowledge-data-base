# Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2409.12191)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：LVLM 受固定输入尺寸限制，缩放或填充会丢细节；多数依赖冻结的 CLIP 式编码器；一维位置编码难以表示图像的二维和视频的时间结构。
- **核心方法**：原生动态分辨率：675M 的 ViT（DFN 初始化）去掉绝对位置编码、换成二维 RoPE，任意尺寸的图变成不定长 token，相邻 2×2 个 token 经 MLP 合成一个（224×224 得 66 个）；M-RoPE 把旋转位置编码拆成时间、高、宽三份，图像与视频（每秒 2 帧、3D 卷积合并相邻两帧）统一处理。三段训练：只训 ViT → 全部解冻 → 冻 ViT 做指令微调，累计 1.4T token。Qwen2-VL-7B 的消融：固定 64 / 576 / 1600 / 3136 个 token 时 InfoVQA 28.9 / 65.7 / 75.0 / 77.3，动态分辨率平均 1924 个 token 得 75.9，MMMU 四档都在 53 左右。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 5 个节点"原生分辨率"一路的代表，视频与时间编码接到[视频与时序方向](../../fields/video-temporal/README.md)。自述的失败：视觉语言导航远落后专用模型；小图放大过头使 OCRBench 严重下降。[判断] 它的 M-RoPE 频谱不均在 [Qwen3-VL](../arxiv-2511.21631/README.md) 被改成交错式；[Molmo](../arxiv-2409.17146/README.md) 的人评中它学术分强、人评偏弱。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2409.12191（Peng Wang 等 19 位作者；当前 v2，2024-10）· [全文 PDF](https://arxiv.org/pdf/2409.12191v2) · 阿里巴巴 Qwen 团队
- 方向：[视觉语言模型](../../fields/vlm/README.md)、[视频与时序](../../fields/video-temporal/README.md)
