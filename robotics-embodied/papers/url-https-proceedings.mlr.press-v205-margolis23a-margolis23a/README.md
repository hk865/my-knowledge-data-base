# Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior

> 状态：文献卡 · 2023 · [原文](https://proceedings.mlr.press/v205/margolis23a.html)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：学到的运动策略在与训练相似的环境里适应很快，但到了分布外环境失败时，没有快速调整的手段，只能改奖励和环境重新训练。
- **核心方法**：多样行为（Multiplicity of Behavior，MoB，一句话：同一个策略额外接收一小组行为参数，对同一指令给出不同走法）：把步频、抬脚高度、站姿宽度、机身姿态等做成可调输入，用 PPO 在 Isaac Gym（NVIDIA 的 GPU 并行物理仿真）中训练（训练框架沿 [Rudin 等 2021](../arxiv-2109.11978/README.md)），部署在 Unitree Go1。遇到新环境时由人实时换一种走法，例如高步频在湿滑地面冲刺、低步频高抬脚上楼梯。作者自述的代价：平地冲刺等分布内性能下降，高线速度与高角速度组合下参数化受限，目前要人手动调。
- **为什么在这个库里**：[运动控制与腿足运动](../../fields/control-locomotion/README.md)方向常用的开源四足控制器参照；在[四足故障后恢复笔记](../../../perspectives/notes/quadruped-recovery.md)里代表"解除限制"一类：失败时换一种走法，而不是重新训练。优先级：必读。

## 身份信息

- 稳定标识：url:https://proceedings.mlr.press/v205/margolis23a/margolis23a.pdf（Margolis、Agrawal；第 6 届 CoRL 论文集 PMLR 205:22–31，2023 年出版；arXiv:2212.03238 注明为 CoRL 2022 口头报告）
- 全文：[PMLR PDF](https://proceedings.mlr.press/v205/margolis23a/margolis23a.pdf) · 代码与视频：[walk-these-ways](https://gmargo11.github.io/walk-these-ways)
- 方向：[运动控制与腿足运动](../../fields/control-locomotion/README.md)
