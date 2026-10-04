# FitNets: Hints for Thin Deep Nets

> 状态：文献卡 · 2014 · [原文](https://arxiv.org/abs/1412.6550)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：网络越深越难用梯度训练。[Hinton 等](../arxiv-1503.02531/README.md)的蒸馏让学生模仿教师的软输出，但只传输出时，比教师更深、更窄的学生仍然训不动，而同样的计算量下更深的网络本可以更准。
- **核心方法**：在蒸馏之外加"提示"：取教师中间一层作提示层、学生中间一层作被引导层，学生的被引导层经过一个回归器（学生层更窄，需要映射到教师的维度）去预测提示层的输出。训练分两段：先只用提示损失训练学生到被引导层为止的部分，再用蒸馏损失训练整个网络，并逐步降低教师软目标的权重（§2.2）。CIFAR-10 上，11 层、约 862K 参数的 FitNet 2 达到 91.06%，超过 5 层、约 9M 参数的教师（90.18%），参数少约 10.4 倍、推理快 4.6 倍；19 层、约 2.5M 参数的 FitNet 4 达到 91.61%（Table 5）。
- **为什么在这个库里**：[知识蒸馏方向](../../fields/knowledge-distillation/README.md)阶段 3 与 [Baseline 页](../../fields/knowledge-distillation/BASELINES.md)"传什么 = 中间层提示"一格的代表，"传中间层"一路从这里开始，后来 [MiniLM](../../../llm/papers/arxiv-2002.10957/README.md) 用注意力关系代替了逐层特征对齐。它写出了两个失败条件：提示本身是正则，被引导层选得越深学生越容易过度正则化，作者只取两边的中间层（§2.2）；3 千万次乘法的计算预算下，标准反传训不动 5 层以上的网络，只加蒸馏能训到 7 层，加上提示才训到 13 层（§4.1）。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1412.6550 · [全文 PDF](https://arxiv.org/pdf/1412.6550) · Adriana Romero、Nicolas Ballas、Samira Ebrahimi Kahou、Antoine Chassang、Carlo Gatta、Yoshua Bengio（Universitat de Barcelona、Université de Montréal、École Polytechnique de Montréal、Centre de Visió per Computador） · ICLR 2015
- 方向：cross-domain/knowledge-distillation
