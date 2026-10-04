# WebArena: A Realistic Web Environment for Building Autonomous Agents

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2307.13854)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有的 agent 评测环境过度简化真实情形，并且只比较动作序列的字面形式，不看任务在功能上是否完成（§1）。
- **核心方法**：自托管四个真实风格的网站（电商、论坛、GitLab、内容管理系统）外加地图、计算器等工具，用 Docker 打包；812 个任务来自 241 个模板（§3.1）。成功由程序判定：信息类任务按精确匹配、包含匹配或 GPT-4 判语义等价打分；操作类任务用数据库查询、API 或页面选择器检查执行后的中间状态（§3.2）。还包含一部分"做不到"的任务，期望 agent 回答 N/A。最好的 GPT-4 agent 成功率 14.41%，人类 78.24%（Table 2）；给"任务可能做不到"的提示时，GPT-4 把 54.9% 可完成的任务误判为做不到（§5.1）。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"真实环境 benchmark"阶段的网页环境代表：第一次把"按执行后的状态判成功"用在网页任务上。这种判定方式也就是一个可用于训练的奖励函数。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2307.13854 · [全文 PDF](https://arxiv.org/pdf/2307.13854)
- 作者：Shuyan Zhou、Frank F. Xu、Hao Zhu、Xuhui Zhou、Robert Lo、Abishek Sridhar、Xianyi Cheng、Tianyue Ou、Yonatan Bisk、Daniel Fried、等 12 位作者（Carnegie Mellon University；ICLR 2024）
- 开放情况：代码与环境开放：webarena.dev、github.com/web-arena-x/webarena（Apache-2.0）。
- 方向：cross-domain/agents、cross-domain/evaluation
