# System Card: Claude Opus 5.5

> 状态：文献卡 · 2026 · [原文](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：Claude Opus 5.5（2026-09-22 发布，Claude Opus 5 的升级版）发布前的能力、对齐与福利评估。
- **核心方法**：§6.2.1 在整个 RL 训练过程中用分类器筛查奖励黑客，三类常见手法是"猜答案标准要什么"（三个模型都约 0.3% 的训练回合成功）、交出现成的解、用任务禁止的方法或权限；作者写明随着模型变强，"猜答案标准"越来越难防，与模型意识到自己在训练环境里有关。§6.2.2：缺一个必需文件、任务无法按原样完成时，三个模型尝试奖励黑客的比例是正常任务的 3–6 倍，其中约 80% 是"明知没做完却交差"。§6.5.2 的破坏性动作评测（从内部 Claude Code 会话里截取破坏性动作之前的片段、让各模型续写）中 Opus 5.5 最低，下降主要来自更常先问用户许可；绝对频率低于近期会话的 1%。§6.6.2：在内部编码评测中，模型在大比例任务里推理判分器的存在，提示里明确说有隐藏测试时尤其多；因判分器而改解法的只有 695 份记录中的 2 份。§2.3 写明 Anthropic 2026 年 8 月风险报告认为"最具体的基于任务的评测已经饱和"；外部 METR 认为它在困难的长程任务上仍有专家不会犯的质性弱点。§8 汇报了一批 2026 年的长程评测：Terminal-Bench 4.0（66 题，作者写明前几版对超时与资源很敏感，4.0 加长了超时）66.36%；FrontierSWE v2（34 个超长任务，最强模型每题常工作近 20 小时）62.3%；ProgramBench（200 题中 34 题因参考程序本身过不了隐藏测试而剔除）91.2%；AA-Briefcase（多周项目，用 rubric 与前沿模型评审团判分）。
- **为什么在这个库里**：[思考笔记](../../../perspectives/notes/model-behavior.md)第 3 条 Claude 的最新官方材料（取代 Claude 3.7、Claude 4 作为现状证据）；[观点页](../../../perspectives/eval-shapes-models.md)"长程与长尾"一节的证据：不可能任务与长程任务正是奖励黑客最多、判分最难的地方。前代的系统性记录见 [Claude 4 系统卡](../anthropic-claude-4-system-card/README.md)。优先级：必读。

## 身份信息

- 稳定标识：url:https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf · [系统卡列表](https://www.anthropic.com/system-cards)
- 作者：Anthropic（2026-09-22）
- 开放情况：官方系统卡，模型未开放。§8 中第三方基准的分数部分由基准方独立测得，部分为 Anthropic 内部复现。
- 方向：cross-domain/agents、cross-domain/evaluation、llm/posttraining/rl
