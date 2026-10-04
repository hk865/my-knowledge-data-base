# 机器人与具身系统

[回到全库](../README.md) · [基础概念](../foundations/README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文与资源](PAPERS.md)

## 读者基础

本组8篇领域讲义面向掌握基础深度学习、物理与运动学的读者，从具体问题与前向过程解释变量、公式、训练或优化、算例和边界。讲义正文在各方向对应的.md文件中，方向README汇集baseline、路线图与论文入口。

## 按细分方向学习

八个方向按"从感知到行动"排列。每个方向有入门页（领域地图）、Baseline 页、路线图和论文列表；同名的领域讲义讲机制与算例。

| 方向 | 回答什么 | 入门页 | 讲义 |
|---|---|---|---|
| 机器人感知 | 传感器数据怎样变成可用的检测、分割、深度，满足帧率、延迟与标定约束 | [入门](fields/perception/README.md) | [讲义](fields/perception.md) |
| 定位与建图 | 机器人在哪、周围是什么，滤波、优化到神经地图 | [入门](fields/localization-mapping/README.md) | [讲义](fields/localization-mapping.md) |
| 导航与规划 | 怎样从这里到那里，从经典规划到语言指令导航 | [入门](fields/navigation-planning/README.md) | [讲义](fields/navigation-planning.md) |
| 运动控制与腿足运动 | 怎样让身体按命令稳定地动起来，MPC、sim-to-real、恢复与鲁棒 | [入门](fields/control-locomotion/README.md) | [讲义](fields/control-locomotion.md) |
| 模仿学习与机器人强化学习 | 策略从示范学还是从试错学，各自的坑 | [入门](fields/imitation-reinforcement-learning/README.md) | [讲义](fields/imitation-reinforcement-learning.md) |
| 视觉-语言-动作模型（VLA） | 怎样借预训练的视觉语言模型，让一个策略覆盖很多操作任务 | [入门](fields/vla/README.md) | [讲义](fields/vla.md) |
| 世界模型（机器人侧） | 预测"做了这个动作会怎样"，用来规划、训练策略与评估 | [入门](fields/world-models/README.md) | [讲义](fields/world-models.md) |
| 具身 Agent | 大模型做高层规划、技能执行底层动作，怎样分工 | [入门](fields/embodied-agents/README.md) | [讲义](fields/embodied-agents.md) |

和四足实验直接相关的问题，见思考笔记[四足策略的故障后恢复](../perspectives/notes/quadruped-recovery.md)。

## 单篇论文目录

本领域收录 148 项资源，其中 14 篇有讲解；其他方向的相关论文通过索引交叉引用。

- [浏览本领域论文与跨方向引用](PAPERS.md)
- [直接浏览单篇文件夹](papers/README.md)

每篇论文的文件夹含文献卡README与source.json；有讲解的论文另含reading.md。

## 阅读状态标记

- 技术精读：按指定论文版本写的完整讲解
- 逐步教学版：在技术精读基础上补充逐步说明与算例
- 选定章节讲解：只讲论文中明确列出的章节
- 文献卡：论文身份、官方原文入口与定位

## 保留的机器人专题入口

- [完整领域讲解目录](fields/)
- [专题历史来源与阅读索引](catalog/README.md)
- [具身Agents完整路线图](roadmaps/embodied-agents.md)

原baselines/和papers/2026/路径保留为单篇规范目录入口，避免已有链接失效。
