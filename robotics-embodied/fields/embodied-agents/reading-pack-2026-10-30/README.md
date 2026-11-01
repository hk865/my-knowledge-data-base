# 机械臂 Embodied Agent 研究资料库

核查截止：**2026-10-30**。本资料包索引 **21 篇固定版本预印本、21 篇中文解读**，覆盖 2022 年技能语言规划，到 2026 年代码策略、VLA 外层 Agent、技能积累与规划器后训练。最新核心条目首投于 2026-10-20；这是围绕本项目问题的选读，不是穷尽整个领域的排行榜。

先读 [发展路线](发展路线.md)，再读 [研究选项与公平对照](研究选项与公平对照.md)。版本与既有资料的关系见 [来源与版本](来源与版本.md)，文件检查见 [校验记录](校验记录.md)。原文使用 arXiv 官方链接。本地 21 份 PDF 全部保留，按照知识库同步约定不公开镜像全文；逐篇许可见[发布与许可记录](来源与版本.md)。

## 建议先读的六篇

1. [Code as Policies](../../../papers/arxiv-2209.07753/reading.md)：理解“代码是策略”究竟输出什么。
2. [Inner Monologue](../../../papers/arxiv-2207.05608/reading.md)：理解执行反馈为何必须回到决策层。
3. [VoxPoser](../../../papers/arxiv-2307.05973/reading.md)：看语言与连续几何控制怎样分工；再读 [ReKep](../../../papers/arxiv-2409.01652/reading.md)。
4. [Harness VLA / RPent](../../../papers/arxiv-2607.08448/reading-2026-10-30.md)：对齐我们当前已经运行的上游系统。
5. [CaP-X](../../../papers/arxiv-2603.22435/reading.md)：把模型、工具、观测和试错预算拆开比较。
6. [RAX](../../../papers/arxiv-2610.22496/reading.md)：理解探索如何沉淀为可重用程序；需要训练路线再读 [AgenticRoboRL](../../../papers/arxiv-2610.28589/reading.md)。

## 全部核心条目

下表按**首次预印本时间**排序，保存的是明确版本。每篇解读给出问题、机械臂执行过程、训练与先验、证据边界和本项目可借鉴点。所有论文均未在本次工作中复现；“定向阅读”不代表逐页通读。

| 首次预印本 | 工作与解读 | 主要问题 | 保存版本 | 官方原文 |
|---|---|---|---|---|
| 2022-04-04 | [SayCan](../../../papers/saycan/reading-2026-10-30.md) | 语言计划怎样受技能可行性约束 | v2 · 2022-08-16 | [官方 PDF](https://arxiv.org/pdf/2204.01691v2) |
| 2022-07-12 | [Inner Monologue](../../../papers/arxiv-2207.05608/reading.md) | 执行反馈怎样改变下一步计划 | v1 · 2022-07-12 | [官方 PDF](https://arxiv.org/pdf/2207.05608v1) |
| 2022-09-16 | [Code as Policies](../../../papers/arxiv-2209.07753/reading.md) | 程序怎样表达空间计算与反馈 | v4 · 2023-05-25 | [官方 PDF](https://arxiv.org/pdf/2209.07753v4) |
| 2022-09-22 | [ProgPrompt](../../../papers/arxiv-2209.11302/reading.md) | 程序计划怎样检查前提并恢复 | v1 · 2022-09-22 | [官方 PDF](https://arxiv.org/pdf/2209.11302v1) |
| 2023-07-12 | [VoxPoser](../../../papers/arxiv-2307.05973/reading.md) | 语言怎样转成可优化的三维目标 | v2 · 2023-11-02 | [官方 PDF](https://arxiv.org/pdf/2307.05973v2) |
| 2024-09-03 | [ReKep](../../../papers/arxiv-2409.01652/reading.md) | 关键点关系怎样约束连续动作 | v2 · 2024-11-12 | [官方 PDF](https://arxiv.org/pdf/2409.01652v2) |
| 2025-04-22 | [π0.5（VLA 背景）](../../../papers/arxiv-2504.16054/reading.md) | 训练的动作底座负责哪一层 | v1 · 2025-04-22 | [官方 PDF](https://arxiv.org/pdf/2504.16054v1) |
| 2025-09-23 | [LYRA（2025 v2）](../../../papers/arxiv-2509.18597/reading.md) | 人类纠错怎样沉淀为代码技能 | v2 · 2025-09-25 | [官方 PDF](https://arxiv.org/pdf/2509.18597v2) |
| 2026-03-03 | [Act-Observe-Rewrite](../../../papers/arxiv-2603.04466/reading.md) | 回合间怎样改写完整控制程序 | v1 · 2026-03-03 | [官方 PDF](https://arxiv.org/pdf/2603.04466v1) |
| 2026-03-23 | [CaP-X](../../../papers/arxiv-2603.22435/reading.md) | 怎样拆开接口、感知与 Agent 能力 | v2 · 2026-07-02 | [官方 PDF](https://arxiv.org/pdf/2603.22435v2) |
| 2026-04-20 | [HELM](../../../papers/arxiv-2604.18791/reading.md) | 记忆与验证器怎样选择动作 | v1 · 2026-04-20 | [官方 PDF](https://arxiv.org/pdf/2604.18791v1) |
| 2026-06-18 | [ENPIRE](../../../papers/arxiv-2606.19980/reading.md) | Agent 怎样组织真机策略改进 | v2 · 2026-09-20 | [官方 PDF](https://arxiv.org/pdf/2606.19980v2) |
| 2026-06-30 | [ASPIRE](../../../papers/arxiv-2607.00272/reading.md) | 失败诊断怎样变成验证过的技能 | v2 · 2026-10-20 | [官方 PDF](https://arxiv.org/pdf/2607.00272v2) |
| 2026-07-09 | [Harness VLA / RPent](../../../papers/arxiv-2607.08448/reading-2026-10-30.md) | 怎样把冻结 VLA 变成可编排原语 | v5 · 2026-09-24 | [官方 PDF](https://arxiv.org/pdf/2607.08448v5) |
| 2026-09-11 | [Agent as Policy](../../../papers/arxiv-2609.12541/reading.md) | 通用 Agent 能否直接写操作程序 | v3 · 2026-09-28 | [官方 PDF](https://arxiv.org/pdf/2609.12541v3) |
| 2026-09-27 | [CodeActionBench](../../../papers/arxiv-2609.33807/reading.md) | 怎样公平评估代码操作 Agent | v1 · 2026-09-27 | [官方 PDF](https://arxiv.org/pdf/2609.33807v1) |
| 2026-09-29 | [RoboSkill](../../../papers/roboskill/reading-2026-10-30.md) | 探索经验怎样复用于下一次执行 | v1 · 2026-09-29 | [官方 PDF](https://arxiv.org/pdf/2609.37810v1) |
| 2026-09-30 | [URAI](../../../papers/arxiv-2609.39018/reading.md) | 工具生成与运行时决策怎样分工 | v1 · 2026-09-30 | [官方 PDF](https://arxiv.org/pdf/2609.39018v1) |
| 2026-10-01 | [OpenRUA](../../../papers/arxiv-2610.02459/reading.md) | 通用 Agent 怎样使用原生机器人接口 | v1 · 2026-10-01 | [官方 PDF](https://arxiv.org/pdf/2610.02459v1) |
| 2026-10-15 | [RAX](../../../papers/arxiv-2610.22496/reading.md) | 在线探索怎样留下可复用程序 | v1 · 2026-10-15 | [官方 PDF](https://arxiv.org/pdf/2610.22496v1) |
| 2026-10-20 | [AgenticRoboRL](../../../papers/arxiv-2610.28589/reading.md) | 怎样只训练高层工具规划器 | v2 · 2026-10-21 | [官方 PDF](https://arxiv.org/pdf/2610.28589v2) |

## 使用这份资料时保留的边界

VLA 是动作模型的一类，完整 Agent 还涉及观测、工具决策、执行、验证和经验管理。生成代码能够表达闭环，但要看程序实际上是否重新获取观测、检查失败并改变动作。本文的“联系”与“本项目启发”是整理者的分析，不代表作者自称继承关系。

π0.5 是解释现有动作底座的背景条目；CodeActionBench/CaP-X 负责评测方法；其余条目回答不同的规划、执行、恢复或经验积累问题。因此本目录没有把论文数字直接排成优劣榜单，也没有把局部演示当作完整 benchmark。

## 目录与发布范围

- 逐篇解读存入每篇论文唯一的规范目录，已有解读保持原样，新版补充另存并相互链接。
- 本目录保存发展路线、公平对照、扩展阅读、来源与版本和校验记录。
- [结构化清单](manifest.json)保留官方来源、固定版本、阅读边界和规范路径。
- [逐篇许可核查](license-audit.json)记录官方许可入口；原文全部使用官方链接。
- [公开资料校验工具](tools/validate_publication.py)检查文件、索引、相对链接与敏感信息。

原本 4 个辅助脚本依赖本地来源快照、全文提取和机器人项目工作区，保留于本地，没有上传这些不可移植的依赖或脚本。下载所得全文提取、已有知识库快照、Git 状态记录与运行日志均未发布。
