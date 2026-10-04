# Agent与上下文系统 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

Agent研究关注模型怎样利用上下文、调用工具、观察结果并调整下一步。任务分解、记忆、执行和验证可以分开设计，评估应覆盖整个闭环而不仅是一次回答。

## 一个容易混淆的边界

文本工具成功不等于真实机器人执行成功；跨场景借鉴时必须说明动作接口和观察误差的差别。

## 入门任务

用ReAct画出一次工具调用闭环，再用SayCan对照低层技能可行性怎样进入选择。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/05-advanced-bridges.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [ReAct: Synergizing Reasoning and Acting in Language Models](../../papers/react/README.md)
2. [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](../../../robotics-embodied/papers/saycan/README.md)

## 权限、隔离与软件协作

[机制导读](permissions-isolation-collaboration.md)与[本轮资料卡](PAPERS.md)把工作负载身份、动作授权、执行沙箱、资源限制、任务分解与集成验收分开。CaMeL方法段选读不计为新增全文精读；工程文档和作者经验不当论文。
