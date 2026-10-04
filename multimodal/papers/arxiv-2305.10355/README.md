# Evaluating Object Hallucination in Large Vision-Language Models

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2305.10355)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：接上 LLM 的视觉语言模型是否仍有物体幻觉（描述中出现图里没有的物体）？基于描述解析的 CHAIR 指标对指令写法和描述长度敏感，评测不稳定。
- **核心方法**：把物体幻觉评测改写成是非题轮询："Is there a <object> in the image?"，真实物体与不存在物体按 1:1 抽取；不存在物体按随机、热门（数据集中高频）、对抗（常与图中物体共现）三种方式采样，报准确率、精确率、召回、F1 和回答"是"的比例。发现原版 LLaVA、MultiModal-GPT、mPLUG-Owl 有 95%–99% 的回答是"是"，F1 低于 70，而 InstructBLIP 最好；三种设置依次变难，说明模型倾向编出指令数据中高频或常共现的物体。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)"评测测到看了吗"一线的起点与 [Baseline 页](../../fields/vlm/BASELINES.md)评测格；它暴露的"一律答是"被 [LLaVA-1.5](../arxiv-2310.03744/README.md) 归因于训练数据缺是非题。自述局限：只测物体有无；回答不含 yes/no 字样时会误判。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2305.10355（Yifan Li 等 6 位作者；当前 v3，2023-10）· [全文 PDF](https://arxiv.org/pdf/2305.10355v3) · 中国人民大学高瓴人工智能学院与信息学院、美团 · EMNLP 2023
- 方向：[视觉语言模型](../../fields/vlm/README.md)
