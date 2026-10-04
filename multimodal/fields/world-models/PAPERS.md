# 世界模型（多模态侧）：论文与资源

[回到入门](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

以下每项链接到唯一的单篇目录，跨方向出现是交叉引用，不重复计算资源。方括号里是该篇在 [Baseline 表](BASELINES.md)中所改的部件：① 状态表示 ② 动力学与生成过程 ③ 动作接口 ④ 记忆与上下文 ⑤ 数据 ⑥ 评估。

## 基线

- [World Models](../../../robotics-embodied/papers/arxiv-1803.10122/README.md) · 2018 · 文献卡 · 基线
- [Genie: Generative Interactive Environments](../../papers/arxiv-2402.15391/README.md) · 2024 · 文献卡 · 基线

## 潜空间动力学，为控制而学

- [Mastering Diverse Domains through World Models](../../papers/dreamerv3/README.md)（DreamerV3） · 2023 · 逐步教学版 · [①②]
- [Diffusion for World Modeling: Visual Details Matter in Atari](../../papers/arxiv-2405.12399/README.md)（DIAMOND） · 2024 · 文献卡 · [①②]

## 结构化状态：对象槽与驾驶

- [SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](../../papers/arxiv-2206.07764/README.md) · 2022 · 文献卡 · [①]
- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](../../papers/arxiv-2210.05861/README.md) · 2022 · 文献卡 · [①②]
- [GAIA-1: A Generative World Model for Autonomous Driving](../../papers/arxiv-2309.17080/README.md) · 2023 · 文献卡 · [①②③]
- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](../../papers/arxiv-2311.16038/README.md) · 2023 · 文献卡 · [①]
- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](../../papers/arxiv-2408.14197/README.md) · 2024 · 文献卡 · [①③]
- [A Survey of World Models for Autonomous Driving](../../papers/arxiv-2501.11260/README.md) · 2025 · 文献卡 · [⑥]

## 视频生成一侧的可交互世界模型

- [Video generation models as world simulators](../../papers/sora-tech-report/README.md)（Sora 技术报告） · 2024 · 文献卡 · [②④]
- [Diffusion Models Are Real-Time Game Engines](../../papers/arxiv-2408.14837/README.md)（GameNGen） · 2024 · 文献卡 · [②④]
- [Genie 2: A large-scale foundation world model](../../papers/genie-2-blog/README.md) · 2024 · 文献卡（官方博客） · [②③]
- [Genie 3: A new frontier for world models](../../papers/genie-3-blog/README.md) · 2025 · 文献卡（官方博客） · [②③④]
- [Cosmos World Foundation Model Platform for Physical AI](../../papers/arxiv-2501.03575/README.md) · 2025 · 文献卡 · [⑤②]

## 在表征空间预测

- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) · 2025 · 文献卡 · [①]
- [Back to the Features: DINO as a Foundation for Video World Models](../../papers/arxiv-2507.19468/README.md)（DINO-world） · 2025 · 文献卡 · [①]

## 物理与一致性评测

- [VideoPhy: Evaluating Physical Commonsense for Video Generation](../../papers/arxiv-2406.03520/README.md) · 2024 · 文献卡 · [⑥]
- [How Far is Video Generation from World Model: A Physical Law Perspective](../../papers/arxiv-2411.02385/README.md)（PhyWorld） · 2024 · 文献卡 · [⑥⑤]
- [Do generative video models understand physical principles?](../../papers/arxiv-2501.09038/README.md)（Physics-IQ） · 2025 · 文献卡 · [⑥]

## 主要属于机器人侧

以下卡片放在本方向目录下，但研究对象是机器人操作或具身规划，归位与讨论在[机器人侧的世界模型页](../../../robotics-embodied/fields/world-models/README.md)及其 [Baseline 页](../../../robotics-embodied/fields/world-models/BASELINES.md)。

- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](../../papers/arxiv-2411.04983/README.md) · 2024 · 文献卡
- [FOCUS: Object-Centric World Models for Robotics Manipulation](../../papers/arxiv-2307.02427/README.md) · 2023 · 文献卡
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](../../papers/arxiv-2505.11528/README.md) · 2025 · 文献卡
- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](../../papers/arxiv-2607.04546/README.md) · 2026 · 文献卡
- [Object-Centric World Model for Language-Guided Manipulation](../../papers/arxiv-2503.06170/README.md) · 2025 · 文献卡
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](../../papers/arxiv-2607.13451/README.md) · 2026 · 文献卡
- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](../../papers/arxiv-2601.03200/README.md) · 2026 · 文献卡
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](../../papers/arxiv-2506.07454/README.md) · 2025 · 文献卡
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](../../papers/arxiv-2603.17808/README.md) · 2026 · 文献卡
- [Hydra-0: Action Flow for Generalist World Modeling and Control](../../papers/arxiv-2608.18077/README.md) · 2026 · 文献卡
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](../../papers/arxiv-2505.06111/README.md) · 2025 · 文献卡
- [What Do Latent Action Models Actually Learn?](../../papers/arxiv-2506.15691/README.md) · 2025 · 文献卡
- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](../../papers/arxiv-2604.11689/README.md) · 2026 · 文献卡
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](../../papers/arxiv-2605.06388/README.md) · 2026 · 文献卡（本方向入门页"画像素还是预测表征"一处引用）
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](../../papers/doi-10.15607-rss.2025.xxi.153/README.md) · 2025 · 文献卡
- [World Models for Robotic Manipulation: A Survey](../../papers/doi-10.1002-smb2.70053/README.md) · 年份见原文 · 文献卡
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../../../robotics-embodied/papers/zero-wam/README.md) · 2026 · 选定章节讲解
- 显式模型的对照物：[ORB-SLAM3](../../../robotics-embodied/papers/orb-slam3/README.md)（显式几何地图） · 2020 · 技术精读；[Convex MPC](../../../robotics-embodied/papers/convex-mpc/README.md)（显式简化刚体动力学） · 技术精读
