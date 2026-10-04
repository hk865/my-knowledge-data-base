# 2026-10-04：各方向从经典基线读到 2025–2026

[判断] 新论文最值得加入的位置，是旧路线留下了尚未回答的问题之处。训练科学需要接上新的对照实验，生成模型需要分清表示空间与采样器，机器人需要把离线能力接到闭环执行；已有近期解释链的方向继续保留经典基线。

这份阅读地图按问题选择后继论文，并说明保留原有内容的原因。“先读”指理解该方向的优先级；具体版本、原始来源和证据边界见链接文献卡与领域页。

## 先读这三处

1. [机器人感知](../robotics-embodied/fields/perception/README.md)：从单图与单帧能力，走到跨帧、语义和计算预算的取舍
2. [生成模型](../multimodal/fields/generation/README.md)：把潜在表示、去噪/流动过程和采样步数分开，再看 2025–2026 后继改了什么
3. [训练科学](../cross-domain/fields/training-science/README.md)：从“哪个优化器更好”转到调参是否公平、训练阶段怎样拆解、同一预算怎样比较

## 机器人与具身：从模块性能走到系统闭环

最明显的断点在感知路线图（止于 2024），以及导航、模仿/RL 路线图（尚未接上 2026）。定位建图和世界模型虽已有新论文，阅读路径仍需明确它们解决哪一层问题。

| 方向 | 原有覆盖与缺口 | 推荐与阅读顺序 / 保留理由 |
|---|---|---|
| [感知](../robotics-embodied/fields/perception/README.md) | 正文已有 SAM3、DA3、FoundationStereo，路线图停在 FM-Fusion/DA2 | 先读原 FoundationStereo，再读 [Fast-FoundationStereo（2025/2026）](../robotics-embodied/papers/arxiv-2512.11130/README.md) 与 [LAS2（2026）](../robotics-embodied/papers/arxiv-2606.24457/README.md)：比较迭代削减、特征使用与实时预算；SAM3/DA3 作为语义与几何对照 |
| [定位与建图](../robotics-embodied/fields/localization-mapping/README.md) | 正文已到 2026-09 AMB3R-SLAM，路线图尚未串起各自目标 | 依次 MASt3R-Fusion（2025）→ VGGT-SLAM2.0（2026）→ AMB3R-SLAM（2026），分别关注尺度、对齐和公里级运行；以 cuVSLAM（2025）作部署对照，均复用原卡 |
| [导航与规划](../robotics-embodied/fields/navigation-planning/README.md) | 主阅读顺序停在 DualVLN（2025），正文已有 2026 模型 | 先 DualVLN 理解高低层接口，再 ABot-N1 / Robostral Navigate（2026）比较模型输出与真机低层执行；补路线连接，复用原卡 |
| [控制与运动](../robotics-embodied/fields/control-locomotion/README.md) | 已有 2026 感知控制、全身跟踪与稀疏三维穿越，缺少生成器后训练对照 | 先按任务选 AME-2（2026）或 SONIC（2025/2026），再读 [Generate, Track, Improve（2026）](../robotics-embodied/papers/arxiv-2609.31577/README.md)：把运动生成与跟踪闭环用于更新生成器 |
| [模仿与强化学习](../robotics-embodied/fields/imitation-reinforcement-learning/README.md) | 正文已有 RL Token/EgoScale，路线图未到 2026 | π*0.6（2025）→ RL Token / EgoScale（2026）→ Generate, Track, Improve（2026）；分别问人工反馈、更新位置、数据来源和生成器反馈，避免把所有 RL 当成同一接口 |
| [世界模型](../robotics-embodied/fields/world-models/README.md) | 已有 2026 策略结合，缺少配方与规划范围诊断 | V-JEPA2（2025）→ [JEPA-WMs（2025/2026）](../robotics-embodied/papers/arxiv-2512.24497/README.md) → Cosmos Policy（2026）→ [Planning Limits（2026）](../robotics-embodied/papers/arxiv-2609.39235/README.md)；先看表示和规划配方，再检验可规划的范围 |
| [VLA](../robotics-embodied/fields/vla/README.md) | 已有 RTC（2025）、REALFAST（2026）和 9 月 IndustrialVLA-Bench，以及记忆与经验学习 | 保留同日已扩充内容；优先沿动作表示 → 实时调度 → 工业评测阅读 |
| [具身 Agents](../robotics-embodied/fields/embodied-agents/README.md) | 已从 SayCan/HiRobot 接到 2026 EmbodiedSkills、RoboSkill、MEMORA | 保留；先 HiRobot 理解分层，再比较技能复用、记忆和部署契约 |

机器人八份逐步机制讲义与经典算法基线保留。新的后继比较放在领域地图和路线图，既能沿原算法学会计算，也能知道下一篇为何值得读。

## LLM：补数据方法与蒸馏失效条件

预训练、架构、推理与长上下文的主体已经延伸到 2026；这次更值得补的是模型报告之间缺少的独立方法对照，以及 SFT 路线图漏掉的后继解释。

| 方向 | 原有覆盖与缺口 | 推荐与阅读顺序 |
|---|---|---|
| [预训练](../llm/fields/pretraining/README.md) | 架构与训练报告已到 2026，数据配方缺少独立实验路线 | 先 [DataDecide（2025）](../llm/papers/arxiv-2504.11393/README.md)：小实验怎样选择大训练的数据；再 [FineWeb2（2025）](../llm/papers/arxiv-2506.20920/README.md)：英语清洗方法怎样迁到多语言；最后 [MIR / SoftQ（2026）](../llm/papers/arxiv-2606.06888/README.md)：独立数据不足时怎样提高重复利用率 |
| [SFT](../llm/fields/posttraining/sft/README.md) | 正文已到 2026，路线图仍主要停在 2025 | 接原有 Rethinking OPD，再读 [OPD II（2026）](../llm/papers/arxiv-2609.04172/README.md)：教师在学生经过的状态上提供监督；再读 [Solving Without Stopping（2026）](../llm/papers/arxiv-2609.37326/README.md)：会解题与会停止是两个目标 |
| [架构与效率](../llm/fields/architecture/README.md) | 已有 Engram、Attention Residuals、V4/V4.1 和混合递推的 2026 解释链 | 保留，先沿页面中条件计算、条件记忆与序列混合三条路线读；Transformer、GQA、Mamba 继续定义比较接口 |
| [推理时计算](../llm/fields/inference/README.md) | 已有 DFlash、SSD、接受感知训练与近期草稿—验证讲义 | 保留，先读[草拟与验证](../llm/fields/inference/draft-verification-guide.md)，比较接受率与真实延迟，不重复新增卡片 |
| [长上下文](../llm/fields/long-context/README.md) | 已接到 2026-08/09 的混合、检索和缓存路线 | 保留，先看能输入多少、真正利用多少和执行成本三种口径；PI、YaRN、RULER 留作历史基线 |
| [偏好学习](../llm/fields/posttraining/preferences/README.md) | 已有生成式奖励、DeepSeekMath-V2、Olmo 3、V4 的 2025–2026 内容 | 保留，先区分奖励的来源与优化方式；InstructGPT、DPO 的价值在于定义后继修改的对象 |
| [语言模型 RL](../llm/fields/posttraining/rl/README.md) | 已有 DAPO、Dr.GRPO、ScaleRL、多域 RL 与 2026 沙箱/蒸馏 | 保留，沿奖励、采样、优化三个接口读；PPO、GRPO 为比较基线 |
| [后训练总览](../llm/fields/posttraining/README.md) | 已解释 2025–2026 奖励来源迁移和训练阶段分工 | 保留总图，新增的状态覆盖与停止行为放进 SFT 子方向，避免总览变成论文清单 |

## 多模态：表示、生成和时序分别补链

视觉表征已有 2026 后继，生成页的公司材料也已到 2026；真正需要接续的是图文对齐的数据范围、VLM 的视觉训练时机、生成的目标与表示、视频的时序取证，以及世界模型的动作接口。

| 方向 | 原有覆盖与缺口 | 推荐与阅读顺序 / 保留理由 |
|---|---|---|
| [视觉表征](../multimodal/fields/visual-representation/README.md) | 已有 DINOv3、V-JEPA2.1、C-RADIOv4、RADIO1D，机制节点到 2026-07 | 保留；先 DINOv3 看密集特征，再按视频、特征融合或 token 压缩的问题选后继 |
| [图文对齐](../multimodal/fields/alignment/README.md) | 已有 SigLIP2，数据链仍以英文 MetaCLIP 为主，缺混合模态检索 | [Meta CLIP 2（2025）](../multimodal/papers/arxiv-2507.22062/README.md) 看全球数据覆盖 → 原有 PE 看内部层读出 → [Qwen3-VL Embedding/Reranker（2026）](../multimodal/papers/arxiv-2601.04720/README.md) 看检索与重排分工 |
| [VLM](../multimodal/fields/vlm/README.md) | 主线停在 Qwen3-VL（2025），未接 LLM 目录已有 2026 模型 | 复用 Kimi K2.5、Qwen3.5、Kimi K3，分别比较视觉注入与初始化；再读 [Qwen3.8-Omni（2026）](../multimodal/papers/arxiv-2609.25611/README.md)，把音视频理解接到工具闭环 |
| [生成](../multimodal/fields/generation/README.md) | 产品材料已到 2026-06，机制路线容易停在 2024 配方 | [MeanFlow（2025）](../multimodal/papers/arxiv-2505.13447/README.md) 改平均速度目标以减少采样步数；另一路 [RAE（2025）](../multimodal/papers/arxiv-2510.11690/README.md) → [文生图 RAE（2026）](../multimodal/papers/arxiv-2601.16208/README.md) 比较表示空间与噪声调度。先分两条路线读，再组合理解 |
| [视频与时序](../multimodal/fields/video-temporal/README.md) | V-JEPA、Qwen2.5 的后继解释不足，缺局部时空特征和反复取证 | 先 V-JEPA2（2025）→ V-JEPA2.1（2026）看局部时空监督；再 Qwen3-VL（2025）→ [InternVideo3（2026）](../multimodal/papers/arxiv-2606.12195/README.md) 看长视频理解怎样变成主动取证 |
| [世界模型](../multimodal/fields/world-models/README.md) | 主线止于 Genie3/初代 Cosmos，缺 Dreamer 直接后继与统一动作接口 | DreamerV3 → [Dreamer4（2025）](../multimodal/papers/arxiv-2509.24527/README.md) 看模型内学习；[Cosmos Predict 2.5（2025）](../multimodal/papers/arxiv-2511.00062/README.md) → [Cosmos 3（2026）](../multimodal/papers/arxiv-2606.02800/README.md) 看视频、动作与场景接口；再回机器人页检查闭环与平台条件 |

LLaVA、DDPM、DreamerV3 三篇原有精读增加后继桥接，原始公式和历史实验保留。CLIP、DINO、MAE、ViT 和 Video Diffusion 已有近期出口，继续保留各自的教学目标。

## 跨方向：训练科学补新对照，其余按已有问题链继续读

| 方向 | 原有覆盖与缺口 | 推荐与阅读顺序 / 保留理由 |
|---|---|---|
| [训练科学](../cross-domain/fields/training-science/README.md) | 原主线最新到 2024，缺少优化规模化与阶段对照 | 先 [Moonlight（2025）](../llm/papers/arxiv-2502.16982/README.md)：矩阵更新怎样规模化；再 [Kimi K3（2026）](../llm/papers/arxiv-2607.24653/README.md)：各自调参后比较学习率调度；然后 [Olmo 3（2025）](../llm/papers/arxiv-2512.13961/README.md) 拆训练阶段，[Thinking-Optimal（2025）](../llm/papers/arxiv-2502.18080/README.md) 看推理长度的收益与成本。四篇均复用原卡 |
| [模型科学](../cross-domain/fields/model-science/README.md) | 已含 2025 FUR、2026 Engram 与 7–8 月记忆后继 | 保留，沿记忆放在哪里、如何读出和怎样验证机制来读；视觉内部机制继续作为明确开放问题 |
| [评估](../cross-domain/fields/evaluation/README.md) | 已有 2026 SWE-bench Verified 退役、隐藏验证器与多领域评测 | 保留，先读评测口径为何改变；经典污染与裁判实验提供解释基础 |
| [知识蒸馏](../cross-domain/fields/knowledge-distillation/README.md) | 已覆盖 2025 推理蒸馏、2026 多教师在线蒸馏及失败条件 | 保留主线，先看监督目标、学生状态与教师来源；此次 SFT 的后继读法可作补充 |
| [Agents](../cross-domain/fields/agents/README.md) | 已延伸到 2025–2026 奖励漏洞、越权、训练与评测；同日已补权限讲义及 CaMeL | 保留，先读[权限、隔离与协作](../cross-domain/fields/agents/permissions-isolation-collaboration.md)，再将能力与可执行权限分开比较 |
| [可解释性入口](../cross-domain/fields/interpretability/README.md) | 已转接模型科学，无独立过时主线 | 保留转接，集中维护同一问题链 |
| [工程探索](../cross-domain/fields/engineering-exploration/README.md) | 传播、回流、建立时间的基础机制 | 保留 ADI/TI 经典教程；实际器件选型再查相应新版手册，教程年份本身不构成缺口 |

## 基础：保留定义，把学习出口接到新研究

| 分区 | 本次处理与建议读法 |
|---|---|
| [架构](../foundations/fields/architectures/README.md) | 新增 2025 门控/混合递推与 2026 查表记忆出口；[Transformer 讲义](../foundations/lessons/14-attention-transformer.md) 先读原机制，再看哪些部分被替换 |
| [优化](../foundations/fields/optimization/README.md) | 已从 Moonlight 接到 2026 DeepSeek-V4/Kimi K3；SGD、Adam、Muon 的手算保留，规模化实验由训练科学承接 |
| [数据](../foundations/fields/data/README.md) | 已有 2025 改写与 2026 污染边界；训练/测试切分和样本接口定义保持，近期配方对照去预训练方向 |
| [目标函数](../foundations/fields/objectives/README.md) | 已有 2026 全词表反向 KL 与在线蒸馏；MSE、交叉熵、ELBO 继续承担基础定义 |
| [高级桥接](../foundations/fields/advanced/README.md) | 分布式 Muon、RL/蒸馏与迁移已连到 2025–2026；保留现有跨模块关系 |
| [VAE 讲义](../foundations/lessons/16-vae.md) | 新接 [RAE（2025）](../multimodal/papers/arxiv-2510.11690/README.md) → [文生图 RAE（2026）](../multimodal/papers/arxiv-2601.16208/README.md)：先问潜空间应保留什么，再看生成器怎样适配 |
| [扩散讲义](../foundations/lessons/17-diffusion.md) | 新接 [MeanFlow（2025）](../multimodal/papers/arxiv-2505.13447/README.md) 的平均速度一步生成，以及 2026 RAE 的潜空间噪声调度；分清减少采样步数和更换表示空间 |

CNN、RNN、LSTM、QKV、SSM/GNN/MoE 以及分布式、RL、迁移基础讲义保留其机制与算例。近期视觉能力由视觉表征方向承接，递推状态和注意力/FFN 关系页已经连到 2025–2026；重复向每章追加同一组新论文会削弱学习顺序。

## 批注

- [判断] 上述优先级按论文能否接续已有问题、是否提供独立对照或揭示失效条件排序，属于阅读建议。
- DataDecide 的目标规模、FineWeb2 的逐语言实验、MIR 的额外训练计算，均应随结论一起阅读。OPD II 的状态覆盖是相对于完整数据轨迹的语义聚类代理，仍依赖反复教师监督；Solving Without Stopping 的停止行为实验限于同一家族的小模型与数学任务。
- RAE 的正式会议 PDF 访问受限，相关机制使用已打开的 arXiv 版本；不据此引用未经核对的正式版数字或定理。
- 本次保留的方向已有近期解释链；保留并不表示重新逐项核验了全部历史事实，也不表示近期工作已经穷尽。新卡记录实际阅读章节，文献卡不等同于全文精读或复现。
