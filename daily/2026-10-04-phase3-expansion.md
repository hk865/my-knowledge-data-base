# 2026-10-04 phase3 内容扩充

本次以 phase3 的写作规范和目录为基础，把同日新增资料纳入现有知识库，并将新证据直接写回领域正文、基线与路线图。阅读顺序仍是先理解问题，再看机制、实验口径和后续方向。

## 机器人：动作表示与实时执行是两个设计选择

连续动作生成与离散自回归模型都需要解决推理期间机器人如何继续运动。更新后的 [VLA 入门](../robotics-embodied/fields/vla/README.md) 把动作表示与调度分开，并引入实时动作块衔接、离散自回归实时执行及新的评测材料。图示帮助比较模型输出形式、已承诺动作和下一段可修改动作的关系。

## 语言模型：让概览与新的证据保持一致

[推理入门](../llm/fields/inference/README.md) 更新公开方法、长度预算和草稿器演进的概括。[草拟与验证讲义](../llm/fields/inference/draft-verification-guide.md) 保留概率算例，并补上接受率与实际延迟之间的成本分析。

[长上下文入门](../llm/fields/long-context/README.md) 将混合架构的新材料写回正文，区分不同型号、训练阶段和评测版本。比较上下文能力时，同时检查可输入的长度、实际利用的信息以及计算代价。

## Agent：一次工具调用怎样经过权限与执行边界

[权限、隔离与协作讲义](../cross-domain/fields/agents/permissions-isolation-collaboration.md) 用一次代码修复串起任务契约、授权、操作系统隔离和集成验收。[CaMeL 精读](../cross-domain/papers/camel/reading.md) 再用日历与文档共享的算例展开数据依赖和信息流策略。

今天的工程资料也保留在库内。[高速电路机制导读](../perspectives/notes/engineering-exploration.md) 从边沿时间、传播延迟、回流与建立时间展开，新增一幅原创对照图。

## 本次讲义的三个入口

1. [VLA 入门](../robotics-embodied/fields/vla/README.md)：看新增证据怎样修正“路线已经合流”的简单概括。
2. [CaMeL 精读](../cross-domain/papers/camel/reading.md)：看每一步中哪个值带着什么权限，以及为什么分支依赖也重要。
3. [长上下文入门](../llm/fields/long-context/README.md)：看模型结构、部署配置和测量口径怎样共同决定一个结论的含义。

<details><summary>整理记录</summary>

以 phase3 的现有内容为基础，整合同日 main 中缺少的 26 项资料。历史来源角色和核验深度保留在 source.json 与来源档案中；新增检索材料独立登记。本轮工作位于 phase3-expand-2026-10-04 分支。未合并 main。

</details>
