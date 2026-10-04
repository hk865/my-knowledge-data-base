# BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2201.12086)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有的视觉–语言预训练模型要么擅长理解、要么擅长生成；性能提升主要靠扩大网页噪声图文数据，而噪声网页文字是次优的监督来源。
- **核心方法**：模型上，一个编码–解码混合结构共享参数，同时训练图文对比（ITC）、图文匹配（ITM）和看图写描述（LM）三个目标；数据上，CapFilt 先用描述器给网页图片写新句子，再用匹配过滤器去掉原 alt-text 与合成句中不匹配的部分。1400 万张图上两步都用时，COCO 检索微调后图到文 R@1 从 78.4 升到 80.6；随机采样写的描述更多样，效果好于集束搜索。
- **为什么在这个库里**：[图文对齐方向](../../fields/alignment/README.md) Baseline 表"训练目标：三目标共享参数"与"数据：CapFilt"两格，是"用模型自己写描述来清洗数据"的早期代表；[ARO](../arxiv-2210.01936/README.md) 发现它在词序题上接近随机。后续 BLIP-2 属于 [VLM 方向](../../fields/vlm/README.md)。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2201.12086 · [全文 PDF](https://arxiv.org/pdf/2201.12086) · Salesforce Research
- 方向：multimodal/alignment、multimodal/vlm
