# VLA 论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [逐步讲义](../vla.md)

按[入门页](README.md)主线历史的阶段排列；每篇链接到唯一的单篇目录，"格"指它在 [Baseline 表](BASELINES.md)中的位置。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 1 多任务真机示教（2022）

- [RT-1: Robotics Transformer for Real-World Control at Scale](../../papers/arxiv-2212.06817/README.md) · 2022 · Google · 文献卡 · 格：动作表示 = 离散 token（前 VLA 参照）

## 2 动作当作词与跨机器人数据（2023）

- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](../../papers/arxiv-2307.15818/README.md) · 2023 · Google DeepMind · 文献卡 · 格：动作表示 = 离散 token（基线）
- [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](../../papers/arxiv-2310.08864/README.md) · 2023 · Open X-Embodiment Collaboration · 文献卡 · 格：数据 = 跨机器人数据集

## 3 开放的通用策略（2024）

- [Octo: An Open-Source Generalist Robot Policy](../../papers/arxiv-2405.12213/README.md) · 2024 · Berkeley、Stanford、CMU、Google DeepMind · 文献卡 · 格：动作表示 = 连续动作块（扩散头）；数据 = 跨机器人数据集
- [OpenVLA: An Open-Source Vision-Language-Action Model](../../papers/openvla/README.md) · 2024 · Stanford、Berkeley、TRI 等 · 技术精读 · 格：动作表示 = 离散 token（基线）；观测表示 = 拼接两种视觉编码器
- [In-Context Imitation Learning via Next-Token Prediction](../../papers/arxiv-2408.15980/README.md) · 2024 · Berkeley · 文献卡 · 格：任务条件 = 示教作提示

## 4 连续动作块（2024）

- [π0: A Vision-Language-Action Flow Model for General Robot Control](../../papers/arxiv-2410.24164/README.md) · 2024 · Physical Intelligence · 文献卡 · 格：动作表示 = 连续动作块（基线）

## 5 修补与分化（2025）

- [FAST: Efficient Action Tokenization for Vision-Language-Action Models](../../papers/arxiv-2501.09747/README.md) · 2025 · Physical Intelligence、Berkeley、Stanford · 文献卡 · 格：动作表示 = 压缩后的离散 token
- [Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success](../../papers/arxiv-2502.19645/README.md)（OpenVLA-OFT） · 2025 · Stanford · 文献卡 · 格：动作表示 = 并行解码 + L1 回归；观测表示 = 加腕部相机与本体状态
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](../../papers/arxiv-2503.14734/README.md) · 2025 · NVIDIA · 文献卡（归属控制方向，在此交叉引用） · 格：推理调度 = 双系统；数据 = 数据金字塔
- [Gemini Robotics: Bringing AI into the Physical World](../../papers/arxiv-2503.20020/README.md) · 2025 · Google DeepMind · 文献卡（官方技术报告） · 格：推理调度 = 云端大骨干 + 本地动作解码器
- [π0.5: a Vision-Language-Action Model with Open-World Generalization](../../papers/arxiv-2504.16054/README.md) · 2025 · Physical Intelligence · 文献卡（机制见[逐步讲义](../vla.md)） · 格：训练目标 = 离散与连续联合；任务条件 = 先生成子任务
- [Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better](../../papers/arxiv-2505.23705/README.md) · 2025 · Physical Intelligence · 文献卡 · 格：训练目标 = 联合并隔离梯度
- [ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation](../../papers/arxiv-2505.22159/README.md) · 2025 · 复旦、上海交大等 · 文献卡 · 格：观测表示 = 加力 / 力矩
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](../../papers/arxiv-2506.01844/README.md) · 2025 · Hugging Face 等 · 文献卡 · 格：数据 = 小模型 + 社区数据；推理调度 = 异步推理

## 6 从经验、示教与提示里继续学（2025 年底–2026）

- [Gemini Robotics 1.5: Pushing the Frontier of Generalist Robots with Advanced Embodied Reasoning, Thinking, and Motion Transfer](../../papers/arxiv-2510.03342/README.md) · 2025 · Google DeepMind · 文献卡（官方技术报告） · 格：任务条件 = 先写思考；数据 = 多本体统一
- [π*0.6: a VLA That Learns From Experience](../../papers/arxiv-2511.14759/README.md) · 2025 · Physical Intelligence · 文献卡（与模仿与强化学习方向共用） · 格：训练目标 = 从自主经验做 RL
- [SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](../../papers/arxiv-2509.09674/README.md) · 2025 · 文献卡（归属模仿与强化学习方向，在此交叉引用） · 格：训练目标 = 仿真中的 RL 微调
- [InternVLA-A1: Unifying Understanding, Generation and Action for Robotic Manipulation](../../papers/arxiv-2601.02456/README.md) · 2026 · 上海人工智能实验室等 · 文献卡 · 格：训练目标 = 加预测未来的生成目标
- [π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities](../../papers/arxiv-2604.15483/README.md) · 2026 · Physical Intelligence · 文献卡 · 格：任务条件 = 可引导的提示；观测表示 = 视频历史
- [Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](../../papers/arxiv-2605.30280/README.md) · 2026 · Qwen Team · 文献卡 · 格：数据 = 多来源统一；整体缩放
- [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](../../papers/arxiv-2606.14752/README.md) · 2026 · X Square Robot 等 · 文献卡 · 格：动作表示 = 与 VLM 语义对齐的离散 token
- [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](../../papers/arxiv-2606.30457/README.md) · 2026 · Stanford、Berkeley · 文献卡 · 格：任务条件 = 示教作提示
- [RoboTTT: Context Scaling for Robot Policies](../../papers/arxiv-2607.15275/README.md) · 2026 · NVIDIA、Stanford、UT Austin · 文献卡 · 格：观测表示 = 长上下文
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](../../papers/zero-wam/README.md) · 2026 · 选定章节讲解 · 格：任务条件 = 示教作提示；训练目标 = 预测未来

## 跨方向的前置与参照

- [Learning Transferable Visual Models From Natural Language Supervision](../../../multimodal/papers/clip/README.md)（CLIP） · 2021 · 技术精读 · 阅读顺序第 1 篇：SigLIP 的来源路线
- [Visual Instruction Tuning](../../../multimodal/papers/llava/README.md)（LLaVA） · 2023 · 技术精读 · 阅读顺序第 2 篇：视觉特征投影进语言模型的接口
- [Emerging Properties in Self-Supervised Vision Transformers](../../../multimodal/papers/dino/README.md)（DINO） · 2021 · 技术精读 · 阅读顺序第 3 篇：DINOv2 的前身
- [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](../../papers/diffusion-policy/README.md) · 2023 · 逐步教学版 · 连续动作块与扩散动作头的来源（归属模仿与强化学习方向）
- [Denoising Diffusion Probabilistic Models](../../../multimodal/papers/ddpm/README.md) · 2020 · 技术精读 · 扩散动作头的生成机制
- [Proximal Policy Optimization Algorithms](../../../llm/papers/ppo/README.md) · 2017 · 技术精读 · π*0.6 把它作为对照：flow matching 策略上的 PPO 需要很小的信赖域才稳定
- [Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](../../../multimodal/papers/arxiv-2605.06388/README.md) · 2026 · 文献卡 · 视觉潜空间该偏重建还是语义，与 VLA 的视觉骨干选择相关
- [Dynamic Locomotion in the MIT Cheetah 3 Through Convex Model-Predictive Control](../../papers/convex-mpc/README.md) · 2018 · 技术精读 · VLA 输出之下的经典控制层参照（归属控制方向）
