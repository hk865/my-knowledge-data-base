# Agent与上下文系统：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

Agent研究关注模型怎样利用上下文、调用工具、观察结果并调整下一步。任务分解、记忆、执行和验证可以分开设计，评估应覆盖整个闭环而不仅是一次回答。

## 第二步：沿具体文章拆机制

[ReAct: Synergizing Reasoning and Acting in Language Models](../../papers/react/README.md) → [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](../../../robotics-embodied/papers/saycan/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

用ReAct画出一次工具调用闭环，再用SayCan对照低层技能可行性怎样进入选择。

## 第四步：保留边界

文本工具成功不等于真实机器人执行成功；跨场景借鉴时必须说明动作接口和观察误差的差别。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。

## 2026年10月3日：验证目标与执行轨迹

[性质测试与MORPHAGENT文献卡](PAPERS.md)分别检查可执行性质与变形关系下的轨迹行为。性质可能错误，关系可能只覆盖目标的一部分；测试通过不等于开放环境中的任意语义目标均正确。

## 2026年10月4日：互补边界与协作接口

先读[机制导读](permissions-isolation-collaboration.md)，再沿资料卡核查Cedar授权、Linux隔离原语、gVisor/Wasmtime与CaMeL威胁模型。另将多Agent任务合同、持续集成与抽象层迁移作为软件协作经验，比较从零开发、既有架构内开发和重构的不同约束。层级深度不作为可靠性保证；未据此实施新架构。
