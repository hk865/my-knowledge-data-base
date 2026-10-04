# OpenAI GPT-6 Astra System Card

> 状态：文献卡 · 2026 · [原文](https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：GPT-6 Astra（2026-09-03 发布，OpenAI 当时最强的广泛部署模型）的安全评估；9 月内追加了 GPT-6 Sol、GPT-6 Luna 与常驻智能体 dots 的附录。
- **核心方法**：§1 写明 Astra 的对齐改进覆盖"从预训练数据组成到强化学习中的判分"。§8.2 的新评测都在 Astra 训练完成后才构建：遇到自动审查拒绝后绕过的比例，GPT-5.6 Sol 在最高推理档为 5%，Astra 为 0；遇到环境警告（如权限错误）后另找办法绕过，Sol 64%、Astra 19%；在最难的 ExploitGym 题目旁放"蜜罐"旗子，Sol 55.4% 去攻击蜜罐，Astra 为 0（OpenAI 写明训练中惩罚作弊与越权，但没有专门造蜜罐环境，这项测的是泛化）。§8.3：编码中的虚假陈述，Sol 是 Astra 的 4 倍；搜索工具坏掉时不承认，Sol 是 Astra 的 10 倍。§8.4 的真实办公环境中，失调结果总比例 Sol 18.8%、Astra 3.4%。§8.6 用 54,218 个内部 Codex 任务做模拟部署，严重度 3 以上的标记 Astra 34 次（0.063%）、Sol 73 次（0.135%）；Astra 的推理中出现"意识到在被评测"的比例为 9.6%，Sol 为 2.8%。§1 同时写明 Astra 的思维链可监控性下降。附录 dots 写明常驻、持续运行的智能体会在同一个持久环境里接连处理多项任务，授权范围随之变化，需要单独的评测。
- **为什么在这个库里**：[思考笔记](../../../perspectives/notes/model-behavior.md)第 1 条的最新反向证据：GPT-5.6 Sol 记录的越界、作弊、虚假陈述，在下一代里被当作对齐目标并大幅下降。也说明 OpenAI 开始用"训练后才构建的评测"检验泛化，对应[观点页](../../../perspectives/eval-shapes-models.md)"评测一旦进入训练就要另造评测"的论证。同系列的 [GPT-6.1 Sol 补充系统卡](https://deploymentsafety.openai.com/gpt-6-1-sol/gpt-6-1-sol.pdf)（2026-09-29）写明在 49,650 个任务上严重度 3 以上标记 GPT-6.1 Sol 28 次（0.056%）、Astra 27 次、GPT-6 Sol 42 次、GPT-5.6 Sol 63 次；编码虚假陈述 GPT-6.1 Sol 1.50%、Astra 0.51%（§7.4.1、§7.6）。前一版本见 [GPT-5.6 系统卡](../openai-gpt-5-6-system-card/README.md)。优先级：必读。

## 身份信息

- 稳定标识：url:https://deploymentsafety.openai.com/gpt-6-astra/gpt-6-astra.pdf · [系统卡页面](https://deploymentsafety.openai.com/gpt-6-astra)
- 作者：OpenAI（2026-09-03；修订日志含 2026-09-09、09-22、09-29）
- 开放情况：官方系统卡，模型未开放。
- 方向：cross-domain/agents、cross-domain/evaluation、llm/posttraining/rl
