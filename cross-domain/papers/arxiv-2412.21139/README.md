# Training Software Engineering Agents and Verifiers with SWE-Gym

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2412.21139)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：软件工程缺少可训练的环境：SWE-bench 的训练集只有补丁，没有逐步动作、可执行环境和奖励信号，而构建环境本身很难（§1）。
- **核心方法**：从 11 个 Python 仓库（与 SWE-bench 的仓库不重叠，以防污染）收集 2,438 个真实任务，每个配可执行的运行环境、单元测试和自然语言任务描述；约 200 人工小时、1 万 CPU 核时，预建 Docker 镜像共 6 TB（§3）。用 GPT-4o 与 Claude 3.5 Sonnet 采样，保留 491 条成功轨迹做拒绝采样微调（即过滤后的行为克隆）Qwen2.5-Coder-32B：OpenHands 框架下 SWE-bench Verified 从 7.0% 升到 20.6%、Lite 从 3.0% 升到 15.3%（Table 3）；再用成功与失败轨迹训练一个结果奖励模型当验证器，在 16 个候选中挑一个，Verified 到 32.0%。在 OpenHands 上做在线自我改进时成绩反而从 15.3% 降到 8.7%，作者写明"自我改进尚未奏效"（§4.2）。自述局限（§6）：环境多样性有限（仓库数、任务类型、语言）；只看任务完成，忽略人在回路中的协作。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)"把 agent 能力训进模型"阶段的开源起点：环境 + 测试就是奖励函数。与 [SWE-RL](../arxiv-2502.18449/README.md)（不执行，只比补丁相似度）对照，可以看出奖励定义怎样改变学到的东西。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2412.21139 · [全文 PDF](https://arxiv.org/pdf/2412.21139)
- 作者：Jiayi Pan、Xingyao Wang、Graham Neubig、Navdeep Jaitly、Heng Ji、Alane Suhr、Yizhe Zhang（UC Berkeley、UIUC、CMU、Apple；ICML 2025）
- 开放情况：环境、模型与轨迹开放：github.com/SWE-Gym/SWE-Gym、Hugging Face SWE-Gym。
- 方向：cross-domain/agents、llm/posttraining/rl、llm/posttraining/sft
