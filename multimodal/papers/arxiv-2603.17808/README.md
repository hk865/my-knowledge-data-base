# EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2603.17808)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：用视频生成模型当机器人世界模型时，先生成未来画面，再用逆动力学模型（IDM：从相邻画面反推动作的模型）解出动作；但视觉上连贯的视频可能违反刚体与运动学一致性，解出的动作不稳定或不可执行，作者称之为"可执行性缺口"。拒绝采样这类推理时补救因视频生成昂贵而低效。
- **核心方法**：把这个缺口当作训练信号：在真实机器人轨迹上训练 IDM，冻结后当奖励模型，生成视频解出的动作序列越平滑（速度、加速度、急动度小）、越不违反本体约束，奖励越高；即便画面有严重伪影，奖励仍有区分度，因为伪影通常会变成不稳定或越界的动作。用 GRPO（按同一提示下一组样本的相对得分更新的策略梯度方法）以 LoRA 后训练视频生成器（从 Large Video Planner 检查点初始化并做监督微调）。RoboTwin 2.0 的 21 个双臂任务平均成功率从未做强化学习时的 46.2% 提到 52.6%（π0 为 45.7%）；真机已见任务 52% → 64%，分布外任务 42% → 60%，π0 在分布外任务只有 11%（Table 2、3）。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"⑥ 训练信号"一行与入门页第 6 阶段；它说明"画面逼真"和"可执行"是两件事，与 [Cosmos](../arxiv-2501.03575/README.md) 的物理对齐实验、[Hydra-0](../arxiv-2608.18077/README.md) 的动作流接口指向同一个问题。做不好的场景：奖励只管运动学可行与平滑，不建模力、摩擦、力矩等接触动力学，精细接触任务不够；扩散式视频生成太慢，用不到高频的反应式控制（Limitations 段）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2603.17808 · [全文 PDF](https://arxiv.org/pdf/2603.17808) · 香港中文大学（深圳）、DexForce Technology
- 方向：multimodal/world-models、robotics/embodied-policies
