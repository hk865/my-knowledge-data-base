# Diffusion Policy Policy Optimization

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2409.00588)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：行为克隆预训练的策略受专家数据质量和覆盖范围限制，常常不是最优；用策略梯度微调扩散策略过去被认为效率太低（§1）。
- **核心方法**：DPPO 把扩散策略的去噪过程本身看作一个内层 MDP（每一步去噪是一个"动作"），与环境 MDP 组成两层 MDP，再用 PPO 对整个链做策略梯度微调。
  - 基准覆盖 Gym、Franka-Kitchen、Robomimic、Furniture-Bench。
  - 像素输入的 Transport 任务上，高斯策略的 PPO 一直停在 0%，DPPO 超过 50%（§5.3）。
  - 家具装配 One-leg 零样本上真机 20 次成功 16 次。高斯策略在仿真中 88%，上真机是 0%（§5.4）。作者也指出，在需要激进探索的任务（Lamp）上，DPPO 略低于高斯策略，推测是它的探索留在示范数据流形附近、反而受限（§6）。
  - 作者自述主要局限：样本效率低于离策略方法（§7）；微调时不用专家数据，对预训练质量敏感（§5.2）。
- **为什么在这个库里**：[模仿与强化学习 Baseline 表](../../fields/imitation-reinforcement-learning/BASELINES.md)中"策略改进 = 在模仿之上用 RL 微调"一格，把 [Diffusion Policy](../diffusion-policy/README.md) 与 [PPO](../../../llm/papers/ppo/README.md) 两个基线接在一起。优先级：必读。
