# 世界模型（多模态侧）

> 状态：领域入门页（§3.6 研究对象型） · v2
>
> 速览：
> 1. 世界模型是一个学到的"状态更新 + 渲染"：给定过去的观测和动作，预测下一刻的状态，并能把它画出来或读出来。本页讲这个对象本身怎样被造出来（状态用什么表示、动力学怎样生成、动作从哪里接入）；机器人怎样拿它规划、学习、评估，在[机器人侧的世界模型页](../../../robotics-embodied/fields/world-models/README.md)。
> 2. 它没有专属 benchmark，"好"由用途与评测协议定义，而且协议之间互相打架：Physics-IQ 上最逼真的 Sora 物理得分并不最高，真实感与物理理解不显著相关（r = −0.46）；Genie 的消融里 FVD 更好的变体可控性更差。
> 3. 主线是"状态保留什么"这个问题的反复改答：VAE 压缩一切（2018）→ 离散潜变量 / token（Dreamer、GAIA-1、OccWorld）→ 对象槽（SAVi++、SlotFormer）→ 像素级扩散逐帧生成（DIAMOND、GameNGen、Genie 2/3、Cosmos）→ 只在表征空间预测、不画像素（V-JEPA 2）。
> 4. 站在现在看过去，每一代都有同几类坑：小而关键的东西丢失（路砖、分数、红绿灯、HUD 数字、文字）、长时漂移与记忆只有几秒到一分钟、动作可控性被画质掩盖、像素逼真却违反物理与物体永久性。
> 5. `[判断]` 2024 年后做世界模型的主力来自视频生成团队，他们把"可交互、长时一致、可编辑、关键符号不变"推成了目标；评测也随之从画质（FVD）转向可控性与物理（ΔtPSNR、Physics-IQ、VideoPhy、PhyWorld）。

本页属于[多模态总目录](../../README.md)。分工：机器人侧页面讲五种用法（想象中学策略、部署时规划、当仿真器、评估 VLA、预测视频再出动作）和 2025–2026 年的机器人工作；本页讲世界模型作为一种学到的模型，表示与生成两侧是怎样把它造出来的。为什么视频团队转去做世界模型，是跨领域的论证，见观点页[《生成收敛》](../../../perspectives/generative-convergence.md#从视频生成到世界模型)；本页给出它在本方向内部的证据。

## 什么是世界模型

一个游戏引擎每一帧做两件事：按玩家输入更新游戏状态，再把状态渲染成屏幕像素（GameNGen 引言的说法）。世界模型就是用神经网络从数据里同时学会这两件事。写成公式是 p(s_{t+1} | s_{≤t}, a_t) 加一个读出 o = g(s)：s 是状态，a 是动作，o 是观测（画面）。这与你熟悉的状态方程 x_{t+1} = f(x_t, u_t)、观测方程 y = h(x) 是同一结构 `[结构]`；差别是 f、h 和"状态是什么"全部从视频里学出来（滤波视角的手算见[机器人世界模型讲义](../../../robotics-embodied/fields/world-models.md)第四节）。

拆开看有四个部件：**表示**（把画面编码成状态：VAE 的连续潜变量，即模型内部概括一帧的低维向量，见 [VAE 讲义](../../../foundations/lessons/16-vae.md)；或离散 token，即把画面切块、每块用码本里的一个编号表示；或对象槽、3D 占据栅格、预训练特征）；**动力学**（怎样产生下一步：循环网络；自回归 Transformer，以前面已生成的 token 为条件逐个预测下一个；扩散模型，从噪声出发逐步去噪出下一帧，见[扩散讲义](../../../foundations/lessons/17-diffusion.md)）；**动作接口**（真实按键与控制量、从无标注视频学出的"潜在动作"、一句文字、相机位姿，或者没有动作）；**读出**（解码回像素，或只给出特征、奖励）。

这个方向没有自己专属的任务和 benchmark：同一个模型拿去训练智能体、给人玩、合成驾驶数据或做物理推理，评价标准都不同，同一个模型在不同协议下的排名会翻转（见"从测量看"）。所以本页按 STYLE §3.6 先讲任务与测量，再讲方法与历史。

## 从任务看

结论：给人看的用途要像素逼真，给智能体用的用途要可控、准确、保留任务相关的细节，做规划的用途要快且抽象；三类要求互相拉扯，不存在一个"最好"的世界模型。机器人规划、评估、合成数据的要求见[机器人侧页面](../../../robotics-embodied/fields/world-models/README.md)"从任务看"。

| 用途 | 需要的性质 | 怎样接到任务上 | 本库中的证据 |
|---|---|---|---|
| 在模型里训练智能体 | 保留决定回报的细节；短时预测准；策略钻不了空子 | 从真实观测起步，在模型里展开、训练控制器或 actor-critic | [World Models](../../../robotics-embodied/papers/arxiv-1803.10122/README.md)、[DreamerV3](../../papers/dreamerv3/reading.md)、[DIAMOND](../../papers/arxiv-2405.12399/README.md) |
| 可玩的神经游戏引擎 / 交互环境 | 实时；逐帧响应动作；长时一致；画面逼真 | 人或智能体每步给一个动作，模型生成下一帧 | [GameNGen](../../papers/arxiv-2408.14837/README.md)、[Genie](../../papers/arxiv-2402.15391/README.md)、[Genie 2](../../papers/genie-2-blog/README.md)、[Genie 3](../../papers/genie-3-blog/README.md) |
| 智能体的训练与评估环境 | 多样；可干预（反事实、世界事件）；对任意动作序列都一致 | 把通用智能体放进生成的世界执行指令 | Genie 2、Genie 3 中的 SIMA 智能体（DeepMind 按自然语言指令用键鼠玩 3D 游戏的通用智能体） |
| 驾驶神经仿真器与数据合成 | 其他交通参与者对自车动作有反应；几何正确；能造出罕见场景 | 以自车速度、转向或文字为条件生成未来；或预测 3D 占据再规划 | [GAIA-1](../../papers/arxiv-2309.17080/README.md)、[OccWorld](../../papers/arxiv-2311.16038/README.md)、[Drive-OccWorld](../../papers/arxiv-2408.14197/README.md)、[Cosmos](../../papers/arxiv-2501.03575/README.md) |
| 物理推理与视频理解 | 物体身份与交互正确；能预测"会不会撞" | 用预测的未来回答问题，或把预测当作预训练目标 | [SlotFormer](../../papers/arxiv-2210.05861/README.md) 的 CLEVRER、Physion 问答；[V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) 的动作识别与动作预期 |

三处拉扯，每处都有原文证据：

- **保真与可预测**。OccWorld 的分词器空间分辨率越高，重建越准，预测与规划反而越差，作者解释为 token 学不到高层概念；V-JEPA 2 的出发点正是不去预测草叶这类不可预测的细节。
- **画质与可控**。Genie 的潜在动作模型改用 token 作输入时 FVD 更好（38.8 对 40.1），可控性指标 ΔtPSNR 却更差（1.33 对 1.91），作者据此认为分词丢掉了动态信息，最终选了像素输入。
- **通用与任务相关**。World Models 的 VAE 复现了 Doom 墙上不重要的砖纹，却没还原 CarRacing 路面上决定任务的路砖；作者写明，无监督学习按定义不知道任务需要什么。

## 从测量看

结论：测量分五类，彼此不一致；"看起来真"在多篇原文里被证明与"可控""物理对"脱钩，所以评测在 2024 年后转向可控性与物理专项考题。

| 协议 | 做法 | 测的是什么 | 已知问题（原文） |
|---|---|---|---|
| 逐帧误差 | PSNR（像素误差的对数尺度）、LPIPS（深度特征上的感知距离），常在教师强制下算（每步都喂真实历史，不喂模型自己的输出） | 单步预测准不准 | GameNGen：自回归时轨迹几步后就因速度的微小差异与真值分开，逐帧指标变差而内容仍合理，逐帧指标抓不住 |
| 分布距离 | FVD（在视频动作识别网络特征上比较生成与真实视频的分布） | 整体像不像真视频 | VideoPhy：需要参考视频、偏向画质、检测不出不现实的运动 |
| 人工辨真伪 | 把真游戏与生成片段并排，让人或多模态大模型挑出真的 | 视觉真实感 | GameNGen：评测者 5–10 分钟自回归后只有 50% 能认出真游戏，熟悉缺陷的作者几秒内就能分辨 |
| 可控性 | Genie 的 ΔtPSNR：用推断出的真实动作与随机动作分别生成，比较两者与真值的 PSNR 差 | 动作对画面有多大影响 | `[判断]` 只测"有没有影响"，不测"影响对不对" |
| 物理与一致性专项 | 真实拍摄续写（Physics-IQ）、文本描述 + 人工判物理常识（VideoPhy）、合成规律下的分布外测试（PhyWorld）、仿真刚体场景与 3D 几何误差（Cosmos） | 物理规律、物体永久性、几何 | Cosmos：物理保真的人工评测受个人偏差影响，且可能与下游任务指标不一致 |
| 下游效果 | 在模型里训练的智能体回报（Atari 100k）、规划成功率、驾驶规划的 L2 误差与碰撞率 | 拿来用好不好 | `[判断]` 每个下游只检验一种用法 |

排名翻转的三个例子（"从任务看"中 Genie 的 FVD 与可控性是第四个）：

1. **真实感与物理**。Physics-IQ 让多模态大模型从一真一假两段视频中挑出生成的那段，对 Sora 只有 55.6% 挑对（50% 为机会水平，越低越逼真），是所有模型里最逼真的；物理理解得分最高的却是 VideoPoet（multiframe），也只有 29.5%（两次真实录制之间的差异记为 100%）。两项指标 Pearson r = −0.46、不显著。一个例子：火柴伸进一杯水，Runway Gen 3 生成的每一帧都清晰逼真，续写里却凭空出现一支蜡烛被点燃。
2. **规模与物理**。Cosmos 的物理对齐评测中，更大的模型画质更好，物理对齐却没有更好；PhyWorld 中把数据从 3 万扩到 300 万段、模型从 22M 扩到 310M，分布内速度误差降到接近真值视频（0.012 对 0.010），分布外误差高一个数量级（0.427）且不随规模下降。
3. **重建与预测**。除 OccWorld 的分词器分析外，机器人侧的 [Reconstruction or Semantics?](../../papers/arxiv-2605.06388/README.md) 报告重建型潜空间画面最好、语义型潜空间规划更好。

benchmark 的替换就是目标的迁移：控制回报（CarRacing、VizDoom，2018）→ 样本效率（Atari 100k）→ 合成物理场景的视频预测与问答（OBJ3D、CLEVRER、Physion，2022）→ 驾驶数据上的 4D 占据预测与规划（公开驾驶数据集 nuScenes 及其占据标注 Occ3D，2023）→ 只有定性样例的"世界模拟器"（Sora、GAIA-1、Genie 2/3）→ 物理专项考题（VideoPhy 2024、PhyWorld 2024、Physics-IQ 2025）。

## 从内部看

结论：本方向特有的内部分析问的是"状态里存了什么"：哪些东西被分成了独立的槽，动作变量对应画面里的什么，游戏状态存在网络里还是存在屏幕上。

- **对象是否被分开**。SAVi++ 用对象槽（slot：每个槽是一个向量，训练后各自绑定场景中的一个物体）在真实的 Waymo 驾驶视频上涌现出分割与跟踪，靠的是预测激光雷达深度而不是光流（光流对静止物体和移动相机无效）。作者写明 Waymo 中物体通常不会再次出现，所以"物体消失后回来仍被同一个槽捕获"没有被建模，这正是物体永久性的问题。
- **动作变量对应什么**。Genie 从无标注视频学出 8 个离散潜在动作，在 CoinRun（一个没训练过的 2D 游戏）上只要 200 个专家样本就能把潜在动作映射到真实动作，达到有专家动作的行为克隆的水平；Genie 2 博客写明模型要自己弄清"方向键该移动机器人而不是树和云"。机器人侧对潜在动作学到了什么（可能学到与动作无关的外部变化）的分析见[机器人侧页面](../../../robotics-embodied/fields/world-models/README.md)"从内部看"。
- **状态存在哪里**。GameNGen 只看得到 3 秒多的历史，却能把游戏逻辑维持得长得多：作者分析，一部分状态通过屏幕像素保存（弹药与血量计数、已有武器），模型从画面推断当前位置，从弹药和血量猜某片区域的敌人是否已被消灭。屏幕上的数字成了外部记忆，这也是"关键符号必须保持不变"的原因：数字一错，状态就错。
- **token 里有多少语义**。GAIA-1 让图像分词器回归 DINO 特征，主成分可视化中车辆、道路、天空的 token 各自聚在一起。

通用的探针与表示分析见[模型科学](../../../cross-domain/fields/model-science/README.md)。

## 方法谱系

结论：每种方法是"状态表示 × 动力学 × 动作接口 × 数据"四条轴上的一个点。表示决定丢什么，动力学决定能否表示多种可能的未来、能否实时，动作接口决定能被怎样控制与编辑，数据决定覆盖什么世界。拆成部件的基线表见 [Baseline 页](BASELINES.md)。

| 状态表示 | 动力学 | 动作接口 | 代表 | 换来的 | 代价（原文） |
|---|---|---|---|---|---|
| VAE 连续潜变量 | MDN-RNN（输出混合高斯，表示多种可能的下一步） | 真实动作 | World Models | 可以完全在梦中训练控制器 | 不知道任务需要什么细节；控制器钻模型空子 |
| 离散随机潜变量 + 循环状态（RSSM）+ 重建损失 | 循环网络 | 真实动作 | [DreamerV3](../../papers/dreamerv3/reading.md) | 一套超参覆盖 150 多个任务 | 每个任务单独训练；单像素重要的 2D 游戏要特别处理表示正则 |
| 离散 token | 自回归 Transformer 逐个预测 | 真实动作 + 文本 | IRIS（经 DIAMOND 转述）、GAIA-1、[OccWorld](../../papers/arxiv-2311.16038/README.md)（3D 占据 token） | 直接借用语言模型的扩展经验（GAIA-1 拟合出规模定律） | 分词丢细节（IRIS 的分数、敌人与奖励互换）；采样会陷入循环或漂出分布 |
| 离散 token | MaskGIT 式掩码预测（一次并行猜出被遮住的多个 token，迭代几轮） | 无监督潜在动作（8 个） | [Genie](../../papers/arxiv-2402.15391/README.md) | 不需要动作标注，网络视频即可 | 约 1 帧/秒；16 帧记忆；幻想不现实的未来 |
| 对象槽 | Transformer 在槽上自回归 | 无（只做无条件预测） | [SlotFormer](../../papers/arxiv-2210.05861/README.md)、[SAVi++](../../papers/arxiv-2206.07764/README.md) | 物体身份明确，可用于物理问答 | 真实视频上扩展不了；需要首帧框和深度监督 |
| 像素或潜空间 | 扩散，逐帧自回归（以过去帧和动作为条件去噪出下一帧） | 真实按键 / 键鼠 | [DIAMOND](../../papers/arxiv-2405.12399/README.md)、[GameNGen](../../papers/arxiv-2408.14837/README.md)、[Genie 2](../../papers/genie-2-blog/README.md)、[Genie 3](../../papers/genie-3-blog/README.md)（另加文字事件） | 细节保真、可实时（20 帧/秒）、可玩 | 记忆短（3 秒到约一分钟）；自回归漂移；实时要靠蒸馏或降分辨率 |
| 时空潜变量 | 扩散 Transformer 一次生成整段 | 文本（无逐帧动作） | [Sora](../../papers/sora-tech-report/README.md) | 一分钟高清视频，涌现 3D 一致 | 玻璃破碎、吃东西的状态变化不对；长视频不连贯 |
| 时空潜变量或离散 token | 扩散与自回归两套，可后训练加相机、动作条件 | 相机位姿、机器人动作、驾驶轨迹 | [Cosmos](../../papers/arxiv-2501.03575/README.md) | 开放权重的通用底座 | 缺乏物体永久性；接触动力学不准；更大不更物理 |
| 自监督视频特征（不解码像素） | 块因果 Transformer 在特征空间自回归 | 末端执行器控制量（后训练） | [V-JEPA 2-AC](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)、[DINO-world](../../papers/arxiv-2507.19468/README.md) | 规划快（每个动作 16 秒对 Cosmos 的 4 分钟） | 对相机位置敏感；误差累积；目标只能是图像 |

**数据轴**：随机策略在单个游戏里采的数据（World Models）→ RL 智能体整个训练过程的录像（GameNGen）→ 合成物理场景（CLEVRER、MOVi、PhyWorld 的 2D 模拟）→ 公司自有车队数据（GAIA-1 的伦敦 4700 小时）→ 网络游戏视频（Genie 从 20 万小时筛出 3 万小时）→ 互联网规模视频（V-JEPA 2 超过 100 万小时；Cosmos 约 2000 万小时原始视频、筛出约 1 亿段）。

## 主线历史

每个节点写"上一节点留下的问题 → 改变 → 做不好的场景 → 站在现在看过去"。

### 1 在潜空间里做梦（2018）

**留下的问题**：基于模型的强化学习早有，但学到的模型大多只辅助、不能替代真实环境。**改变**：[World Models](../../../robotics-embodied/papers/arxiv-1803.10122/README.md)（Google Brain、IDSIA）用 VAE 把每帧压成一个低维向量（CarRacing 32 维、VizDoom 64 维），MDN-RNN 预测下一步，线性控制器出动作；CarRacing 906 ± 21（此前 A3C 591–652），VizDoom 的控制器完全在模型生成的梦里训练后迁回真实环境。

**做不好**：控制器在梦里学会让火球凭空熄灭，τ = 0.10 时梦中 2086、真实只有 193；任务简单到随机策略采的数据就够；VAE 复现了不重要的墙砖、丢了决定任务的路砖；LSTM 容量有限。

`[判断]` 站在现在看过去：路砖一例是"压缩表示会丢掉小而关键的东西"在本方向的第一个案例，六年后 DIAMOND 把它重新提出来（节点 5）。

### 2 潜空间动力学成为主线：Dreamer 一线与离散潜变量（2019–2023）

**留下的问题**：VAE 与动力学分开训练，表示不服务于预测；随机潜变量多步展开误差大。**改变**：Dreamer 一线（Hafner 等）把编码、动力学、奖励预测放进一个循环状态空间模型端到端训练，DreamerV2 改用离散潜变量减少误差累积（据 DIAMOND 的相关工作综述），[DreamerV3](../../papers/dreamerv3/reading.md)（2023）用一套固定超参在 150 多个任务上超过专门方法，第一次在 Minecraft 中不靠人类数据挖到钻石。IRIS 等用离散自编码器把画面变成 token、再用自回归 Transformer 组合，把语言模型的做法搬进来。

**做不好**：DreamerV3 每个任务单独训练智能体；2023 年 v1 的 Minecraft 结果只是有时挖到钻石，且加快了方块破坏速度；2025 年 Nature 版报告全部训练运行均挖到钻石，版本差异见 [DreamerV3 精读](../../papers/dreamerv3/reading.md)。它写明以往世界模型要按环境调表示损失：3D 环境细节多需要强正则，2D 游戏里单个像素可能决定任务、需要弱正则。

`[判断]` 站在现在看过去：DreamerV3 的这段话说明"保留哪些细节"一直靠调权重处理，而不是由模型自己知道。DIAMOND（2024）的对比图把问题摆在眼前：IRIS 生成的 Asterix 里敌人与奖励来回互换，Breakout 的砖块与分数前后不一致，Road Runner 路上的小奖励点时有时无。

### 3 给状态加结构：对象槽与驾驶世界模型（2022–2023）

**留下的问题**：像素级预测对前景和背景一视同仁，物体动力学学不好、长时预测不现实（SlotFormer 引言）；驾驶需要几何与多个交通参与者。**改变**分两支：

- **对象中心**（Google Research 的 Kipf 等）：[SAVi++](../../papers/arxiv-2206.07764/README.md)（2022）让对象槽预测深度，作者称这是端到端槽模型在真实复杂视频上涌现出物体分解的第一个概念验证（Waymo 驾驶视频）；[SlotFormer](../../papers/arxiv-2210.05861/README.md)（2022，Toronto 与 Google Research）在槽上用 Transformer 自回归预测，长时动力学好于像素基线，并用于 CLEVRER、Physion 问答和 PHYRE 规划。
- **驾驶**：[GAIA-1](../../papers/arxiv-2309.17080/README.md)（2023，Wayve）把视频、文本、动作统一成 token，6.5B 自回归世界模型加 2.6B 视频扩散解码器，4700 小时自有数据，并拟合出规模定律；[OccWorld](../../papers/arxiv-2311.16038/README.md)（2023，清华）在 3D 占据栅格上做同样的 token 预测，同时输出自车轨迹。

**做不好**：SlotFormer 自述所依赖的对象中心模型仍扩展不到真实世界视频，而且是确定性的，表示不了未来的不确定性；SAVi++ 需要首帧物体框作提示和深度监督，物体消失再出现没有建模。GAIA-1 不能实时，评测几乎全是定性示例；OccWorld 预测不出从视野外新进入的车辆，3 秒规划误差（1.99 米）落后于端到端驾驶模型 UniAD（1.65 米）。

`[判断]` 站在现在看过去：结构化状态在"结构可以从传感器拿到"的地方站住了（激光雷达给深度、占据栅格给几何，于是驾驶一支延续下来），在通用视频上没有扩展开。2024 年视频生成团队选择的是另一条路：不预先规定结构，让一致性从规模中涌现（Genie 3 博客明说其一致性是涌现的，没有显式 3D 表示）。驾驶综述（[A Survey of World Models for Autonomous Driving](../../papers/arxiv-2501.11260/README.md)）把可扩展的时序记忆和有原则的安全验证列为仍未解决的问题，并指出纯合成训练数据的安全评估是开放问题。

### 4 视频生成被宣称为世界模拟器，可控交互从无标注视频中学出（2024 年上半年）

**留下的问题**：此前的世界模型都在窄领域里训练，需要动作标注；视频生成正在规模化，但只能"看"不能"玩"。**改变**：OpenAI 的 [Sora 技术报告](../../papers/sora-tech-report/README.md)（2024 年 2 月）题为"视频生成模型作为世界模拟器"，报告随规模涌现出 3D 一致、物体被遮挡后仍保持（"并不总是"）、Minecraft 模拟，结论是扩大视频模型是通向物理与数字世界通用模拟器的可行路径。同月 Google DeepMind 的 [Genie](../../papers/arxiv-2402.15391/README.md) 从 3 万小时无标注平台游戏视频学出 8 个潜在动作，原文自称是第一个只用无标注网络视频训练、可逐帧操控的生成式交互环境。

**做不好**：Sora 自述玻璃破碎等基本交互的物理不对，吃东西不总留下咬痕，长视频不连贯、物体凭空出现；它没有逐帧动作接口。Genie 约 1 帧/秒，只有 16 帧记忆，会幻想不现实的未来，也没有发布权重。

`[判断]` 站在现在看过去：Sora 的"世界模拟器"是从样例里归纳的主张，后来的专项评测给它设了边界。Physics-IQ（2025）发现 Sora 视觉真实感最高、物理理解并不领先，还常违背"固定机位"的要求插入切镜；PhyWorld（2024）在可控的合成数据上说明，单纯扩大规模解决不了分布外的物理，模型按最相近的训练样例泛化，属性优先级是颜色 > 大小 > 速度 > 形状，作者用它解释视频模型为什么难以保持物体一致。VideoPhy（2024）在 12 个模型上发现，同时符合描述和物理常识的比例最高只有 39.6%。

### 5 可玩的扩散世界模型（2024 年下半年）

**留下的问题**：离散 token 丢细节（节点 2），Genie 太慢（节点 4）。**改变**：三家几乎同时把扩散模型改造成"以过去帧和动作为条件、去噪出下一帧"的逐帧自回归生成器。

- [DIAMOND](../../papers/arxiv-2405.12399/README.md)（Geneva、Edinburgh、Microsoft Research）：智能体完全在扩散世界模型里训练，Atari 100k 平均人类归一化分 1.46，小细节重要的游戏上优势最大；DDPM 少步去噪时误差迅速累积，换成 EDM 形式（Karras 等 2022 提出的一种扩散参数化与训练配方）后一步也稳定。
- [GameNGen](../../papers/arxiv-2408.14837/README.md)（Google Research 与 DeepMind）：改造 Stable Diffusion，单 TPU 上 20 帧/秒运行 DOOM；训练时给上下文帧加噪声，让模型学会修正自己生成的错误，否则静止不动的轨迹在 20–30 步后画质就迅速变差；单独微调解码器修复底部状态栏（HUD：显示弹药、血量、武器的抬头显示）这类小细节。
- [Genie 2](../../papers/genie-2-blog/README.md)（2024 年 12 月，DeepMind）：从一张图生成可用键鼠操作的 3D 世界，结构是"自回归的潜空间扩散模型"，用无分类器引导（同时算有条件和无条件两次预测、放大两者差异）增强动作可控性。

**做不好**：记忆是共同瓶颈。DIAMOND 的 CS:GO 模型靠近墙或丢失视野就忘记当前状态，换出新武器或新区域，还允许空中连跳，作者预期规模能修复多数问题，唯独记忆除外；GameNGen 只看 3 秒多历史，增大上下文收益很小，会学到"反复开枪就生成敌人"这类错误启发式，只能模拟训练过的那一个游戏；Genie 2 一致的世界最长约一分钟、多数 10–20 秒，实时版本是蒸馏模型、画质下降。

`[判断]` 站在现在看过去：这一节点的三个工程补丁（加噪训练抗漂移、EDM 抗少步误差、解码器微调保小细节）都在处理同一个矛盾：训练时看真实历史，生成时看自己的输出，误差会沿时间累积。屏幕上的数字既要画对又承担记忆，所以"关键符号不变"在这里第一次成为可检验的要求：DIAMOND 的 Breakout 分数按规则正确加 7，IRIS 的不行；GameNGen 专门为 HUD 微调解码器。

### 6 世界基础模型与"要不要画像素"的分岔（2025）

**留下的问题**：可玩的世界只覆盖单个游戏或几十秒；物理一致性没有被系统测量。**改变**：

- NVIDIA 的 [Cosmos](../../papers/arxiv-2501.03575/README.md)（2025 年 1 月）把世界模型做成开放权重的视频底座：约 2000 万小时原始视频筛出约 1 亿段，同时提供扩散与自回归两类，并受 PhyWorld 启发用物理仿真场景测物理对齐。
- Meta FAIR 的 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)（2025 年 6 月）走相反方向：JEPA（联合嵌入预测架构：在学到的表征空间里预测被遮住或未来的部分，不重建像素）在 100 万小时以上视频上预训练，再用 62 小时无标注机器人视频后训练动作条件预测器 V-JEPA 2-AC。它在引言里批评视频生成一线"往往更重视预测的保真度和画质，而不是规划能力"。同一机械臂抓放任务上，V-JEPA 2-AC 每个动作规划 16 秒、抓放杯子 80%，以 Cosmos 作世界模型时每个动作 4 分钟、0%。前作 V-JEPA（2024）属于[视频与时序方向](../video-temporal/README.md)。
- Google DeepMind 的 [Genie 3](../../papers/genie-3-blog/README.md)（2025 年 8 月）：文字生成世界，720p、24 帧/秒实时，数分钟内基本一致，视觉记忆约一分钟；新增"可提示的世界事件"，交互中用文字改天气、加入物体与角色。

**做不好**：Cosmos 自述缺乏物体永久性、接触丰富的动力学不准、指令遵循不一致，自回归模型常有物体从下方凭空冒出，更大的模型物理并不更好。V-JEPA 2-AC 对相机位置敏感（要从单目画面隐式推断动作坐标轴），误差随自回归累积，目标只能给图像。Genie 3 的动作空间有限、多智能体交互难、真实地点不准、清晰文字通常只在描述里写明时才出现、连续交互只支撑几分钟。

`[判断]` 站在现在看过去：分岔的根源是用途。要给人看、给智能体当环境，就必须画像素，于是继承了视频生成的物理与一致性问题（Cosmos、Genie 3）；只要拿来规划，就可以不画像素，换来速度，代价是目标要用图像给出、结果难以被人检查（V-JEPA 2）。2025–2026 年这两条线在机器人上的用法（评估 VLA、合成数据、与策略合并）见[机器人侧页面](../../../robotics-embodied/fields/world-models/README.md)的节点 5–6。

### 7 视频动力学、想象训练与动作接口重新汇合（2025 年末–2026）

**留下的问题**：Dreamer 一线会在想象中学策略，但要扩展到复杂视频；视频生成一线能造更多场景，但模型接口与真实动作、奖励学习仍然分开。接在节点 6 后，优先读三篇：

1. **[Dreamer 4](../../papers/arxiv-2509.24527/README.md)，必读。** 将循环动力学换成可扩展的 Transformer，连续视频分词器保留可生成的状态；shortcut forcing（一并训练少步跨越去噪区间与带噪历史续写）让长时间想象训练算得起。它把“纯离线数据训练的智能体能否挖到 Minecraft 钻石”作为验证，连接了生成质量与控制结果。
2. **[Cosmos-Predict2.5 / Transfer2.5](../../papers/arxiv-2511.00062/README.md)，选读桥接。** 前者统一文本、图像、视频条件，用视频奖励做后训练；后者用空间控制条件改变外观。这解释了初代平台怎样从通用生成走到更可控的数据生成与仿真接口。
3. **[Cosmos 3](../../papers/arxiv-2606.02800/README.md)，必读。** 把推理流与扩散生成流放入 Mixture-of-Transformers（不同模态使用不同参数、通过注意力交换信息的结构）。给动作加噪、给视频加噪或两者都加噪，分别得到逆动力学、正向动力学和视频–动作联合生成；状态预测与动作输出由同一个接口连接。

`[判断]` 新的分歧已经不只是“画像素还是不画像素”，还包括模型负责什么闭环：Dreamer 4 用生成轨迹训练行为，Cosmos 3 同时学习状态变化与动作。应把视频真实感、动作条件预测、最终控制效果分开评测，才能知道统一接口是否带来任务收益。预测式表征的另一条后继 [V-JEPA 2.1](../../papers/arxiv-2603.14482/README.md) 则修复局部特征的训练约束，见[视频与时序方向](../video-temporal/README.md)。

## 趋势

以下都是 `[判断]`，支撑论文和反例列在批注。观点层的对应论证见[《生成收敛》](../../../perspectives/generative-convergence.md#从视频生成到世界模型)。

**1. "状态保留什么"出现了两个相反的答案。** 早期是"压缩一切再说"（VAE），之后发现压缩会丢掉关键的小东西（路砖、分数、红绿灯），一条线改为保留全部像素细节（DIAMOND、GameNGen、Genie 2/3、Cosmos），另一条线改为主动丢弃不可预测的细节（V-JEPA 2）。哪个对取决于用途：要被人看、要当环境就选前者，要快速规划就选后者。这与[视觉表征方向](../visual-representation/README.md)"按性质组合多种表征"的结论一致。

**2. 动作接口从"真实动作"扩展到"潜在动作"和"文字"，可编辑性成为目标。** 2018–2023 年的世界模型只接受环境定义的动作；Genie 从无标注视频学出潜在动作，GAIA-1 用文字改天气、加车辆，Genie 2 从同一帧生成不同动作下的反事实，Genie 3 用文字触发世界事件。可编辑意味着用户能改变一个正在运行的世界，而不只是续写它；它同时带来新的失败：Genie 3 的世界事件不一定由智能体自己执行，《生成收敛》引用的 Seedance 2.0 报告记录了编辑没被响应或改了不该改的区域。

**3. 一致性的标准从"帧像"升到"世界不变"，关键符号与物体成为试金石。** 下表把各阶段"该不变的东西变了"的证据放在一起：

| 该保持不变的东西 | 失败的证据 | 补救或进展 |
|---|---|---|
| 决定任务的小图块 | World Models 的 VAE 丢了路砖 | DIAMOND 直接生成像素 |
| 分数、物体类别 | IRIS 中敌人与奖励来回互换，Breakout 分数不一致 | DIAMOND 的分数按规则加分 |
| HUD 数字（兼作记忆） | GameNGen 的预训练自编码器在 HUD 上产生明显伪影 | 微调解码器 |
| 文字 | Genie 3：清晰文字通常只在描述里写明时才出现 | 未解决 |
| 物体身份与形状 | PhyWorld：红方块变成球，形状的优先级最低；VideoPhy：刚体随时间变形 | 增加组合多样的数据（PhyWorld 的建议） |
| 物体永久性 | Sora：物体凭空出现；Cosmos：缺乏物体永久性；SAVi++：消失再出现未建模；DIAMOND：视野丢失后换出新区域 | Genie 2/3：离开视野的区域回来时正确渲染，视觉记忆约一分钟 |

**4. 做世界模型的主力从强化学习团队转向视频生成团队，评测随之从"像不像"转向"对不对"。** 2018–2023 年的代表作出自基于模型的强化学习（Ha 与 Schmidhuber、Hafner 等），评测是回报；2024 年后受关注的大模型出自视频生成团队（OpenAI 的 Sora、DeepMind 的 Genie 与 GameNGen、NVIDIA 的 Cosmos），他们最初用定性样例与 FVD 展示，随后的专项评测（VideoPhy、PhyWorld、Physics-IQ，以及 Cosmos 自己的物理对齐）证明画质与物理脱钩。人员上的连续性（Genie 3 两位署名作者分别来自 Genie 与 GameNGen；Sora 报告作者 Peebles 是 DiT 第一作者）见[《生成收敛》](../../../perspectives/generative-convergence.md#从视频生成到世界模型)；对应的假说与检验方法记在思考笔记[《学术界的研究方向为什么会收敛》](../../../perspectives/notes/research-convergence.md)的假说三。

## 主要路线与团队偏好

| 团队 | `[判断]` 押注 | 代表 | 代价与做不好的地方 |
|---|---|---|---|
| Ha 与 Schmidhuber（Google Brain、IDSIA），Hafner 等（DeepMind、Toronto） | 学潜空间动力学，在想象中训练策略 | World Models、DreamerV3 | 每任务单独训练；保留哪些细节靠调正则 |
| Google DeepMind 的 Genie 团队（Parker-Holder、Rocktäschel 等）与 GameNGen 作者 | 从视频学可交互的像素世界，用来给通用智能体造无限的训练环境 | Genie、Genie 2、Genie 3、GameNGen | 不发布权重（Genie 原文明确不发布，Genie 3 为有限预览）；记忆一分钟级；动作空间窄 |
| OpenAI | 扩大视频生成本身即通向世界模拟器 | Sora | 无动作接口；物理与长时一致自述不足；不公开实现 |
| NVIDIA | 开放权重的世界基础模型平台，供物理 AI 开发者后训练成专用模型 | Cosmos | 用途列表未给实证；物理对齐不随规模提升 |
| Meta FAIR（LeCun 等） | 在表征空间预测，不生成像素 | V-JEPA 2、DINO-world | 目标要用图像给；预测结果难以直接检查 |
| 驾驶：Wayve 与学术团队 | 公司用自有车队数据做像素 token 世界模型（GAIA-1）；学术团队在公开的 nuScenes 上做 3D 占据（OccWorld） | GAIA-1、OccWorld、Drive-OccWorld | GAIA-1 不能实时、评测定性；OccWorld 长时规划变差 |
| Google Research 的对象中心一系（Kipf 等） | 先把场景分解成物体，再学物体间的动力学 | SAVi++、SlotFormer（Kipf 同时署名） | 真实视频上扩展不了 |
| 评测团队：Google DeepMind、ByteDance Research、UCLA 与 Google Research | 构造专项考题检验物理 | Physics-IQ、PhyWorld、VideoPhy | 各自覆盖一小部分物理；人工评测有偏差 |

`[判断]` 两点观察。其一，开放程度与各自的目标相关：做平台的 NVIDIA 开放权重，自己做智能体的 DeepMind 与做产品的 OpenAI 不开放，学术团队（OccWorld、DIAMOND、SlotFormer）开放代码。其二，评测物理的团队里有两家本身就训练视频模型（Google、字节跳动），但 Physics-IQ 没有测自家的 Veo 2（原文说明写作时 Veo 2 尚未普遍可用）；Physics-IQ 的末位作者 Geirhos 此前用"线索冲突"图像揭示了 ImageNet CNN 的纹理捷径（见[视觉表征方向](../visual-representation/README.md)"从测量看"），同一种"构造诊断测试找捷径"的方法被搬到了视频上。

## 当前开放问题

- **记忆靠什么？** Genie 16 帧 → GameNGen 3 秒 → Genie 2 约一分钟 → Genie 3 视觉记忆约一分钟，官方都没有说明记忆机制；DIAMOND 认为规模修不好记忆，GameNGen 发现加长上下文收益很小。入口：[Genie 3](../../papers/genie-3-blog/README.md)、[GameNGen](../../papers/arxiv-2408.14837/README.md)、[DIAMOND](../../papers/arxiv-2405.12399/README.md)。
- **只看视频能学到物理吗？** Physics-IQ 认为不排除继续扩大规模可以做到，也可能需要更具交互性的训练；PhyWorld 认为单纯扩大规模不够，组合多样的数据更有用；Cosmos 认为需要过滤掉物理上不合理的训练视频并改进模型设计。入口：[Physics-IQ](../../papers/arxiv-2501.09038/README.md)、[PhyWorld](../../papers/arxiv-2411.02385/README.md)、[Cosmos](../../papers/arxiv-2501.03575/README.md)。
- **画像素，还是只预测表征？** 入口：[V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)、[DINO-world](../../papers/arxiv-2507.19468/README.md)、[Reconstruction or Semantics?](../../papers/arxiv-2605.06388/README.md)。
- **状态应该有怎样的结构？** 对象槽、3D 占据、隐式涌现三种答案并存；怎样区分"对任务有用的特征""能预测的表征""有结构的表征"和"符合因果与物理的表征"，还没有统一的测量。入口：[SAVi++](../../papers/arxiv-2206.07764/README.md)、[OccWorld](../../papers/arxiv-2311.16038/README.md)、[研究地图笔记](../../../perspectives/notes/research-map.md)中"世界模型与结构化表征"一条。
- **怎样评估一个世界模型？** Cosmos 写明物理保真的人工评测难以定标、可能与下游指标不一致；Physics-IQ、VideoPhy、PhyWorld 各测一部分。入口：[评估方法](../../../cross-domain/fields/evaluation/README.md)与上述三篇。

## 阅读顺序

1. [World Models](../../../robotics-embodied/papers/arxiv-1803.10122/README.md) 与 [VAE 讲义](../../../foundations/lessons/16-vae.md)：先看清"表示 + 动力学 + 控制器"三件套和路砖的例子，这是之后所有问题的起点。
2. [DreamerV3 精读](../../papers/dreamerv3/reading.md)：潜空间世界模型的完整形态，重点看表示损失与"保留哪些细节"的取舍。
3. [DIAMOND](../../papers/arxiv-2405.12399/README.md) 与 [GameNGen](../../papers/arxiv-2408.14837/README.md)：同一年从潜变量转向像素级扩散，对照看它们怎样处理自回归漂移和小细节；先读[扩散讲义](../../../foundations/lessons/17-diffusion.md)。
4. [Genie](../../papers/arxiv-2402.15391/README.md) → [Genie 2](../../papers/genie-2-blog/README.md) → [Genie 3](../../papers/genie-3-blog/README.md)：一个团队三代的自述局限，正好是"可交互、长时一致、可编辑"的进展表。
5. [Physics-IQ](../../papers/arxiv-2501.09038/README.md) 与 [PhyWorld](../../papers/arxiv-2411.02385/README.md)：读完生成一侧再读评测，检验"世界模拟器"的说法。
6. [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)：不画像素的另一条路，接着读[机器人侧页面](../../../robotics-embodied/fields/world-models/README.md)。

按问题排列的学习路线见[路线图](ROADMAP.md)，部件拆分见 [Baseline 页](BASELINES.md)，全部论文见[论文目录](PAPERS.md)。

## 批注

**为什么用 §3.6 的结构**

- 按 STYLE §3.6 的判定条件：世界模型没有自己专属的任务与 benchmark，它的"好"由用途（训练智能体、给人玩、合成驾驶数据、规划）和评测协议（逐帧误差、FVD、人工辨真伪、可控性、物理专项、下游效果）定义。2024 年后出现的物理基准（VideoPhy、PhyWorld、Physics-IQ）是评测协议而不是任务，而且它们与画质协议给出相反的排名，正是 §3.6 要先讲清楚测量的情形。机器人侧页面基于同样的理由采用 §3.6。

**易误读**

- Physics-IQ 的 29.5% 是相对"两次真实录制之间的差异 = 100%"的归一化分；MLLM 辨真伪的 55.6% 越接近 50% 越逼真。Sora 只测了图像到视频（i2v）一种设置（Physics-IQ Fig.4–5）。
- PhyWorld 的 0.012、0.427 是 2D 合成场景中的速度误差，模型规模最大 310M，结论不能直接外推到工业级视频模型；作者在附录中另用 CogVideo 的 VAE 复验了部分结论。
- GameNGen 的 58%/60% 是 10 名评测者在 1.6 秒/3.2 秒片段上认出真游戏的比例；50% 是 5–10 分钟自回归之后的 3 秒片段。
- V-JEPA 2-AC 与 Cosmos 的 16 秒对 4 分钟、80% 对 0% 来自同一实验室（Lab 2）的抓放任务（V-JEPA 2 Table 3），Cosmos 由 V-JEPA 2 作者自行微调，不是 NVIDIA 报告的结果；Cosmos 在到达任务上也有 80%。

**后继工作的证据边界**

- Dreamer 4 的离线协议来自 [§4.1](https://arxiv.org/html/2509.24527v1#S4.SS1)，使用离线动作数据与无动作视频的设置应分别读，不能把“没有环境交互”读成“没有监督”。
- Cosmos-Predict2.5 的奖励与偏好提升见 [§4.2](https://arxiv.org/html/2511.00062v2#S4.SS2)；Transfer2.5 的特定下游任务结果不等于通用接触动力学验证。
- Cosmos 3 的统一接口见 [v4 §2.2–2.3、Fig.4–5](https://arxiv.org/html/2606.02800v4#S2)。机器人策略结果有指定平台、微调数据与评测协议，榜单名次只代表论文写作时。节点 7 的“重新汇合”是对这三篇方法接口的判断。

**判断的支撑论文**（各行见 [synthesis.csv](synthesis.csv)）

- 速览 5、趋势 4（主力来自视频团队、评测转向）：Sora 报告标题与结论；Genie §1；Genie 2、Genie 3 博客与作者名单；GameNGen 作者名单；Cosmos 摘要；VideoPhy、PhyWorld、Physics-IQ 的引言都以"视频模型能否成为世界模拟器"为出发点。反例：DIAMOND（Geneva、Edinburgh、Microsoft Research）出自强化学习世界模型一线，却同样转向像素扩散；V-JEPA 2 出自表征学习团队。
- 趋势 1（两个相反的答案）：World Models §7；DreamerV3 方法一节；DIAMOND §1；V-JEPA 2 §1；OccWorld 分词器分析。反例：GAIA-1 同时做了两件事，token 回归 DINO 特征偏语义，再用扩散解码器补回像素。
- 趋势 2（动作接口与可编辑）：Genie §2；GAIA-1 §7.3；Genie 2 博客"Generating counterfactuals"；Genie 3 博客"Promptable world events"与 Limitations。
- 趋势 3（关键符号与物体）：表中各行出处见对应卡片与 synthesis.csv。边界：Genie 2/3 的"记得住"是官方定性展示。
- 节点 3 的"结构在传感器给出结构的地方站住了"：SAVi++ 依赖激光雷达深度；OccWorld 依赖占据真值或由相机自监督得到的占据；SlotFormer 附录 F。证据只有三篇，偏弱。
- 团队偏好：Genie 与 Genie 2、3 的作者重合（Parker-Holder、Bruce、Rocktäschel 等）；Kipf 同时署名 SAVi++ 与 SlotFormer；LeCun 同时署名 V-JEPA 2 与 DINO-world。开放程度一条依据：Genie §5 发布声明、Genie 3 博客、Cosmos 摘要、OccWorld 与 DIAMOND 的代码链接。

**哪些已有卡片主要属于机器人侧页面**

- 本方向目录下的 DINO-WM、FOCUS、LaDi-WM、Mask2Real-WM、EVA、Hydra-0、UniVLA、LARY、PIN-WM 等 16 张卡片以机器人操作为对象，归位与讨论在[机器人侧 Baseline 页](../../../robotics-embodied/fields/world-models/BASELINES.md)，清单见本方向[论文目录](PAPERS.md)的"主要属于机器人侧"一节。本页只在"画像素还是预测表征""潜在动作"两处引用其中几篇。

**与其他页面的关联**

- `[结构]` 世界模型的"状态更新 + 渲染"对应状态方程与观测方程；RSSM 的先验与后验对应卡尔曼滤波的预测与校正，见[机器人世界模型讲义](../../../robotics-embodied/fields/world-models.md)第四节。
- 自回归漂移（训练时喂真实历史、生成时喂自己的输出）与 [Zero-WAM 精读](../../../robotics-embodied/papers/zero-wam/reading.md)中"训练时以真实未来视频为条件、部署时只能用生成视频"是同一类问题；World Models 中控制器钻模型空子，与 LLM 后训练中策略钻奖励模型空子同类，见 [LLM 强化学习方向](../../../llm/fields/posttraining/rl/README.md)。
- 扩散、自回归、潜空间切块这些生成机制见[视觉生成方向](../generation/README.md)；视频理解一侧与 V-JEPA（2024）见[视频与时序方向](../video-temporal/README.md)。
- Physics-IQ 的"构造诊断测试"与[视觉表征方向](../visual-representation/README.md)中 Geirhos 等的线索冲突实验是同一方法。

**未核实 / 待验证**

- Sora 官方技术报告页本轮返回 403，Sora 相关内容依据本库 [Sora 卡](../../papers/sora-tech-report/README.md)在 2026-10-04 的核实记录。
- Dreamer（2019）、DreamerV2、IRIS、TWM、STORM 的原文本轮没有打开，相关描述转引自 DIAMOND 的相关工作与对照表。
- LeCun（2022）提出 JEPA 的立场论文本轮无法打开（OpenReview 返回 403），JEPA 的定义依据 V-JEPA 2 引言。
- Oasis 等其他可交互游戏世界模型、GAIA-2、Genie Envisioner 之外的驾驶与机器人视频世界模型本轮未打开原文，未收录。
- [Drive-OccWorld](../../papers/arxiv-2408.14197/README.md) 与 [DINO-world](../../papers/arxiv-2507.19468/README.md) 只核对了 arXiv 摘要；驾驶综述只核对了摘要与第 4、7 节的结论段。
- VideoPhy 的正式发表出处未核对，按 arXiv v2 引用。
