# Addendum to GPT-4o System Card: Native image generation

> 状态：文献卡 · 2025 · [原文](https://openai.com/index/gpt-4o-image-generation-system-card-addendum/)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：说明 4o 图像生成相对 DALL·E 系列新增了哪些能力、带来哪些新风险，以及怎样缓解。
- **核心方法**：系统卡写明：DALL·E 是扩散模型，而 4o 图像生成是"原生嵌入 ChatGPT 的自回归模型"，嵌在全模态 GPT-4o 的架构深处，能调用模型已有的全部知识；能以一张或多张图为输入做变换（编辑），出照片级写实图，遵循详细指令并可靠地写字、画说明图。结构、参数与训练数据没有公开。安全栈分对话模型拒绝、提示拦截、输出拦截（带安全推理监控）三层；偏见评测的各项指标都优于 DALL·E 3；所有输出带 C2PA 来源元数据。后续的 [ChatGPT Images 2.0 系统卡](https://deploymentsafety.openai.com/chatgpt-images-2-0)（2026-04-21）加入"思考模式"：生成前先推理、可联网搜索、一次出多张图，同样没有写结构。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 10 个节点"语言模型本身成为生成器"的闭源证据，也是 Qwen-Image、Seedream 3.0/4.0 报告的主要比较对象（GPT Image 1）。它只写能力与风险，读时要和公开结构的 [HunyuanImage 3.0](../arxiv-2509.23951/README.md) 对照。优先级：选读。

## 身份信息

- 稳定标识：url:https://openai.com/index/gpt-4o-image-generation-system-card-addendum/ · OpenAI · 官方系统卡（GPT-4o 系统卡的附录），2025-03-25
- 方向：multimodal/generation、multimodal/vlm
