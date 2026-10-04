# 运动控制与腿足运动：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

六步。前两步建立两条基线，第三步看它们各自在真机上坏在哪里，第四步看两条路线怎样合流，第五步看模仿学习怎样进入运动控制，第六步回到自己的问题。

## 第一步：把接口和误差层次理顺

读[运动控制讲义](../control-locomotion.md)第 5–10 节，以及 [05b 强化学习](../../../foundations/lessons/05b-reinforcement-learning.md)第 3–7 节。

为什么在这里：后面每篇论文都在改"观测 → 动作接口 → 执行"链条上的某一层。不先分清动作是关节角、接触力还是落脚点，就看不出一篇论文改的是哪个部件。

## 第二步：读两条基线

先读 [Convex MPC 精读](../../papers/convex-mpc/reading.md)，再读 [Rudin 2021](../../papers/arxiv-2109.11978/README.md)，对照 [PPO 精读](../../../llm/papers/ppo/reading.md)。

为什么在这里：
- MPC 把接触时序、摩擦、地形当作已知；
- 仿真 RL 流水线把它们交给随机化和课程。

记下两者各自假设了什么，后面的失败几乎都出在这些假设上。

## 第三步：沿 sim-to-real 的差距读学习控制

按顺序读：
1. [Hwangbo 2019](../../papers/arxiv-1901.08652/README.md)：执行器差距；
2. [Lee 2020](../../papers/arxiv-2010.11251/README.md) 与 [RMA 精读](../../papers/rma/reading.md)：接触与地面差距，以及盲走的极限；
3. [Miki 2022](../../papers/arxiv-2201.08117/README.md) 与 [Agarwal 2022](../../papers/url-https-proceedings.mlr.press-v205-agarwal23a-agarwal23a/README.md)：感知差距。

为什么在这里：这四篇各修一项差距，又各自暴露出下一项。读的时候对照[入门页](README.md)的"sim-to-real 的差距从哪里来"一表，把每篇的失败场景归到对应的行。

## 第四步：看两条路线怎样合流

先读 [DTC](../../papers/arxiv-2309.15462/README.md)，再读 [AME-1](../../papers/arxiv-2506.09588/README.md) 与 [AME-2](../../papers/arxiv-2601.08485/README.md)；可选 [Extreme Parkour](../../papers/arxiv-2309.14341/README.md) 作为不用规划器的对照。

为什么在这里：只有知道纯 RL 在稀疏落脚点上学不会（DTC 的引言）、纯模型方法在打滑和遮挡下会摔（DTC 图 4），才能理解为什么同一个团队把规划放回来，又让本体感知充当注意力的查询、直接在地图上找落脚点。读完对照[入门页](README.md#从本体状态到环境状态)"从本体状态到环境状态"一表，把 Lee 2020、RMA、Miki 2022、AME-1/2 排成一条线。

## 第五步：看模仿学习怎样进入运动控制

依次读：
1. [DeepMimic](../../papers/arxiv-1804.02717/README.md) → [AMP](../../papers/arxiv-2104.02180/README.md)：参考动作从逐帧跟踪变成判别器给的风格奖励；
2. [Escontrela 2022](../../papers/arxiv-2203.15103/README.md)：AMP 搬上四足 A1，替代 Rudin 2021 的 13 项手调风格惩罚；
3. [ExBody](../../papers/arxiv-2402.16796/README.md) 与 [OmniH2O](../../papers/arxiv-2406.08858/README.md)：人形上的动作模仿，以及"模仿特权教师比自己做 RL 好得多"的直接对照。

为什么在这里：前四步的工作大多以奖励为主要信号，读到这里才看得出模仿藏在哪些地方（参考动作、教师-学生的学生一侧、先模仿后强化），以及没有它时 RL 卡在哪里（探索不到、奖励写不出自然）。对照[入门页](README.md#为什么绕不开模仿学习)的三种形式表。

## 第六步：回到恢复与鲁棒

读[四足故障后恢复思考笔记](../../../perspectives/notes/quadruped-recovery.md)，按笔记"待验证"第 1–3 步补齐实验记录。相关论文按需读：
- 先读 [Lee 2019](../../papers/arxiv-1901.07517/README.md)（倒地起身）与 [CaT](../../papers/arxiv-2403.18765/README.md)（失败后不重置）；
- 再读 [Shi 2024](../../papers/arxiv-2405.12424/README.md)（主动搜长尾失败）。

为什么在这里：恢复问题依赖前四步的全部概念，包括终止条件怎样设、策略看到了什么、仿真里有没有这种状态。前四步读完，笔记里第 8 条的排查顺序就有了论文依据。

## 可选支线

- **人形与全身控制**：[Humanoid-Gym](../../papers/arxiv-2404.05695/README.md) → [H2O](../../papers/arxiv-2403.04436/README.md) → [BeyondMimic](../../papers/arxiv-2508.08241/README.md) → [规模化行为基础模型](../../papers/arxiv-2607.15163/README.md)。看四足的流水线搬到人形后哪些部件要换。
- **四足动作模仿上真机**：[Peng 2020](../../papers/arxiv-2004.00784/README.md)（模仿真狗，真机上用 RL 适应）对照 Escontrela 2022。
- **工业界方案**：读[入门页的工业界方案](README.md#工业界方案成熟在哪里没公开什么)，再打开 [unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) 的配置文件，逐项对照自己的训练设置（随机化、PD 增益、sim2sim 校验）。
- **步态先验**：[CPG-RL](../../papers/arxiv-2211.00458/README.md) 与 [相位引导的步态切换](../../papers/arxiv-2201.00206/README.md)。动作接口的另一种设计，对应思考笔记"背景"中提到的 CPG。
