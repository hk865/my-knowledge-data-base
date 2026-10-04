# Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.04720)

- **解决什么**：短句与图片的双塔匹配难以覆盖文档、视频及混合模态查询，还要兼顾大库召回效率与细粒度相关性。
- **核心方法**：用 Qwen3-VL 独立编码查询与候选以召回，再将二者联合编码做重排；训练从对比学习推进到排序器蒸馏。
- **为什么在这个库里**：补上 [图文对齐基线](../../fields/alignment/BASELINES.md)中"VLM 反过来成为检索编码器"的路径；与 CLIP 的相似度接口相接，但训练与评测协议不同。优先级：选读。
