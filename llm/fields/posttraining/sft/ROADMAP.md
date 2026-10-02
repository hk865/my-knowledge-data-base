# 监督微调 SFT：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

监督微调用示范告诉模型在什么上下文里产生什么回应。理解它时要同时看数据的角色标记、损失掩码、示范质量和部署任务，而不能只把它当成继续训练若干轮。

## 第二步：沿具体文章拆机制

[Language Models are Few-Shot Learners](../../../papers/gpt3/README.md) → [Training language models to follow instructions with human feedback](../../../papers/instructgpt/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

给一个多轮对话标出仅对回答计算损失的token，再对照InstructGPT的SFT阶段。

## 第四步：保留边界

SFT拟合示范；偏好学习利用回答之间的比较。两者可以顺序组合，但监督对象不同。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
