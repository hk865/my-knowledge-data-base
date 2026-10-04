# Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2205.11487)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：此前的文本到图像模型，文本编码器只在图文配对数据上训练。只在纯文本上预训练的大语言模型，能否让生成模型更好地理解提示？
- **核心方法**：冻结的 T5-XXL 编码文本；2B 参数的 64×64 基础扩散模型加两级超分辨率扩散（600M 到 256×256、400M 到 1024×1024，后者去掉自注意力），用"动态阈值"让大引导权重下不过饱和，并提出更省内存的 Efficient U-Net。关键发现：扩大文本编码器比扩大 U-Net 更能同时提升画质与图文对齐。MS-COCO 零样本 FID-30K 7.27；新建 DrawBench，按组合、计数、空间关系、长文本、罕见词等类别出题，人评中优于 VQ-GAN+CLIP、LDM、GLIDE、DALL·E 2。作者自述：生成人物的质量明显下降（COCO 人评写实度偏好率 39.2%，去掉含人物的参考图后升到 43.6%）；存在肤色、性别、职业刻板印象；训练数据（约 4.6 亿对内部图文加约 4 亿对 LAION）含不当内容，因此不发布代码与公开演示。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 7 个节点，[Baseline 页](../../fields/generation/BASELINES.md)部件 6"冻结纯文本语言模型作编码器"与部件 9"分项考题"两格。T5 一路后来进入 [Imagen Video](../arxiv-2210.02303/README.md) 与 [SD3](../arxiv-2403.03206/README.md)，视频报告再换成 decoder-only 大模型（[HunyuanVideo](../arxiv-2412.03603/README.md)、[Seedance 1.0](../arxiv-2506.09113/README.md)）。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2205.11487 · [全文 PDF](https://arxiv.org/pdf/2205.11487) · Google Research, Brain Team
- 方向：multimodal/generation
