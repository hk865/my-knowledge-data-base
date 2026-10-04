# Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2404.10719)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：学术 benchmark 上最好的结果多来自 DPO 这类无奖励模型的方法，而 ChatGPT、Claude 用的是奖励模型加 PPO；DPO 是否真的更好，PPO 为什么在学术 benchmark 上表现差。
- **核心方法**：理论上证明 PPO 能找到的解 DPO 也能找到，而 DPO 还可能找到偏向分布外回答、偏离参考策略的解（定理 4.1）；实验显示 DPO 的效果明显受模型输出与偏好数据之间分布偏移的影响，先在偏好数据上补做 SFT 能缓解。消融找出 PPO 的关键因素：优势归一化、大批量、参考模型的指数滑动平均更新。在对话（HH-RLHF、SafeRLHF）和代码竞赛（APPS、CodeContest）上，PPO 超过 DPO 等方法。
- **为什么在这个库里**：后训练总览"DPO 的分布外问题"一条的主要证据，[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)"优化器 = 离线还是在线"一格。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2404.10719 · [全文 PDF](https://arxiv.org/pdf/2404.10719) · 清华大学、OpenPsi、上海期智研究院
- 方向：llm/posttraining/preferences、llm/posttraining/rl
