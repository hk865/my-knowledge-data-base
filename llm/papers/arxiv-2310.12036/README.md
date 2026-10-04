# A General Theoretical Paradigm to Understand Learning from Human Preferences

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.12036)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：RLHF 与 DPO 都依赖"成对偏好可以换成逐点奖励（Bradley–Terry 模型）"这个近似，它在什么情况下出问题。
- **核心方法**：提出统一目标 ΨPO，指出当偏好是确定性或接近确定性时（有限数据下很常见，例如某对回答只被比较过一次），DPO 的最优解会把较差回答的概率压到 0，KL 正则形同虚设，从而过拟合偏好数据；标准 RLHF 因为奖励模型本身欠拟合，反而保留了对参考策略的正则。取 Ψ 为恒等函数得到 IPO，避免这一过拟合（§4.2）。
- **为什么在这个库里**：[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)"损失形式"一格；DPO 过拟合与分布外问题的理论一侧，实验一侧见 Xu 等（2024）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2310.12036 · [全文 PDF](https://arxiv.org/pdf/2310.12036) · Google DeepMind
- 方向：llm/posttraining/preferences
