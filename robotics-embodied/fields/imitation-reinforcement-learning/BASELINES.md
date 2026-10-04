# 模仿学习与机器人强化学习的基线

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md) · [综合表](synthesis.csv)

## 基线是谁、为什么是它

| 基线 | 定义了什么 | 为什么是它 |
|---|---|---|
| 行为克隆，及其修正 [DAgger](../../papers/arxiv-1011.0686/README.md)（2011） | 接口：观测 → 动作；训练：在示范的 (观测, 动作) 对上做监督学习；DAgger 把数据来源换成策略自己到达的状态；评估：任务成功率与代价界 | 复合误差的定理（T²ε 对 uTε）出自这里，后来所有"纠正"类方法都在它的框架内 |
| [Diffusion Policy](../../papers/diffusion-policy/reading.md)（2023） | 接口：最近 2 帧观测 → 未来 16 步动作，执行其中 8 步再重新观测；训练：对动作序列加噪、学习去噪；评估：RoboMimic、Push-T 等仿真成功率 + 真机 | 视觉动作模仿的公认基线，同时处理多峰与时间一致性；DPPO、π0 的微调实验都拿它作对照 |
| [PPO](../../../llm/papers/ppo/reading.md)（2017） | 接口：状态 → 动作分布；训练：裁剪概率比的同策略策略梯度 + GAE 优势；评估：回报 | 机器人仿真 RL 与 LLM 后训练的共同默认算法；RL 微调工作要么在它上面改（DPPO），要么拿它作对照（π*0.6） |

## 基线的结构拆分

1. **数据来源**：遥操作示范、动作捕捉与动画（只有状态的运动学示范）、仿真专家（特权教师、脚本、规划器）、人工纠正、策略的自主执行。
2. **动作表示**：单步回归、动作块、多峰分布（扩散、CVAE、flow matching）、离散 token。
3. **训练目标**：监督回归、去噪、策略梯度、优势加权或优势条件化。
4. **分布纠正**：DAgger 式查询、人工接管、从失败状态起步。
5. **条件与上下文**：语言指令、目标图像、示范作为提示。
6. **奖励来源**：仿真中可编程的奖励、二分类奖励模型、人工成功标签、价值函数。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 分布纠正 | 在策略自己的状态上向专家查询并聚合数据 | [DAgger](../../papers/arxiv-1011.0686/README.md) | 代价界从 T²ε 降到 uTε / 专家必须随时可查询 |
| 分布纠正 + 数据来源 | 仿真里的 RL 特权教师作为 DAgger 的专家 | [Lee 2020](../../papers/arxiv-2010.11251/README.md)、[Miki 2022](../../papers/arxiv-2201.08117/README.md)、[Lee 2019](../../papers/arxiv-1901.07517/README.md) | 专家可无限查询，学生只用真机传感器 / 蒸馏丢信息（Robot Parkour 攀爬 95% → 86%） |
| 分布纠正 + 数据来源 | 稀疏输入的人形学生按 DAgger 模仿全身特权教师 | [OmniH2O](../../papers/arxiv-2406.08858/README.md) | 带长历史的学生 94.10%，同一学生直接 RL 47.11% / 依赖根部里程计 |
| 数据来源 + 训练目标 | 动作捕捉或动画的状态序列作为跟踪奖励或判别器风格奖励，用 RL 优化 | [DeepMimic](../../papers/arxiv-1804.02717/README.md)、[AMP](../../papers/arxiv-2104.02180/README.md)、[Escontrela 2022](../../papers/arxiv-2203.15103/README.md)、[ExBody](../../papers/arxiv-2402.16796/README.md) | 不需要关节力矩示范，给探索一个起点、代替手调风格项 / 数据之外的行为做不好；对抗训练不稳 |
| 数据来源 | 用特权模仿器筛掉机器人做不到的人体动作 | [H2O](../../papers/arxiv-2403.04436/README.md) | 约 1 万段留 8.5k，成功率 67.9% → 72.5% / 没有系统判断可行性的算法 |
| 训练目标 | 模仿真狗动作后，真机上在隐变量空间用 RL 适应 | [Peng 2020](../../papers/arxiv-2004.00784/README.md) | 约 50 次真机试验完成适应 / 学不会大跳与奔跑 |
| 动作表示 | 动作块 + 时间集成 + CVAE | [ACT](../../papers/arxiv-2304.13705/README.md) | 不分块 1% → 分块 44%，不需要在线专家 / 低对比度、细小物体上失败（穿扎带 20%） |
| 动作表示 | 用扩散模型表示动作序列分布 | [Diffusion Policy](../../papers/diffusion-policy/reading.md) | 处理多峰，真机 Push-T 19/20 / 推理需多步去噪，示范不足时欠佳 |
| 动作表示 | 底座换成视觉语言模型，动作用 flow matching 生成 | [π0](../../papers/arxiv-2410.24164/README.md)；同类见 [VLA 方向](../vla/BASELINES.md) | 1 万小时跨机器人数据，可微调到新任务 / 数据配比不清楚 |
| 数据来源 | 13 台机器人、17 个月的真实示范 | [RT-1](../../papers/arxiv-2212.06817/README.md) | 未见指令 76% / 不能泛化到全新动作，跨机器人 0% |
| 数据来源 | 22 种机器人、60 个数据集汇总 | [Open X-Embodiment](../../papers/arxiv-2310.08864/README.md) | 小数据域上正迁移 / 大数据域上 RT-1-X 欠拟合 |
| 数据来源 | 在 80 万条跨机器人轨迹上训练开放的通用策略 | [Octo](../../papers/arxiv-2405.12213/README.md) | 约 100 条示范即可适配新平台 / 腕部相机处理差 |
| 数据来源 | 人类视频作为上下文提示 | [Zero-WAM](../../papers/zero-wam/README.md) | RoboTwin 未见任务高于最强基线 29.5 个百分点 / 只在静态桌面场景 |
| 条件与上下文 | 推理时把示范轨迹当作提示，不更新权重 | [ICRT](../../papers/arxiv-2408.15980/README.md)、[Behavior Prompting Policy](../../papers/arxiv-2606.30457/README.md) | 新任务一条示范即可执行 / 不能适配全新的动作基元 |
| 条件与上下文 | 测试时训练层把长历史压进快权重 | [RoboTTT](../../papers/arxiv-2607.15275/README.md) | 上下文 8K 步，延迟不增长 / 训练成本增加 |
| 训练目标 | 把去噪链作为内层 MDP，用 PPO 微调扩散策略 | [DPPO](../../papers/arxiv-2409.00588/README.md) | 像素 Transport 0% → 50% 以上，零样本上真机 16/20 / 样本效率低于离策略方法 |
| 训练目标 + 奖励来源 | 真机离策略 RL + 示范 + 人工纠正 + 奖励分类器 | [HIL-SERL](../../papers/arxiv-2410.21845/README.md) | 同等人类数据成功率 100% 对 49.7% / 每任务从零训练，长时域未知 |
| 训练目标 + 奖励来源 | 0/1 结果奖励 + GRPO 微调 VLA | [SimpleVLA-RL](../../papers/arxiv-2509.09674/README.md) | 单示范 LIBERO-Long 17.3% → 91.7% / 基座零能力时无效；出现示范外行为 |
| 训练目标 + 奖励来源 | 价值函数算优势，作为策略的条件输入；人工成功标签 | [π*0.6](../../papers/arxiv-2511.14759/README.md) | 吞吐量翻倍以上 / 依赖人工标签、介入与重置 |
| 训练目标 | 裁剪概率比（基线本身） | [PPO](../../../llm/papers/ppo/reading.md) | 一阶优化即可稳定多轮更新 / 不管探索；超参敏感 |
| 训练分布 | 按 TD 误差优先回放经验或选关卡 | [Prioritized Experience Replay](../../papers/arxiv-1511.05952/README.md)、[Prioritized Level Replay](../../papers/arxiv-2010.03934/README.md) | 把更新集中到预测误差大的地方 / 前者针对离策略回放，后者依赖程序化关卡 |
| 系统结构 | 任务策略与恢复策略分开 | [Recovery RL](../../papers/arxiv-2010.15920/README.md) | 约束违反更少 / 安全评论家的质量是瓶颈 |
| 训练目标 | 风险敏感的分布式价值 | [RALL](../../papers/arxiv-2308.09405/README.md)、[DPPO（风险）](../../papers/arxiv-2309.14246/README.md) | 部署时可调风险偏好 / 超出能力时只会拒绝 |
| （参照）世界模型 | 在学到的潜在动力学中想象训练 | [DreamerV3](../../../multimodal/papers/dreamerv3/reading.md)、[潜空间选择](../../../multimodal/papers/arxiv-2605.06388/README.md) | 用模型代替真实交互 / 模型误差与多步预测偏差 |
| （参照）生成机制与 LLM 后训练 | 扩散生成、视觉指令微调、RLHF、可验证奖励 RL | [DDPM](../../../multimodal/papers/ddpm/README.md)、[LLaVA](../../../multimodal/papers/llava/README.md)、[InstructGPT](../../../llm/papers/instructgpt/README.md)、[DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) | 本方向借用的机制来源；DeepSeek-V2/V3、Qwen2.5 技术报告只作交叉引用 |
| （参照）专家来源 | 模型控制器作为示范来源 | [Convex MPC](../../papers/convex-mpc/reading.md) | 讲义第 8 节讨论过用 MPC 生成示范；接口要与学生一致 |
| 训练目标（2026 年补充） | 冻结 VLA，在压缩出的 RL token 上在线训练小 actor-critic，修正动作块并正则到 VLA 动作附近 | [RL Token](../../papers/arxiv-2604.23073/README.md) | 每任务几小时真机数据，精密阶段提速最高约 3 倍 / 奖励、干预与切换仍靠人 |
| 数据（2026 年补充） | 第一视角人类视频经姿态估计转成动作，作为模仿的主数据源 | [EgoScale](../../papers/arxiv-2602.16710/README.md) | 2 万小时、对数线性尺度律，灵巧手成功率 +54% / 需要人-机对齐数据；尺度律不外推 |
| 数据（2025 年补充） | 人形全身的 VR 遥操作示范，扩散 Transformer 输出手、躯干和脚的位姿，下层 MPC | [Atlas 大行为模型](../../papers/boston-dynamics-atlas-lbm/README.md) | 边走边操作的长任务，推理时可提速 1.5–2 倍 / 没有量化对比，RL 留作后续 |

## 批注

**易误读**

- Diffusion Policy 的"2 帧观测、16 步预测、执行 8 步"是多数任务的设置，不同任务的观测和执行长度不同（精读第五节）。
- DPPO 有两篇同名缩写：本表"训练目标"一行的 [DPPO](../../papers/arxiv-2409.00588/README.md) 是 Diffusion Policy Policy Optimization；风险一行的 [DPPO](../../papers/arxiv-2309.14246/README.md) 是 Schneider 等的 Distributional PPO。
- 腿足的教师-学生在这里归到"分布纠正"，在[运动控制的基线表](../control-locomotion/BASELINES.md)里归到"观测"，两种归类回答的问题不同。
- 动作捕捉一行的"示范"只有状态、没有动作，用的是 RL 加跟踪或风格奖励，不是行为克隆；AMP 的判别器只看状态转移（AMP §5.1）。

**与其他论文的关联**

- VLA 的模型结构（离散 token、flow matching、动作 tokenizer）在 [VLA 方向的基线表](../vla/BASELINES.md)，本表只列它们作为模仿学习数据与动作表示的一面。
- 各格的失败场景与"站在现在看过去"在[入门页](README.md)的主线历史一节。
