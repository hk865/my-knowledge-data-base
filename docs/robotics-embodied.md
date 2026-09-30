# 机器人与具身智能

云端来源（可能仅原账户可访问）：https://chatgpt.com/space/page_2ac2740d1ed88191a4b6b8ff416f53b9

本页贯通传统机器人感知、状态估计、规划导航和运动控制，以及 VLA、具身基础模型与世界模型。传统机器人是一条独立而实质的研究线，不能用 VLA 标签替代。优先根据可检索对话中的具体问题组织阅读。

## 初始研究地图

持续关注：IMU 与 EKF、SLAM、深度与 LiDAR 融合、导航规划、PID 与 LQR；四足 PPO、CPG 与周期控制、课程学习、sim to real、非对称策略与教师学生蒸馏。

具身模型：VLA 与 VLN、跨本体动作接口、世界模型与结构化表征；区分感知估计、策略、规划和低层控制的职责。初始画像可修订，不等于每一项都是已选课题。

待核实条件：目前机器人平台、传感器、仿真环境和任务指标；避免把仿真经验推断为大量真机实验。

## 已有材料

保留并复用 2026年9月11日的 VLA 模块化研究手册目录（原 Library 来源仅原账户可访问；手册条目已在本仓库独立标注，整套文件未迁移）。已读取目录，它按任务接口、数据、模型模块、动作生成、训练评估和机器人系统组织内容。目录内的相对链接尚未逐一验证，不视为已读完整手册；原文件未改动。

## 基础论文

### OpenVLA An Open Source Vision Language Action Model

原题 OpenVLA: An Open-Source Vision-Language-Action Model · 2024年 · [原文](https://arxiv.org/abs/2406.09246) · 去重键 arXiv:2406.09246

问题：VLA 的开放使用与新任务适配。方法：7B 语言模型结合视觉编码器，在机器人示范上训练，并研究高效微调。原文证据：多任务操纵和适配实验。

证据边界与关联判断：操纵评测不能替代移动导航或四足稳定性验证；适合从编码器、数据配比、动作接口、微调成本切入与你的多模态训练问题对照。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

### RMA Rapid Motor Adaptation for Legged Robots

原题 RMA: Rapid Motor Adaptation for Legged Robots · 2021年 · [原文](https://arxiv.org/abs/2107.04034) · 去重键 arXiv:2107.04034

问题：四足机器人如何适应未见地形、负载等变化。方法：基础策略与适应模块组合，在仿真训练后部署到 A1。原文证据：仿真与多种真实地形实验，无真机微调。

证据边界与关联判断：不能由单一平台结果推出任何传感器组合都有效；与适应、特权信息及部署观测差异相关，可作为教师学生路线的比较入口，本文不等同于深度加 IMU 导航方案。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

### Mastering Diverse Domains through World Models

2023年首次公开 · [原文](https://arxiv.org/abs/2301.04104) · 去重键 arXiv:2301.04104

问题：RL 在跨任务应用时如何减少专门调参。方法：DreamerV3 学习环境模型，再通过想象轨迹改进行为，并用稳定化机制提高跨域训练适用性。原文证据：多种控制与游戏任务。

证据边界与关联判断：任务表现不能单独证明 latent 具有因果物理结构，也不能直接证明真机安全性；适合围绕可预测、可干预、等变性与长期控制分别设计检验。阅读状态：摘要与元数据已核验，全文精读待做；你的阅读状态待确认。

## 后续检索队列

根据聊天问题优先补充传统机器人路线：FAST LIVO2 与 ROS2 适配、视觉惯性与 LiDAR 融合、定位建图、规划导航和运动控制。具身路线补充 VLN、动作时序、跨本体与模型辅助控制。新论文须区分仿真、真机、开环、闭环及安全证据。

## 从历史聊天提取的论文链接

2026年9月30日更新。以下按研究问题分组，从历史聊天检索摘要恢复具体链接，再核验题名与标识。每条标注用户提供或助手提供及可恢复日期；助手推荐不代表你已采纳。用户阅读状态均待确认，本次不是全文精读或独立复现。跨方向条目可重复展示，但按统一标识只计一次。

原有3篇基础论文卡保留为初始推荐，不冒充聊天中提取的论文；已有手册来源另列。架构和监督方式为交叉标签，无已核实聊天链接的细类保留覆盖缺口。

### 机器人与具身系统

#### 感知与传感融合

- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](https://arxiv.org/abs/1609.05130) · 2016 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：CNN, geometric-fusion, semantic-labels

- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](https://arxiv.org/abs/1903.01177) · 2019 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：CNN, geometric-fusion, semantic-labels

- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](https://pmc.ncbi.nlm.nih.gov/articles/PMC6164553/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：pixel-voxel-network, RGB-D-SLAM, semantic-labels

- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](https://github.com/HKUST-Aerial-Robotics/FM-Fusion) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：vision-language-foundation-model, mapping, pretrained-foundation-model；代码仓库，非论文

#### 定位与建图

- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](https://arxiv.org/abs/1609.05130) · 2016 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：CNN, geometric-fusion, semantic-labels

- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](https://arxiv.org/abs/1903.01177) · 2019 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：CNN, geometric-fusion, semantic-labels

- [DS-VIO: Robust and Efficient Stereo Visual Inertial Odometry based on Dual Stage EKF](https://arxiv.org/abs/1905.00684) · 2019 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-01-07；标签：dual-stage-EKF, model-based-estimation

- [PLV-IEKF: Consistent Visual-Inertial Odometry using Points, Lines, and Vanishing Points](https://arxiv.org/abs/2311.04477) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-01-07；标签：IEKF, model-based-estimation

- [EqVIO: An Equivariant Filter for Visual Inertial Odometry](https://arxiv.org/abs/2205.01980) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-01-07；标签：equivariant-filter, model-based-estimation

- [A Self-Supervised, Differentiable Kalman Filter for Uncertainty-Aware Visual-Inertial Odometry](https://arxiv.org/abs/2203.07207) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-01-07；标签：differentiable-Kalman-filter, self-supervised

- [Learned IMU Bias Prediction for Invariant Visual Inertial Odometry](https://arxiv.org/abs/2505.06748) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-01-07；标签：learned-IMU-bias, learned-bias-prediction

- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](https://pmc.ncbi.nlm.nih.gov/articles/PMC6164553/) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：pixel-voxel-network, RGB-D-SLAM, semantic-labels

- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](https://github.com/HKUST-Aerial-Robotics/FM-Fusion) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-09-08；标签：vision-language-foundation-model, mapping, pretrained-foundation-model；代码仓库，非论文

#### 导航与规划

覆盖缺口：本次没有恢复并核验到该细类的历史聊天论文链接；不据此判断你没有兴趣，也不补入通用推荐。

#### 运动控制

- [CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion](https://arxiv.org/abs/2211.00458) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：CPG, reinforcement-learning

- [Learning Quadruped Locomotion using Bio-Inspired Neural Networks with Intrinsic Rhythmicity](https://arxiv.org/abs/2305.07300) · 2023 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：intrinsic-rhythmic-network, reinforcement-learning

- [Learning Free Gait Transition for Quadruped Robots via Phase-Guided Controller](https://arxiv.org/abs/2201.00206) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：phase-guided-controller, reinforcement-learning

- [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](https://arxiv.org/abs/2011.01387) · 2020 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：periodic-reward-composition, reinforcement-learning

- [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](https://arxiv.org/abs/2404.05695) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：sim-to-real, reinforcement-learning

- [Learning from Massive Human Videos for Universal Humanoid Pose Control](https://arxiv.org/abs/2412.14172) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：video-to-pose-control, human-videos

- [A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots](https://arxiv.org/abs/2506.20487) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：survey, mixed-or-not-applicable

- [Scaling Behavior Foundation Model for Humanoid Robots](https://arxiv.org/abs/2607.15163) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：behavior-foundation-model, mixed-or-not-applicable

- [Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning](https://arxiv.org/abs/2501.02116) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：survey, mixed-or-not-applicable

- [Attention-Based Map Encoding for Learning Generalized Legged Locomotion](https://arxiv.org/abs/2506.09588) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-22；标签：attention-map-encoder, reinforcement-learning

- [Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](https://arxiv.org/abs/2601.08485) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-22；标签：attention-map-encoder, reinforcement-learning

- [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717) · 2018 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：physics-based-character-policy, motion-reference-imitation

- [ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](https://arxiv.org/abs/2205.01906) · 2022 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：adversarial-skill-embedding, adversarial-imitation

- [ExBody2: Advanced Expressive Humanoid Whole-Body Control](https://arxiv.org/abs/2412.13196) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：whole-body-controller, motion-reference-imitation

- [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](https://arxiv.org/abs/2508.08241) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：guided-diffusion, motion-reference-imitation

- [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](https://arxiv.org/abs/2510.02252) · 2025 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：motion-retargeting, motion-retargeting

- [PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots](https://arxiv.org/abs/2408.13740) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：implicit-explicit-framework, reinforcement-learning

- [Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](https://proceedings.mlr.press/v205/margolis23a/margolis23a.pdf) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：multiplicity-of-behavior, reinforcement-learning

- [Legged Locomotion in Challenging Terrains using Egocentric Vision](https://proceedings.mlr.press/v205/agarwal23a/agarwal23a.pdf) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：depth-vision-policy, reinforcement-learning, supervised-distillation

- [MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202524345?af=R) · 年份待核 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-21；标签：depth-perception-model, recipe-needs-full-text-review

#### 具身策略与 VLA

- [RoboTTT: Context Scaling for Robot Policies](https://arxiv.org/abs/2607.15275) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-24；标签：context-scaling, imitation-learning

- [In-Context Imitation Learning via Next-Token Prediction](https://arxiv.org/abs/2408.15980) · 2024 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-24；标签：next-token-prediction, imitation-learning

- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](https://arxiv.org/abs/2606.30457) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-24；标签：demonstration-prompting, imitation-learning

- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](https://arxiv.org/abs/2601.02456) · 2026 · 聊天助手提供，未表示你采纳 · 聊天日期 2026-08-24；标签：unified-understanding-generation-action, imitation-learning

### 已有手册中的参考文献

以下来自已有手册，单独标源，不计入历史聊天恢复数。

- [RT-1: Robotics Transformer for Real-World Control at Scale](https://arxiv.org/abs/2212.06817) · 2022 · 手册来源

- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) · 2023 · 手册来源

- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864) · 2023 · 手册来源

- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137) · 2023 · 手册来源

- [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213) · 2024 · 手册来源

- [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) · 2024 · 手册来源

- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) · 2024 · 手册来源

- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747) · 2025 · 手册来源

- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](https://arxiv.org/abs/2502.19645) · 2025 · 手册来源

- [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](https://arxiv.org/abs/2504.16054) · 2025 · 手册来源

- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844) · 2025 · 手册来源

- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025 · 手册来源

- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](https://arxiv.org/abs/2604.15483) · 2026 · 手册来源

- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/abs/2605.30280) · 2026 · 手册来源

- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](https://arxiv.org/abs/2606.14752) · 2026 · 手册来源

- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](https://arxiv.org/abs/2505.22159) · 2025 · 手册来源

### 待核验线索

以下只恢复名称、截断链接或其他不足信息，暂不作为已核验论文入库：TLIO；Yan ICRA 2018；Extreme Parkour；GEN-1.5 / MimicDroid / AIRSOUL。

[细分类目录](topics.md) · [全部论文与来源](paper-catalog.md)
