# 世界模型（机器人侧）

> 状态：领域入门页（§3.6 研究对象型） · v2（2026-10-04 追加 Cosmos 一线） · 依据 [synthesis.csv](synthesis.csv)（15 行）
>
> 速览：
> 1. 机器人里的世界模型是一个学到的预测器：给定历史观测和一段动作，预测之后会看到什么（像素、潜变量或预训练特征），有时还预测奖励。它没有专属的任务和 benchmark，好坏由它被拿去做什么来定义：在想象中学策略、部署时规划、当仿真器产生数据、评估别人的策略，或者先预测视频再反解动作。
> 2. 预测得像不等于用得好：World Models 里"梦中"得分 2086 的控制器，回到真实环境只有 193；2026 年的对比实验发现重建型潜空间画面最逼真，语义型潜空间做规划和训练策略更好。
> 3. 主线是"表示 × 用法"两条轴的移动：像素与 VAE 潜变量上学策略（World Models、Dreamer 一线，DayDreamer 让四足在真机上 1 小时学会走）→ 视频生成当策略与仿真器（UniPi、UniSim）→ 冻结预训练特征上规划（DINO-WM、V-JEPA 2）→ 视频世界基础模型用来评估 VLA 策略、合成数据（Veo 评估器、Ctrl-World、Genie Envisioner）→ 世界模型与动作模型合并（Zero-WAM）。
> 4. 各阶段都卡在同几件事上：接触丰富的物理（Veo 评估器与 Ctrl-World 自述）、长时预测漂移与记忆（V-JEPA 2 的误差累积、Veo 只能生成约 8 秒）、规划太慢（DINO-WM 一次规划约 53 秒，V-JEPA 2-AC 每个动作 16 秒、Cosmos 4 分钟）、策略钻模型的空子。
> 5. `[判断]` 2025 年后世界模型在机器人里的主要角色从"替代真实环境来学策略"转向"为模仿学习训练的 VLA 做评估与数据"，同时与策略合并成"世界—动作模型"。

本页是[机器人与具身](../../README.md)领域的世界模型方向，只讲**世界模型在机器人里怎样用**。分工如下：

- 机制与手算（RSSM 的先验与后验、四类训练损失、想象中的 actor-critic、部署时搜索动作、Zero-WAM 的视频—动作分解）在[世界模型讲义](../world-models.md)，本页不重复。
- 世界模型作为一种生成对象（视频生成器怎样变成可交互的模拟器，长时一致、可编辑、像素质量）在[多模态的世界模型方向](../../../multimodal/fields/world-models/README.md)。
- 为什么做视频生成的团队转去做世界模型，是跨领域的论证，在观点页[《生成收敛》的"从视频生成到世界模型"一节](../../../perspectives/generative-convergence.md#从视频生成到世界模型)。

本页采用 STYLE §3.6 的研究对象型结构：先讲对象是什么、被哪些任务使用、怎样测量，再讲方法与历史。

## 什么是机器人里的世界模型

世界模型是一个学到的动力学模型：输入当前及过去的观测 o、以及准备执行的动作 a，输出下一时刻的预测，写成 p(o_{t+1} 或 z_{t+1} | o_{≤t}, a_t)。z 是某个编码器给出的潜变量，可以是 VAE 的压缩向量、Dreamer 的离散类别变量、冻结的 DINOv2 图像块特征，或者视频扩散模型的时空潜变量。很多世界模型还带奖励头、终止头或价值头（Dreamer、TD-MPC2），用来在想象中算回报。

它和你熟悉的状态方程 x_{t+1} = f(x_t, u_t) 是同一种结构 `[结构]`：MPC 在已知的 f 上优化控制序列；世界模型把 f 换成从数据学到的网络，状态换成从像素编码出的潜变量（[讲义](../world-models.md)第三、四节的 RSSM 先验与后验，对应卡尔曼滤波的预测与校正）。

一个世界模型好不好，由使用它的方式定义：用来学策略时看最终策略的回报和样本效率，用来规划时看规划成功率和耗时，用来评估时看它给出的成功率排名与真机排名是否一致。同一个模型换一种用法，评价可以完全不同，所以本页先讲用法和测量。

## 从任务看

结论：五种用法对世界模型的要求互相拉扯，不存在一个"最好"的世界模型。

| 用法 | 需要的性质 | 怎样接到任务上 | 本库中的证据 |
|---|---|---|---|
| (a) 在想象中学策略 | 短时预测准；奖励与终止预测可靠；策略钻不了空子 | 从真实经验中的状态起跑，在模型里展开十几步，训练 actor-critic（[讲义](../world-models.md)第六节路线 A） | World Models 的 VizDoom"梦中训练"；[DayDreamer](../../papers/arxiv-2206.14176/README.md) 四足 1 小时学会走；[DreamerV3](../../../multimodal/papers/dreamerv3/reading.md) |
| (b) 部署时规划 | 推理快；潜空间里的距离对目标有意义；多步预测不漂 | 用 CEM（交叉熵法：反复采样动作序列、保留最好的一批再重新拟合分布）或 MPPI（按预测回报加权平均采样的动作序列）搜索动作，使预测终点接近目标或回报最高（讲义第六节路线 B） | [PlaNet](../../papers/arxiv-1811.04551/README.md)、[TD-MPC2](../../papers/arxiv-2310.16828/README.md)、[DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md)、[V-JEPA 2](../../papers/arxiv-2506.09985/README.md) |
| (c) 当仿真器训练策略、合成数据 | 多样；能被动作精确控制；物理上可信 | 在模型里跑策略、筛出成功轨迹，再用来做 RL 或监督微调 | [UniSim](../../papers/arxiv-2310.06114/README.md) 的 RL 58% → 81%；[Ctrl-World](../../papers/arxiv-2510.10125/README.md) 让 π0.5 从 38.7% 升到 83.4% |
| (d) 评估策略 | 给出的成功率排名与真机一致；能模拟分布外场景 | 让待测策略在模型里闭环跑，由人或 VLM 判定成功 | [Veo 评估器](../../papers/arxiv-2512.10675/README.md) Pearson 0.92；[Genie Envisioner](../../papers/arxiv-2508.05635/README.md) 的 GE-Sim；[Hydra-0](../../../multimodal/papers/arxiv-2608.18077/README.md) r = 0.96 |
| (e) 预测未来视频再反解动作 | 生成的视频在机器人上可执行；生成足够快 | 先生成"任务完成过程"的视频，再用逆动力学或动作头解出动作 | [UniPi](../../papers/arxiv-2302.00111/README.md)、[Zero-WAM](../../papers/zero-wam/reading.md)、Genie Envisioner 的 GE-Act、[EVA](../../../multimodal/papers/arxiv-2603.17808/README.md) |

拉扯的例子：(b) 要求推理快，DINO-WM 因此放弃生成像素，只在特征空间预测；(d) 需要人或 VLM 看得懂结果，Veo 评估器与 Ctrl-World 因此保留了像素级的多视角视频。(a) 需要奖励头，(d)(e) 通常不需要。

## 从测量看

结论：世界模型有两类测量——预测本身的质量（画面像不像、特征误差多小）和下游用起来的效果；前者高不保证后者高，同一组模型在两类指标下的排名会翻转。

| 测量 | 测什么 | 例子 | 已知问题 |
|---|---|---|---|
| 像素或特征的预测误差 | 预测与真实未来的距离（LPIPS、FVD、特征 MSE） | DINO-WM 报告 LPIPS；Genie Envisioner 的 EWMBench 测场景一致性、轨迹对齐、运动语义 | 与控制效果不一定相关 |
| 规划成功率与耗时 | 用模型规划能否完成任务、多快 | DINO-WM Push-T 0.90，每次规划约 53 s；V-JEPA 2-AC 抓放 80%/65%，每个动作 16 s | 规划器的超参（候选数、步长）会改变结论 |
| 策略学习效果 | 想象中学出的策略回报、样本效率 | DreamerV3 的 150 多个任务；DayDreamer 的真机学习时间 | 每个任务单独训练一个智能体 |
| 评估一致性 | 模型给出的成功率与真机成功率的相关性与排名违例（MMRV） | Veo 评估器：1600 多次真机试验、8 个策略检查点，常规场景 Pearson 0.92、MMRV 0.03 | 需要人工判定视频成功；相关高不代表单个策略的成功率准 |

两个排名翻转的证据：

- **World Models（2018）**：温度参数 τ 调低时，模型几乎确定性，控制器在"梦中"得分 2086，回到真实 VizDoom 只有 193；τ = 1.15 时梦中更难，真实得分 1092（Table 2）。模型"越好学"，策略越容易钻它的空子。
- **[Reconstruction or Semantics?](../../../multimodal/papers/arxiv-2605.06388/README.md)（2026）**：在 BridgeV2 上比较六种编码器的潜空间训练的动作条件视频扩散模型，重建型（VAE 类）像素保真度最好，语义型（V-JEPA 2.1 类）在规划与下游策略上更好，作者结论是视觉保真度不足以用来挑选世界模型。

Ctrl-World 给出第三个提醒：策略在世界模型里的高层指令遵循行为与真实世界密切相关，但执行成功率有时被低估。

## 从内部看

本方向特有的内部分析集中在一个问题上：潜变量里编码的是可控的变化，还是与动作无关的背景变化。

- [What Do Latent Action Models Actually Learn?](../../../multimodal/papers/arxiv-2506.15691/README.md)（2025）用线性模型分析从无标注视频里学"潜在动作"的方法，指出它可能学到外部噪声而非可控变化，并据此解释数据增强、清洗和辅助动作预测为什么有效。
- [LARY](../../../multimodal/papers/arxiv-2604.11689/README.md)（2026）在 100 多万段视频上测潜在动作表示能否对齐到机器人动作，发现通用视觉基础模型的表示好于专门的具身模型，潜空间的语义表示好于像素表示。

通用的探针与表示分析方法见[模型科学](../../../cross-domain/fields/model-science/README.md)。

## 方法谱系

结论：每种方法是"表示 × 动力学 × 用法"三条轴上的一个点。表示决定能预测多远、多快、多可读，动力学结构决定能否表示多种未来，用法决定需要哪些输出头。

| 表示 | 动力学 | 用法 | 代表 | 换来的性质 | 代价 |
|---|---|---|---|---|---|
| VAE 潜变量 | MDN-RNN | (a) | World Models | 可以完全在梦中训练控制器 | 策略钻模型空子；VAE 不区分任务相关特征 |
| 确定 + 随机潜变量（RSSM） | RNN | (b) PlaNet / (a) Dreamer 一线 | PlaNet、DayDreamer、DreamerV3 | 样本效率高，可在真机上直接学 | 真机磨损；无一般的稳定性与安全保证 |
| 无解码器的潜变量 | MLP + SimNorm | (b) MPPI + 策略先验 | TD-MPC2 | 一套超参覆盖 104 个任务 | 只支持连续动作；规划带来额外计算 |
| 冻结的预训练图像块特征 | ViT 预测器 | (b) CEM | DINO-WM、DINO-world | 不训练编码器，零样本规划 | 需要动作覆盖充分的离线数据；规划慢 |
| 自监督视频特征（V-JEPA 2） | 动作条件预测器 | (b) | V-JEPA 2-AC | 62 小时无标注机器人视频即可零样本规划 | 对相机位置敏感；长程误差累积；目标只能是图像 |
| 像素或视频潜变量 | 视频扩散 | (e) 与 (c) | UniPi、UniSim | 网络视频知识可迁移；可当仿真器 | 生成慢；幻觉；记忆短 |
| 视频基础模型潜变量，多视角 | 视频扩散 + 动作条件 | (c)(d)(e) | Veo 评估器、Ctrl-World、Genie Envisioner、Cosmos | 评估与数据合成，可编辑出分布外场景 | 接触丰富的物理不准；时长有限；需要人或 VLM 判定 |
| 分割掩码、物理参数 | 学到的动力学 + 渲染，或可微物理 + 残差 | (b)(c) | [Mask2Real-WM](../../../multimodal/papers/arxiv-2607.04546/README.md)、[PIN-WM](../../../multimodal/papers/doi-10.15607-rss.2025.xxi.153/README.md)、[物理引导残差动力学](../../../multimodal/papers/arxiv-2607.13451/README.md) | 可控、少量真实数据即可适配 | 适用的物体与任务类型窄 |
| 视频 + 动作联合 | 因果视频—动作模型 | (e) 带上下文 | Zero-WAM、[Hydra-0](../../../multimodal/papers/arxiv-2608.18077/README.md) | 用人类视频说明新任务；同时可评估与控制 | 视频预测错，动作跟着错 |

## 主线历史

结论：两条轴依次移动：表示从像素重建走向预训练语义特征，用法从"替代真实环境学策略"走向"为 VLA 做评估与数据"，最后与策略合并。

### 1 在梦中学策略（2018）

[World Models](../../papers/arxiv-1803.10122/README.md)（Google Brain、IDSIA）用 VAE 压缩画面、MDN-RNN 预测下一步潜变量、一个线性控制器出动作；CarRacing 得分 906 ± 21，VizDoom 的控制器完全在模型生成的"梦"里训练后迁回真实环境。

做不好的场景：控制器学会了钻模型的空子，例如让火球不合理地消失；作者用温度参数 τ 增加梦的随机性来缓解，τ = 0.10 时梦中 2086、真实 193（Table 2）。作者也写明 VAE 不会优先保留与任务相关的特征。

`[判断]` 站在现在看过去：这是"策略利用模型误差"在机器人世界模型里的第一个清楚案例，与 LLM 后训练中的奖励黑客是同一类问题：优化器总会找到被优化对象（这里是学到的模型，那里是奖励模型）最不准的地方。

### 2 潜空间动力学成为主线：PlaNet、Dreamer 到真机（2018–2023）

- [PlaNet](../../papers/arxiv-1811.04551/README.md)（2018）提出 RSSM（循环状态空间模型，一句话：同时有确定的循环记忆和随机的潜变量），在潜空间里用 CEM 规划（视野 12 步、每次 1000 个候选、10 轮迭代），在 DeepMind Control 上用远少于无模型方法的回合数达到相近水平。
- [DayDreamer](../../papers/arxiv-2206.14176/README.md)（UC Berkeley，2022）把 Dreamer 直接放到 4 台真实机器人上学，不用仿真器：A1 四足从仰躺开始，1 小时学会翻身、站立和行走，10 分钟内适应外力推搡；UR5 与 XArm 从像素和稀疏奖励学抓放。
- [DreamerV3](../../../multimodal/papers/dreamerv3/reading.md)（2023）用一套固定配置在 150 多个任务上超过专门方法，在 Minecraft 中不靠人类数据挖到钻石；v1 的评测都在仿真基准与游戏中（精读第八节）。
- [TD-MPC2](../../papers/arxiv-2310.16828/README.md)（UCSD，2023）去掉解码器，只学对规划有用的潜变量，用 MPPI 加策略先验规划，317M 参数的单一模型覆盖 4 个领域的 80 个任务。

做不好的场景：DayDreamer 写明在硬件上学几个小时会磨损机器人，可能需要人工干预或维修；DreamerV3 精读指出它没有提供闭环稳定性、碰撞约束或仿真到真实的保证，真机碰撞未必可以重来。TD-MPC2 写明扩展到离散动作空间仍是开放问题，规划带来额外计算。

`[判断]` 站在现在看过去：这一线证明了世界模型能把真机学习的样本量降到小时级，但机器人学习的主流在 2023 年后转向了模仿学习训练的 VLA（见 [VLA 方向](../vla/README.md)），"在想象中学策略"没有成为通用机器人策略的主要训练方式。原因之一写在 DreamerV3 精读里：每个任务单独训练一个智能体，需要为每个任务定义奖励。

### 3 视频生成当策略与仿真器（2023）

- [UniPi](../../papers/arxiv-2302.00111/README.md)（MIT、Google DeepMind 等）把决策写成文本条件的视频生成：扩散模型生成任务完成的视频，逆动力学模型从相邻帧解出动作。
- [UniSim](../../papers/arxiv-2310.06114/README.md)（UC Berkeley、Google DeepMind 等）把多种数据训练成一个可交互的真实世界模拟器，在里面训练高层 VLM 规划器与低层 RL 策略，RL 让成功率从 58% 升到 81%（Table 3），两者都零样本迁移到真实的 Language Table 机器人。

做不好的场景：UniPi 生成一段高真实度视频要约一分钟，部分可观测时会凭空生成物体或运动。UniSim 自述四点：对不现实的动作会编造结果（对桌面机器人说"洗手"，桌子变成了水槽）；只以最近几帧为条件，记不住长程状态；在没见过的机器人形态上明显变差；只模拟视觉，不能表示抓取力这类非视觉后果（第 6 节）。

### 4 在冻结的预训练特征上规划（2024–2025）

- [DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md)（NYU，2024）冻结 DINOv2，只训练一个预测未来图像块特征的 ViT，测试时用 CEM 让预测特征接近目标图像的特征；不需要奖励和专家示范，Push-T 成功率 0.90。
- [V-JEPA 2](../../papers/arxiv-2506.09985/README.md)（Meta FAIR 等，2025）先在大规模视频上自监督预训练，再用 DROID（多个实验室用 Franka 机械臂采集的大规模遥操作数据集）中约 62 小时无标注的机器人视频后训练一个动作条件预测器（V-JEPA 2-AC），在两个实验室的 Franka 上零样本做抓放，成功率 80% 与 65%（Octo 的抓取为 15%）。
- 同一思路的 [Back to the Features（DINO-world）](../../../multimodal/papers/arxiv-2507.19468/README.md) 与 [LaDi-WM](../../../multimodal/papers/arxiv-2505.11528/README.md)（在视觉基础模型潜空间里做扩散预测，LIBERO-LONG 上提升 27.9%）。

做不好的场景：DINO-WM 一次规划约 53 秒（100 个候选 × 10 轮），需要动作覆盖充分的离线数据，没有分层规划。V-JEPA 2-AC 每个动作规划 16 秒（Cosmos 为 4 分钟）；它要求人工摆好相机，因为模型要隐式推断动作坐标轴；自回归预测会累积误差，长程任务做不好；目标只能是图像。

`[判断]` 站在现在看过去：这一线用"不生成像素"换来了速度和泛化，与[视觉表征](../../../multimodal/fields/visual-representation/README.md)方向"冻结编码器服务多个任务"的趋势是同一件事；它的弱点（规划慢、目标要给图像）恰好是语言条件的 VLA 的强项，两者至今没有合流。

### 5 视频世界基础模型：评估 VLA、合成数据（2025）

- [Cosmos](../../../multimodal/papers/arxiv-2501.03575/README.md)（NVIDIA，2025 年 1 月）列出世界基础模型在物理 AI 中的五种用途：策略评估、策略初始化、策略训练、规划、合成数据，同时写明论文没有给出这些用途的实证结果。
- [Genie Envisioner](../../papers/arxiv-2508.05635/README.md)（智元等，2025）在约 3000 小时、100 万回合的自家数据上训练多视角视频扩散模型 GE-Base，接上 160M 参数的流匹配动作头 GE-Act，再做成动作条件的神经仿真器 GE-Sim 做闭环评估；每个新机器人只用 1 小时遥操作数据适配。
- [Veo 评估器](../../papers/arxiv-2512.10675/README.md)（Google DeepMind，2025）把 Veo 2 在机器人数据上微调成多视角、动作条件的模拟器，用来评估 Gemini Robotics 策略：对照 1600 多次真机试验、8 个策略检查点与 5 个任务，常规场景预测成功率与真实成功率的 Pearson 相关 0.92；用图像编辑生成背景、干扰物、新物体等分布外场景，相关 0.86。
- [Ctrl-World](../../papers/arxiv-2510.10125/README.md)（Stanford、清华，2025）在 DROID 上微调多视角、逐帧动作条件、带位姿记忆检索的视频模型，评估 π0、π0-FAST、π0.5，并用在模型里筛出的成功轨迹微调 π0.5，在新物体与新指令上从 38.7% 升到 83.4%。

做不好的场景：Veo 评估器自述难以模拟与小物体的接触，只能生成约 8 秒（任务需要 60 秒以上），操作中物体会凭空出现或消失，仍依赖人工给视频打分。Ctrl-World 自述在精细交互、长程推理、碰撞、物体滑走与旋转上有差距，成功轨迹要靠人挑选。Genie Envisioner 只用自家一种数据源，只覆盖平行夹爪的桌面上半身操作，任务成功的自动评估仍未解决。Cosmos 自述缺乏物体永久性、接触丰富的动力学不准、物理对齐不足。

2025 年 10 月，NVIDIA 发布 Cosmos 的下一版 [Cosmos-Predict2.5](https://arxiv.org/abs/2511.00062)（官方技术报告，本页未建卡）：基于 flow matching，把文本、图像、视频到世界的生成统一进一个模型，用 Cosmos-Reason1 做文本条件，在 2 亿段筛选过的视频上训练、再用强化学习后训练，2B 与 14B 两档按 NVIDIA Open Model License 开放；报告列出的机器人用途包括动作条件的视频生成（用于策略验证）与相机可控的多视角操作视频。

`[判断]` 站在现在看过去：世界模型在这一阶段找到了一个不需要"完美物理"的用途：评估只要求排名对，不要求每段视频都对，所以 Pearson 0.92 的评估器可以在接触物理不准的情况下仍然有用。这也解释了为什么做这件事的多是同时拥有大视频模型和大 VLA 的团队（Google DeepMind、NVIDIA、智元）。

### 6 世界模型与动作模型合并（2026）

- [Zero-WAM](../../papers/zero-wam/reading.md)（2026 年 8 月）把人类示范视频作为上下文，先预测机器人接下来的视频，再由动作分支解码动作；在 RoboTwin 2.0 的 7 个未见任务上平均 47.0%，比最强的视频—动作基线高 29.5 个百分点。它的 IFP 目标（训练时额外预测更远的未来片段）消融显示从 28.55% 升到 46.95%。
- [EVA](../../../multimodal/papers/arxiv-2603.17808/README.md)（2026）指出视觉上连贯的生成视频可能违反刚体与运动学一致性，用逆动力学模型把生成视频解成动作、以动作的可执行性作为强化学习奖励来对齐视频世界模型。
- [Hydra-0](../../../multimodal/papers/arxiv-2608.18077/README.md)（2026）用"像素运动"作为跨本体的统一接口，同时做世界建模与控制，在 RoboLab 上预测成功率与实际成功率相关 r = 0.96。
- [Cosmos Policy](../../papers/arxiv-2601.16163/README.md)（NVIDIA、Stanford，2026 年 1 月，补充）把 2B 的视频扩散模型 Cosmos-Predict2 直接后训练成策略、不改结构：动作块、本体状态、未来图像和价值都编码成"潜在帧"排进同一段扩散序列，同一个模型既出动作、又预测未来和价值，可以对候选动作块做 best-of-N 规划。LIBERO 98.5%、RoboCasa 67.1%；真机 ALOHA 四个双臂任务平均 93.6 分，作者报告整体高于 π0.5；加规划后两个最难任务再提高约 12.5 分。

做不好的场景：Zero-WAM 训练时动作分支以真实的未来视频为条件（teacher forcing），部署时只能用生成的视频，视频错了动作跟着错；7 个任务里放空杯 84.87%、叠三个方块只有 9%（[Zero-WAM 精读](../../papers/zero-wam/reading.md)）。Cosmos Policy 加规划时约 5 秒才出一个动作块，作者写明难用于动态任务，有效规划需要大量 rollout 数据，目前只做一层 best-of-N。

`[判断]` 站在现在看（2026 年补充）：Cosmos 平台论文（2025 年 1 月）只列出世界模型的五种机器人用途、没有实证；一年后 NVIDIA 自己用 Cosmos Policy 给出了"策略初始化"与"规划"两种用途的实证，并在 GR00T N1.7 里用同一平台的 Cosmos-Reason2 当 VLA 的视觉语言骨干（见 [VLA 方向](../vla/README.md)第 7 阶段）。Physical Intelligence 的 π0.7 用一个轻量世界模型生成子目标图像放进提示，是另一种"世界模型服务策略"的接法。规划仍然慢：Cosmos Policy 的 5 秒一个动作块，与 V-JEPA 2-AC 的每个动作 16 秒是同一个数量级的问题。

## 趋势

以下都是 `[判断]`，支撑论文列在批注。

1. **规划用的表示从像素走向语义特征，评估用的表示留在像素。** DINO-WM、V-JEPA 2、Reconstruction or Semantics?、LARY 都指向语义潜空间更适合规划与动作对齐；Veo 评估器、Ctrl-World、Genie Envisioner 仍生成多视角像素，因为评估结果要由人或 VLM 看懂。表示的选择由用法决定。
2. **用法从"替代真实环境"转向"为 VLA 服务"。** 2018–2023 年的主流用法是在模型里学策略（World Models、Dreamer 一线）；2025 年后的主要用法是评估 VLA、给 VLA 合成数据（Veo 评估器、Ctrl-World、Cosmos 列出的用途）。驱动力是机器人策略的主流变成了模仿学习训练的 VLA，它没有奖励函数可以在想象中优化，却很需要便宜的评估。
3. **世界模型与策略合并。** UniPi 的"视频 + 逆动力学"、Genie Envisioner 的 GE-Act、Zero-WAM、Hydra-0 都让同一个模型既预测未来又输出动作。2026 年的 Cosmos Policy 连价值也放进同一个视频模型，并在 LIBERO、RoboCasa 与真机 ALOHA 上与 π0.5 一类 VLA 直接比较。
4. **薄弱环节一直没变。** 接触丰富的物理、长时记忆、推理速度，从 UniSim（2023）到 Veo 评估器（2025）都被自述为局限；视频生成一侧的同样问题见观点页[《生成收敛》](../../../perspectives/generative-convergence.md#从视频生成到世界模型)。

## 主要路线与团队偏好

| 团队 | `[判断]` 押注 | 代表 | 代价与做不好的地方 |
|---|---|---|---|
| Hafner、Abbeel 等 | 学潜空间动力学（RSSM），在想象中学策略，一套配置跨领域 | PlaNet、DayDreamer、DreamerV3 | 每任务单独训练、需要奖励；真机磨损 |
| Meta FAIR（LeCun 等）与 NYU | 在预训练或自监督特征空间里预测，不生成像素，用于规划 | DINO-WM、V-JEPA 2、DINO-world | 规划慢；目标是图像而非语言 |
| Google DeepMind（Yilun Du、Sherry Yang 等） | 视频生成作为策略、仿真器与评估器 | UniPi、UniSim、Veo 评估器（Du 也参与 Hydra-0） | 生成慢、幻觉、时长短；需要人工判定 |
| NVIDIA、智元（AgiBot） | 世界基础模型平台：视频模型 + 动作头 + 仿真评估 | Cosmos、Genie Envisioner | Cosmos 未给出机器人用途的实证；GE 只用自家数据 |
| UCSD（Hansen、Wang） | 不要解码器，只学对规划有用的潜变量 | TD-MPC2 | 只有一篇代表，偏好证据弱 |
| NVIDIA（2026 年补充） | 同一个 Cosmos 平台同时供给世界模型（Cosmos-Predict2.5）、策略（Cosmos Policy）与 VLA 骨干（GR00T N1.7 的 Cosmos-Reason2） | Cosmos、Cosmos-Predict2.5、Cosmos Policy | 带规划时约 5 秒一个动作块；Predict2.5 报告本页未逐节核读 |

`[判断]` 收敛的部分：都用某种潜空间而非原始像素做动力学；2025 年后都在 DROID、Bridge、AgiBot World 这类大规模机器人数据上微调。分化的部分：生成像素（DeepMind、NVIDIA、智元、Stanford）还是只预测特征（Meta）；模型用来规划、评估还是直接出动作。

## 当前开放问题

- **接触丰富的物理能否预测对？** Veo 评估器、Ctrl-World、Cosmos 都把它列为局限。入口：[Veo 评估器](../../papers/arxiv-2512.10675/README.md)、[PIN-WM](../../../multimodal/papers/doi-10.15607-rss.2025.xxi.153/README.md)（可微物理与高斯泼溅结合）、[Mask2Real-WM](../../../multimodal/papers/arxiv-2607.04546/README.md)。
- **长程预测怎样不漂？** V-JEPA 2 的误差累积、Veo 的 8 秒上限、UniSim 的短记忆。入口：[V-JEPA 2](../../papers/arxiv-2506.09985/README.md)、[Ctrl-World](../../papers/arxiv-2510.10125/README.md) 的位姿条件记忆检索。
- **怎样挑世界模型？** 视觉保真度不足以作为标准。入口：[Reconstruction or Semantics?](../../../multimodal/papers/arxiv-2605.06388/README.md)、[LARY](../../../multimodal/papers/arxiv-2604.11689/README.md)。
- **生成的未来能否被机器人执行？** 入口：[EVA](../../../multimodal/papers/arxiv-2603.17808/README.md)、[Zero-WAM](../../papers/zero-wam/reading.md)。
- **规划能否快到闭环可用？** DINO-WM 53 秒、V-JEPA 2-AC 16 秒每个动作。入口：[DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md)、[TD-MPC2](../../papers/arxiv-2310.16828/README.md)。2026 年补充：Cosmos Policy 带规划时约 5 秒一个动作块，入口 [Cosmos Policy](../../papers/arxiv-2601.16163/README.md)。

## 阅读顺序

1. [世界模型讲义](../world-models.md)：先把 RSSM 的先验与后验、四类损失、两条用法路线手算一遍；用你熟悉的状态估计去类比。
2. [DreamerV3 精读](../../../multimodal/papers/dreamerv3/reading.md) → [DayDreamer](../../papers/arxiv-2206.14176/README.md)：同一个算法从仿真基准走到四足真机，看清楚真机学习多了哪些问题。
3. [DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md) 与 [V-JEPA 2](../../papers/arxiv-2506.09985/README.md)：在特征空间里规划，对照读规划耗时与目标形式。
4. [Veo 评估器](../../papers/arxiv-2512.10675/README.md) 与 [Ctrl-World](../../papers/arxiv-2510.10125/README.md)：世界模型怎样为 VLA 做评估与数据，注意相关系数说明了什么、没说明什么。
5. [Zero-WAM 精读](../../papers/zero-wam/reading.md)：世界模型与动作模型合并的当前形态，注意训练与部署时视频来源的不同。
6. （2026 年补充）[Cosmos Policy](../../papers/arxiv-2601.16163/README.md)：把一个现成的视频世界模型直接后训练成策略加价值函数，对照 [Cosmos](../../../multimodal/papers/arxiv-2501.03575/README.md) 平台论文列出、但没有实证的用途。

基线拆分见 [Baseline 页](BASELINES.md)，按问题排列的学习路线见[路线图](ROADMAP.md)，本方向收录的论文见[论文目录](PAPERS.md)。

## 批注

**为什么用 §3.6 的结构**

- 按 STYLE §3.6 的判定条件：机器人侧的世界模型没有自己专属的任务与 benchmark。它的"好"由下游用法定义（策略回报、规划成功率、评估相关性），已有的专门评测（Genie Envisioner 的 EWMBench）测的是视频性质，Reconstruction or Semantics? 显示这类性质与控制效果不一致。所以本页先讲用法与测量，再讲方法与历史。

**易误读**

- World Models 的 2086 与 193 是同一个控制器在梦中与真实 VizDoom 的得分（τ = 0.10）；1092 ± 556 是 τ = 1.15 时的真实得分（Table 2）。
- DayDreamer 的"1 小时学会走"指从仰躺开始学会翻身、站立和行走，是 A1 上的单次真机学习。
- V-JEPA 2-AC 的 80%/65% 是两个实验室的抓放成功率；16 秒对 4 分钟是每个动作的规划时间。
- Veo 评估器的 Pearson 0.92 是策略层面的成功率相关（8 个检查点、5 个任务），不说明单段视频的物理是否正确。
- Ctrl-World 的 38.7% → 83.4% 是在新物体与新指令上、用想象中筛出的成功轨迹微调 π0.5 后的结果，成功轨迹由人挑选。
- Cosmos 列出的五种机器人用途，原文写明没有实证结果。
- Zero-WAM 的 47.0% 是 7 个留出任务的宏平均，各任务从 9% 到 84.87% 不等。
- Cosmos Policy 的 ALOHA 93.6 是四个任务的平均得分；对 π0.5 并非每项都高（装糖果进碗 89.6 对 95.2），"约 12.5 分"只在两个最难的任务上、加规划之后。
- Cosmos-Predict2.5 的描述只取自 arXiv 摘要页（v2，2026-02），没有核读正文的机器人实验。

**判断的支撑论文**（各行见 [synthesis.csv](synthesis.csv)）

- 趋势 1：DINO-WM 局限与规划设置；V-JEPA 2-AC；Reconstruction or Semantics? 摘要；LARY 摘要。反例：Ctrl-World、Veo 评估器、Genie Envisioner 保留像素且效果好，说明在评估用途上像素有必要。
- 趋势 2：Cosmos §2.1 的用途列表；Veo 评估器；Ctrl-World；DreamerV3 精读中"每任务单独训练"的说明。反例：TD-MPC2 与 DayDreamer 仍在用模型学策略；Zero-WAM 直接出动作。
- 趋势 3：UniPi、GE-Act、Zero-WAM、Hydra-0 摘要；2026 年补充 Cosmos Policy 摘要与 ALOHA 表。
- NVIDIA 用一个平台供给世界模型、策略与 VLA 骨干（2026 年补充）：Cosmos-Predict2.5 摘要、Cosmos Policy 摘要、GR00T N1.7 官方博客（VLM 为 Cosmos-Reason2-2B）。边界：三者是否共享训练数据与权重，官方材料没有写。
- 团队偏好：Hafner 出现在 PlaNet、DayDreamer、DreamerV3 的作者列表；Abbeel 出现在 DayDreamer、UniPi、UniSim；Yilun Du 出现在 UniPi、UniSim、Veo 评估器、Hydra-0，Sherry Yang 出现在 UniSim 与 Veo 评估器；LeCun 出现在 DINO-WM。V-JEPA 2 的作者列表本轮只核对了单位（Meta FAIR、Mila、Polytechnique Montréal）。

**与其他论文的关联**

- `[结构]` RSSM 的先验与后验对应卡尔曼滤波的预测与校正，见[讲义](../world-models.md)第四节；PlaNet、TD-MPC2 的潜空间规划与[运动控制](../control-locomotion/README.md)中的 MPC 是同一结构，只是动力学由数据学到。
- World Models 中策略钻模型空子，与 LLM 后训练里策略钻奖励模型空子是同一类问题，见 [LLM 强化学习方向](../../../llm/fields/posttraining/rl/README.md)。
- Zero-WAM 用人类视频说明新任务，是[具身 Agent](../embodied-agents/README.md)中"技能库覆盖不到时"的一种回答；UniSim 与 Ctrl-World 评估的 VLA 策略见 [VLA 方向](../vla/README.md)。
- 视频生成团队为什么转向世界模型，以及 Genie、Sora 一侧的可交互性与长时一致，见观点页[《生成收敛》](../../../perspectives/generative-convergence.md#从视频生成到世界模型)与[多模态世界模型方向](../../../multimodal/fields/world-models/README.md)。

**未核实 / 待验证**

- PlaNet 与无模型方法的样本效率倍数在摘要页与全文中的表述没有逐一核对，本页只写"远少于"。
- Genie Envisioner 的真机成功率表格没有逐项核对；"1 小时适配"来自其跨本体实验的描述。
- WorldGym、WorldEval、dWorldEval、RoboWorld 等其他用世界模型评估策略的工作本轮只看到检索结果，未打开原文，未收录。
- 多模态目录下的 SlotFormer、SAVi++、FOCUS、OccWorld 等卡片目前只有题录，本页只按摘要在 [Baseline 页](BASELINES.md)中归位。
- Cosmos-Predict2.5（arXiv:2511.00062）未建卡，可能由[多模态世界模型方向](../../../multimodal/fields/world-models/README.md)收录；NVIDIA DreamGen / GR00T Dreams、1X 世界模型、Genie 3 在机器人评估中的用法本轮未打开原文。
