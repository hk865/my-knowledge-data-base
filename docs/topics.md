# 研究方向与交叉标签

按研究问题组织主目录，允许跨主题交叉引用。ViT 是视觉编码架构，CLIP 属于图文对齐方法/模型家族，WM 是世界模型研究方向；它们不是同一层级的互斥分类。

监督方式另行标注：监督学习、对比学习、掩码重建、生成预测、自蒸馏、偏好学习、强化学习与模仿学习。推理搜索、采样、提示与剪枝属于方法标签；探针与忠实性测量属于评估标签。

当前每篇均可在[完整目录](paper-catalog.md)查看来源；同一资源在多个主题出现不重复计入总数。空分类意味着本轮未检索到已核验的对应聊天链接，不代表历史中不存在；不会用通用经典论文冒充聊天提取。

## 大语言模型

### 预训练

细分：训练目标与规模规律；数据选择与混合；课程与持续预训练

- [Qwen2 Technical Report](paper-catalog.md#p005) · 历史聊天中的助手推荐链接
- [Qwen2.5 Technical Report](paper-catalog.md#p006) · 历史聊天中的助手推荐链接
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007) · 历史聊天中的助手推荐链接
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008) · 历史聊天中的助手推荐链接
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009) · 历史聊天中的助手推荐链接
- [OLMo: Accelerating the Science of Language Models](paper-catalog.md#p010) · 历史聊天中的助手推荐链接
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](paper-catalog.md#p012) · 历史聊天中的助手推荐链接
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](paper-catalog.md#p013) · 历史聊天中的助手推荐链接
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014) · 历史聊天中的助手推荐链接
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](paper-catalog.md#p015) · 历史聊天中的助手推荐链接
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](paper-catalog.md#p020) · 历史聊天中的助手推荐链接
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021) · 历史聊天中的助手推荐链接
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024) · 历史聊天中的助手推荐链接
- [Probing Pretrained Models of Source Code](paper-catalog.md#p029) · 历史聊天中的助手推荐链接

### 后训练 监督微调

细分：指令与示范数据；轨迹监督与任务适配

- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](paper-catalog.md#p002) · 历史聊天中的助手推荐链接
- [s1: Simple test-time scaling](paper-catalog.md#p003) · 历史聊天中的助手推荐链接
- [Qwen2 Technical Report](paper-catalog.md#p005) · 历史聊天中的助手推荐链接
- [Qwen2.5 Technical Report](paper-catalog.md#p006) · 历史聊天中的助手推荐链接
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007) · 历史聊天中的助手推荐链接
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008) · 历史聊天中的助手推荐链接
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011) · 历史聊天中的助手推荐链接
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014) · 历史聊天中的助手推荐链接
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019) · 历史聊天中的助手推荐链接
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](paper-catalog.md#p023) · 历史聊天中的助手推荐链接
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](paper-catalog.md#p035) · 历史聊天中的助手推荐链接

### 后训练 偏好学习

细分：偏好数据与奖励模型；直接偏好优化

- [Qwen2 Technical Report](paper-catalog.md#p005) · 历史聊天中的助手推荐链接
- [Training language models to follow instructions with human feedback](paper-catalog.md#p115) · 先前建立的基础种子条目

### 后训练 强化学习

细分：策略优化算法；结果与过程奖励；轨迹采样与数据回流

- [Qwen2.5 Technical Report](paper-catalog.md#p006) · 历史聊天中的助手推荐链接
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007) · 历史聊天中的助手推荐链接
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011) · 历史聊天中的助手推荐链接
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014) · 历史聊天中的助手推荐链接

### 架构与效率

细分：注意力与状态空间模型；稀疏专家与条件计算；KV cache 与压缩

- [Qwen2 Technical Report](paper-catalog.md#p005) · 历史聊天中的助手推荐链接
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007) · 历史聊天中的助手推荐链接
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008) · 历史聊天中的助手推荐链接
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009) · 历史聊天中的助手推荐链接
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](paper-catalog.md#p012) · 历史聊天中的助手推荐链接
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](paper-catalog.md#p013) · 历史聊天中的助手推荐链接
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014) · 历史聊天中的助手推荐链接
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](paper-catalog.md#p015) · 历史聊天中的助手推荐链接
- [Tokenizer-Agnostic Engram Module](paper-catalog.md#p016) · 历史聊天中的助手推荐链接
- [Cross-Model Memory Transfer via Target-Side Reader Adaptation](paper-catalog.md#p017) · 历史聊天中的助手推荐链接
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](paper-catalog.md#p020) · 历史聊天中的助手推荐链接
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021) · 历史聊天中的助手推荐链接
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](paper-catalog.md#p022) · 历史聊天中的助手推荐链接
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024) · 历史聊天中的助手推荐链接
- [Naturalness of Attention: Revisiting Attention in Code Language Models](paper-catalog.md#p028) · 历史聊天中的助手推荐链接
- [Attention Is All You Need](paper-catalog.md#p113) · 先前建立的基础种子条目

### 推理时计算

细分：搜索与验证；多路径与多 Agent；预算分配与 token 效率

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](paper-catalog.md#p001) · 历史聊天中的助手推荐链接
- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](paper-catalog.md#p002) · 历史聊天中的助手推荐链接
- [s1: Simple test-time scaling](paper-catalog.md#p003) · 历史聊天中的助手推荐链接
- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](paper-catalog.md#p004) · 历史聊天中的助手推荐链接
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008) · 历史聊天中的助手推荐链接
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009) · 历史聊天中的助手推荐链接
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011) · 历史聊天中的助手推荐链接
- [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](paper-catalog.md#p018) · 历史聊天中的助手推荐链接
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019) · 历史聊天中的助手推荐链接
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](paper-catalog.md#p023) · 历史聊天中的助手推荐链接
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](paper-catalog.md#p031) · 历史聊天中的助手推荐链接
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034) · 历史聊天中的助手推荐链接
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](paper-catalog.md#p035) · 历史聊天中的助手推荐链接
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036) · 历史聊天中的助手推荐链接
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](paper-catalog.md#p037) · 历史聊天中的助手推荐链接
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](paper-catalog.md#p038) · 历史聊天中的助手推荐链接
- [Self-Discover: Large Language Models Self-Compose Reasoning Structures](paper-catalog.md#p039) · 历史聊天中的助手推荐链接
- [ReAct: Synergizing Reasoning and Acting in Language Models](paper-catalog.md#p040) · 历史聊天中的助手推荐链接
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](paper-catalog.md#p041) · 历史聊天中的助手推荐链接

## 多模态与世界表征

### 视觉表征

细分：视觉编码器；局部与全局表征；自监督视觉学习

本轮无已核验条目；保留为后续检索入口。

### 图文对齐

细分：联合嵌入与检索；对比学习；跨模态迁移

本轮无已核验条目；保留为后续检索入口。

### 视觉语言模型

细分：连接器与融合；多模态指令学习；空间与推理能力

本轮无已核验条目；保留为后续检索入口。

### 视觉生成

细分：图像生成；视频生成；扩散与 Flow

本轮无已核验条目；保留为后续检索入口。

### 世界模型

细分：预测与潜在动力学；结构化与可干预表征；行动条件与规划

- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](paper-catalog.md#p042) · 历史聊天中的助手推荐链接
- [SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](paper-catalog.md#p043) · 历史聊天中的助手推荐链接
- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](paper-catalog.md#p044) · 历史聊天中的助手推荐链接
- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](paper-catalog.md#p045) · 历史聊天中的助手推荐链接
- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](paper-catalog.md#p046) · 历史聊天中的助手推荐链接
- [Back to the Features: DINO as a Foundation for Video World Models](paper-catalog.md#p047) · 历史聊天中的助手推荐链接
- [FOCUS: Object-Centric World Models for Robotics Manipulation](paper-catalog.md#p048) · 历史聊天中的助手推荐链接
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](paper-catalog.md#p049) · 历史聊天中的助手推荐链接
- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](paper-catalog.md#p050) · 历史聊天中的助手推荐链接
- [A Survey of World Models for Autonomous Driving](paper-catalog.md#p051) · 历史聊天中的助手推荐链接
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052) · 历史聊天中的助手推荐链接
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](paper-catalog.md#p053) · 历史聊天中的助手推荐链接
- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](paper-catalog.md#p054) · 历史聊天中的助手推荐链接
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055) · 历史聊天中的助手推荐链接
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](paper-catalog.md#p056) · 历史聊天中的助手推荐链接
- [Hydra-0: Action Flow for Generalist World Modeling and Control](paper-catalog.md#p057) · 历史聊天中的助手推荐链接
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](paper-catalog.md#p058) · 历史聊天中的助手推荐链接
- [What Do Latent Action Models Actually Learn?](paper-catalog.md#p059) · 历史聊天中的助手推荐链接
- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](paper-catalog.md#p060) · 历史聊天中的助手推荐链接
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061) · 用户在聊天提供链接
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](paper-catalog.md#p062) · 历史聊天中的助手推荐链接
- [World Models for Robotic Manipulation: A Survey](paper-catalog.md#p063) · 历史聊天中的助手推荐链接
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117) · 先前建立的基础种子条目

## 机器人与具身系统

### 感知与传感融合

细分：视觉 深度 LiDAR；惯性与多传感器融合

- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](paper-catalog.md#p080) · 历史聊天中的助手推荐链接
- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](paper-catalog.md#p081) · 历史聊天中的助手推荐链接
- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](paper-catalog.md#p108) · 历史聊天中的助手推荐链接
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](paper-catalog.md#p109) · 历史聊天中的助手推荐链接

### 定位与建图

细分：里程计与状态估计；SLAM 与地图

- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](paper-catalog.md#p080) · 历史聊天中的助手推荐链接
- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](paper-catalog.md#p081) · 历史聊天中的助手推荐链接
- [DS-VIO: Robust and Efficient Stereo Visual Inertial Odometry based on Dual Stage EKF](paper-catalog.md#p082) · 历史聊天中的助手推荐链接
- [PLV-IEKF: Consistent Visual-Inertial Odometry using Points, Lines, and Vanishing Points](paper-catalog.md#p083) · 历史聊天中的助手推荐链接
- [EqVIO: An Equivariant Filter for Visual Inertial Odometry](paper-catalog.md#p084) · 历史聊天中的助手推荐链接
- [A Self-Supervised, Differentiable Kalman Filter for Uncertainty-Aware Visual-Inertial Odometry](paper-catalog.md#p085) · 历史聊天中的助手推荐链接
- [Learned IMU Bias Prediction for Invariant Visual Inertial Odometry](paper-catalog.md#p086) · 历史聊天中的助手推荐链接
- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](paper-catalog.md#p108) · 历史聊天中的助手推荐链接
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](paper-catalog.md#p109) · 历史聊天中的助手推荐链接

### 导航与规划

细分：几何与运动规划；视觉语言导航

本轮无已核验条目；保留为后续检索入口。

### 运动控制

细分：经典与最优控制；腿足策略与适应；sim to real

- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075) · 已有手册提取
- [CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion](paper-catalog.md#p091) · 历史聊天中的助手推荐链接
- [Learning Quadruped Locomotion using Bio-Inspired Neural Networks with Intrinsic Rhythmicity](paper-catalog.md#p092) · 历史聊天中的助手推荐链接
- [Learning Free Gait Transition for Quadruped Robots via Phase-Guided Controller](paper-catalog.md#p093) · 历史聊天中的助手推荐链接
- [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](paper-catalog.md#p094) · 历史聊天中的助手推荐链接
- [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](paper-catalog.md#p095) · 历史聊天中的助手推荐链接
- [Learning from Massive Human Videos for Universal Humanoid Pose Control](paper-catalog.md#p096) · 历史聊天中的助手推荐链接
- [A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots](paper-catalog.md#p097) · 历史聊天中的助手推荐链接
- [Scaling Behavior Foundation Model for Humanoid Robots](paper-catalog.md#p098) · 历史聊天中的助手推荐链接
- [Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning](paper-catalog.md#p099) · 历史聊天中的助手推荐链接
- [Attention-Based Map Encoding for Learning Generalized Legged Locomotion](paper-catalog.md#p100) · 历史聊天中的助手推荐链接
- [Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](paper-catalog.md#p101) · 历史聊天中的助手推荐链接
- [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](paper-catalog.md#p102) · 历史聊天中的助手推荐链接
- [ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](paper-catalog.md#p103) · 历史聊天中的助手推荐链接
- [ExBody2: Advanced Expressive Humanoid Whole-Body Control](paper-catalog.md#p104) · 历史聊天中的助手推荐链接
- [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](paper-catalog.md#p105) · 历史聊天中的助手推荐链接
- [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](paper-catalog.md#p106) · 历史聊天中的助手推荐链接
- [PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots](paper-catalog.md#p107) · 历史聊天中的助手推荐链接
- [Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](paper-catalog.md#p110) · 历史聊天中的助手推荐链接
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](paper-catalog.md#p111) · 历史聊天中的助手推荐链接
- [MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion](paper-catalog.md#p112) · 历史聊天中的助手推荐链接
- [RMA Rapid Motor Adaptation for Legged Robots](paper-catalog.md#p116) · 先前建立的基础种子条目

### 具身策略与 VLA

细分：动作表示与生成；跨本体与数据；模型 规划与控制接口

- [RT-1: Robotics Transformer for Real-World Control at Scale](paper-catalog.md#p064) · 已有手册提取
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](paper-catalog.md#p065) · 已有手册提取
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](paper-catalog.md#p066) · 已有手册提取
- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](paper-catalog.md#p067) · 已有手册提取
- [Octo: An Open-Source Generalist Robot Policy](paper-catalog.md#p068) · 已有手册提取
- [OpenVLA: An Open-Source Vision-Language-Action Model](paper-catalog.md#p069) · 已有手册提取 / 先前建立的基础种子条目
- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](paper-catalog.md#p070) · 已有手册提取
- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](paper-catalog.md#p071) · 已有手册提取
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](paper-catalog.md#p072) · 已有手册提取
- [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](paper-catalog.md#p073) · 已有手册提取
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](paper-catalog.md#p074) · 已有手册提取
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076) · 已有手册提取
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](paper-catalog.md#p077) · 已有手册提取
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078) · 已有手册提取
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079) · 已有手册提取
- [RoboTTT: Context Scaling for Robot Policies](paper-catalog.md#p087) · 历史聊天中的助手推荐链接
- [In-Context Imitation Learning via Next-Token Prediction](paper-catalog.md#p088) · 历史聊天中的助手推荐链接
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](paper-catalog.md#p089) · 历史聊天中的助手推荐链接
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090) · 历史聊天中的助手推荐链接

## 跨方向方法与探索

### Agent 与上下文系统

- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019) · 历史聊天中的助手推荐链接
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034) · 历史聊天中的助手推荐链接
- [ReAct: Synergizing Reasoning and Acting in Language Models](paper-catalog.md#p040) · 历史聊天中的助手推荐链接
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](paper-catalog.md#p041) · 历史聊天中的助手推荐链接

### 机制与可信解释

- [OLMo: Accelerating the Science of Language Models](paper-catalog.md#p010) · 历史聊天中的助手推荐链接
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](paper-catalog.md#p022) · 历史聊天中的助手推荐链接
- [In-context Learning and Induction Heads](paper-catalog.md#p025) · 历史聊天中的助手推荐链接
- [Transformer Feed-Forward Layers Are Key-Value Memories](paper-catalog.md#p026) · 历史聊天中的助手推荐链接
- [Locating and Editing Factual Associations in GPT](paper-catalog.md#p027) · 历史聊天中的助手推荐链接
- [Naturalness of Attention: Revisiting Attention in Code Language Models](paper-catalog.md#p028) · 历史聊天中的助手推荐链接
- [Probing Pretrained Models of Source Code](paper-catalog.md#p029) · 历史聊天中的助手推荐链接
- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](paper-catalog.md#p030) · 历史聊天中的助手推荐链接
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](paper-catalog.md#p031) · 历史聊天中的助手推荐链接
- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](paper-catalog.md#p032) · 历史聊天中的助手推荐链接
- [On scalable oversight with weak LLMs judging strong LLMs](paper-catalog.md#p033) · 历史聊天中的助手推荐链接
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034) · 历史聊天中的助手推荐链接
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036) · 历史聊天中的助手推荐链接
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](paper-catalog.md#p037) · 历史聊天中的助手推荐链接
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](paper-catalog.md#p038) · 历史聊天中的助手推荐链接
- [Training Compute Optimal Large Language Models](paper-catalog.md#p114) · 先前建立的基础种子条目

### 生物计算探索

本轮无已核验条目；保留为后续检索入口。

### 评估与监督可靠性

- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](paper-catalog.md#p030) · 历史聊天中的助手推荐链接
- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](paper-catalog.md#p032) · 历史聊天中的助手推荐链接
- [On scalable oversight with weak LLMs judging strong LLMs](paper-catalog.md#p033) · 历史聊天中的助手推荐链接
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034) · 历史聊天中的助手推荐链接
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036) · 历史聊天中的助手推荐链接
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](paper-catalog.md#p037) · 历史聊天中的助手推荐链接
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](paper-catalog.md#p038) · 历史聊天中的助手推荐链接

## 监督方式子导航

以下按当前元数据标签检索，不把推理方法当作监督信号。

### 对比学习

- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)

### 掩码建模

- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024)
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)

### 蒸馏与自蒸馏

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011)
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](paper-catalog.md#p020)
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021)
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](paper-catalog.md#p111)

### 生成与预测

- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](paper-catalog.md#p002)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009)
- [OLMo: Accelerating the Science of Language Models](paper-catalog.md#p010)
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](paper-catalog.md#p015)
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021)
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](paper-catalog.md#p023)
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024)
- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](paper-catalog.md#p042)
- [SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](paper-catalog.md#p043)
- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](paper-catalog.md#p044)
- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](paper-catalog.md#p046)
- [Back to the Features: DINO as a Foundation for Video World Models](paper-catalog.md#p047)
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](paper-catalog.md#p049)
- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](paper-catalog.md#p050)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [What Do Latent Action Models Actually Learn?](paper-catalog.md#p059)
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)
- [Learned IMU Bias Prediction for Invariant Visual Inertial Odometry](paper-catalog.md#p086)

### 偏好与奖励

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](paper-catalog.md#p001)
- [Qwen2 Technical Report](paper-catalog.md#p005)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011)
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](paper-catalog.md#p056)

### 强化学习

- [Qwen2.5 Technical Report](paper-catalog.md#p006)
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011)
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014)
- [FOCUS: Object-Centric World Models for Robotics Manipulation](paper-catalog.md#p048)
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](paper-catalog.md#p056)
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](paper-catalog.md#p062)
- [CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion](paper-catalog.md#p091)
- [Learning Quadruped Locomotion using Bio-Inspired Neural Networks with Intrinsic Rhythmicity](paper-catalog.md#p092)
- [Learning Free Gait Transition for Quadruped Robots via Phase-Guided Controller](paper-catalog.md#p093)
- [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](paper-catalog.md#p094)
- [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](paper-catalog.md#p095)
- [Attention-Based Map Encoding for Learning Generalized Legged Locomotion](paper-catalog.md#p100)
- [Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](paper-catalog.md#p101)
- [PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots](paper-catalog.md#p107)
- [Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](paper-catalog.md#p110)
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](paper-catalog.md#p111)

### 模仿学习

- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019)
- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](paper-catalog.md#p050)
- [RT-1: Robotics Transformer for Real-World Control at Scale](paper-catalog.md#p064)
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](paper-catalog.md#p065)
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](paper-catalog.md#p066)
- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](paper-catalog.md#p067)
- [Octo: An Open-Source Generalist Robot Policy](paper-catalog.md#p068)
- [OpenVLA: An Open-Source Vision-Language-Action Model](paper-catalog.md#p069)
- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](paper-catalog.md#p070)
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](paper-catalog.md#p074)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075)
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076)
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079)
- [RoboTTT: Context Scaling for Robot Policies](paper-catalog.md#p087)
- [In-Context Imitation Learning via Next-Token Prediction](paper-catalog.md#p088)
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](paper-catalog.md#p089)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](paper-catalog.md#p102)
- [ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](paper-catalog.md#p103)
- [ExBody2: Advanced Expressive Humanoid Whole-Body Control](paper-catalog.md#p104)
- [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](paper-catalog.md#p105)

## 2026-09-30 细粒度问题导航补充

- 预训练：训练目标与规模规律；数据选择与混合；课程与持续预训练；数据质量与配比；训练目标与监督位置；长上下文课程
- 后训练 强化学习：策略优化算法；结果与过程奖励；轨迹采样与数据回流；奖励与验证器；长轨迹信用分配；探索与轨迹分布
- 架构与效率：注意力与状态空间模型；稀疏专家与条件计算；KV cache 与压缩；线性与稀疏注意力；因果掩码与复杂度
- 视觉生成：图像生成；视频生成；扩散与 Flow；理解与生成的联合学习
- 视频与时序表征：时序对应与记忆；动作条件视频；预测与时间一致性
- 世界模型：预测与潜在动力学；结构化与可干预表征；行动条件与规划；几何与物理约束
- 感知与传感融合：视觉 深度 LiDAR；惯性与多传感器融合；传统 学习与混合方法
- 导航与规划：几何与运动规划；视觉语言导航；VLA 与 VLN 的任务边界
- 具身策略与 VLA：动作表示与生成；跨本体与数据；模型 规划与控制接口；模仿学习；机器人强化学习

新维度表示检索入口，未逐篇补贴标签；没有已核验对应论文的子类仍是覆盖缺口。模态与任务作为正交标签。视频时序与世界模型可交叉，不重复计数。

- Q-0930-context → [问题图](model-training-multimodal.md) → [Qwen2.5-1M](paper-catalog.md#p008)
- Q-0930-sft → [问题图](model-training-multimodal.md) → [InstructGPT](paper-catalog.md#p115)
