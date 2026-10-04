# Qwen3.5-397B-A17B（官方模型卡）

> 状态：文献卡 · 2026 · [模型卡](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：模型卡列出的目标是三件事：文本与视觉统一的基座、高吞吐的混合结构、在真实智能体任务上可泛化的 RL。规模从 Qwen3 最大的 235B 扩到 397B 总参数、17B 激活。
- **核心方法**：沿用 Qwen3-Next 的混合结构：60 层按"3 层 Gated DeltaNet（带门控的线性注意力）+ 1 层门控注意力"重复 15 次，即线性层与全注意力层 3:1；每层后接 MoE（512 个专家，每 token 激活 10 个路由专家与 1 个共享专家）；带多步 MTP。原生上下文 262,144 token，可扩展到约 1M。模型卡称 RL 扩展到"百万级智能体环境"、任务分布逐步加难。2026-02-16 发布 397B-A17B，2026-02-24 与 03-02 陆续发布 122B 到 0.8B 的各尺寸。2026 年 4 月的 Qwen3.6 开放模型（35B-A3B MoE 与 27B 稠密）都保留这种 3:1 混合，并新增"思考保留"选项：把历史轮次的思考内容留在上下文里，模型卡称这能让智能体决策更一致、减少重复推理的 token。
- **为什么在这个库里**：[架构方向](../../fields/architecture/README.md)"线性与全注意力 3:1 混合"在 Kimi 之外的第二个大团队采用；[长上下文方向](../../fields/long-context/README.md)主线 5 的补充节点；Qwen3.6 的思考保留是[推理时计算方向](../../fields/inference/README.md)"跨轮保留思考"的证据。厂商模型卡，未发布完整技术报告（本轮未检索到）。优先级：选读。

## 批注

**易误读**
- 3:1 指层数之比；每个 Gated DeltaNet 层与门控注意力层的头数、维度不同（见模型卡），不能把它换算成"KV 缓存少 75%"。

**未核实 / 待验证**
- 官方博客（qwen.ai/blog?id=qwen3.5）为动态页面，本轮未能读取；第三方转述的"32K/256K 下解码吞吐为 Qwen3-Max 的 8.6/19.0 倍"未经核实，不写入正文。
- RL 算法（是否沿用 GSPO）与训练 token 数，模型卡未写。

## 身份信息

- 稳定标识：url:https://huggingface.co/Qwen/Qwen3.5-397B-A17B · [GitHub 仓库](https://github.com/QwenLM/Qwen3.5) · 阿里巴巴 Qwen 团队，2026-02-16
- 相关模型卡：[Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)、[Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B)（2026-04）
- 方向：llm/architecture、llm/long-context
