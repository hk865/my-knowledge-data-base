# Visual Instruction Tuning

> 状态：技术精读 · 2023 · [原文](https://arxiv.org/abs/2304.08485) · [NeurIPS 2023 正式版](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：CLIP 让图像与文字对齐，但只会算相似度、不会回答问题；Flamingo、BLIP-2 已把视觉编码器接上语言模型，训练数据却是图文对，模型倾向于描述图像，而不是按用户的要求作答。卡住的是数据：多模态指令数据要靠人工众包，成本高、定义也模糊。
- **核心方法**：把语言侧 InstructGPT 式的指令微调搬到视觉：让只看文字的 GPT-4 根据 COCO 的描述和目标框，改写出 15.8 万条视觉指令数据（对话、详细描述、复杂推理三类）。连接器换成最简的一个可训练线性层，把冻结的 CLIP ViT-L/14 网格特征投影后接进 Vicuna，替代 Flamingo 的门控交叉注意力和 BLIP-2 的 Q-Former；先只训投影层，再连同语言模型一起训，视觉编码器始终冻结。自建评测上的相对得分（以纯文本 GPT-4 的得分为分母，不是准确率）从不做指令微调的 21.5 升到 85.1（表 4），ScienceQA 微调后 90.92%（表 7）。
- **为什么在这个库里**：[视觉语言模型方向 Baseline 页](../../fields/vlm/BASELINES.md)的主基线是 LLaVA-1.5 连同本篇，定义了"ViT–投影–LLM、两段训练"的默认接口，也是[入门页](../../fields/vlm/README.md)阅读顺序的第一篇；它取 CLIP 倒数第二层特征的做法，是[视觉表征方向 Baseline 页](../../fields/visual-representation/BASELINES.md)"读出接口"一行的代表。优先级：必读。

## 阅读入口

- [技术精读](reading.md)：线性投影 + GPT-4 合成的指令数据；"局限与后续"补了 POPE 幻觉评测与 LLaVA-1.5、Qwen-VL 的修正
- [本篇图解与说明](figures/README.md)

## 可选的阅读顺序

[Learning Transferable Visual Models From Natural Language Supervision](../clip/README.md) → [Training language models to follow instructions with human feedback](../../../llm/papers/instructgpt/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 身份信息

- 稳定标识：arxiv:2304.08485 · 威斯康星大学麦迪逊分校、微软研究院、哥伦比亚大学 · NeurIPS 2023
- 年份：2023
- [官方原文页面](https://arxiv.org/abs/2304.08485)
- [官方全文入口](https://arxiv.org/pdf/2304.08485v2)
- 阅读版本：v2
- 方向：multimodal/vlm、robotics/embodied-policies
