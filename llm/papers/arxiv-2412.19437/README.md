# DeepSeek-V3 Technical Report

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：arxiv:2412.19437
- 年份：2024
- [官方原文页面](https://arxiv.org/abs/2412.19437)
- [官方全文入口](https://arxiv.org/pdf/2412.19437)
- 阅读版本：未固定版本；请核对官方版本记录
- 方向：llm/posttraining/sft、llm/pretraining、llm/architecture、llm/posttraining/rl

## 阅读内容与边界

这是文献卡，目前没有该论文的独立精读正文。标题、标识或摘要层面的核验不等于全文阅读。

本目录只有文献卡与原文元数据，没有生成 reading.md，也没有把元数据卡计为精读。

## 原文保存与许可

当前以官方原文链接为入口。本地PDF是否保存、对应版本和可再分发许可，以 [source.json](source.json) 为准；没有明确许可时不把第三方论文镜像到公开仓库。

## 2026年10月3日核验与阅读线索

- 阅读范围：§2.2 MTP、§5.4.3 Multi-Token Prediction Evaluation；不是技术报告全文阅读
- 核验版本：v2 2025-02-18
- 来源关系：历史助手推荐，检索摘要回收；不是用户亲自提供的论文，也没有原会话直链

顺序 MTP 模块融合前一深度表示与后续 token embedding，共享 embedding 和输出头，保留因果链；主目标是增强训练，推理可丢弃模块或将其作为草拟模块复用。

不能写成独立小模型给任意大模型做 draft，也不能写成多个独立预测头；报告实验第二 token 接受率 85–90%、1.8× TPS 为特定配置。

分布或质量保证：MTP 本身不构成精确分布保证；与标准验证结合才可

官方核验来源：
- [https://arxiv.org/abs/2412.19437](https://arxiv.org/abs/2412.19437)
- [https://arxiv.org/html/2412.19437v2](https://arxiv.org/html/2412.19437v2)

未独立复现，不镜像PDF。
