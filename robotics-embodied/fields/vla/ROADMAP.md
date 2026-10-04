# VLA 路线图

> 状态：路线图 · v2

[入门页](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md) · [逐步讲义](../vla.md)

结论：前五步建立模型主线，第六步检查真实执行与评测；前五步按"先弄清 VLM 怎样看图 → 读透一个离散 token 基线 → 换成连续动作块 → 看 π0.5、KI 一支怎样分工 → 看前沿在扩充什么"排列。每一步都有一个能动手检验的问题。阅读顺序与 [OpenVLA 文献卡](../../papers/openvla/README.md)一致：CLIP → LLaVA → DINO → OpenVLA。

## 第 1 步：VLM 的视觉输入从哪里来

读 [CLIP](../../../multimodal/papers/clip/reading.md) → [LLaVA](../../../multimodal/papers/llava/reading.md) → [DINO](../../../multimodal/papers/dino/reading.md)。

为什么在这里：OpenVLA 的视觉骨干是 SigLIP（CLIP 式图文对比）与 DINOv2（DINO 式自监督）的拼接，投影进语言模型的接口与 LLaVA 相同；不先读这三篇，后面"冻结视觉编码器为什么掉点""视觉 token 为什么占大部分推理时间"都无从谈起。两种特征各自擅长什么，见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)"从任务看"一节。

检验：说出 224×224 的图在 patch 14 下产生多少个视觉 token，它们怎样和文字 token 排进同一个序列（答案在 [VLA 讲义](../vla.md)第三节）。

## 第 2 步：读透离散 token 基线

读 [OpenVLA 精读](../../papers/openvla/reading.md)，对照 [RT-2](../../papers/arxiv-2307.15818/README.md) 与 [RT-1](../../papers/arxiv-2212.06817/README.md)。

为什么在这里：这是 [Baseline 页](BASELINES.md)"动作表示 = 离散 token"一格的开放代表，接口、数据清洗、评测口径都能在一篇里看全；后面每一篇都在改它的某个部件。

检验：手算一个动作维度的分桶与还原（精读"机制"第 2 小节）；再算一次 50 Hz、14 维、1 秒的动作块逐维分桶要多少个 token（700，FAST Table I），解释为什么这样的序列学不动。

## 第 3 步：换成连续动作块

读 [VLA 逐步讲义](../vla.md)第六、十节与 [π0](../../papers/arxiv-2410.24164/README.md)；动作块与扩散动作头的来源见 [Diffusion Policy 精读](../../papers/diffusion-policy/reading.md)，机制见[扩散讲义](../../../foundations/lessons/17-diffusion.md)第 6.1、7 节；跨模态的背景见[生成配方的收敛](../../../perspectives/generative-convergence.md)。

为什么在这里：π0 把"动作当词"换成 flow matching 生成的 50 步动作块，解决的正是第 2 步算出来的高频问题；讲义以 π0.5 为例，把一次训练前向和推理时的十步积分分开讲。

检验：解释为什么输出 50 步动作不等于每秒运行大模型 50 次（讲义 10.3–10.4 节）；对照 π0 的 73 ms 机载推理与 OpenVLA 在 RTX 4090 上约 6 Hz，算各自能支持的控制频率。

## 第 4 步：π0.5、KI 一支怎样分工

读 [FAST](../../papers/arxiv-2501.09747/README.md) 与 [OpenVLA-OFT](../../papers/arxiv-2502.19645/README.md)（对照着读），再读 [π0.5](../../papers/arxiv-2504.16054/README.md) → [Knowledge Insulation](../../papers/arxiv-2505.23705/README.md)。

为什么在这里：FAST 修离散 token "学不动"，OFT 修它"太慢"，两篇合起来说明离散 token 的两个坑原因不同；π0.5 与 KI 再说明连续动作头会伤 VLM，形成了"离散 token 当训练信号、连续头负责部署"的一支；第 6 步再看自回归部署的反例。

检验：用 OpenVLA-OFT 的消融（76.5% → 90.2% → 95.3% → 97.1%）分别说出并行解码与动作块、连续表示、腕部图像与本体状态各贡献多少；说出 KI 的 stop-gradient 加在哪里、为什么部署时不需要离散分支。

## 第 5 步：前沿在扩充什么

读 [π*0.6](../../papers/arxiv-2511.14759/README.md) → [π0.7](../../papers/arxiv-2604.15483/README.md)，对照 [Gemini Robotics](../../papers/arxiv-2503.20020/README.md) 与 [Gemini Robotics 1.5](../../papers/arxiv-2510.03342/README.md)；按兴趣选读 [GR00T N1](../../papers/arxiv-2503.14734/README.md)（双系统与数据金字塔）、[RoboTTT](../../papers/arxiv-2607.15275/README.md)（长上下文）、[ForceVLA](../../papers/arxiv-2505.22159/README.md)（力觉）、[Behavior Prompting Policy](../../papers/arxiv-2606.30457/README.md)（示教作提示）。

为什么在这里：2025 年底以后的工作不再主要改动作表示，而是改训练信号（从经验学）、任务条件（子任务、子目标图、元数据、示教）和上下文长度；把它们放在 [Baseline 表](BASELINES.md)里逐行对照，能看出各家押注的差别。有四足 RL 背景的话，π*0.6 的价值函数与优势可以直接对照 PPO 的做法，看它为什么在 flow matching 策略上改用优势条件化（原文 §IV-B：flow matching 没有可处理的对数似然）。

检验：给定一个自己的任务（例如四足机器人按语言指令推门），按 Baseline 表的六个部件写出要做的选择，并为每个选择指出一篇论文里的失败案例。

## 第 6 步：动作在真实时间里怎样接上、成绩在什么条件下成立

读 [RTC](../../papers/arxiv-2506.07339/README.md)（实时动作块接续：旧块执行期间生成能衔接的新块）→ [Training-time RTC](../../papers/arxiv-2512.05964/README.md)，再对照 [π0-REALFAST](../../papers/arxiv-2606.13355/README.md)。为什么在这里：第 3 步说明"怎样生成"，这一步说明"新块还没算完时谁在控制、算完后接哪一段"；它与第 4 步的训练 / 部署分工形成对照，说明自回归也可以实时执行。先看[时间轴示意](README.md#动作块之后怎样一边行动一边重新计算)。

检验（示例数值）：机器人每 20 ms 取一个动作，旧块还剩 15 步，新推理需要 100 ms。算出推理期间必须由旧块承接 5 步、余量为 10 步；再解释为什么队列里有动作，还要测轨迹跳变与新观测响应。若外部延迟变成 400 ms，原队列会先耗尽，原有预算须重设。

按自己的问题选读评测：[RoboDojo](../../papers/arxiv-2607.04434/README.md) 看多维能力与真机接口，[VLA-REPLICA](../../papers/arxiv-2605.20774/README.md) 看本地复搭，[IndustrialVLA-Bench](../../papers/arxiv-2609.25562/README.md) 看协议与证据分级。检验：为同一结果写清检查点、输入与动作接口、推理/排队方式、任务划分、成功定义、聚合方式和运行版本，再判断两行数字能否比较。

## 动手时先查什么

接一个开源 VLA（openpi 中的 π0 / π0.5、OpenVLA、SmolVLA）到自己的机器人上时，先核对动作字段的顺序、单位、绝对还是增量、坐标系和归一化统计量，再谈调模型；OpenVLA 精读里的"过滤全零首帧"、讲义 13.2 节的清单都属于这一类。离线损失和闭环成功率分开测：OpenVLA 的 int8 量化离线准确率接近，闭环成功率却从 71% 掉到 58%。
