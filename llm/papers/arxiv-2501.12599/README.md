# Kimi k1.5: Scaling Reinforcement Learning with LLMs

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.12599)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：下一词预训练受限于高质量数据的总量，强化学习让模型通过奖励自己探索，是新的扩展维度；但摘要写明此前公开的工作没有用 RL 做出有竞争力的结果。
- **核心方法**：长思维链 RL：把 RL 的上下文窗口扩到 128K，作者认为长思维链相当于把规划搜索"压平"进上下文，因此不用蒙特卡洛树搜索、价值函数和过程奖励模型（§1、§2.3）。超长轨迹用 partial rollouts：每轮只生成固定 token 预算，没写完的存起来下一轮续写（§2.6.2）。针对回答越训越长，加入长度奖励：同题多个回答中，答对的越短奖励越高，又长又错的受罚（§2.3.3）。再用 long2short 把长思考模型的能力转到短回答模型：模型权重平均、取最短正确回答做 SFT、DPO、带长度惩罚的第二阶段 RL；后者 AIME 2024 为 60.8、平均只用 3,272 个 token（§2.4、§3.4）。长思考版 AIME 2024 为 77.5，o1 为 74.4（Table 2）。
- **为什么在这个库里**：[推理时计算方向](../../fields/inference/README.md)"推理模型"阶段与 [DeepSeek-R1](../arxiv-2501.12948/README.md) 同日发布的另一份公开配方：两家都不用过程奖励与搜索，Kimi 额外把"控制思考长度"写进训练，是 long2short 一支的起点；RL 算法部分见[强化学习方向](../../fields/posttraining/rl/README.md)。结论写明未来要在不损害探索的前提下减少过度思考。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2501.12599 · [全文](https://arxiv.org/pdf/2501.12599) · Kimi Team（Moonshot AI）
- 方向：llm/posttraining/rl、llm/inference
