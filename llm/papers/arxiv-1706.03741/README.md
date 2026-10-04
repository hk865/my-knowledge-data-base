# Deep reinforcement learning from human preferences

> 状态：文献卡 · 2017 · [原文](https://arxiv.org/abs/1706.03741)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：很多任务写不出奖励函数；能否只靠人对两段行为的比较训练 RL 智能体，并把人工标注量压到实用范围。
- **核心方法**：一边用人对两段轨迹片段的偏好训练奖励预测器（按 Bradley–Terry 模型，一句话：两者得分之差经 sigmoid 给出"前者更好"的概率），一边用 RL 优化这个预测器，查询与训练交替在线进行；在 Atari 与 MuJoCo 上只需对不到 1% 的交互给反馈，约一小时人工就能教会 Hopper 连续后空翻这类新行为。作者特别指出离线训练奖励预测器（不随策略更新）效果很差：由于策略访问的状态分布在变，预测器只学到部分真实奖励，Pong 上的智能体学会只避免丢分、不去得分，打出极长的来回（§3.3）。
- **为什么在这个库里**：RLHF 的源头，[偏好学习 Baseline 表](../../fields/posttraining/preferences/BASELINES.md)的前史；"奖励模型必须跟着策略分布更新"这个坑的最早记录，后来 Llama 2 每轮重采偏好数据、DPO 被指出的分布外问题都是它的延续。也可以从机器人 RL 的角度读：它本来就是为 MuJoCo 与 Atari 写的。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1706.03741 · [全文 PDF](https://arxiv.org/pdf/1706.03741) · OpenAI、DeepMind
- 方向：llm/posttraining/preferences、llm/posttraining/rl
