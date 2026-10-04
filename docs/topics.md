# 研究主题目录

研究问题为主分类；架构、监督信号、模态和聊天来源为正交标签。一个条目可跨方向引用，不重复计数。

[论文总目录](paper-catalog.md) · [待核实条目](unresolved.md)

## 标签词表

模态和任务类型不建目录，用 `papers.json` 的 `modality_tags`、`task_tags` 表达（[STYLE.md §15](../STYLE.md#15-目录与标签)）。一篇论文可以有多个标签。文末的[按模态与任务的交叉目录](#按模态与任务的交叉目录)由脚本从这两个字段生成。

| 字段 | 标签 | 含义 |
|---|---|---|
| modality_tags | text | 自然语言文本 |
| | image | 单帧视觉输入，包括 RGB、深度图、高程图等几何感知 |
| | video | 时序视觉输入，包括视频和 3D 占据序列 |
| | audio | 语音与音频 |
| | action | 机器人动作、控制指令、运动轨迹 |
| | state | 本体状态、IMU、力觉等传感器时序 |
| | code | 源代码 |
| | multimodal | 视觉与语言（或音频）联合建模，例如图文对齐、VLM、VLA、语言条件的世界模型；视觉与惯性的传感器融合记为 image + state |
| | tabular | 结构化表格特征，词表的补充项，目前只有 [Model Compression](paper-catalog.md#p140) 使用 |
| task_tags | understanding | 理解、表示、判别、状态估计与建图 |
| | generation | 生成文本、图像、视频、动作序列，包括预测未来观测或未来表征的世界模型 |
| | decision | 决策、控制、规划、Agent 行动 |
| | evaluation | 评估方法、benchmark、评审模型 |
| | analysis | 分析模型本身：机制、探针、规模与训练规律、表示空间比较 |

task 标签写论文的方法服务于哪类任务；论文的主要贡献是分析或评估时，加 analysis 或 evaluation。

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

### 架构与效率（18）

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
- [Frozen Memory Is Not Enough: Rethinking External Memory as Extraction](paper-catalog.md#p017)
- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](paper-catalog.md#p020)
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021)
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](paper-catalog.md#p022)
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024)
- [Naturalness of Attention: Revisiting Attention in Code Language Models](paper-catalog.md#p028)
- [Attention Is All You Need](paper-catalog.md#p113)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)
- [Resurrecting Recurrent Neural Networks for Long Sequences](paper-catalog.md#p163)

### 推理时计算（29）

细分：搜索与验证；多路径与多 Agent；预算分配与 token 效率；精确目标分布与投机验证；近似质量协作与关键段接管；MTP草拟与验证接口；精确级联混合分布

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](paper-catalog.md#p001)
- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](paper-catalog.md#p002)
- [s1: Simple test-time scaling](paper-catalog.md#p003)
- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](paper-catalog.md#p004)
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007)
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


### 运动控制（41）

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
- [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](paper-catalog.md#p165)
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](paper-catalog.md#p166)
- [Extreme Parkour with Legged Robots](paper-catalog.md#p167)
- [Robot Parkour Learning](paper-catalog.md#p168)
- [CaT: Constraints as Terminations for Legged Locomotion Reinforcement Learning](paper-catalog.md#p169)
- [Prioritized Experience Replay](paper-catalog.md#p170)
- [First return, then explore](paper-catalog.md#p171)


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

### Agent 与上下文系统（12）

细分：Agent轨迹与性质验证

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


### 模型科学（18）

细分：机制可解释性；知识存储、定位与编辑；探针分析；推理忠实性；层冗余与模式坍缩；开放模型与可复现性

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
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](paper-catalog.md#p118)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)
- [Dissecting Recall of Factual Associations in Auto-Regressive Language Models](paper-catalog.md#p164)

### 训练科学（1）

细分：规模定律；优化地形；训练动态；双下降；本征维度与参数有效性；遗忘

- [Training Compute-Optimal Large Language Models](paper-catalog.md#p114)


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

## 正交标签

- architecture：Transformer, ViT, state-space, MoE, dual-encoder, world-model, diffusion, flow
- supervision：supervised, contrastive, masked-reconstruction, generative-prediction, self-distillation, preference, reinforcement-learning, imitation, distillation, feature-hint supervision
- evidence_origin：user-provided-exact-link, assistant-provided-exact-link, chat-name-resolved, previous-starter, handbook-only, unresolved, new-baseline-selection
- method：inference-time search, sampling, prompting, pruning
- evaluation：probing, causal analysis, faithfulness, LLM judge
- modality：text, image, video, audio, action, state, code, multimodal, tabular（定义见文首「标签词表」）
- task：understanding, generation, decision, evaluation, analysis（定义见文首「标签词表」）

## 按模态与任务的交叉目录

本节由脚本从 `papers.json` 的 `modality_tags` × `task_tags` 生成，不手工编辑。一篇论文按它的每个标签组合出现，所以各格相加大于论文总数。格中数字是篇数，点击跳到对应小节。

| 模态 \ 任务 | understanding | generation | decision | evaluation | analysis |
|---|---:|---:|---:|---:|---:|
| text | [11](#x-text-understanding) | [45](#x-text-generation) | [30](#x-text-decision) | [7](#x-text-evaluation) | [12](#x-text-analysis) |
| image | [24](#x-image-understanding) | [7](#x-image-generation) | [48](#x-image-decision) | [3](#x-image-evaluation) | · |
| video | [4](#x-video-understanding) | [13](#x-video-generation) | [15](#x-video-decision) | [1](#x-video-evaluation) | [2](#x-video-analysis) |
| audio | [2](#x-audio-understanding) | [1](#x-audio-generation) | · | · | · |
| action | [6](#x-action-understanding) | [17](#x-action-generation) | [81](#x-action-decision) | [3](#x-action-evaluation) | [2](#x-action-analysis) |
| state | [7](#x-state-understanding) | [2](#x-state-generation) | [46](#x-state-decision) | [1](#x-state-evaluation) | · |
| code | [1](#x-code-understanding) | [3](#x-code-generation) | [3](#x-code-decision) | [2](#x-code-evaluation) | [3](#x-code-analysis) |
| multimodal | [7](#x-multimodal-understanding) | [4](#x-multimodal-generation) | [26](#x-multimodal-decision) | [1](#x-multimodal-evaluation) | · |
| tabular | [1](#x-tabular-understanding) | · | · | · | · |

<a id="x-text-understanding"></a>

### text × understanding（11）

- [MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers](paper-catalog.md#p020)
- [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](paper-catalog.md#p021)
- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](paper-catalog.md#p109)
- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Learning Transferable Visual Models From Natural Language Supervision](paper-catalog.md#p132)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)
- [Resurrecting Recurrent Neural Networks for Long Sequences](paper-catalog.md#p163)

<a id="x-text-generation"></a>

### text × generation（45）

- [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](paper-catalog.md#p001)
- [Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning](paper-catalog.md#p002)
- [s1: Simple test-time scaling](paper-catalog.md#p003)
- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](paper-catalog.md#p004)
- [Qwen2 Technical Report](paper-catalog.md#p005)
- [Qwen2.5 Technical Report](paper-catalog.md#p006)
- [DeepSeek-V3 Technical Report](paper-catalog.md#p007)
- [Qwen2.5-1M Technical Report](paper-catalog.md#p008)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009)
- [OLMo: Accelerating the Science of Language Models](paper-catalog.md#p010)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](paper-catalog.md#p011)
- [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](paper-catalog.md#p012)
- [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](paper-catalog.md#p013)
- [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](paper-catalog.md#p014)
- [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](paper-catalog.md#p015)
- [Tokenizer-Agnostic Engram Module](paper-catalog.md#p016)
- [Frozen Memory Is Not Enough: Rethinking External Memory as Extraction](paper-catalog.md#p017)
- [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](paper-catalog.md#p018)
- [Recursive Introspection: Teaching Language Model Agents How to Self-Improve](paper-catalog.md#p019)
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](paper-catalog.md#p022)
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](paper-catalog.md#p023)
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](paper-catalog.md#p031)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](paper-catalog.md#p035)
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036)
- [Self-Discover: Large Language Models Self-Compose Reasoning Structures](paper-catalog.md#p039)
- [ReAct: Synergizing Reasoning and Acting in Language Models](paper-catalog.md#p040)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Attention Is All You Need](paper-catalog.md#p113)
- [Training Compute-Optimal Large Language Models](paper-catalog.md#p114)
- [Training language models to follow instructions with human feedback](paper-catalog.md#p115)
- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Video Diffusion Models](paper-catalog.md#p122)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](paper-catalog.md#p128)
- [Fast Inference from Transformers via Speculative Decoding](paper-catalog.md#p144)
- [Accelerating Large Language Model Decoding with Speculative Sampling](paper-catalog.md#p145)
- [EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test](paper-catalog.md#p146)
- [DFlash: Block Diffusion for Flash Speculative Decoding](paper-catalog.md#p147)
- [Speculative Decoding with Big Little Decoder](paper-catalog.md#p148)
- [RelayLLM: Efficient Reasoning via Collaborative Decoding](paper-catalog.md#p149)
- [Judge Decoding: Faster Speculative Sampling Requires Going Beyond Model Alignment](paper-catalog.md#p150)
- [DFlash 2: Keep Drafting Parallel](paper-catalog.md#p151)
- [Faster Cascades via Speculative Decoding](paper-catalog.md#p152)

<a id="x-text-decision"></a>

### text × decision（30）

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)
- [ReAct: Synergizing Reasoning and Acting in Language Models](paper-catalog.md#p040)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](paper-catalog.md#p041)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](paper-catalog.md#p058)
- [RT-1: Robotics Transformer for Real-World Control at Scale](paper-catalog.md#p064)
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](paper-catalog.md#p065)
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](paper-catalog.md#p066)
- [Octo: An Open-Source Generalist Robot Policy](paper-catalog.md#p068)
- [OpenVLA: An Open-Source Vision-Language-Action Model](paper-catalog.md#p069)
- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](paper-catalog.md#p070)
- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](paper-catalog.md#p071)
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](paper-catalog.md#p072)
- [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](paper-catalog.md#p073)
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](paper-catalog.md#p074)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075)
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076)
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](paper-catalog.md#p077)
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Learning from Massive Human Videos for Universal Humanoid Pose Control](paper-catalog.md#p096)
- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](paper-catalog.md#p135)
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](paper-catalog.md#p136)
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](paper-catalog.md#p137)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)
- [Finding bugs across the Python ecosystem with Claude and property-based testing](paper-catalog.md#p160)

<a id="x-text-evaluation"></a>

### text × evaluation（7）

- [PersonaEval: Are LLM Evaluators Human Enough to Judge Role-Play?](paper-catalog.md#p032)
- [On scalable oversight with weak LLMs judging strong LLMs](paper-catalog.md#p033)
- [Reasoning Does Not Necessarily Improve Role-Playing Ability](paper-catalog.md#p038)
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](paper-catalog.md#p118)
- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Finding bugs across the Python ecosystem with Claude and property-based testing](paper-catalog.md#p160)
- [Metamorphic Testing of Multi-Agent LLM Systems: A Trace-Based Behavioral Oracle Framework](paper-catalog.md#p161)

<a id="x-text-analysis"></a>

### text × analysis（12）

- [OLMo: Accelerating the Science of Language Models](paper-catalog.md#p010)
- [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect](paper-catalog.md#p022)
- [In-context Learning and Induction Heads](paper-catalog.md#p025)
- [Transformer Feed-Forward Layers Are Key-Value Memories](paper-catalog.md#p026)
- [Locating and Editing Factual Associations in GPT](paper-catalog.md#p027)
- [Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity](paper-catalog.md#p031)
- [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](paper-catalog.md#p035)
- [Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning](paper-catalog.md#p036)
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](paper-catalog.md#p037)
- [Training Compute-Optimal Large Language Models](paper-catalog.md#p114)
- [Language Models are Few-Shot Learners](paper-catalog.md#p127)
- [Dissecting Recall of Factual Associations in Auto-Regressive Language Models](paper-catalog.md#p164)

<a id="x-image-understanding"></a>

### image × understanding（24）

- [FOCUS: Object-Centric World Models for Robotics Manipulation](paper-catalog.md#p048)
- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](paper-catalog.md#p054)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [SemanticFusion: Dense 3D Semantic Mapping with Convolutional Neural Networks](paper-catalog.md#p080)
- [PanopticFusion: Online Volumetric Semantic Mapping at the Level of Stuff and Things](paper-catalog.md#p081)
- [DS-VIO: Robust and Efficient Stereo Visual Inertial Odometry based on Dual Stage EKF](paper-catalog.md#p082)
- [PLV-IEKF: Consistent Visual-Inertial Odometry using Points, Lines, and Vanishing Points](paper-catalog.md#p083)
- [EqVIO: An Equivariant Filter for Visual Inertial Odometry](paper-catalog.md#p084)
- [A Self-Supervised, Differentiable Kalman Filter for Uncertainty-Aware Visual-Inertial Odometry](paper-catalog.md#p085)
- [Learned IMU Bias Prediction for Invariant Visual Inertial Odometry](paper-catalog.md#p086)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Dense RGB-D Semantic Mapping with Pixel-Voxel Neural Network](paper-catalog.md#p108)
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](paper-catalog.md#p109)
- [Visual Instruction Tuning](paper-catalog.md#p120)
- [ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](paper-catalog.md#p123)
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](paper-catalog.md#p130)
- [Masked Autoencoders Are Scalable Vision Learners](paper-catalog.md#p131)
- [Learning Transferable Visual Models From Natural Language Supervision](paper-catalog.md#p132)
- [Emerging Properties in Self-Supervised Vision Transformers](paper-catalog.md#p133)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)
- [Do Deep Nets Really Need to be Deep?](paper-catalog.md#p141)
- [FitNets: Hints for Thin Deep Nets](paper-catalog.md#p142)
- [Distilling the Knowledge in a Neural Network](paper-catalog.md#p143)
- [Resurrecting Recurrent Neural Networks for Long Sequences](paper-catalog.md#p163)

<a id="x-image-generation"></a>

### image × generation（7）

- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](paper-catalog.md#p046)
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](paper-catalog.md#p049)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117)
- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Denoising Diffusion Probabilistic Models](paper-catalog.md#p121)

<a id="x-image-decision"></a>

### image × decision（48）

- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](paper-catalog.md#p046)
- [FOCUS: Object-Centric World Models for Robotics Manipulation](paper-catalog.md#p048)
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](paper-catalog.md#p049)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](paper-catalog.md#p054)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](paper-catalog.md#p058)
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
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075)
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076)
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](paper-catalog.md#p077)
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079)
- [RoboTTT: Context Scaling for Robot Policies](paper-catalog.md#p087)
- [In-Context Imitation Learning via Next-Token Prediction](paper-catalog.md#p088)
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](paper-catalog.md#p089)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Attention-Based Map Encoding for Learning Generalized Legged Locomotion](paper-catalog.md#p100)
- [Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding](paper-catalog.md#p101)
- [PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots](paper-catalog.md#p107)
- [Legged Locomotion in Challenging Terrains using Egocentric Vision](paper-catalog.md#p111)
- [MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion](paper-catalog.md#p112)
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117)
- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Proximal Policy Optimization Algorithms](paper-catalog.md#p129)
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](paper-catalog.md#p135)
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](paper-catalog.md#p136)
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](paper-catalog.md#p137)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)
- [Recovery RL: Safe Reinforcement Learning With Learned Recovery Zones](paper-catalog.md#p155)
- [Learning robust perceptive locomotion for quadrupedal robots in the wild](paper-catalog.md#p156)
- [Prioritized Level Replay](paper-catalog.md#p157)
- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](paper-catalog.md#p162)
- [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](paper-catalog.md#p165)
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](paper-catalog.md#p166)
- [Extreme Parkour with Legged Robots](paper-catalog.md#p167)
- [Robot Parkour Learning](paper-catalog.md#p168)
- [Prioritized Experience Replay](paper-catalog.md#p170)
- [First return, then explore](paper-catalog.md#p171)

<a id="x-image-evaluation"></a>

### image × evaluation（3）

- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](paper-catalog.md#p060)
- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](paper-catalog.md#p166)

<a id="x-video-understanding"></a>

### video × understanding（4）

- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](paper-catalog.md#p042)
- [SAVi++: Towards End-to-End Object-Centric Learning from Real-World Videos](paper-catalog.md#p043)
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](paper-catalog.md#p062)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)

<a id="x-video-generation"></a>

### video × generation（13）

- [SlotFormer: Unsupervised Visual Dynamics Simulation with Object-Centric Models](paper-catalog.md#p042)
- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](paper-catalog.md#p044)
- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](paper-catalog.md#p045)
- [Back to the Features: DINO as a Foundation for Video World Models](paper-catalog.md#p047)
- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](paper-catalog.md#p050)
- [A Survey of World Models for Autonomous Driving](paper-catalog.md#p051)
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](paper-catalog.md#p053)
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](paper-catalog.md#p056)
- [Hydra-0: Action Flow for Generalist World Modeling and Control](paper-catalog.md#p057)
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [World Models for Robotic Manipulation: A Survey](paper-catalog.md#p063)
- [Video Diffusion Models](paper-catalog.md#p122)
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](paper-catalog.md#p134)

<a id="x-video-decision"></a>

### video × decision（15）

- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](paper-catalog.md#p044)
- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](paper-catalog.md#p045)
- [Back to the Features: DINO as a Foundation for Video World Models](paper-catalog.md#p047)
- [A Survey of World Models for Autonomous Driving](paper-catalog.md#p051)
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](paper-catalog.md#p053)
- [Hydra-0: Action Flow for Generalist World Modeling and Control](paper-catalog.md#p057)
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](paper-catalog.md#p058)
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](paper-catalog.md#p062)
- [World Models for Robotic Manipulation: A Survey](paper-catalog.md#p063)
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)
- [RoboTTT: Context Scaling for Robot Policies](paper-catalog.md#p087)
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](paper-catalog.md#p089)
- [Learning from Massive Human Videos for Universal Humanoid Pose Control](paper-catalog.md#p096)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)

<a id="x-video-evaluation"></a>

### video × evaluation（1）

- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](paper-catalog.md#p060)

<a id="x-video-analysis"></a>

### video × analysis（2）

- [What Do Latent Action Models Actually Learn?](paper-catalog.md#p059)
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](paper-catalog.md#p134)

<a id="x-audio-understanding"></a>

### audio × understanding（2）

- [Do Deep Nets Really Need to be Deep?](paper-catalog.md#p141)
- [Distilling the Knowledge in a Neural Network](paper-catalog.md#p143)

<a id="x-audio-generation"></a>

### audio × generation（1）

- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](paper-catalog.md#p009)

<a id="x-action-understanding"></a>

### action × understanding（6）

- [FOCUS: Object-Centric World Models for Robotics Manipulation](paper-catalog.md#p048)
- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](paper-catalog.md#p054)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](paper-catalog.md#p062)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)

<a id="x-action-generation"></a>

### action × generation（17）

- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](paper-catalog.md#p044)
- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](paper-catalog.md#p045)
- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](paper-catalog.md#p046)
- [Back to the Features: DINO as a Foundation for Video World Models](paper-catalog.md#p047)
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](paper-catalog.md#p049)
- [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](paper-catalog.md#p050)
- [A Survey of World Models for Autonomous Driving](paper-catalog.md#p051)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](paper-catalog.md#p053)
- [EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](paper-catalog.md#p056)
- [Hydra-0: Action Flow for Generalist World Modeling and Control](paper-catalog.md#p057)
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [World Models for Robotic Manipulation: A Survey](paper-catalog.md#p063)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](paper-catalog.md#p105)
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117)
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](paper-catalog.md#p134)

<a id="x-action-decision"></a>

### action × decision（81）

- [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](paper-catalog.md#p044)
- [Driving in the Occupancy World: Vision-Centric 4D Occupancy Forecasting and Planning via World Models for Autonomous Driving](paper-catalog.md#p045)
- [DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning](paper-catalog.md#p046)
- [Back to the Features: DINO as a Foundation for Video World Models](paper-catalog.md#p047)
- [FOCUS: Object-Centric World Models for Robotics Manipulation](paper-catalog.md#p048)
- [LaDi-WM: A Latent Diffusion-based World Model for Predictive Manipulation](paper-catalog.md#p049)
- [A Survey of World Models for Autonomous Driving](paper-catalog.md#p051)
- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [Learning Physics-Guided Residual Dynamics for Deformable Object Simulation](paper-catalog.md#p053)
- [A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting](paper-catalog.md#p054)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [Hydra-0: Action Flow for Generalist World Modeling and Control](paper-catalog.md#p057)
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](paper-catalog.md#p058)
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](paper-catalog.md#p061)
- [PIN-WM: Learning Physics-INformed World Models for Non-Prehensile Manipulation](paper-catalog.md#p062)
- [World Models for Robotic Manipulation: A Survey](paper-catalog.md#p063)
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
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075)
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076)
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](paper-catalog.md#p077)
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079)
- [RoboTTT: Context Scaling for Robot Policies](paper-catalog.md#p087)
- [In-Context Imitation Learning via Next-Token Prediction](paper-catalog.md#p088)
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](paper-catalog.md#p089)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
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
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117)
- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](paper-catalog.md#p124)
- [Sampling-based Algorithms for Optimal Motion Planning](paper-catalog.md#p126)
- [Proximal Policy Optimization Algorithms](paper-catalog.md#p129)
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](paper-catalog.md#p135)
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](paper-catalog.md#p136)
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](paper-catalog.md#p137)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)
- [Learning Quadrupedal Locomotion over Challenging Terrain](paper-catalog.md#p153)
- [Robust Recovery Controller for a Quadrupedal Robot using Deep Reinforcement Learning](paper-catalog.md#p154)
- [Recovery RL: Safe Reinforcement Learning With Learned Recovery Zones](paper-catalog.md#p155)
- [Learning robust perceptive locomotion for quadrupedal robots in the wild](paper-catalog.md#p156)
- [Prioritized Level Replay](paper-catalog.md#p157)
- [Robust Quadrupedal Locomotion via Risk-Averse Policy Learning](paper-catalog.md#p158)
- [Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning](paper-catalog.md#p159)
- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](paper-catalog.md#p162)
- [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](paper-catalog.md#p165)
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](paper-catalog.md#p166)
- [Extreme Parkour with Legged Robots](paper-catalog.md#p167)
- [Robot Parkour Learning](paper-catalog.md#p168)
- [CaT: Constraints as Terminations for Legged Locomotion Reinforcement Learning](paper-catalog.md#p169)
- [Prioritized Experience Replay](paper-catalog.md#p170)
- [First return, then explore](paper-catalog.md#p171)

<a id="x-action-evaluation"></a>

### action × evaluation（3）

- [LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment](paper-catalog.md#p060)
- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](paper-catalog.md#p166)

<a id="x-action-analysis"></a>

### action × analysis（2）

- [What Do Latent Action Models Actually Learn?](paper-catalog.md#p059)
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](paper-catalog.md#p134)

<a id="x-state-understanding"></a>

### state × understanding（7）

- [DS-VIO: Robust and Efficient Stereo Visual Inertial Odometry based on Dual Stage EKF](paper-catalog.md#p082)
- [PLV-IEKF: Consistent Visual-Inertial Odometry using Points, Lines, and Vanishing Points](paper-catalog.md#p083)
- [EqVIO: An Equivariant Filter for Visual Inertial Odometry](paper-catalog.md#p084)
- [A Self-Supervised, Differentiable Kalman Filter for Uncertainty-Aware Visual-Inertial Odometry](paper-catalog.md#p085)
- [Learned IMU Bias Prediction for Invariant Visual Inertial Odometry](paper-catalog.md#p086)
- [ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](paper-catalog.md#p123)
- [Quaternion kinematics for the error-state Kalman filter](paper-catalog.md#p125)

<a id="x-state-generation"></a>

### state × generation（2）

- [BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](paper-catalog.md#p105)
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117)

<a id="x-state-decision"></a>

### state × decision（46）

- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](paper-catalog.md#p067)
- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](paper-catalog.md#p070)
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](paper-catalog.md#p072)
- [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](paper-catalog.md#p073)
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](paper-catalog.md#p074)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075)
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076)
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079)
- [In-Context Imitation Learning via Next-Token Prediction](paper-catalog.md#p088)
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
- [Mastering Diverse Domains through World Models](paper-catalog.md#p117)
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](paper-catalog.md#p124)
- [Sampling-based Algorithms for Optimal Motion Planning](paper-catalog.md#p126)
- [Proximal Policy Optimization Algorithms](paper-catalog.md#p129)
- [Learning Quadrupedal Locomotion over Challenging Terrain](paper-catalog.md#p153)
- [Robust Recovery Controller for a Quadrupedal Robot using Deep Reinforcement Learning](paper-catalog.md#p154)
- [Recovery RL: Safe Reinforcement Learning With Learned Recovery Zones](paper-catalog.md#p155)
- [Learning robust perceptive locomotion for quadrupedal robots in the wild](paper-catalog.md#p156)
- [Robust Quadrupedal Locomotion via Risk-Averse Policy Learning](paper-catalog.md#p158)
- [Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning](paper-catalog.md#p159)
- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](paper-catalog.md#p162)
- [Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](paper-catalog.md#p165)
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](paper-catalog.md#p166)
- [Extreme Parkour with Legged Robots](paper-catalog.md#p167)
- [Robot Parkour Learning](paper-catalog.md#p168)
- [CaT: Constraints as Terminations for Legged Locomotion Reinforcement Learning](paper-catalog.md#p169)

<a id="x-state-evaluation"></a>

### state × evaluation（1）

- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](paper-catalog.md#p166)

<a id="x-code-understanding"></a>

### code × understanding（1）

- [GraphCodeBERT: Pre-training Code Representations with Data Flow](paper-catalog.md#p024)

<a id="x-code-generation"></a>

### code × generation（3）

- [Large Language Monkeys: Scaling Inference Compute with Repeated Sampling](paper-catalog.md#p004)
- [Enhancing Code Generation Performance of Smaller Models by Distilling the Reasoning Ability of LLMs](paper-catalog.md#p023)
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)

<a id="x-code-decision"></a>

### code × decision（3）

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](paper-catalog.md#p034)
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](paper-catalog.md#p041)
- [Finding bugs across the Python ecosystem with Claude and property-based testing](paper-catalog.md#p160)

<a id="x-code-evaluation"></a>

### code × evaluation（2）

- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](paper-catalog.md#p030)
- [Finding bugs across the Python ecosystem with Claude and property-based testing](paper-catalog.md#p160)

<a id="x-code-analysis"></a>

### code × analysis（3）

- [Naturalness of Attention: Revisiting Attention in Code Language Models](paper-catalog.md#p028)
- [Probing Pretrained Models of Source Code](paper-catalog.md#p029)
- [INSPECT: Intrinsic and Systematic Probing Evaluation for Code Transformers](paper-catalog.md#p030)

<a id="x-multimodal-understanding"></a>

### multimodal × understanding（7）

- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [FM-Fusion: Instance-aware Semantic Mapping Boosted by Vision-Language Foundation Models](paper-catalog.md#p109)
- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Learning Transferable Visual Models From Natural Language Supervision](paper-catalog.md#p132)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)

<a id="x-multimodal-generation"></a>

### multimodal × generation（4）

- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Visual Instruction Tuning](paper-catalog.md#p120)
- [Video Diffusion Models](paper-catalog.md#p122)

<a id="x-multimodal-decision"></a>

### multimodal × decision（26）

- [Object-Centric World Model for Language-Guided Manipulation](paper-catalog.md#p052)
- [Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs](paper-catalog.md#p055)
- [UniVLA: Learning to Act Anywhere with Task-centric Latent Actions](paper-catalog.md#p058)
- [RT-1: Robotics Transformer for Real-World Control at Scale](paper-catalog.md#p064)
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](paper-catalog.md#p065)
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](paper-catalog.md#p066)
- [Octo: An Open-Source Generalist Robot Policy](paper-catalog.md#p068)
- [OpenVLA: An Open-Source Vision-Language-Action Model](paper-catalog.md#p069)
- [$π_0$: A Vision-Language-Action Flow Model for General Robot Control](paper-catalog.md#p070)
- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](paper-catalog.md#p071)
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](paper-catalog.md#p072)
- [$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization](paper-catalog.md#p073)
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](paper-catalog.md#p074)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](paper-catalog.md#p075)
- [$π_{0.7}$: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](paper-catalog.md#p076)
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](paper-catalog.md#p077)
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](paper-catalog.md#p078)
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](paper-catalog.md#p079)
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](paper-catalog.md#p090)
- [Learning from Massive Human Videos for Universal Humanoid Pose Control](paper-catalog.md#p096)
- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)
- [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](paper-catalog.md#p135)
- [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](paper-catalog.md#p136)
- [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](paper-catalog.md#p137)
- [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](paper-catalog.md#p138)
- [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](paper-catalog.md#p139)

<a id="x-multimodal-evaluation"></a>

### multimodal × evaluation（1）

- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](paper-catalog.md#p119)

<a id="x-tabular-understanding"></a>

### tabular × understanding（1）

- [Model Compression](paper-catalog.md#p140)
