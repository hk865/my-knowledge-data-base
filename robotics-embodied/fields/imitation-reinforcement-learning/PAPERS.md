# 模仿学习与机器人强化学习：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [综合表](synthesis.csv)

按[入门页](README.md)的主线分组。每项链接到唯一的单篇目录；跨方向出现的论文是交叉引用，不重复计数。

## 行为克隆与分布偏移

- [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](../../papers/arxiv-1011.0686/README.md) · 2011 · 文献卡 · DAgger：在策略自己到达的状态上向专家要标签
- [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](../../papers/arxiv-2304.13705/README.md) · 2023 · 文献卡 · ACT：动作分块与时间集成，缓解复合误差
- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../../papers/diffusion-policy/README.md) · 2023 · 技术精读 · 用扩散模型表示多峰动作分布

## 强化学习算法

- [Proximal Policy Optimization Algorithms](../../../llm/papers/ppo/README.md) · 2017 · 技术精读 · 机器人与 LLM 共用的同策略算法基线
- [Prioritized Experience Replay](../../papers/arxiv-1511.05952/README.md) · 2016 · 文献卡 · 离策略回放的优先级
- [Prioritized Level Replay](../../papers/arxiv-2010.03934/README.md) · 2020 · 文献卡 · 按学习潜力选训练关卡
- [Recovery RL: Safe Reinforcement Learning With Learned Recovery Zones](../../papers/arxiv-2010.15920/README.md) · 2021 · 文献卡 · 任务与恢复双策略

## 仿真 RL + 特权蒸馏（腿足中模仿与强化的组合）

- [Learning Quadrupedal Locomotion over Challenging Terrain](../../papers/arxiv-2010.11251/README.md) · 2020 · 文献卡 · RL 训练特权教师，模仿学习蒸馏到可部署的学生
- [Robust Recovery Controller for a Quadrupedal Robot using Deep Reinforcement Learning](../../papers/arxiv-1901.07517/README.md) · 2019 · 文献卡 · 分层恢复控制
- [Learning robust perceptive locomotion for quadrupedal robots in the wild](../../papers/arxiv-2201.08117/README.md) · 2022 · 文献卡 · 教师-学生 + 外部感知
- [Robust Quadrupedal Locomotion via Risk-Averse Policy Learning](../../papers/arxiv-2308.09405/README.md) · 2023 · 文献卡 · 风险规避
- [Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning](../../papers/arxiv-2309.14246/README.md) · 2023 · 文献卡 · 风险敏感 PPO

- [OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning](../../papers/arxiv-2406.08858/README.md) · 2024 · 文献卡 · 人形学生按 DAgger 模仿特权教师（交叉引用运动控制）

更多腿足论文见[运动控制方向](../control-locomotion/PAPERS.md)。

## 运动控制中的动作模仿（交叉引用）

只有状态、没有动作的示范（动作捕捉、动画、人体视频），用作 RL 的跟踪目标或风格奖励。详见[运动控制方向](../control-locomotion/README.md#为什么绕不开模仿学习)。

- [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](../../papers/arxiv-1804.02717/README.md) · 2018 · 文献卡 · 跟踪参考动作 + 参考状态初始化
- [Learning Agile Robotic Locomotion Skills by Imitating Animals](../../papers/arxiv-2004.00784/README.md) · 2020 · 文献卡 · 四足模仿真狗，真机上用 RL 适应
- [AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control](../../papers/arxiv-2104.02180/README.md) · 2021 · 文献卡 · 判别器风格奖励
- [Adversarial Motion Priors Make Good Substitutes for Complex Reward Functions](../../papers/arxiv-2203.15103/README.md) · 2022 · 文献卡 · AMP 用于四足 A1
- [Expressive Whole-Body Control for Humanoid Robots](../../papers/arxiv-2402.16796/README.md) · 2024 · 文献卡 · ExBody：上半身模仿动作捕捉
- [Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation](../../papers/arxiv-2403.04436/README.md) · 2024 · 文献卡 · H2O：筛掉人形做不到的动作

## 大规模模仿（真实示范）

- [RT-1: Robotics Transformer for Real-World Control at Scale](../../papers/arxiv-2212.06817/README.md) · 2022 · 文献卡 · 13 万条真实示范上的 Transformer 策略
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../../papers/arxiv-2310.08864/README.md) · 2023 · 文献卡 · 跨机器人的示范数据合集
- [Octo: An Open-Source Generalist Robot Policy](../../papers/arxiv-2405.12213/README.md) · 2024 · 文献卡 · 开放的通用策略，扩散动作头
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../../papers/arxiv-2307.15818/README.md) · 2023 · 文献卡 · 交叉引用 VLA
- [OpenVLA: An Open-Source Vision-Language-Action Model](../../papers/openvla/README.md) · 2024 · 技术精读 · 交叉引用 VLA
- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](../../papers/arxiv-2410.24164/README.md) · 2024 · 文献卡 · 交叉引用 VLA
- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](../../papers/arxiv-2501.09747/README.md) · 2025 · 文献卡 · 交叉引用 VLA
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](../../papers/arxiv-2502.19645/README.md) · 2025 · 文献卡 · 交叉引用 VLA
- [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](../../papers/arxiv-2504.16054/README.md) · 2025 · 文献卡 · 交叉引用 VLA
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](../../papers/arxiv-2506.01844/README.md) · 2025 · 文献卡 · 交叉引用 VLA
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](../../papers/arxiv-2505.22159/README.md) · 2025 · 文献卡 · 交叉引用 VLA
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](../../papers/arxiv-2601.02456/README.md) · 2026 · 文献卡 · 交叉引用 VLA
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../../papers/arxiv-2604.15483/README.md) · 2026 · 文献卡 · 交叉引用 VLA
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](../../papers/arxiv-2605.30280/README.md) · 2026 · 文献卡 · 交叉引用 VLA
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](../../papers/arxiv-2606.14752/README.md) · 2026 · 文献卡 · 交叉引用 VLA

## 上下文模仿（示范作为提示）

- [In-Context Imitation Learning via Next-Token Prediction](../../papers/arxiv-2408.15980/README.md) · 2024 · 文献卡 · 推理时给几条示范，不更新权重
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](../../papers/arxiv-2606.30457/README.md) · 2026 · 文献卡 · 示范作为提示
- [RoboTTT: Context Scaling for Robot Policies](../../papers/arxiv-2607.15275/README.md) · 2026 · 文献卡 · 扩大策略的上下文
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../../papers/zero-wam/README.md) · 2026 · 选定章节讲解 · 从人类视频做上下文世界-动作建模

## 在模仿之上用强化学习微调

- [Diffusion Policy Policy Optimization](../../papers/arxiv-2409.00588/README.md) · 2024 · 文献卡 · DPPO：把扩散去噪链当作 MDP，用 PPO 微调
- [Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](../../papers/arxiv-2410.21845/README.md) · 2024 · 文献卡 · HIL-SERL：示范 + 人工纠正 + 真机离策略 RL
- [π*0.6: a VLA That Learns From Experience](../../papers/arxiv-2511.14759/README.md) · 2025 · 文献卡 · RECAP：优势条件化，把部署经验与纠正喂回 VLA
- [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](../../papers/arxiv-2509.09674/README.md) · 2025 · 文献卡 · 仿真中用结果奖励对 VLA 做 RL
- [RL Token: Bootstrapping Online RL with Vision-Language-Action Models](../../papers/arxiv-2604.23073/README.md) · 2026 · 文献卡 · 冻结 π0.6，在 RL token 上在线训练小 actor-critic

## 2026 年：模仿的数据源变大（人类视频、全身遥操作、动作捕捉）

- [EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data](../../papers/arxiv-2602.16710/README.md) · 2026 · 文献卡 · 2 万小时第一视角人类视频，对数线性尺度律（交叉引用 VLA）
- [Large Behavior Models and Atlas Find New Footing](../../papers/boston-dynamics-atlas-lbm/README.md) · 2025 · 官方博客卡 · Boston Dynamics 与 TRI，人形全身遥操作示范 + 扩散 Transformer
- [SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](../../papers/arxiv-2511.07820/README.md) · 2025 年预印本；Science Robotics 2026 · 文献卡 · 700 小时动作捕捉的通用跟踪器（交叉引用运动控制）
- [Introducing Helix 02: Full-Body Autonomy](../../papers/figure-helix-02/README.md) · 2026 · 官方博客卡 · 人体动作数据 + 仿真 RL 训练的全身控制器（交叉引用运动控制）
- [Learning Agile Perceptive Traversal of Sparse 3D Structures for Humanoids](../../papers/arxiv-2608.29769/README.md) · 2026 · 文献卡 · DAgger 模仿特权教师 → 带行为锚定的 PPO（交叉引用运动控制）

## 世界模型（交叉引用）

- [Mastering Diverse Domains through World Models](../../../multimodal/papers/dreamerv3/README.md) · 2023 · 技术精读 · 在学到的潜在动力学里想象训练
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](../../../multimodal/papers/arxiv-2605.06388/README.md) · 2026 · 文献卡 · 世界模型的潜空间选择

## 生成模型与 LLM 后训练（跨领域对照）

本方向借用的机制来自这里，结论不能直接搬到机器人上。

- [Denoising Diffusion Probabilistic Models](../../../multimodal/papers/ddpm/README.md) · 2020 · 技术精读 · Diffusion Policy 的生成机制来源
- [Visual Instruction Tuning](../../../multimodal/papers/llava/README.md) · 2023 · 技术精读 · VLA 底座的视觉指令微调
- [Training language models to follow instructions with human feedback](../../../llm/papers/instructgpt/README.md) · 2022 · 逐步教学版 · PPO 用于 RLHF
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](../../../llm/papers/arxiv-2501.12948/README.md) · 2025 · 文献卡 · 可验证奖励的 RL（GRPO）
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](../../../llm/papers/deepseek-v2/README.md) · 2024 · 技术精读 · 交叉引用
- [DeepSeek-V3 Technical Report](../../../llm/papers/arxiv-2412.19437/README.md) · 2024 · 文献卡 · 交叉引用
- [Qwen2.5 Technical Report](../../../llm/papers/arxiv-2412.15115/README.md) · 2024 · 文献卡 · 交叉引用
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](../../papers/convex-mpc/README.md) · 2018 · 技术精读 · 模型控制对照，可作为模仿学习的专家来源

## 后续问题与近期方法

- [Generate, Track, Improve：用 RL 改进流匹配运动生成器](../../papers/arxiv-2609.31577/README.md) · 2026 · 文献卡
