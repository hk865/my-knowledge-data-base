# PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation

> 状态：文献卡 · 2025 · [原文](https://www.roboticsproceedings.org/rss21/p153.html)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：推、拨这类非抓取操作对摩擦、恢复系数等物理参数高度敏感：模仿学习要昂贵的示范，仿真里做强化学习又有仿真—真实差距。
- **核心方法**：学习三维刚体动力学的物理信息世界模型：以可微物理仿真为骨干，从视觉观测端到端辨识物理参数，观测损失由高斯泼溅渲染给出，不需要单独做状态估计，只要少量、与任务无关的交互轨迹；再在辨识出的参数均值附近扰动物理与渲染参数，生成一组"数字表亲"（physics-aware digital cousins）做域随机化，在其中用 PPO 训练策略并直接部署到真机。真机 Push 与 Flip 任务成功率 75% 与 65%，优于其他 Real2Sim2Real 方法；纯数据驱动的 DreamerV2 学不准目标域的动力学。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"② 动力学"一行：把"系统辨识 + 域随机化"这一机器人学老办法与可微渲染结合，对照纯学习的视频世界模型；入门页把它列为"接触丰富的物理能否预测对"的入口之一。做不好的场景：机器人运动带来的阴影会扭曲渲染损失、影响物理参数的精度；只覆盖刚体，可变形物体要换 MPM 一类物理引擎（结论中的 Limitation 段）。优先级：选读。

## 身份信息

- 稳定标识：doi:10.15607/rss.2025.xxi.153 · [全文 PDF](https://www.roboticsproceedings.org/rss21/p153.pdf) · 国防科技大学、武汉大学、深圳大学、广东省人工智能与数字经济实验室 · RSS 2025 · arXiv 预印本 [2504.16693](https://arxiv.org/abs/2504.16693)
- 方向：multimodal/world-models、robotics/control
