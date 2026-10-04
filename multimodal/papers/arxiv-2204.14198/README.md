# Flamingo: a Visual Language Model for Few-Shot Learning

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2204.14198)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视觉任务的主流做法是预训练后每个任务用上千条标注微调；CLIP 式对比模型只会打相似度分，不能生成开放回答。能否像 GPT-3 那样只给几个示例就适应新的图像、视频任务？
- **核心方法**：冻结 70B 的 Chinchilla 语言模型与对比预训练的 NFNet 视觉编码器，只训练两类新模块：Perceiver Resampler（一组可学查询，把任意大小的特征图压成 64 个视觉 token）和插在 LLM 层间的门控交叉注意力（tanh(α)、α 初始化为 0，开训时模型等于原 LLM）。在约 4300 万网页抽出的图文交错数据 M3W 和图文、视频文本对上训练。32 个示例的少样本提示在 16 个任务中的 6 个超过逐任务微调的最好结果。消融（Flamingo-3B、4-shot）：去掉 M3W 总分降 17% 以上，微调 LLM 降 8.0%，去掉零初始化门控降 4.2% 且训练不稳。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 1 个节点、[Baseline 页](../../fields/vlm/BASELINES.md)的对照基线（门控交叉注意力一格）。它自述分类不如对比模型、继承 LLM 幻觉、代码与数据专有；输入只有 320 像素，微调时要解冻视觉编码器并升到 480 才拿到最好成绩，这为后来"解冻视觉塔、提高分辨率"埋下伏笔。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2204.14198（Jean-Baptiste Alayrac 等 27 位作者；当前 v2，2022-11）· [全文 PDF](https://arxiv.org/pdf/2204.14198v2) · DeepMind · NeurIPS 2022
- 方向：[视觉语言模型](../../fields/vlm/README.md)
