# EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.01840)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：EAGLE 系列是投机解码（草拟器先猜后续 token、目标模型并行验证）的草拟器，在目标模型顶层特征上做特征级的自回归草拟；作者发现扩大训练数据对 EAGLE 的提升有限，原因在于"预测特征"这一约束。
- **核心方法**：相对 EAGLE 与 EAGLE-2：放弃预测特征，改为直接预测 token；不再只用顶层特征，而是融合目标模型低、中、高三层的特征；训练时模拟推理过程（training-time test：草拟后续步时，用草拟器自己的输出代替尚未得到的目标特征）。验证沿用动态草稿树与树注意力的精确投机验证。最高加速 6.5 倍，约为 EAGLE-2 的 1.4 倍；在 SGLang 中批量为 64 时吞吐提高 1.38 倍。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"草拟器设计"一格的主流基线，[DFlash](../arxiv-2602.06036/README.md) 以它为主要对照。理解它需要先读 [Leviathan 等的投机解码](../arxiv-2211.17192/README.md)。优先级：必读。

## 批注

**易误读**
- 草拟器要针对每个目标模型专门训练，并能读取目标模型的内部特征，不能拿任意黑箱小模型直接替代。

## 身份信息

- 稳定标识：arxiv:2503.01840 · [全文 PDF](https://arxiv.org/pdf/2503.01840) · 代码在 SafeAILab/EAGLE
- 作者：Yuhui Li、Fangyun Wei、Chao Zhang、Hongyang Zhang（北京大学、Microsoft Research、滑铁卢大学、Vector Institute）
- 方向：llm/inference
