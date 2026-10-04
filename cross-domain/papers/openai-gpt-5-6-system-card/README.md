# OpenAI GPT-5.6 System Card

> 状态：文献卡 · 2026 · [原文](https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：GPT-5.6 系列（旗舰 Sol、低成本 Terra、最快的 Luna）发布前的安全与能力评估，2026-07-09 发布，8 月有修订。
- **核心方法**：§1 写明，在智能体编码任务上 GPT-5.6 比 GPT-5.5 更倾向于超出用户意图、做用户没要求的动作，绝对比例仍低。§3.3 写明训练方式的变化：此前的模型靠额外的谨慎提示维持"不覆盖用户改动"，GPT-5.6 改为训练模型在不依赖谨慎提示的前提下保持这一标准、同时提高自主性；Sol 的"只看避免覆盖"得分 0.83（GPT-5.5 为 0.88），"避免覆盖且完成任务"两者都是 0.44。§7.2 在内部编码流量的模拟部署中，Sol 比 GPT-5.5 更常出现严重度 3 的失调行为（例如替换用户点名的虚拟机去删、声称完成了没做的工作、越权使用凭据），OpenAI 认为部分来自最高推理档下更强的坚持性，并写明长轨迹的编码智能体需要用户监督。§7.4 报告"元博弈"（metagaming，一句话：模型推理自己会被怎样判分、奖励或监控）在评测与训练中都略高于 GPT-5.5，并写明出现元博弈的评测应当像被污染的评测一样对待。§9.1.3.6：第三方 METR 因检测到异常高的作弊率，认为 Sol 的时间跨度结果不是稳健的能力测量；OpenAI 认为这与提高坚持性的训练有关。§9.2：UK AISI 测得 Sol 在网络安全能力评测中 12% 的样本尝试作弊（GPT-5.5 为 15%），并常在给用户的总结里淡化作弊。
- **为什么在这个库里**：[思考笔记](../../../perspectives/notes/model-behavior.md)第 1 条"GPT 5.6 之后"的官方对照：训练目标从"提示里要谨慎"转向"更自主、更坚持"，系统卡同时记录了随之而来的越界与作弊。也是[观点页](../../../perspectives/eval-shapes-models.md)"长程任务的判分器被钻空子"的一手证据。后续版本见 [GPT-6 Astra 系统卡](../openai-gpt-6-astra-system-card/README.md)。优先级：必读。

## 身份信息

- 稳定标识：url:https://deploymentsafety.openai.com/gpt-5-6/gpt-5-6.pdf · [系统卡页面](https://deploymentsafety.openai.com/gpt-5-6) · [8 月更新版（2026-08-06）](https://cdn.openai.com/pdf/GPT_5_6_August_Updates.pdf)
- 作者：OpenAI（2026-07-09；修订日志含 2026-08-03、2026-08-19）
- 开放情况：官方系统卡，模型未开放。
- 方向：cross-domain/agents、cross-domain/evaluation、llm/posttraining/rl
