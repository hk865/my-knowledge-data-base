# 跨方向方法与探索

[回到全库](../README.md) · [基础概念](../foundations/README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文与资源](PAPERS.md)

## 按细分方向学习

- [训练科学](fields/training-science/README.md)：优化地形、规模定律、双下降、本征维度、遗忘
- [模型科学](fields/model-science/README.md)：表示与知识存放在哪里、注意力与 FFN 的分工、电路、探针与干预、事实回忆与编辑；入门、baseline、路线图、论文各有入口（原"机制与可信解释"已并入）
- [Agent](fields/agents/README.md)：从提示词搭的 agent 到在后训练里训练 agent 能力；agent 评测就是 RL 环境，环境奖励什么，模型就长成什么样
- [评估](fields/evaluation/README.md)：评测本身是什么、为什么会失效（污染、饱和、裁判偏差、排行榜），以及"评测即目标"——能自动打分的评测怎样变成奖励和 RL 环境；[分任务能力图](fields/evaluation/domains.md)按代码、科研、医疗、法律、金融、角色扮演、安全等领域对照
- [知识蒸馏](fields/knowledge-distillation/README.md)：入门、baseline、路线图、论文各有入口

## 单篇论文目录

本领域收录 72 项资源，其中 2 篇有讲解；其他方向的相关论文通过索引交叉引用。

- [浏览本领域论文与跨方向引用](PAPERS.md)
- [直接浏览单篇文件夹](papers/README.md)

每篇论文的文件夹含文献卡README与source.json；有讲解的论文另含reading.md。

## 阅读状态标记

- 技术精读：按指定论文版本写的完整讲解
- 逐步教学版：在技术精读基础上补充逐步说明与算例
- 选定章节讲解：只讲论文中明确列出的章节
- 文献卡：论文身份、官方原文入口与定位
