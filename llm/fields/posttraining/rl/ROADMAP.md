# 语言模型强化学习：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

强化学习把生成过程与奖励连接起来。先区分策略、参考策略、价值估计和奖励来源，再问采样数据怎样影响更新，以及奖励怎样分配给一串token。

## 第二步：沿具体文章拆机制

[Proximal Policy Optimization Algorithms](../../../papers/ppo/README.md) → [Training language models to follow instructions with human feedback](../../../papers/instructgpt/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

用一次短轨迹说明观察、动作、回报和优势，随后核对PPO中的概率比值与InstructGPT的训练角色。

## 第四步：保留边界

生成更长的回答不自动等于更好的推理。PPO的截断比值也不是对任何规模更新都有效的硬性保证。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
