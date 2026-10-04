# 语言模型强化学习的基线

> 状态：Baseline 页 · v1 · 依据 [synthesis.csv](synthesis.csv) 与各篇原文

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md) · [后训练总览](../README.md)

## 基线是谁、为什么是它

结论：有两个基线。InstructGPT 的 PPO 定义了"奖励模型打分 + 价值模型估优势 + 奖励中扣 KL"的 RLHF 形态；DeepSeekMath 提出、DeepSeek-R1 规模化的 GRPO 定义了"规则验证 + 组内相对优势 + 无价值模型"的 RLVR 形态。2025 年以后的工作几乎都以 GRPO 为起点，在实验表里拿它作对照。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| [InstructGPT](../../../papers/instructgpt/reading.md) 的 PPO（2022，OpenAI；算法来自 [PPO](../../../papers/ppo/reading.md)，2017） | 状态 = 提示 + 前缀，动作 = token；奖励 = 6B 奖励模型分数 − β·逐 token KL(策略‖SFT)；价值模型从奖励模型初始化，GAE 估优势；PPO-Clip 更新，PPO-ptx 混入预训练梯度。评估：成对人评与对齐税 | RLHF 的标准实现；Anthropic HH、Llama 2、Tulu 3、Xu 等都按它实现 PPO，DeepSeekMath 提出 GRPO 时以它为对照 |
| GRPO：[DeepSeekMath](../../../papers/arxiv-2402.03300/README.md)（2024）→ [DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md)（2025） | 每题采 G 个回答（R1 为 16），优势 = (奖励 − 组内均值) / 组内标准差，整条回答共享；不要价值模型；KL 直接加进损失；R1 的奖励只有答案正确与格式两项规则。评估：AIME、MATH-500、GPQA、LiveCodeBench、Codeforces 的 pass@1 | R1 公开后成为开源推理 RL 的默认算法；DAPO、Dr. GRPO、Cui 等都以"朴素 GRPO"作基线，Qwen3、V3.2、V4 直接采用 |

同期还有一条不用价值网络、也不用组内标准差的路线：[Kimi k1.5](../../../papers/arxiv-2501.12599/README.md) 的在线镜像下降变体，以组内平均奖励为基线，并加平方形式的正则；Kimi K2 沿用它。

## 基线的结构拆分

结论：一个语言模型 RL 方案可以拆成七个可替换的部件；两个基线在"奖励来源""优势估计""正则"上差别最大。

| 部件 | 含义 | InstructGPT PPO | GRPO（R1） |
|---|---|---|---|
| 奖励来源 | 回答好坏由谁判 | 人类偏好训练的标量奖励模型 | 规则：答案匹配、编译与测试用例、格式；第二轮 RL 才加奖励模型 |
| 优势估计 | 怎样把整条回答的奖励分到 token 上 | 价值模型 + GAE，逐 token 不同 | 组内标准化的整条回答奖励，所有 token 相同 |
| 正则 | 防止策略跑偏 | 奖励中扣逐 token KL；PPO-ptx | 损失中加 KL（系数 0.001），每 400 步更新参考模型 |
| 裁剪与离策略 | 一批数据能复用几次 | PPO 裁剪 | 同样裁剪；R1 的一批 rollout 切成 16 个小批量、只训一个内层 epoch |
| 损失聚合 | 先在回答内平均还是在 token 上平均 | — | 先在每个回答内按 token 平均，再在回答间平均（样本级） |
| 数据与采样 | 训练哪些题、每题采多少 | 3.1 万条 API 提示 | 数学、代码、逻辑题；每题 16 个回答，温度 1 |
| 长度与多领域 | 怎样控制长度、怎样覆盖多个领域 | 不显式控制 | 长度自然增长；多领域靠后续的 SFT 与第二轮 RL |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 奖励来源 | 过程奖励模型（每步打分） | [Let's Verify Step by Step](../../../papers/arxiv-2305.20050/README.md)、DeepSeekMath | best-of-N 重排更准 / 步骤难定义、难标注、会被钻空子（R1 附录 G.2） |
| 奖励来源 | 规则验证器（RLVR） | [Tulu 3](../../../papers/arxiv-2411.15124/README.md)、[DeepSeek-R1](../../../papers/arxiv-2501.12948/README.md)、[Kimi k1.5](../../../papers/arxiv-2501.12599/README.md) | 不易被钻空子 / 只覆盖有标准答案的任务；能猜中答案的题要剔除 |
| 奖励来源 | 参照答案的模型评分；按 rubric 的生成式奖励模型；策略兼任评委 | [Qwen3](../../../papers/arxiv-2505.09388/README.md)、[Kimi K2](../../../papers/arxiv-2507.20534/README.md)、[DeepSeek-V3.2](../../../papers/arxiv-2512.02556/README.md)、[DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md) | 覆盖写作、对话等不可验证任务 / 评委本身的偏差与长度偏好 |
| 奖励来源 | 语言一致性奖励 | DeepSeek-R1 | 可读 / 代码评测略降 |
| 优势估计 | 组内相对，去掉价值模型（GRPO） | [DeepSeekMath](../../../papers/arxiv-2402.03300/README.md) | 省掉与策略同样大的价值模型 / 整条回答共享一个优势，无逐步信用分配 |
| 优势估计 | 去掉除以标准差与按长度归一化（Dr. GRPO） | [Dr. GRPO](../../../papers/arxiv-2503.20783/README.md) | 消除长度与难度偏差，错误回答不再越写越长 / — |
| 优势估计 | 镜像下降变体，组内均值作基线，不用价值网络 | [Kimi k1.5](../../../papers/arxiv-2501.12599/README.md)、[Kimi K2](../../../papers/arxiv-2507.20534/README.md) | 允许"走错再纠正"的轨迹得到奖励 / — |
| 正则 | 去掉 KL | [DAPO](../../../papers/arxiv-2503.14476/README.md) | 长思维链本来就要远离初始模型 / 失去对参考的约束 |
| 正则 | 无偏 KL 估计，按领域调强度 | [DeepSeek-V3.2](../../../papers/arxiv-2512.02556/README.md) | 消除 K3 估计在低概率 token 上的大梯度 / — |
| 正则 | 辅助 PTX 损失（精选高质量数据） | [Kimi K2](../../../papers/arxiv-2507.20534/README.md) | 防遗忘、防过拟合到训练任务 / 需维护精选数据 |
| 裁剪 | 上下界解耦，放宽上界（Clip-Higher） | [DAPO](../../../papers/arxiv-2503.14476/README.md) | 低概率 token 能被提起来，避免熵坍缩 / 熵过高会乱码、重复 |
| 裁剪 | 只限制高协方差 token（Clip-Cov、KL-Cov） | [Cui 等](../../../papers/arxiv-2505.22617/README.md) | 维持熵，32B 上 AIME 明显提高 / 多一个筛选超参 |
| 裁剪与离策略 | 屏蔽偏离过大的负优势序列；沿用采样时的 MoE 路由与截断掩码 | [DeepSeek-V3.2](../../../papers/arxiv-2512.02556/README.md) | 容忍推理与训练框架的不一致 / 要在推理引擎里记录路由与掩码 |
| 裁剪与离策略 | 部分 rollout；逐 token 正则容忍过期数据 | [Kimi k1.5](../../../papers/arxiv-2501.12599/README.md)、[Kimi K3](../../../papers/arxiv-2607.24653/README.md) | 长轨迹不再拖慢整批 / 数据过期 |
| 损失聚合 | 按 token 平均（token 级损失） | [DAPO](../../../papers/arxiv-2503.14476/README.md) | 长回答里的乱码与重复受到惩罚，长度增长更健康 / 分数只 +1 |
| 数据与采样 | 丢掉全对或全错的题组（动态采样） | [DAPO](../../../papers/arxiv-2503.14476/README.md) | 每批都有有效梯度 / 要多采样 |
| 数据与采样 | 少量高难度、可学的题；大批量、多 rollout | [Qwen3](../../../papers/arxiv-2505.09388/README.md)、[Kimi k1.5](../../../papers/arxiv-2501.12599/README.md) | 3,995 题、170 步 AIME'24 70.1 → 85.1 / 题目筛选成本 |
| 长度与多领域 | 长度奖励、按任务的 token 预算、按推理强度训练专家 | [Kimi k1.5](../../../papers/arxiv-2501.12599/README.md)、[Kimi K2](../../../papers/arxiv-2507.20534/README.md)、[DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md)、[Kimi K3](../../../papers/arxiv-2607.24653/README.md) | token 效率 / 预算太紧会抑制探索 |
| 长度与多领域 | 领域专家 → 蒸馏 → 混合 RL | [DeepSeek-V3.2](../../../papers/arxiv-2512.02556/README.md) | 避免多阶段的灾难性遗忘 / 仍需数千步 RL |
| 长度与多领域 | 领域专家 → 多教师 on-policy 蒸馏（替代混合 RL） | [DeepSeek-V4](../../../papers/arxiv-2606.19348/README.md)、[Kimi K3](../../../papers/arxiv-2607.24653/README.md)、[Qwen3](../../../papers/arxiv-2505.09388/README.md)（小模型） | 合并时不掉点，省算力 / 需同时服务多个教师；两家目标不同 |
| 评测口径 | 大 k 的 pass@k 测能力边界 | [Yue 等](../../../papers/arxiv-2504.13837/README.md)、DeepSeekMath §5.2.2 | 揭示 RL 主要提高采样效率 / — |
| 对照 | 同一初始化下比较 SFT 与 RL 的泛化 | [SFT Memorizes, RL Generalizes](../../../papers/arxiv-2501.17161/README.md) | RL 泛化、SFT 记忆 / 只在规则游戏与导航上 |

## 批注

**易误读**

- "GRPO 去掉价值模型"不等于不估计优势：它把同组其他回答当基线，代价是一条回答里所有 token 的优势相同，没有逐步的信用分配。
- DeepSeekMath 的 GRPO 用的是训练的奖励模型（含过程监督），"GRPO + 规则奖励"的组合来自 R1；两者不要混为一谈。
- R1 的 GRPO 裁剪比率是 10（§3.2.1），DAPO 的上界是 1 + 0.28，PPO 原文常用 1 ± 0.2；"裁剪"在三篇里的松紧差别很大。

**与其他论文的关联**

- [偏好学习 Baseline 页](../preferences/BASELINES.md)：InstructGPT 的奖励模型部分在那里拆；DeepSeekMath 认为组内相对优势与奖励模型"在同一问题的回答间比较"的训练方式相契合（§4.1）。
- [SFT Baseline 页](../sft/BASELINES.md)：冷启动 SFT 是 RL 前的一格，on-policy 蒸馏在两张表中都出现。
- [PPO 精读](../../../papers/ppo/reading.md)批注："PPO 的 KL"与"RLHF 的 KL"的区别，是读懂本表"正则"一行的前提。
- 机器人侧的同类改动：[SimpleVLA-RL](../../../../robotics-embodied/papers/arxiv-2509.09674/README.md) 在 VLA 上采用了放宽裁剪上界、动态采样与去 KL。

**未核实 / 待验证**

- Kimi k1.5 与 K2 的策略优化目标中"平方形式的正则"按 K2 第 3.2.3 节公式的结构描述，系数与推导本轮未逐项核对。
