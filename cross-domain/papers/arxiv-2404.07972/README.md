# OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.07972)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有的电脑操作数据集只有示范、没有可执行环境；不执行的评测假设每个任务只有一种解法，会错判其他正确做法（§1）。
- **核心方法**：在真实操作系统虚拟机（Ubuntu、Windows、macOS）里，agent 用原始鼠标键盘动作操作任意应用。每个任务带初始状态配置和自定义评测脚本：取出最终状态中的关键内容（例如被修改的文件）再判断是否成功，共 134 个评测函数；也包含 30 个做不到的任务（§2–3）。369 个 Ubuntu 任务约 1800 人时标注。人类成功率约 72.36%，最好的模型（以可访问性树为文本输入的 GPT-4）12.24%，跨应用工作流任务最高只有 6.57%（Table 5、§1）。550 个失败案例中超过 75% 存在鼠标点击不准，agent"规划强、执行弱"（§5.4）。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"真实环境 benchmark"阶段的电脑操作代表；按最终状态判分与 SWE-bench 的"跑测试"同理。2025 年官方推出 OSWorld-Verified 修复社区报告的问题，是"benchmark 本身会坏"的一个例子。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2404.07972 · [全文 PDF](https://arxiv.org/pdf/2404.07972)
- 作者：Tianbao Xie、Danyang Zhang、Jixuan Chen、Xiaochuan Li、Siheng Zhao、Ruisheng Cao、Toh Jing Hua、Zhoujun Cheng、Dongchan Shin、Fangyu Lei、等 17 位作者（香港大学、CMU、Salesforce Research、University of Waterloo）
- 开放情况：代码与环境开放：os-world.github.io、github.com/xlang-ai/OSWorld（Apache-2.0）。
- 方向：cross-domain/agents、cross-domain/evaluation
