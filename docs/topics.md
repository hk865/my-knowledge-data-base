# 研究主题目录

研究问题为主分类；架构、监督信号、模态和聊天来源为正交标签。一个条目可跨方向引用，不重复计数。

[论文总目录](paper-catalog.md) · [待核实条目](unresolved.md)

## 大语言模型

### 预训练（15）

细分：训练目标与规模规律；数据选择与混合；课程与持续预训练；数据质量与配比；训练目标与监督位置；长上下文课程

- [Qwen2 Technical Report](paper-catalog.md#p005)
- [Qwen2.5 Technical Report](paper-catalog.md#p006)
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007)
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009)
- [OLMo: Accelerating the Science of Language Models](paper-catalog.md#p010)
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](paper-catalog.md#p012)
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](paper-catalog.md#p013)
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014)
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](paper-catalog.md#p015)
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](paper-catalog.md#p020)
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021)
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024)
- [Probing Pretrained Models of Source Code](paper-catalog.md#p029)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)

### 后训练 监督微调（12）

细分：指令与示范数据；轨迹监督与任务适配

- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](paper-catalog.md#p002)
- [s1: Simple test-time scaling](paper-catalog.md#p003)
- [Qwen2 Technical Report](paper-catalog.md#p005)
- [Qwen2.5 Technical Report](paper-catalog.md#p006)
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007)
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011)
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014)
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019)
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](paper-catalog.md#p023)
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](paper-catalog.md#p035)
- [Training language models to follow instructions with human feedback](paper-catalog.md#p115)

### 后训练 偏好学习（5）

细分：偏好数据与奖励模型；直接偏好优化

- [Qwen2 Technical Report](paper-catalog.md#p005)
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008)
- [Training language models to follow instructions with human feedback](paper-catalog.md#p115)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](paper-catalog.md#p118)
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](paper-catalog.md#p128)

### 后训练 强化学习（6）

细分：策略优化算法；结果与过程奖励；轨迹采样与数据回流；奖励与验证器；长轨迹信用分配；探索与轨迹分布

- [Qwen2.5 Technical Report](paper-catalog.md#p006)
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011)
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014)
- [Training language models to follow instructions with human feedback](paper-catalog.md#p115)
- [Proximal Policy Optimization Algorithms](paper-catalog.md#p129)

### 架构与效率（17）

细分：注意力与状态空间模型；稀疏专家与条件计算；KV cache 与压缩；线性与稀疏注意力；因果掩码与复杂度

- [Qwen2 Technical Report](paper-catalog.md#p005)
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007)
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009)
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](paper-catalog.md#p012)
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](paper-catalog.md#p013)
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014)
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](paper-catalog.md#p015)
- [Tokenizer-Agnostic Engram Module](paper-catalog.md#p016)
- [Cross-Model Memory Transfer via Target-Side Reader Adaptation](paper-catalog.md#p017)
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](paper-catalog.md#p020)
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021)
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](paper-catalog.md#p022)
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024)
- [Naturalness of Attention: Revisiting Attention in Code Language Models](paper-catalog.md#p028)
- [Attention Is All You Need](paper-catalog.md#p113)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)

### 推理时计算（29）

细分：搜索与验证；多路径与多 Agent；预算分配与 token 效率；精确目标分布与投机验证；近似质量协作与关键段接管；MTP草拟与验证接口；精确级联混合分布

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](paper-catalog.md#p001)
- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](paper-catalog.md#p002)
- [s1: Simple test-time scaling](paper-catalog.md#p003)
- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](paper-catalog.md#p004)
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011)
- [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](paper-catalog.md#p018)
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019)
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](paper-catalog.md#p023)
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](paper-catalog.md#p031)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](paper-catalog.md#p035)
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036)
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](paper-catalog.md#p037)
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](paper-catalog.md#p038)
- [Self-Discover: Large Language Models Self-Compose Reasoning Structures](paper-catalog.md#p039)
- [ReAct: Synergizing Reasoning and Acting in Language Models](paper-catalog.md#p040)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](paper-catalog.md#p041)
- [Fast Inference from Transformers via Speculative Decoding](paper-catalog.md#p144)
- [Accelerating Large Language Model Decoding with Speculative Sampling](paper-catalog.md#p145)
- [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](paper-catalog.md#p146)
- [DFlash: Block Diffusion for Flash Speculative Decoding](paper-catalog.md#p147)
- [Speculative Decoding with Big Little Decoder](paper-catalog.md#p148)
- [RelayLLM: Efficient Reasoning via Collaborative Decoding](paper-catalog.md#p149)
- [Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment](paper-catalog.md#p150)
- [DFlash 2: Keep Drafting Parallel](paper-catalog.md#p151)
- [Faster Cascades via Speculative Decoding](paper-catalog.md#p152)


## 多模态与世界表征

### 视觉表征（3）

细分：视觉编码器；局部与全局表征；自监督视觉学习

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](paper-catalog.md#p130)
- [Masked Autoencoders Are Scalable Vision Learners](paper-catalog.md#p131)
- [Emerging Properties in Self-Supervised Vision Transformers](paper-catalog.md#p133)

### 图文对齐（2）

细分：联合嵌入与检索；对比学习；跨模态迁移

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](paper-catalog.md#p130)
- [Learning Transferable Visual Models From Natural Language Supervision](paper-catalog.md#p132)

### 视觉语言模型（2）

细分：连接器与融合；多模态指令学习；空间与推理能力

- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Learning Transferable Visual Models From Natural Language Supervision](paper-catalog.md#p132)

### 视觉生成（3）

细分：图像生成；视频生成；扩散与 Flow；理解与生成的联合学习

- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Denoising Diffusion Probabilistic Models](paper-catalog.md#p121)
- [Video Diffusion Models](paper-catalog.md#p122)

### 视频与时序表征（1）

细分：时序对应与记忆；动作条件视频；预测与时间一致性

- [Video Diffusion Models](paper-catalog.md#p122)

### 世界模型（26）

细分：预测与潜在动力学；结构化与可干预表征；行动条件与规划；几何与物理约束

- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](paper-catalog.md#p042)
- [SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](paper-catalog.md#p043)
- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](paper-catalog.md#p044)
- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](paper-catalog.md#p045)
- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](paper-catalog.md#p046)
- [Back to the Features: DINO as a Foundation for Video World Models](paper-catalog.md#p047)
- [FOCUS: Object-Centric World Models for Robotics Manipulation](paper-catalog.md#p048)
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](paper-catalog.md#p049)
- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](paper-catalog.md#p050)
- [A Survey of World Models for Autonomous Driving](paper-catalog.md#p051)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](paper-catalog.md#p053)
- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](paper-catalog.md#p054)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](paper-catalog.md#p056)
- [Hydra-0: Action Flow for Generalist World Modeling and Control](paper-catalog.md#p057)
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](paper-catalog.md#p058)
- [What Do Latent Action Models Actually Learn?](paper-catalog.md#p059)
- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](paper-catalog.md#p060)
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](paper-catalog.md#p062)
- [World Models for Robotic Manipulation: A Survey](paper-catalog.md#p063)
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117)
- [ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](paper-catalog.md#p123)
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](paper-catalog.md#p124)
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](paper-catalog.md#p134)

## 机器人与具身系统

### 感知与传感融合（8）

细分：视觉 深度 LiDAR；惯性与多传感器融合；传统 学习与混合方法

- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](paper-catalog.md#p080)
- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](paper-catalog.md#p081)
- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](paper-catalog.md#p108)
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](paper-catalog.md#p109)
- [ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](paper-catalog.md#p123)
- [Quaternion kinematics for the error-state Kalman filter](paper-catalog.md#p125)
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](paper-catalog.md#p130)
- [Learning Transferable Visual Models From Natural Language Supervision](paper-catalog.md#p132)

### 定位与建图（11）

细分：里程计与状态估计；SLAM 与地图

- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](paper-catalog.md#p080)
- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](paper-catalog.md#p081)
- [DS-VIO: Robust and Efficient Stereo Visual Inertial Odometry based on Dual Stage EKF](paper-catalog.md#p082)
- [PLV-IEKF: Consistent Visual-Inertial Odometry using Points, Lines, and Vanishing Points](paper-catalog.md#p083)
- [EqVIO: An Equivariant Filter for Visual Inertial Odometry](paper-catalog.md#p084)
- [A Self-Supervised, Differentiable Kalman Filter for Uncertainty-Aware Visual-Inertial Odometry](paper-catalog.md#p085)
- [Learned IMU Bias Prediction for Invariant Visual Inertial Odometry](paper-catalog.md#p086)
- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](paper-catalog.md#p108)
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](paper-catalog.md#p109)
- [ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](paper-catalog.md#p123)
- [Quaternion kinematics for the error-state Kalman filter](paper-catalog.md#p125)

### 导航与规划（4）

细分：几何与运动规划；视觉语言导航；VLA 与 VLN 的任务边界

- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](paper-catalog.md#p124)
- [Sampling-based Algorithms for Optimal Motion Planning](paper-catalog.md#p126)
- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](paper-catalog.md#p162)


### 运动控制（34）

细分：经典与最优控制；腿足策略与适应；sim to real；风险敏感策略与恢复控制；恢复控制与自主练习

- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075)
- [CPG-RL: Learning Central Pattern Generators for Quadruped Locomotion](paper-catalog.md#p091)
- [Learning Quadruped Locomotion using Bio-Inspired Neural Networks with Intrinsic Rhythmicity](paper-catalog.md#p092)
- [Learning Free Gait Transition for Quadruped Robots via Phase-Guided Controller](paper-catalog.md#p093)
- [Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition](paper-catalog.md#p094)
- [Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](paper-catalog.md#p095)
- [Learning from Massive Human Videos for Universal Humanoid Pose Control](paper-catalog.md#p096)
- [A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots](paper-catalog.md#p097)
- [Scaling Behavior Foundation Model for Humanoid Robots](paper-catalog.md#p098)
- [Humanoid Locomotion and Manipulation: Current Progress and Challenges in Control, Planning, and Learning](paper-catalog.md#p099)
- [Attention-Based Map Encoding for Learning Generalized Legged Locomotion](paper-catalog.md#p100)
- [Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](paper-catalog.md#p101)
- [DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](paper-catalog.md#p102)
- [ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters](paper-catalog.md#p103)
- [ExBody2: Advanced Expressive Humanoid Whole-Body Control](paper-catalog.md#p104)
- [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](paper-catalog.md#p105)
- [Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](paper-catalog.md#p106)
- [PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots](paper-catalog.md#p107)
- [Walk These Ways: Tuning Robot Control for Generalization with Multiplicity of Behavior](paper-catalog.md#p110)
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](paper-catalog.md#p111)
- [MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion](paper-catalog.md#p112)
- [RMA: Rapid Motor Adaptation for Legged Robots](paper-catalog.md#p116)
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](paper-catalog.md#p124)
- [Quaternion kinematics for the error-state Kalman filter](paper-catalog.md#p125)
- [Sampling-based Algorithms for Optimal Motion Planning](paper-catalog.md#p126)
- [Proximal Policy Optimization Algorithms](paper-catalog.md#p129)
- [Learning Quadrupedal Locomotion over Challenging Terrain](paper-catalog.md#p153)
- [Robust Recovery Controller for a Quadrupedal Robot using Deep Reinforcement Learning](paper-catalog.md#p154)
- [Recovery RL: Safe Reinforcement Learning With Learned Recovery Zones](paper-catalog.md#p155)
- [Learning robust perceptive locomotion for quadrupedal robots in the wild](paper-catalog.md#p156)
- [Prioritized Level Replay](paper-catalog.md#p157)
- [Robust Quadrupedal Locomotion via Risk-Averse Policy Learning](paper-catalog.md#p158)
- [Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning](paper-catalog.md#p159)
- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](paper-catalog.md#p162)


### 具身策略与 VLA（25）

细分：动作表示与生成；跨本体与数据；模型 规划与控制接口；模仿学习；机器人强化学习

- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [RT-1: Robotics Transformer for Real-World Control at Scale](paper-catalog.md#p064)
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](paper-catalog.md#p065)
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](paper-catalog.md#p066)
- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](paper-catalog.md#p067)
- [Octo: An Open-Source Generalist Robot Policy](paper-catalog.md#p068)
- [OpenVLA: An Open-Source Vision-Language-Action Model](paper-catalog.md#p069)
- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](paper-catalog.md#p070)
- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](paper-catalog.md#p071)
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](paper-catalog.md#p072)
- [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](paper-catalog.md#p073)
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](paper-catalog.md#p074)
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076)
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](paper-catalog.md#p077)
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079)
- [RoboTTT: Context Scaling for Robot Policies](paper-catalog.md#p087)
- [In-Context Imitation Learning via Next-Token Prediction](paper-catalog.md#p088)
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](paper-catalog.md#p089)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Denoising Diffusion Probabilistic Models](paper-catalog.md#p121)
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](paper-catalog.md#p124)
- [Proximal Policy Optimization Algorithms](paper-catalog.md#p129)
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](paper-catalog.md#p134)

### 具身 Agents 与闭环系统（6）

细分：任务理解与技能选择；行动记忆与空间记忆；规划—执行—反馈；技能获取与复用；VLA策略编排与部署

- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](paper-catalog.md#p135)
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](paper-catalog.md#p136)
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](paper-catalog.md#p137)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)

## 跨方向方法与探索

### Agent 与上下文系统（34）

细分：Agent轨迹与性质验证；权限与执行隔离；协作与软件流程

- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)
- [ReAct: Synergizing Reasoning and Acting in Language Models](paper-catalog.md#p040)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](paper-catalog.md#p041)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](paper-catalog.md#p135)
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](paper-catalog.md#p136)
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](paper-catalog.md#p137)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)
- [Finding bugs across the Python ecosystem with Claude and property-based testing](paper-catalog.md#p160)
- [Metamorphic Testing of Multi-Agent LLM Systems: A Trace-Based Behavioral Oracle Framework](paper-catalog.md#p161)
- [Running Codex safely at OpenAI](paper-catalog.md#p163)
- [Mitigating the risk of prompt injections in browser use](paper-catalog.md#p164)
- [SPIFFE Overview](paper-catalog.md#p165)
- [How Cedar authorization works](paper-catalog.md#p166)
- [Docker Engine security](paper-catalog.md#p167)
- [namespaces(7) — Linux manual page](paper-catalog.md#p168)
- [Seccomp BPF (SECure COMPuting with filters)](paper-catalog.md#p169)
- [Landlock: unprivileged access control](paper-catalog.md#p170)
- [Control Group v2](paper-catalog.md#p171)
- [Bubblewrap](paper-catalog.md#p172)
- [Agent approvals & security](paper-catalog.md#p173)
- [git-worktree - Manage multiple working trees](paper-catalog.md#p174)
- [Security Model](paper-catalog.md#p175)
- [Security](paper-catalog.md#p176)
- [Defeating Prompt Injections by Design](paper-catalog.md#p177)
- [Scaling the Practice of Architecture, Conversationally](paper-catalog.md#p178)
- [Building multi-agent systems: When and how to use them](paper-catalog.md#p179)
- [How we built our multi-agent research system](paper-catalog.md#p180)
- [Continuous Integration](paper-catalog.md#p181)
- [The Architect Elevator — Visiting the upper floors](paper-catalog.md#p182)
- [NanmiCoder/dsh-agent-teams — AgentTeams plugin for DeepSeek Harness](paper-catalog.md#p183)
- [Branch By Abstraction](paper-catalog.md#p184)


### 机制与可信解释（18）

细分：

- [OLMo: Accelerating the Science of Language Models](paper-catalog.md#p010)
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](paper-catalog.md#p022)
- [In-context Learning and Induction Heads](paper-catalog.md#p025)
- [Transformer Feed-Forward Layers Are Key-Value Memories](paper-catalog.md#p026)
- [Locating and Editing Factual Associations in GPT](paper-catalog.md#p027)
- [Naturalness of Attention: Revisiting Attention in Code Language Models](paper-catalog.md#p028)
- [Probing Pretrained Models of Source Code](paper-catalog.md#p029)
- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](paper-catalog.md#p030)
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](paper-catalog.md#p031)
- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](paper-catalog.md#p032)
- [On scalable oversight with weak LLMs judging strong LLMs](paper-catalog.md#p033)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036)
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](paper-catalog.md#p037)
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](paper-catalog.md#p038)
- [Training Compute Optimal Large Language Models](paper-catalog.md#p114)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](paper-catalog.md#p118)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)

### 生物计算探索（0）

细分：


### 评估与监督可靠性（10）

细分：性质测试、变形测试与行为验证边界

- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](paper-catalog.md#p030)
- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](paper-catalog.md#p032)
- [On scalable oversight with weak LLMs judging strong LLMs](paper-catalog.md#p033)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036)
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](paper-catalog.md#p037)
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](paper-catalog.md#p038)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](paper-catalog.md#p118)
- [Finding bugs across the Python ecosystem with Claude and property-based testing](paper-catalog.md#p160)
- [Metamorphic Testing of Multi-Agent LLM Systems: A Trace-Based Behavioral Oracle Framework](paper-catalog.md#p161)


### 知识蒸馏与模型压缩（4）

细分：输出分布与软目标；中间特征与提示监督；教师学生迁移；模型压缩历史与来源边界

- [Model Compression](paper-catalog.md#p140)
- [Do Deep Nets Really Need to be Deep?](paper-catalog.md#p141)
- [FitNets: Hints for Thin Deep Nets](paper-catalog.md#p142)
- [Distilling the Knowledge in a Neural Network](paper-catalog.md#p143)

### 工程探索（临时线索）（4）

细分：高速电子器件设计与应用（探索）

仅作临时探索分类，不表示长期方向或已实施硬件项目。

- [MT-097: Dealing with High-Speed Logic](paper-catalog.md#p185)
- [MT-046: Op Amp Settling Time](paper-catalog.md#p186)
- [High-Speed Layout Guidelines (SCAA082A)](paper-catalog.md#p187)
- [High-Speed Interface Layout Guidelines (SPRAAR7J, Rev. J)](paper-catalog.md#p188)

## 正交标签

- architecture：Transformer, ViT, state-space, MoE, dual-encoder, world-model, diffusion, flow
- supervision：supervised, contrastive, masked-reconstruction, generative-prediction, self-distillation, preference, reinforcement-learning, imitation, distillation, feature-hint supervision
- evidence_origin：user-provided-exact-link, assistant-provided-exact-link, chat-name-resolved, previous-starter, handbook-only, unresolved, new-baseline-selection
- method：inference-time search, sampling, prompting, pruning
- evaluation：probing, causal analysis, faithfulness, LLM judge
- modality：text, image, video, audio, depth, LiDAR, IMU, action
- task：representation, alignment, generation, dynamics-prediction, localization-mapping, navigation, control, manipulation
