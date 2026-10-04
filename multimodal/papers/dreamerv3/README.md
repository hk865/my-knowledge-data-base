# Mastering Diverse Domains through World Models

> 状态：逐步教学版精读 · 2023 · [原文](https://arxiv.org/abs/2301.04104)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用学到的模型产生额外经验不是新想法（Dyna、World Models、PlaNet、Dreamer、DreamerV2），卡住的是换一个领域就要重新调参：不同任务的画面、奖励大小与稀疏程度、动作类型差别很大，世界模型、critic 和 actor 各项损失的相对大小随之漂移。论文要回答：能否用一组固定的核心超参，在从机器人控制到 Minecraft 的各类任务上都学得好。
- **核心方法**：沿用 Dreamer 系的三件套：RSSM 世界模型（一句话：确定性的 GRU 记忆加离散随机潜变量，按动作预测下一状态、奖励和是否终止）、在模型里滚动短的想象轨迹训练 actor 与 critic、部署时 actor 直接出动作。相对 DreamerV2 的增量是让各种量的数值尺度不再依赖任务：symlog 变换（保留符号、压缩大数）、two-hot 回归奖励与价值、分母下限为 1 的回报归一化，以及 KL balancing 加 free bits。v1 用一套核心超参在 7 类基准、150 多个任务上各自训练一个智能体；Minecraft 中不用人类数据，40 次训练里 24 次至少一局达到含钻石的最高里程碑（附录 G）。
- **为什么在这个库里**：[机器人世界模型方向的 Baseline 页](../../../robotics-embodied/fields/world-models/BASELINES.md)把它作为"在想象中学策略"的基线，[多模态世界模型 Baseline 页](../../fields/world-models/BASELINES.md)把它列在部件①②（状态表示、动力学）"RSSM 联合训练、固定超参"一行。它每个任务单独训练、需要人写奖励，是理解[世界模型方向](../../fields/world-models/README.md)后来转向视频生成底座的对照。优先级：必读。

## 阅读入口

- [逐步教学版精读](reading.md)：世界模型、想象训练与稳健化技巧；"局限与后续"补了 DayDreamer 真机与 TD-MPC2 的对照
- [本篇图解与说明](figures/README.md)

## 可选的阅读顺序

[Proximal Policy Optimization Algorithms](../../../llm/papers/ppo/README.md) → 本篇。这个顺序是教学建议，不表示论文之间的直接历史继承。

## 原文与许可

- [官方原文页面](https://arxiv.org/abs/2301.04104v1)
- [官方全文PDF](https://arxiv.org/pdf/2301.04104v1)
- [作者归属与许可记录](ATTRIBUTION.md)

本仓库仅提供官方原文链接，没有公开保存论文PDF。版本、许可与阅读深度见 [source.json](source.json)；许可已核验不代表PDF已上传或镜像。

## 身份信息

- 稳定标识：arxiv:2301.04104 · Google DeepMind、多伦多大学
- 年份：2023
- [官方原文页面](https://arxiv.org/abs/2301.04104)
- [官方全文入口](https://arxiv.org/pdf/2301.04104v1)
- 阅读版本：v1
- 方向：multimodal/world-models、robotics/embodied-policies
