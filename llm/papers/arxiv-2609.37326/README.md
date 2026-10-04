# Solving Without Stopping: On-Policy Distillation at Small Scale

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.37326)

- **解决什么**：小模型蒸馏后分数变化，究竟来自解题能力，还是它不会结束思考并交出答案。
- **核心方法**：以 Qwen3-8B 教 4B、1.7B、0.6B 学生，对照思考与非思考模式，分别跟踪答案标记、正确性和停止；在其数学实验中，解题改善可以伴随停止能力退化。
- **为什么在这个库里**：接续[SFT](../../fields/posttraining/sft/README.md)的 OPD 成败条件，也连接[推理时计算](../../fields/inference/README.md)的过度思考问题。优先级：选读。

## 批注

**易误读**

- 证据限于同一家族小模型与数学蒸馏；不能外推为所有 OPD 模型都会丧失停止能力。
