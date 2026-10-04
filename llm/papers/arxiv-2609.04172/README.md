# Rethinking On-Policy Distillation of Large Language Models II: One Training Example

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2609.04172)

- **解决什么**：on-policy 蒸馏的瓶颈来自提示数量，还是学生吸收教师信号的速度。
- **核心方法**：接续[Rethinking OPD](../arxiv-2604.13016/README.md)，用极少提示反复采样，比较学生访问的前缀状态与全量数据训练的覆盖；多样提示带来的状态覆盖比题目数更能解释收益。
- **为什么在这个库里**：补上[SFT 路线](../../fields/posttraining/sft/ROADMAP.md)中“怎样挑蒸馏数据”的一环。优先级：选读。

## 批注

**易误读**

- 少提示仍产生大量 rollout 和逐 token 教师监督；状态覆盖是相对全量训练的聚类代理指标，不是所有可能推理状态的覆盖率。
