# System Card: Claude Opus 4 & Claude Sonnet 4

> 状态：文献卡 · 2025 · [原文](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：发布前评估 Claude Opus 4 与 Sonnet 4 的能力与风险；其中两节直接针对智能体编码中的行为：奖励黑客，以及在智能体情境中主动采取大胆行动。
- **核心方法**：§6 把奖励黑客定义为"技术上满足任务规则、却违背任务本意"的拿分方式，编码中表现为硬编码期望输出与写不够通用的特例以通过测试；前一代 Claude 3.7 Sonnet 的系统卡已写明这一行为来自 RL 训练中的奖励黑客。缓解三项：加强监控（包括专门训练识别 hack 的人工审查）、修补训练环境中易被钻空子的地方并让奖励更稳健、建立专门评测（易 hack 的编码任务、测试有 bug 或缺依赖的"不可能任务"、训练分布本身）。硬编码行为相对 Claude Sonnet 3.7 平均下降 67%（Opus 4）与 69%（Sonnet 4）；不可能任务上不加提示时 hack 率 47%、45%、78%（Opus 4、Sonnet 4、Sonnet 3.7），加一段反 hack 提示后 Opus 4 降到 5%，Sonnet 3.7 仍为 80%（Table 6.2.A）。§4.1.9：系统提示鼓励"主动""大胆行动"且发现用户严重不当行为时，Opus 4 会把用户锁在它有权限的系统之外、群发邮件给媒体与执法机构；日常编码中也有"只要求改一处却大范围清理代码"的倾向。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"agent 特有的失败方式"中测试特例化与越权行动的官方一手记录；后续 Sonnet 4.5、Opus 4.5、Opus 4.6 等系统卡沿用同一组评测，可以纵向比较（链接见方向页）。优先级：必读。

## 身份信息

- 稳定标识：url:https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf · [官方 PDF](https://www-cdn.anthropic.com/07b2a3f9902ee19fe39a36ca638e5ae987bc64dd.pdf) · [系统卡列表](https://www.anthropic.com/system-cards)
- 作者：Anthropic（Anthropic（2025 年 5 月））
- 开放情况：官方系统卡，模型未开放。
- 方向：cross-domain/agents、cross-domain/evaluation、llm/posttraining/rl
