# 运动控制与腿足运动：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [综合表](synthesis.csv)

按[入门页](README.md)的主线分组。每项链接到唯一的单篇目录；跨方向出现的论文是交叉引用，不重复计数。每组内按年份排列。

## 模型控制

- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](../../papers/convex-mpc/README.md) · 2018 · 技术精读 · 模型控制的基线：单刚体 + 预定接触时序 → 凸 QP
- [DTC: Deep Tracking Control](../../papers/arxiv-2309.15462/README.md) · 2024 · 文献卡 · 轨迹优化给落脚点，RL 策略负责跟踪：模型与学习的混合

## 从仿真到真机的学习型运控（本体感知）

- [Learning agile and dynamic motor skills for legged robots](../../papers/arxiv-1901.08652/README.md) · 2019 · 文献卡 · 执行器网络缩小 sim-to-real 差距，ANYmal 上第一批 RL 实机策略
- [Learning Quadrupedal Locomotion over Challenging Terrain](../../papers/arxiv-2010.11251/README.md) · 2020 · 文献卡 · 特权教师 → 本体感知历史学生，野外零样本
- [RMA: Rapid Motor Adaptation for Legged Robots](../../papers/rma/README.md) · 2021 · 技术精读 · 从 50 步历史估计环境隐变量，部署时不更新权重
- [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](../../papers/arxiv-2109.11978/README.md) · 2021 · 文献卡 · GPU 上数千台并行，训练从天缩短到分钟
- [Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](../../papers/url-https-proceedings.mlr.press-v205-margolis23a-margolis23a/README.md) · 2022 · 文献卡 · 一个策略学一族行为参数，部署时由人切换以应对分布外

## 感知运控与跑酷

- [Learning robust perceptive locomotion for quadrupedal robots in the wild](../../papers/arxiv-2201.08117/README.md) · 2022 · 文献卡 · 高程图与本体感知的置信融合
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md) · 2022 · 文献卡 · 单个前向深度相机端到端，靠记忆补看不见的后腿下方
- [Robot Parkour Learning](../../papers/arxiv-2309.05665/README.md) · 2023 · 文献卡 · 允许穿透的软约束预训练 + 多技能蒸馏
- [Extreme Parkour with Legged Robots](../../papers/arxiv-2309.14341/README.md) · 2023 · 文献卡 · 统一的朝向内积奖励，低成本 A1 上的极限跳跃
- [PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots](../../papers/arxiv-2408.13740/README.md) · 2024 · 文献卡 · 单阶段训练的跑酷，隐式与显式地形估计并用
- [Attention-Based Map Encoding for Learning Generalized Legged Locomotion](../../papers/arxiv-2506.09588/README.md) · 2025 · 文献卡 · 以本体感知为查询的注意力地图编码，面向稀疏落脚地形
- [Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](../../papers/arxiv-2601.08485/README.md) · 2026 · 文献卡 · 加入带不确定性的神经建图与目标到达，四足与双足
- [MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion](../../papers/doi-10.1002-advs.202524345/README.md) · 2026 · 文献卡 · 对比式深度模型与深度去噪，单阶段训练（只核实了元数据）

## 恢复、鲁棒与约束

与[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)思考笔记的四类解法对应。

- [Robust Recovery Controller for a Quadrupedal Robot using Deep Reinforcement Learning](../../papers/arxiv-1901.07517/README.md) · 2019 · 文献卡 · 倒地起身：三个行为策略 + 选择器
- [Recovery RL: Safe Reinforcement Learning With Learned Recovery Zones](../../papers/arxiv-2010.15920/README.md) · 2021 · 文献卡 · 任务策略与恢复策略分开（非腿足）
- [Prioritized Level Replay](../../papers/arxiv-2010.03934/README.md) · 2020 · 文献卡 · 按学习潜力选训练关卡（Procgen）
- [Robust Quadrupedal Locomotion via Risk-Averse Policy Learning](../../papers/arxiv-2308.09405/README.md) · 2023 · 文献卡 · 分布式价值 + 风险扭曲度量
- [Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning](../../papers/arxiv-2309.14246/README.md) · 2023 · 文献卡 · 风险敏感的 PPO（DPPO），可调风险偏好
- [CaT: Constraints as Terminations for Legged Locomotion Reinforcement Learning](../../papers/arxiv-2403.18765/README.md) · 2024 · 文献卡 · 约束写成按违反程度截断回报的随机终止
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](../../papers/arxiv-2405.12424/README.md) · 2024 · 文献卡 · 用对抗策略搜长尾失败，再微调修补

## 步态先验与节律

- [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](../../papers/arxiv-2011.01387/README.md) · 2020 · 文献卡 · 用周期性奖励组合指定双足步态
- [Learning Free Gait Transition for Quadruped Robots via Phase-Guided Controller](../../papers/arxiv-2201.00206/README.md) · 2022 · 文献卡 · 相位引导的步态切换
- [CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion](../../papers/arxiv-2211.00458/README.md) · 2022 · 文献卡 · 策略输出 CPG 振荡器参数而非关节目标
- [Learning Quadruped Locomotion using Bio-Inspired Neural Networks with Intrinsic Rhythmicity](../../papers/arxiv-2305.07300/README.md) · 2023 · 文献卡 · 网络自带节律

## 动作模仿：参考动作、风格先验与人形重定向

与[入门页](README.md#为什么绕不开模仿学习)"为什么绕不开模仿学习"一节对应。

- [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../../papers/arxiv-1804.02717/README.md) · 2018 · 文献卡 · 用 RL 跟踪参考动作（仿真角色）；去掉参考状态初始化学不会空翻
- [Learning Agile Robotic Locomotion Skills by Imitating Animals](../../papers/arxiv-2004.00784/README.md) · 2020 · 文献卡 · 四足模仿真狗动作捕捉，真机上在隐变量空间用 RL 适应
- [AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](../../papers/arxiv-2104.02180/README.md) · 2021 · 文献卡 · 判别器风格奖励代替逐帧跟踪
- [ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](../../papers/arxiv-2205.01906/README.md) · 2022 · 文献卡 · 对抗式技能嵌入，模仿预训练低层技能、RL 训高层
- [Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions](../../papers/arxiv-2203.15103/README.md) · 2022 · 文献卡 · AMP 搬上 A1，替代 13 项手调风格惩罚
- [Expressive Whole-Body Control for Humanoid Robots](../../papers/arxiv-2402.16796/README.md) · 2024 · 文献卡 · ExBody：上半身模仿动作捕捉，腿只跟根部运动命令
- [Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](../../papers/arxiv-2403.04436/README.md) · 2024 · 文献卡 · H2O：用特权模仿器筛掉人形做不到的人体动作
- [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](../../papers/arxiv-2406.08858/README.md) · 2024 · 文献卡 · 稀疏输入学生按 DAgger 模仿特权教师，比直接 RL 高约 47 个百分点

## 人形与全身控制（运动跟踪）

- [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](../../papers/arxiv-2404.05695/README.md) · 2024 · 文献卡 · 人形 RL 训练框架与 sim-to-sim 验证
- [ExBody2: Advanced Expressive Humanoid Whole-Body Control](../../papers/arxiv-2412.13196/README.md) · 2024 · 文献卡 · 表现力全身动作跟踪
- [Learning from Massive Human Videos for Universal Humanoid Pose Control](../../papers/arxiv-2412.14172/README.md) · 2024 · 文献卡 · 从人类视频得到大规模姿态数据
- [Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning](../../papers/arxiv-2501.02116/README.md) · 2025 · 文献卡 · 综述
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](../../papers/arxiv-2503.14734/README.md) · 2025 · 文献卡 · 人形通用 VLA，只做桌面双臂操作（交叉引用 VLA）
- [A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots](../../papers/arxiv-2506.20487/README.md) · 2025 · 文献卡 · 综述
- [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](../../papers/arxiv-2508.08241/README.md) · 2025 · 文献卡 · 动作跟踪 + 引导扩散
- [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](../../papers/arxiv-2510.02252/README.md) · 2025 · 文献卡 · 重定向质量对跟踪的影响
- [Scaling Behavior Foundation Model for Humanoid Robots](../../papers/arxiv-2607.15163/README.md) · 2026 · 文献卡 · 行为基础模型的规模化

## 跨方向的工具与算法（交叉引用）

- [Proximal Policy Optimization Algorithms](../../../llm/papers/ppo/README.md) · 2017 · 技术精读 · 腿足 RL 的默认优化器
- [Quaternion kinematics for the error-state Kalman filter](../../papers/eskf/README.md) · 2017 · 技术精读 · 机身状态估计的数学基础
- [Sampling-based Algorithms for Optimal Motion Planning](../../papers/rrt-star/README.md) · 2011 · 技术精读 · 几何路径规划，与本方向的力规划分层
- [Prioritized Experience Replay](../../papers/arxiv-1511.05952/README.md) · 2016 · 文献卡 · 按 TD 误差排优先级
- [First return, then explore](../../papers/arxiv-2004.12919/README.md) · 2021 · 文献卡 · Go-Explore：先回到罕见状态再探索
- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](../../papers/fastrlap/README.md) · 2023 · 文献卡 · 轮式平台上的真机自主练习与自动重置

## 工业界官方材料（外部链接，不建卡）

对照见[入门页的工业界方案](README.md#工业界方案成熟在哪里没公开什么)。

- [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) · Unitree 官方仓库 · 训练 → 回放 → Sim2Sim → Sim2Real 的完整流水线；另有 [unitree_rl_lab](https://github.com/unitreerobotics/unitree_rl_lab)（Isaac Lab）
- [Isaac Gym](https://arxiv.org/abs/2108.10470) · 2021 · NVIDIA 论文 · GPU 上的物理仿真与策略训练
- [Isaac Lab](https://arxiv.org/abs/2511.04831) · 2025 · NVIDIA 论文 · 执行器模型、随机化事件与多种腿足机器人的训练环境
- [Eureka](https://arxiv.org/abs/2310.12931) · 2023 · 论文（NVIDIA 等）· 大语言模型写奖励
- [DrEureka](https://arxiv.org/abs/2406.01967) · 2024 · 论文（UPenn、NVIDIA 等）· 大语言模型写奖励与域随机化范围，Go1 上真机
- [Starting on the Right Foot with Reinforcement Learning](https://bostondynamics.com/blog/starting-on-the-right-foot-with-reinforcement-learning/) · Boston Dynamics 官方博客 · Spot 的 RL 策略与 MPC 配合、车队验证与上线
- [Superior Robot Mobility – Where AI Meets the Real World](https://www.anybotics.com/news/superior-robot-mobility-where-ai-meets-the-real-world/) · 2023 · ANYbotics 官方新闻 · ANYmal 的 RL 运动控制产品化
- [Training a Whole-Body Control Foundation Model](https://www.agilityrobotics.com/content/training-a-whole-body-control-foundation-model) · 2025 · Agility Robotics 官方博客 · Digit 的全身控制模型
- [Design and Control of a Bipedal Robotic Character](https://arxiv.org/abs/2501.05204) · 2025 · Disney Research 论文 · 动画参考 + 模仿奖励，执行器辨识
