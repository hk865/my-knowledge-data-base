# Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2308.12966)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源视觉语言模型训练与优化不足、远落后闭源模型，而且多只做粗粒度感知，缺少物体定位、读字等细粒度能力。
- **核心方法**：1.9B 的 ViT（OpenCLIP ViT-bigG 初始化）+ 单层交叉注意力适配器（256 个可学查询，加二维绝对位置编码）+ 7.7B 的 Qwen-7B。三段训练：先冻结 LLM、在 224 分辨率上训 ViT 与适配器（50 亿对图文清洗到 14 亿，英文 77.3%、中文 22.7%）；再升到 448、解冻全部参数，做描述、VQA、定位、指代、OCR 等 7 类多任务；最后冻结 ViT 做 35 万条 SFT 得到 Qwen-VL-Chat。物体框坐标归一化到 [0, 1000) 后直接写成文字。VQAv2 79.5%。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 4 个节点、Qwen 系列的起点："先训视觉侧、再全量解冻、SFT 冻 ViT"的三段日程与"坐标写成文字"在之后三代中反复出现。下一代 [Qwen2-VL](../arxiv-2409.12191/README.md) 把查询适配器换成 MLP、固定分辨率换成原生分辨率。论文只写未来方向，未单列局限。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2308.12966（Jinze Bai 等 9 位作者；当前 v3，2023-10）· [全文 PDF](https://arxiv.org/pdf/2308.12966v3) · 阿里巴巴 Qwen 团队
- 旧题名：Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities（arXiv 早期版本，LLaVA-1.5 的参考文献按旧题名引用）
- 方向：[视觉语言模型](../../fields/vlm/README.md)
