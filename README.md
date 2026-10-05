# 研究兴趣与论文知识库

按基础概念、研究领域、细分问题和单篇论文逐层阅读。跨方向的同一论文只维护一个规范目录。

> 收录 596 项资源，其中 42 篇有讲解。

## 四层入口

建议的阅读顺序：基础 → 观点 → 领域 → 单篇论文；跨方向页在需要时查阅。

- **基础** · [深度学习基础](foundations/README.md)：24 个模块讲机制怎么算，分区页是概念地图，[关系页](foundations/relations/README.md)讲模块之间的结构对应
- **观点** · [观点与思考笔记](perspectives/README.md)：跨领域的论证，例如[深度学习的规模化](perspectives/scaling.md)、[CNN 与 Transformer](perspectives/cnn-vs-transformer.md)、[生成式建模的收敛](perspectives/generative-convergence.md)
- **领域**
  - [大语言模型](llm/README.md)：预训练、SFT、偏好学习、强化学习、架构、推理与长上下文
  - [多模态与世界表征](multimodal/README.md)：视觉表征、图文对齐、VLM、生成、视频与世界模型
  - [机器人与具身系统](robotics-embodied/README.md)：感知、状态估计、导航、控制、策略、VLA、世界模型与Agents
- **跨方向** · [跨方向方法与科学](cross-domain/README.md)：[训练科学](cross-domain/fields/training-science/README.md)、[模型科学](cross-domain/fields/model-science/README.md)、评估、Agents、知识蒸馏与生物计算线索

每个领域方向都有入门、Baseline、路线图和论文入口。按模态（文本、图像、视频、动作等）与任务（理解、生成、决策等）的交叉浏览见[主题目录](docs/topics.md)。

## 机器人领域教学讲义

[8篇机器人领域讲义](robotics-embodied/README.md)面向已有基础深度学习、物理与运动学知识的读者，包含逐步解释、算例与原创图示。

## 单篇论文怎样组织

每篇论文或资源有唯一文件夹：

- README：文献卡或资料卡，说明问题、方法、阅读理由并提供官方原文入口
- reading.md：独立讲解，只在有讲解的论文中出现
- figures/：讲解中的原创图示
- source.json：原文地址、阅读版本、许可与规范路径
- 原文：使用官方全文链接，不镜像论文PDF

阅读的主入口是领域目录和单篇文件夹。旧docs/deep-readings、机器人baselines和2026论文路径保留可打开的转接页。

## 目录与索引

- [全部论文与资源目录](docs/paper-catalog.md)
- [按细分类浏览](docs/topics.md)
- [待核实线索](docs/unresolved.md)
- [Baseline总导航](BASELINES.md)
- [结构化论文JSON](papers.json) · [CSV](papers.csv)
- [学术内容索引](index.json) · [CSV](index.csv)

## 研究问题与日常更新

- [研究兴趣与问题地图](perspectives/notes/research-map.md)
- [模型训练与多模态背景](perspectives/notes/model-training-multimodal.md)
- [知识蒸馏的历史文献入口](cross-domain/fields/knowledge-distillation/history.md)
- [每日短报](daily/)
- [写作规范](STYLE.md) · [维护手册](MAINTAINING.md) · [同步约定](SYNC.md)

本仓库为公开学术知识库，不存放原始聊天记录、凭据或无关个人资料。

## 最新短报与机制导读

[10月5日研究短报](daily/2026-10-05.md)：Agent 记忆的历史证据、Cordis 组件生命周期与算子实现入口。

[记忆机制讲义](cross-domain/fields/agents/memory-evidence-loop.md) · [本地结构中的记忆问题](perspectives/notes/agent-memory-questions.md)

[10月4日修订说明](daily/2026-10-04-review.md)：事实勘误、证据边界、目录修复与临时兴趣归档。

[最新研究短报：从经典基线读到新问题](daily/2026-10-04-direction-recency.md)：机器人闭环、语言模型数据与蒸馏、多模态表示与生成。具体阅读顺序由各方向页维护。

[同日机制讲义更新记录](daily/2026-10-04-phase3-expansion.md)：VLA、长上下文与 CaMeL 的讲义和配图。

[2026年10月4日研究短报](daily/2026-10-04.md) · [Agent 权限、隔离与协作](cross-domain/fields/agents/permissions-isolation-collaboration.md) · [工程资源](cross-domain/resources/README.md)

[10月3日短报](daily/2026-10-03.md) · [大小模型草拟与验证](llm/fields/inference/draft-verification-guide.md)
