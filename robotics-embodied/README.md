# 机器人与具身研究库

这里把机器人与具身研究整理成真正的分层目录：领域讲解、baseline正文、近期论文、路线图、结构化索引各有位置。重点专题是具身Agents：一个系统怎样观察、保留记忆、选择任务、调用动作并验证结果。传统感知、定位、规划和运动控制分别保留，不被一个VLA标签代替。

每篇领域讲解可以独立阅读。先用具体问题理解模块职责，再按需要读baseline和近期研究；正文中的必要背景在篇内解释，原文和延伸阅读集中在末尾。

## 从哪个领域进入

- [感知与传感器](fields/perception.md)：像素、深度和惯性读数怎样变成对象与空间信息
- [状态估计与建图](fields/localization-mapping.md)：机器人怎样知道自己在哪里
- [导航与规划](fields/navigation-planning.md)：语义目标怎样成为可执行路线
- [运动控制与腿足运动](fields/control-locomotion.md)：计划怎样变成稳定的物理运动
- [模仿学习与机器人强化学习](fields/imitation-reinforcement-learning.md)：示范和试错分别提供什么信号
- [视觉语言动作模型](fields/vla.md)：图片、语言、机器人状态怎样进入动作预测
- [世界模型](fields/world-models.md)：预测未来怎样帮助行动，潜变量是否具有物理结构
- [具身Agents](fields/embodied-agents.md)：感知、记忆、任务规划、技能调用、执行验证与恢复

## Baseline 长文

正文直接保存在本目录的baselines子目录中，不只是外链清单。以下“技术精读”保留已有公式、实验和证据审计；它们尚未全部改成新的逐步教学风格。阅读状态在索引中逐篇标注。

- [SayCan](baselines/saycan.md)：新增机制教学，先算清语言相关性与技能可行性；核读关键章节，不冒称全部附录精读
- [Diffusion Policy](baselines/diffusion-policy.md)：本轮逐步教学版，动作分布、去噪和闭环执行
- [DreamerV3](baselines/dreamerv3.md)：本轮逐步教学版，真实经验、潜在动力学与想象训练
- [OpenVLA](baselines/openvla.md)：已有技术精读，开放VLA训练与适配
- [ESKF](baselines/eskf.md)：已有技术精读，误差状态与姿态估计
- [ORB-SLAM3](baselines/orb-slam3.md)：已有技术精读，视觉惯性定位与地图
- [RRT*](baselines/rrt-star.md)：已有技术精读，采样规划与渐近最优边界
- [Convex MPC](baselines/convex-mpc.md)：已有技术精读，四足接触力规划；沿用现有公开正文
- [RMA](baselines/rma.md)：已有技术精读，腿足策略适应
- [R2R](baselines/r2r.md)：已有技术精读，视觉语言导航任务与评估
- [PPO](baselines/ppo.md)：已有技术精读，策略更新与稳定性
- [ReAct](baselines/react.md)：已有技术精读，工具反馈与上下文闭环；仿真交互不等于真机控制证据

## 近期论文和历史回收

- [Zero-WAM](papers/2026/zero-wam.md)：用户曾主动提供的论文，优先重新核读；解释人类视频如何指定新任务，以及动作底座和完整Agent的关系
- [RoboSkill](papers/2026/roboskill.md)：2026年9月29日新发现，探索、执行与技能复用
- [EmbodiedSkills](papers/2026/embodiedskills.md)：2026年9月1日新发现，执行前检查与执行后验证
- [MEMORA](papers/2026/memora.md)：2026年8月31日v2，经验记忆与规划；重点区分条件问答成绩、全量指标和真机演示
- [HoloAgent-0](papers/2026/holoagent-0.md)：2026年6月工作，空间记忆与执行系统选读；尚非全部图表审计

这些论文的日期是官方发表或修订日期，检索截至2026年10月2日，不声称穷尽最新研究。文章会说明实际阅读章节和未独立复现的边界。

## 路线图和可下载索引

- [具身Agents研究路线与版本表](roadmaps/embodied-agents.md)
- [论文阅读索引](catalog/README.md)
- [结构化论文JSON](catalog/papers.json)
- [论文CSV](catalog/papers.csv)
- [历史来源证据与未核验名称](catalog/history-recovery.json)
- [专题分类与正交标签](catalog/taxonomy.json)

本轮定向回收20篇历史对话论文，另列15篇旧文件引用；它们不是35篇新精读。原会话链接未取得，来源证据明确标为检索摘要。没有恢复链接的名称保留待核验，不并入已核验论文；助手推荐也不视为用户已选定研究课题。

旧的docs/deep-readings入口保留，避免既有链接失效。专题内的对应正文按同一篇源稿生成，后续更新应一并检查两处；复制到新目录不增加论文计数。全局旧目录和本专题目录的覆盖范围不同，以各自日期与说明为准。
