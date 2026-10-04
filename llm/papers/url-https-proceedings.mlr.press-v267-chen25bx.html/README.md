# Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models

> 状态：文献卡 · 2025 · [原文](https://proceedings.mlr.press/v267/chen25bx.html)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：长推理模型（推理时生成很长思维链的模型）在简单问题上也会生成多轮冗余的解答，耗费计算却几乎不提高准确率和多样性，即过度思考。
- **核心方法**：首次系统研究过度思考，从结果和过程两个角度提出衡量计算是否用得合理的效率指标。缓解方法用自训练：QwQ-32B-Preview 在 PRM12K 上自己生成长推理，剪去多余的解答轮次构造短轨迹（例如只保留第一个正确解），以（短，最长）回答为偏好对做长度偏好优化，比较了 DPO、RPO、SimPO 三种偏好优化损失。在 GSM8K、MATH500、GPQA、AIME 上减少了计算开销，表现保持。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"思考长度怎样按难度分配"一问；与 [TOPS](../arxiv-2502.18080/README.md) 是同一问题的两种做法。缓解手段用的是[偏好学习方向](../../fields/posttraining/preferences/README.md)的偏好优化（[DPO](../dpo/README.md) 及其变体），分析对象包括 [DeepSeek-R1](../arxiv-2501.12948/README.md)。优先级：选读。

## 身份信息

- 稳定标识：url:https://proceedings.mlr.press/v267/chen25bx.html · [全文 PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf) · ICML 2025（PMLR 267）· 预印本 arXiv:2412.21187，预印本题名为 Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs
- 作者：Xingyu Chen、Jiahao Xu、Tian Liang、Zhiwei He、Jianhui Pang、Dian Yu、Linfeng Song、Qiuzhi Liu、Mengfei Zhou、Zhuosheng Zhang、Rui Wang、Zhaopeng Tu、Haitao Mi、Dong Yu（上海交通大学、腾讯）
- 方向：llm/inference、llm/posttraining/preferences
