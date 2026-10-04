# Solving Without Stopping: On-Policy Distillation at Small Scale

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.37326)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：同策略蒸馏（OPD：在学生自己生成的前缀上向教师学习）后，小模型分数变化，究竟来自解题能力，还是它不会结束思考并交出答案。
- **核心方法**：以 Qwen3-8B 教 4B、1.7B、0.6B 学生，对照思考与非思考模式，分别跟踪答案标记、正确性和停止；在其数学实验中，解题改善可以伴随停止能力退化。
- **为什么在这个库里**：接续[SFT](../../fields/posttraining/sft/README.md)的 OPD 成败条件，与[知识蒸馏](../../../cross-domain/fields/knowledge-distillation/README.md)共同讨论小模型行为迁移，也连接[推理时计算](../../fields/inference/README.md)的过度思考问题。优先级：选读。

## 身份信息

- 作者：Hongyang Li、Yiming Zhu、Xiao Li、Caesar Wu、Said Mammar、Pascal Bouvry
- 稳定标识：arxiv:2609.37326 · [全文](https://arxiv.org/pdf/2609.37326)
- 方向：llm/posttraining/sft、cross-domain/knowledge-distillation

## 批注

**易误读**

- 证据限于同一家族小模型与数学蒸馏；不能外推为所有 OPD 模型都会丧失停止能力。

**与其他论文的关联**

- [配对阅读](../arxiv-2609.04172/README.md)：后者分析提示诱发的状态覆盖与监督吸收；本篇的停止退化证据来自另一组实验。
- [知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)：把教师信号、采样分布和训练目标放到同一张机制表中比较。
