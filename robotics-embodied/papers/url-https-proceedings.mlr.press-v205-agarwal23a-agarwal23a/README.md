# Legged Locomotion in Challenging Terrains using Egocentric Vision

> 状态：文献卡 · 2023 · [原文](https://proceedings.mlr.press/v205/agarwal23a.html)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：传统视觉腿足运动分两步：先建高程图，再规划落脚点；高程图容易失败、噪声大，还需要专门硬件。
- **核心方法**：第一个只用一个前向深度相机、端到端走楼梯、路沿、踏石和间隙的四足系统（A1）。训练分两阶段：先用机身下方的扫描点（scandots，一句话：在机器人坐标系里若干固定位置查询到的地形高度）代替深度图做 RL，再用 DAgger（一句话：让学生策略自己跑、由教师策略给它访问到的状态打动作标签的模仿学习）监督蒸馏成直接吃深度图的策略；相机看不到后腿下方，策略用循环网络记住过去的画面。其中一种架构沿用 [RMA](../rma/README.md) 的"基础策略 + 环境隐变量"结构。作者自述：仿真与真实在视觉或地形上不匹配时会失败，现有范式下只能把该情况补进仿真再训练。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向"外部感知怎样进入策略"一格的深度端到端代表；在[四足故障后恢复笔记](../../../perspectives/notes/quadruped-recovery.md)里属于"加维度"一类。优先级：选读。

## 身份信息

- 稳定标识：url:https://proceedings.mlr.press/v205/agarwal23a/agarwal23a.pdf（Agarwal、Kumar、Malik、Pathak；第 6 届 CoRL 论文集 PMLR 205:403–415，2023 年出版；arXiv:2211.07638 注明为 CoRL 2022 口头报告）
- 全文：[PMLR PDF](https://proceedings.mlr.press/v205/agarwal23a/agarwal23a.pdf) · 项目页：[vision-locomotion.github.io](https://vision-locomotion.github.io)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
