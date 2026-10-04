# 导航与规划的基线

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md) · [讲义](../navigation-planning.md)

## 基线是谁、为什么是它

- **经典导航栈：A\* 或 [RRT\*](../../papers/rrt-star/reading.md) 做全局规划，DWA 做局部避障。** 它定义了导航最基本的接口：输入是度量地图、机器人位姿和目标坐标，输出是一条几何路径，再由局部控制器在速度空间里挑出当下可执行的指令。评估看路径代价、计算时间和是否碰撞。A*、RRT* 的机制与手算见[讲义](../navigation-planning.md)第三、四节，DWA 与 MPC 见第六节。
- **[R2R](../../papers/r2r/reading.md)（2018）。** 它把"目标"换成了自然语言路线指令，定义了语言导航的接口：输入是全景图像和指令，输出是导航图上的离散动作与 stop；训练是对最短路教师的模仿学习（student-forcing）；评估看未见建筑里 3 m 内停下的成功率。几乎所有 VLN 工作都以它为起点，并以它的假设为改造对象。

两条基线回答不同的问题：前者回答"怎样安全到达给定坐标"，后者回答"指令说的目标在哪里"。后续工作要么把语言层接到几何层上，要么用学习替换其中一层。

## 基线的结构拆分

| 部件 | 经典栈中的形态 | R2R 中的形态 |
|---|---|---|
| ① 目标表达 | 地图坐标或目标区域 | 自然语言路线指令 |
| ② 环境表示 | 占据栅格、代价地图 | 预先建好的视点图，位姿由模拟器给出 |
| ③ 全局决策 | 图搜索或采样，最小化路径代价 | LSTM 策略按指令注意力选下一个动作 |
| ④ 局部执行 | 速度空间搜索或 MPC，满足动力学和制动约束 | 在视点之间瞬移，没有局部控制 |
| ⑤ 训练与评估 | 无训练；看路径代价、计算时间、碰撞 | 对最短路教师的模仿；看未见建筑的成功率 |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| ③ 全局决策 | 邻域按 (log n / n)^(1/d) 收缩并重连 | [RRT*](../../papers/rrt-star/reading.md) | 路径代价渐近最优；有限样本表现没有保证，狭窄通道仍难 |
| ④ 局部执行 | 学习人群交互的价值函数，代替反应式避障 | [CrowdNav（SARL）](../../papers/arxiv-1809.08835/README.md) | ORCA 人群仿真里成功率 43% → 100%；人群模型与真实行人不同，动作离散 |
| ④ 局部执行 | 在真实小车上用 RL 自主练习高速驾驶 | [FastRLAP](../../papers/fastrlap/README.md) | 真实世界在线学习；需要卡住惩罚与伪重置，否则会卡住 |
| ④ 局部执行（足式） | 凸 MPC 分配接触力，跟踪上层给的速度 | [Convex MPC](../../papers/convex-mpc/reading.md) | 四足动态步态；与路径规划是不同变量，属于[运动控制](../control-locomotion/README.md)的接口 |
| ① 目标表达 + ⑤ 训练 | 说话者模型合成指令、语用推断 | [Speaker-Follower](../../papers/arxiv-1806.02724/README.md) | R2R 测试成功率 20.4% → 53.5%；路线搜索让轨迹长达上千米 |
| ③ 全局决策 | 全景动作空间：直接选相邻视点 | [Speaker-Follower](../../papers/arxiv-1806.02724/README.md) | 每步决策粒度与人写指令的粒度一致；仍依赖导航图 |
| ⑤ 训练 | 分布式 PPO，仿真 25 亿步 | [DD-PPO](../../papers/arxiv-1911.00357/README.md) | 有 GPS+Compass 时 PointNav SPL 0.948；没有时 0.15 |
| ② 环境表示 + ④ 局部执行 | 去掉导航图，在连续环境里用低层动作执行 | [VLN-CE](../../papers/arxiv-2004.02857/README.md) | 暴露导航图的虚高（SPL 0.21 对 0.38）；任务更难、动作序列更长 |
| ④ 局部执行 + ⑤ 评估 | 子目标模型把离散动作接到真机连续运动；真机评估 | [Sim-to-Real VLN](../../papers/arxiv-2011.03807/README.md) | 有地图 46.8%、无地图 22.5%（仿真 55.9%）；子目标预测在窄缝处最难 |
| ① 目标表达 + ② 环境表示 | LLM 抽地标、CLIP 对齐到拓扑图，图搜索 | [LM-Nav](../../papers/arxiv-2207.04429/README.md) | 不需要语言标注的导航数据；忽略动词，需预先建图 |
| ③ + ④ | 跨 8 种机器人训练图像目标导航模型 | [ViNT](../../papers/arxiv-2306.14846/README.md) | 零样本控制新机器人；目标是图像，要求机器人结构与动作表示相近 |
| ③ + ④ | 目标遮罩 + 扩散策略，一个模型同时探索与到达 | [NoMaD](../../papers/arxiv-2310.07896/README.md) | 探索成功率 98%，参数 19M；目标仍只能是图像 |
| ① + ② | 前沿地图 + BLIP-2 价值图，零样本找物体 | [VLFM](../../papers/arxiv-2312.03275/README.md) | 不训练即可在 HM3D 上 SR 52.5%；只做单层 |
| ③ + ④ | VLA 输出中层语言动作，足式 RL 策略执行 | [NaVILA](../../papers/arxiv-2412.04453/README.md) | R2R-CE 54%，真机 88%；两层接口是语言，偏航后缺少纠错 |
| ③ + ④ | 慢 VLM 预测像素目标，快扩散策略出轨迹 | [DualVLN](../../papers/arxiv-2512.08186/README.md) | R2R-CE 64.3%；Social-VLN 撞人率仍有 35.4% |
| ① + ③ + ⑤ | 五类任务 3000 万样本训练的双通路模型 | [ABot-N1](../../papers/arxiv-2607.10383/README.md) | POI 到达率 77.3%；坐标漂移与城市尺度评测是作者自建 benchmark |

## 批注

**易误读**

- DD-PPO 的 SPL 0.948 依赖模拟器给出的 GPS+Compass，不能与 VLN-CE、Sim-to-Real VLN 这类不给定位的结果比较（DD-PPO Table 1）。
- Speaker-Follower 的 53.5% 用了路线搜索，提交时轨迹平均 1257 m；与贪心解码的模型比较时要看同一解码设置（Speaker-Follower 附录 E）。
- 表中 FastRLAP 与 Convex MPC 的定位依据本库已有的文献卡和精读，不是本轮新核读。

**与其他论文的关联**

- R2R 的 student-forcing 与 [RMA](../../papers/rma/reading.md) 都是 DAgger 式的数据收集，见 [R2R 精读](../../papers/r2r/reading.md)批注。
- NaVILA 与 DualVLN 的"高层定目标、低层执行"与[具身 Agent 的基线](../embodied-agents/BASELINES.md)中 SayCan 的"语言规划、技能执行"是同一种分层；部件②的环境表示由[定位与建图](../localization-mapping/README.md)提供。
- 本表各行的原文出处见 [synthesis.csv](synthesis.csv)。

**未核实 / 待验证**

- A* 与 DWA 没有建立文献卡，原文入口见 [synthesis.csv](synthesis.csv) 的来源列。
