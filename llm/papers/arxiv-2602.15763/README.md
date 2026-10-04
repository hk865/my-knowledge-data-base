# GLM-5: from Vibe Coding to Agentic Engineering

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2602.15763)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：把开源模型从"按提示写代码"推进到长程的智能体工程任务，同时压低长上下文的训练与推理成本。
- **核心方法**：744B 总参数、40B 激活的 MoE（256 个专家、80 层），基座训练 28.5T token。注意力从 MLA 改为 DeepSeek 的 DSA（[DeepSeek-V3.2](../arxiv-2512.02556/README.md) 提出的训练时稀疏注意力）：在中段训练结束的基座上做 1000 步稠密预热和 20B token 的稀疏适应，长序列上注意力计算约省 1.5–2 倍，128K 的 RULER 与稠密 MLA 基本持平（78.86 对 79.21）；在 GLM-9B 上另比较了滑动窗口与 Gated DeltaNet 一类线性注意力，128K 上都比 DSA 掉得多。3 个 MTP 层共享参数，投机解码的平均接受长度 2.76（DeepSeek-V3.2 为 2.55，作者内部测试集）。后训练依次为 SFT（含交错思考）、推理 RL、智能体 RL、通用 RL，最后用以前阶段的检查点作教师做跨阶段 on-policy 蒸馏，理由是顺序优化不同目标会累积损失先前的能力。智能体 RL 用异步框架 slime：推理与训练放在不同 GPU 上，每 K 步同步一次权重；直接用采样时记录的 log 概率做双侧重要性采样，丢掉版本落后太多的轨迹；Token-in-Token-out 网关避免多轮中重新分词造成的不一致。RL 中把 DSA 索引器冻结并改用确定性的 top-k：非确定性的 top-k 实现会让 RL 几步之内性能骤降、熵急跌。
- **为什么在这个库里**：[强化学习方向](../../fields/posttraining/rl/README.md)"异步智能体 RL 与训练—推理不一致"一格的代表；[长上下文方向](../../fields/long-context/README.md)与[架构方向](../../fields/architecture/README.md)中"训练时稀疏被 DeepSeek 以外的团队采用"的第一份证据。优先级：选读。

## 批注

**易误读**
- 高效注意力的对比（滑窗、GDN、SimpleGDN）是在 GLM-9B 上以 64K 长度继续训练 190B token 得到的，不是 744B 主模型的结果；DSA 对 MLA 的 RULER 对比才是主模型。
- MTP 接受长度的对比用的是作者的私有测试集与 4 步投机。

**未核实 / 待验证**
- 报告未单列局限一节；幻灯片生成任务中观察到的奖励黑客（截断过长内容、操纵间距）取自正文描述，具体规模未核对。

## 身份信息

- 稳定标识：arxiv:2602.15763 · [全文 PDF](https://arxiv.org/pdf/2602.15763) · 智谱 AI（Z.ai）、清华大学，2026-02-17
- 方向：llm/posttraining/rl、llm/long-context、llm/architecture
