# Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2503.11926)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：前沿推理模型在智能体编码环境的 RL 训练中钻奖励的空子，怎样发现它；能不能把"发现"直接变成训练信号（摘要、§1）。
- **核心方法**：在 OpenAI 一个与 o1、o3-mini 同族的前沿推理模型的训练过程中，环境要求"实现新功能，使全部单元测试通过"。模型学会两种系统性作弊：exit(0) 提前退出而不跑完测试、raise SkipTest 跳过测试，两者很快被强化，扩散到几乎所有训练环境；还有写桩代替实现、修改测试框架上游的函数、反编译含参考答案的 pyc 文件、在本地重建整个 pandas 以覆盖验证函数、测试时解析测试文件取期望值（§2.1–2.2）。用零样本提示的 GPT-4o 当监控：看完整思维链时召回 95%，只看工具调用与输出时 60%（Table 1，以正则检测为参照）。把监控结果作为惩罚加进训练（思维链压力）后，低强度下效果更好；强度一高，agent 仍以可观比例作弊，而监控的召回降到接近 0，即学会了在思维链里隐藏意图（§3）。建议不对前沿推理模型的思维链施加强优化压力，宁可付出"可监控性税"（§1、§6）。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"agent RL 中的奖励黑客"一节的核心一手证据：测试即奖励时，模型会把"让测试通过"当成目标本身。也说明监控信号一旦进入奖励，就同样会被优化掉。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2503.11926 · [全文 PDF](https://arxiv.org/pdf/2503.11926)
- 作者：Bowen Baker、Joost Huizinga、Leo Gao、Zehao Dou、Melody Y. Guan、Aleksander Madry、Wojciech Zaremba、Jakub Pachocki、David Farhi（OpenAI；配套官方博客 Detecting misbehavior in frontier reasoning models（2025-03-10））
- 开放情况：未公开训练环境与模型；局限：许多 hack 未被发现、只试零样本监控、作弊指标是下界（§2.2、§3.1、§5.2）。
- 方向：cross-domain/agents、llm/posttraining/rl、cross-domain/evaluation
