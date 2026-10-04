# Zero-Shot Text-to-Image Generation

> 状态：文献卡 · 2021 · [原文](https://arxiv.org/abs/2102.12092)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：文本到图像此前主要在 MS-COCO、CUB 这类小数据集上改模型假设（复杂结构、辅助损失、部件标注），样本仍常有物体变形、摆放不合逻辑。作者问：瓶颈是不是数据与模型规模？
- **核心方法**：dVAE 把 256×256 的图压成 32×32 = 1024 个 token（码本 8192），与最多 256 个 BPE 文本 token 拼成一条序列，用 120 亿参数的稀疏 Transformer 自回归建模，训练数据为 2.5 亿对网页图文；采样 512 张后用对比模型（CLIP）重排取最好的。不少篇幅花在 16 位混合精度训练的稳定性上。MS-COCO 零样本人评中，按描述匹配 93%、按真实感 90% 的多数票偏好它而非 DF-GAN，FID 与此前最好的方法相差 2 以内。作者自述：dVAE 重建会丢失或扭曲毛发纹理、店面文字和细线；在 CUB 这类专门分布上 FID 比最好的方法差近 40 点。只公开 dVAE 代码。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 4 个节点，[Baseline 页](../../fields/generation/BASELINES.md)部件 2"离散 token"与部件 3"自回归 Transformer"两格；同一第一作者一年后的 [DALL·E 2](../arxiv-2204.06125/README.md) 改用扩散解码器。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2102.12092 · [全文 PDF](https://arxiv.org/pdf/2102.12092) · OpenAI
- 名称：通称 DALL·E
- 方向：multimodal/generation
