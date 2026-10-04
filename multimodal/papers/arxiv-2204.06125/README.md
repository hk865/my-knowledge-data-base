# Hierarchical Text-Conditional Image Generation with CLIP Latents

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2204.06125)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CLIP 的图像表示同时抓住语义与风格。能否用它做文本到图像生成，并换来比直接以文字为条件更高的多样性？
- **核心方法**：两段（unCLIP）：先验根据文字生成 CLIP 图像嵌入（试了自回归与扩散两种，扩散先验是带因果 mask 的 decoder-only Transformer）；解码器是改自 GLIDE 的扩散模型，以 CLIP 图像嵌入为条件在 64×64 生成，再由两级扩散上采样到 256 与 1024；训练时以 10% 概率丢弃嵌入、50% 丢弃文字，以便用无分类器引导。MS-COCO 零样本 FID 10.39；与 GLIDE 的人评中写实度相近、多样性明显更好、描述匹配略差。作者自述：属性绑定比 GLIDE 差，要求两个方块各配一种颜色时会弄混（假设原因是 CLIP 嵌入本身不显式绑定属性与物体）；写不出连贯的文字（CLIP 嵌入可能不编码拼写，BPE 分词又遮住了单词的拼写）；复杂场景缺细节，归因于从 64×64 起步的级联。论文未声明代码或权重发布。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 7 个节点，[Baseline 页](../../fields/generation/BASELINES.md)部件 6"以 CLIP 图像嵌入为中间表示"一格。它自述的三条失败（绑定、写字、细节）正是 [Imagen](../arxiv-2205.11487/README.md) 换 T5、[SD3](../arxiv-2403.03206/README.md) 换 MM-DiT 加 T5 的出发点；[DALL·E](../arxiv-2102.12092/README.md) 的第一作者一年后改用扩散解码器。条件来自 [CLIP](../clip/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2204.06125 · [全文 PDF](https://arxiv.org/pdf/2204.06125) · OpenAI
- 名称：通称 DALL·E 2 或 unCLIP
- 方向：multimodal/generation
