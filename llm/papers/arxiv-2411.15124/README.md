# Tulu 3: Pushing Frontiers in Open Language Model Post-Training

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2411.15124)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源模型的后训练配方落后于闭源，而后训练的数据与配方恰恰最不透明。
- **核心方法**：在 Llama 3.1 基座上公开全部数据、代码与评测的配方：SFT → 长度归一化的 DPO（加入从自家 SFT 模型采样的 on-policy 偏好数据后效果更好）→ RLVR（Reinforcement Learning with Verifiable Rewards，一句话：只有答案能被程序验证为正确时才给固定奖励的 RL；在 GSM8K、MATH 与可验证的指令约束上训练）。评测分开发集与未见集，开发时不看未见集。作者记录：降低 KL 惩罚后出现过度优化，IFEval 上有只为满足约束而写的怪异输出（附录 B.4）；在没有专门调参的对照中，PPO 的平均分与 DPO 相近、略低，而迭代成本更高。
- **为什么在这个库里**：RLVR 这一名称的出处；[SFT](../../fields/posttraining/sft/BASELINES.md)、[偏好学习](../../fields/posttraining/preferences/BASELINES.md)、[强化学习](../../fields/posttraining/rl/BASELINES.md)三张 Baseline 表里都有它的位置。完全开放，是复现与对照时的参照。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2411.15124 · [全文 PDF](https://arxiv.org/pdf/2411.15124) · AI2（Allen Institute for AI）、华盛顿大学
- 方向：llm/posttraining/sft、llm/posttraining/preferences、llm/posttraining/rl
