# Gemini 3.1 Flash Image Model Card

> 状态：文献卡 · 2026 · [原文](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-1-Flash-Image-Model-Card.pdf)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Google 对 Nano Banana 2（[官方博客](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/)于 2026-02-26 发布）的官方说明：能力、评测与已知局限。
- **核心方法**：模型卡只写"基于 Gemini 3 Flash"，结构与训练数据都指向 Gemini 3 Flash 的模型卡；输入可含文本与图像（上下文 100 万 token），输出图像与文本。评测是人评 Elo：GenAI-Bench 总体偏好 1073（开思考与图文检索时 1079），同表 Nano Banana Pro 1021、GPT-Image 1.5 1047、Seedream 5.0 Lite 928。自述局限：小字模糊（1K 版）、长段落与整页文字、输入图与输出之间的角色一致性、涂鸦或遮罩编辑只部分遵循、编辑时偶尔把输入图原样贴过来、偶尔混淆左右这类空间位置、世界知识、三维推理与事实性仍有限。前一代 [Gemini 3 Pro Image 模型卡](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Image-Model-Card.pdf)（Nano Banana Pro，2025 年 11 月，"基于 Gemini 3 Pro"）列出同一组局限。
- **为什么在这个库里**：2026 年闭源图像模型自述局限的最新清单，用来对照[入门页](../../fields/generation/README.md)主线：Parti（2022）列出的左右关系错误、DALL·E 2 写不好字，到 2026 年仍在已知局限里，只是从"基本做不到"变成"偶尔出错、小字和长文出错"。优先级：选读。

## 身份信息

- 稳定标识：url:https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-1-Flash-Image-Model-Card.pdf · Google DeepMind · 官方模型卡，2026 年 2 月
- 方向：multimodal/generation、multimodal/vlm
