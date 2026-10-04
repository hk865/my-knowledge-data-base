# Rethinking On-Policy Distillation of Large Language Models II: One Training Example

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.04172)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：同策略蒸馏（OPD：学生自行生成，教师逐 token 提供监督）的瓶颈来自提示数量，还是学生吸收教师信号的速度。
- **核心方法**：用极少提示反复采样，测量学生访问的前缀状态及每步缩小师生差距的比例；少量多样提示可覆盖大部分参考状态，但增加提示后，教师信号的吸收仍逐步变慢。
- **为什么在这个库里**：补上[SFT 路线](../../fields/posttraining/sft/ROADMAP.md)中"怎样挑蒸馏数据与提高学习效率"的一环，并连接[知识蒸馏](../../../cross-domain/fields/knowledge-distillation/README.md)的训练机制比较。优先级：选读。

## 身份信息

- 作者：Zixuan Fu、Bingxiang He、Yuxin Zuo、Haohuan Huang、Jinqian Zhang、Ruhang Xiao、Cheng Qian、Qinyu Luo、Huan-ang Gao、Yudong Wang、Zhiyuan Liu、Ning Ding、Chaojun Xiao
- 稳定标识：arxiv:2609.04172 · [全文](https://arxiv.org/pdf/2609.04172)
- 方向：llm/posttraining/sft、cross-domain/knowledge-distillation

## 批注

**易误读**

- 少提示仍产生大量 rollout 和逐 token 教师监督；状态覆盖是相对全量训练的聚类代理指标，不是所有可能推理状态的覆盖率。

**与其他论文的关联**

- [配对阅读](../arxiv-2609.37326/README.md)：后者诊断同族小模型的答案标记与停止；与本篇的监督吸收效率分别比较。
- [知识蒸馏方向](../../../cross-domain/fields/knowledge-distillation/README.md)：把教师信号、采样分布和训练目标放到同一张机制表中比较。
