# 世界模型（机器人侧）的基线

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md) · [讲义](../world-models.md)

## 基线是谁、为什么是它

- **[DreamerV3](../../../multimodal/papers/dreamerv3/reading.md)（2023）。** 它定义了"在想象中学策略"的标准接口：输入是图像（及其他观测）、动作、奖励；RSSM 把观测编码成离散潜变量并按动作预测下一步，同时预测奖励与是否终止；actor-critic 只在模型展开的想象轨迹上训练，部署时直接用 actor。评估看最终策略的回报与样本效率。机制见[讲义](../world-models.md)第三至六节。
- **[DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md)（2024）。** 它定义了"部署时用模型规划"的另一种接口：编码器是冻结的 DINOv2，只训练一个预测未来图像块特征的 ViT；不预测奖励，测试时用 CEM 搜索动作序列，使预测特征接近目标图像的特征。评估看规划成功率与规划耗时。

两条基线对应入门页"从任务看"一表的用法 (a) 与 (b)。用法 (c)(d)(e) 的工作大多以视频生成模型为底座，在下表中按部件归位。

## 基线的结构拆分

| 部件 | DreamerV3 | DINO-WM |
|---|---|---|
| ① 观测表示 | 从像素学到的编码器 + 重建损失 | 冻结的 DINOv2 图像块特征，不重建像素（解码器可选、单独训练） |
| ② 动力学结构 | RSSM：确定的循环状态 + 离散随机潜变量 | 因果 ViT 预测器 |
| ③ 动作条件 | 每步动作输入循环状态 | 动作嵌入与特征拼接 |
| ④ 输出头与用法 | 奖励、终止、价值头；想象中训练 actor-critic | 无奖励头；CEM 规划到目标特征 |
| ⑤ 数据 | 在线与环境交互、每任务单独训练 | 离线轨迹，需动作覆盖充分 |
| ⑥ 评估 | 策略回报、样本效率 | 规划成功率、耗时、LPIPS |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| ①② | VAE + MDN-RNN，控制器在梦中训练 | [World Models](../../papers/arxiv-1803.10122/README.md) | 第一次完全在模型里学控制；控制器钻模型空子 |
| ② + ④ | RSSM + 潜空间 CEM 规划 | [PlaNet](../../papers/arxiv-1811.04551/README.md) | 基线 RSSM 的来源；规划需要大量候选 |
| ⑤ 数据 | 不用仿真器，直接在 4 台真机上在线学习 | [DayDreamer](../../papers/arxiv-2206.14176/README.md) | 四足 1 小时学会走；硬件磨损 |
| ① + ④ | 去掉解码器，MPPI + 策略先验，多任务 | [TD-MPC2](../../papers/arxiv-2310.16828/README.md) | 一套超参覆盖 104 个任务；只支持连续动作 |
| ①② + ④ | 文本条件视频扩散 + 逆动力学出动作 | [UniPi](../../papers/arxiv-2302.00111/README.md) | 网络视频知识迁移；生成慢、幻觉 |
| ④ 用法：仿真器 | 多源数据训练可交互模拟器，在其中训练 VLM 规划器与 RL 策略 | [UniSim](../../papers/arxiv-2310.06114/README.md) | RL 58% → 81%、零样本到真机；编造结果、记忆短 |
| ① 表示 | 自监督视频特征 + 62 小时无标注机器人视频后训练 | [V-JEPA 2](../../papers/arxiv-2506.09985/README.md) | Franka 零样本抓放 80%/65%；对相机位置敏感，长程误差累积 |
| ① 表示 | 在 DINOv2 潜空间上训练大规模视频预测器 | [Back to the Features（DINO-world）](../../../multimodal/papers/arxiv-2507.19468/README.md) | 视频预测基准领先，可微调做动作条件规划 |
| ① + ④ | 视觉基础模型潜空间里的扩散预测，配合扩散策略 | [LaDi-WM](../../../multimodal/papers/arxiv-2505.11528/README.md) | LIBERO-LONG 提升 27.9%、真实场景 20% |
| ① 表示 | 对象槽表示 + 基于对象的探索奖励 | [FOCUS](../../../multimodal/papers/arxiv-2307.02427/README.md) | 更一致地探索机器人与物体的交互；真机 Franka |
| ① 表示 | 槽注意力的对象中心表示，按语言预测未来 | [Object-Centric World Model for Language-Guided Manipulation](../../../multimodal/papers/arxiv-2503.06170/README.md) | 样本与计算效率高于扩散类方法 |
| ① 表示 | 对象中心的视频动力学（题录） | [SlotFormer](../../../multimodal/papers/arxiv-2210.05861/README.md)、[SAVi++](../../../multimodal/papers/arxiv-2206.07764/README.md) | 本轮未核读 |
| ② 动力学 | 可微物理 + 高斯泼溅观测损失，生成物理参数变体 | [PIN-WM](../../../multimodal/papers/doi-10.15607-rss.2025.xxi.153/README.md) | 推、戳类非抓取操作迁移到真机；只覆盖刚体 |
| ② 动力学 | 弹簧—质点仿真为骨干 + 神经网络预测残差 | [物理引导残差动力学](../../../multimodal/papers/arxiv-2607.13451/README.md) | 可变形物体预测更准；任务类型窄 |
| ①② | 先预测分割掩码再渲染成图像，仿真预训练 + 少量真实数据 | [Mask2Real-WM](../../../multimodal/papers/arxiv-2607.04546/README.md) | 23 个自由度逐维可控；摘要只报告了一个灵巧抓放任务 |
| ⑤ 数据 / ④ 仿真 | 3DGS 从稀疏 RGB 快速重建可碰撞的数字孪生 | [3DGS 数字孪生](../../../multimodal/papers/arxiv-2601.03200/README.md) | 显式重建而非学习动力学，支撑抓放规划 |
| ④ 用法：平台 | 视频世界基础模型，列出评估、初始化、训练、规划、合成数据五种用途 | [Cosmos](../../../multimodal/papers/arxiv-2501.03575/README.md) | 开放权重；机器人用途无实证结果 |
| ④ 用法：评估 + 出动作 | 多视角视频模型 GE-Base + 动作头 GE-Act + 神经仿真器 GE-Sim | [Genie Envisioner](../../papers/arxiv-2508.05635/README.md) | 1 小时数据适配新本体；只用自家数据 |
| ④ 用法：评估 | 微调 Veo 成多视角动作条件模拟器，编辑出分布外场景 | [Veo 评估器](../../papers/arxiv-2512.10675/README.md) | 与真机成功率 Pearson 0.92；约 8 秒时长、需人工打分 |
| ③ + ④ | 逐帧动作条件、位姿记忆检索；评估并合成成功轨迹 | [Ctrl-World](../../papers/arxiv-2510.10125/README.md) | π0.5 38.7% → 83.4%；接触物理有差距 |
| ④ 用法：出动作 | 人类视频作上下文，先预测机器人视频再解码动作，IFP 目标 | [Zero-WAM](../../papers/zero-wam/reading.md) | 未见任务 47.0%；视频错则动作错 |
| ⑥ 训练信号 | 以逆动力学解出动作的可执行性作为 RL 奖励对齐视频模型 | [EVA](../../../multimodal/papers/arxiv-2603.17808/README.md) | 生成视频更可执行；需要真实轨迹训练逆动力学 |
| ③ 动作接口 | 像素运动（动作流）作跨本体接口，同时评估与控制 | [Hydra-0](../../../multimodal/papers/arxiv-2608.18077/README.md) | 预测与实际成功率 r = 0.96 |
| ③ 动作接口 | 从无标注视频学潜在动作 | [UniVLA](../../../multimodal/papers/arxiv-2505.06111/README.md) | 预训练算力少于 OpenVLA 的 1/20 |
| ⑥ 评估与分析 | 潜在动作模型学到什么；潜在动作表示的 benchmark | [What Do LAMs Learn?](../../../multimodal/papers/arxiv-2506.15691/README.md)、[LARY](../../../multimodal/papers/arxiv-2604.11689/README.md) | 指出可能学到外部噪声；语义表示优于像素表示 |
| ⑥ 评估 | 比较重建型与语义型潜空间 | [Reconstruction or Semantics?](../../../multimodal/papers/arxiv-2605.06388/README.md) | 视觉保真度不足以挑选世界模型 |
| ③ 动作条件 + ④ 输出头与用法（2026 年补充） | 不改结构，把动作、本体状态、未来图像与价值编码成"潜在帧"放进视频扩散序列；同一模型出动作、预测未来与价值，best-of-N 规划 | [Cosmos Policy](../../papers/arxiv-2601.16163/README.md) | LIBERO 98.5%、RoboCasa 67.1%，真机 ALOHA 平均 93.6 / 带规划约 5 秒一个动作块，规划需大量 rollout |
| ①–④ 的设计对照 | 固定潜空间规划配方，分开比较编码器、本体信息、多步训练和优化器 | [JEPA-WMs 系统研究](../../papers/arxiv-2512.24497/README.md) | 得到任务相关的可检验配方 / 最优选项随数据和任务改变 |
| ④ + ⑥ 规划与诊断 | 分开改变预测展开和目标距离，用准确动力学隔离预测误差 | [The Planning Limits of Latent World Models](../../papers/arxiv-2609.39235/README.md) | 区分预测误差与看得太短 / 经验范围依赖协议；闭环限单臂仿真、子目标来自专家 |

## 批注

**易误读**

- SlotFormer、SAVi++ 两行只依据题名归位，本轮未打开摘要；其余多模态目录下的卡片依据 arXiv 摘要页归位，未读全文。
- 表中数字的口径见[入门页](README.md)批注与 [synthesis.csv](synthesis.csv)。

**跨方向参照**

- 驾驶方向的占据世界模型（[OccWorld](../../../multimodal/papers/arxiv-2311.16038/README.md)、[Drive-OccWorld](../../../multimodal/papers/arxiv-2408.14197/README.md)、[驾驶世界模型综述](../../../multimodal/papers/arxiv-2501.11260/README.md)）与[操作世界模型综述](../../../multimodal/papers/doi-10.1002-smb2.70053/README.md)可作为对照，本轮未核读。
- [ORB-SLAM3](../../papers/orb-slam3/reading.md) 与 [Convex MPC](../../papers/convex-mpc/reading.md) 代表显式几何地图与显式物理模型，是"学到的世界模型"的对照物：前者维护可度量的状态估计，后者在已知的简化刚体动力学上做 MPC。
- [多机器人三维场景图上的语言规划](../../../multimodal/papers/arxiv-2506.07454/README.md)用 LLM 把指令翻译成 PDDL（一种符号任务规划语言）目标，属于显式符号世界表示，与[具身 Agent](../embodied-agents/README.md) 的高层规划更接近。
