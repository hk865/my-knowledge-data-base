# Beyond Correctness: Benchmarking Multi-dimensional Code Generation for Large Language Models

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2407.11470)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：代码评测几乎只看正确性，忽略真实开发中同样重要的可读性、可维护性与效率；只看正确性也容易受数据污染影响。
- **核心方法**：RACE 测四个维度：Readability、mAintainability、Correctness、Efficiency。可读性拆成代码长度、命名风格（驼峰或下划线）、注释粒度（行级或函数级）；可维护性用可维护性指数 MI（由 Halstead 体积、圈复杂度、代码行数与注释比例算出的 0–100 分）与模块化（要求用 1、2 或 3 个函数实现，用语法树数函数个数）；效率按给定的时间、空间复杂度要求打归一化分。每个维度都写成用户的具体要求，检查代码是否既正确又满足要求，判定用静态分析、正则与语法树。评测 28 个模型：只看正确性的 benchmark 看不到这些缺陷；要求一多，最强的代码模型也明显变差；多数模型有固有的代码风格偏好，用户要求与偏好不一致时难以遵从。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"代码质量"一节：它把"代码规范"操作化为"按明说的要求写"，测得到遵从，测不到没有明说的项目约定和需求变化后的维护代价（后者见 [MaintainCoder](../arxiv-2503.24260/README.md)）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2407.11470 · [全文 PDF](https://arxiv.org/pdf/2407.11470) · 中国科学院软件研究所
- 发表：arXiv v2（预印本）
- 方向：cross-domain/evaluation
