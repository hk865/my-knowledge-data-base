# Kimi-VL Technical Report

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2504.07491)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源 VLM 在可扩展性、效率和推理上落后纯语言模型：Qwen2.5-VL、Gemma-3 是稠密结构且不支持长思维链；早期 MoE VLM 中 DeepSeek-VL2 用固定尺寸编码器、上下文只有 4K，Aria 细粒度视觉任务弱。
- **核心方法**：400M 的 MoonViT（SigLIP-SO-400M 初始化，NaViT 式打包加二维 RoPE，原生分辨率）+ pixel shuffle 与两层 MLP + Moonlight MoE 语言模型（16B 总参数、2.8B 激活）。语言模型从已训 5.2T 文本 token 的中间检查点接着训练；多模态阶段共 4.4T token（ViT 单独训练、联合预训练、冷却、长上下文），凡是更新语言模型的阶段都是文本与多模态联合训练，上下文 128K，全程用 Muon 优化器。Thinking 版用长 CoT SFT 加在线策略镜像下降 RL，奖励只判答案对错，另加长度奖励惩罚过长回答以抑制过度思考。
- **为什么在这个库里**：[视觉语言模型方向](../../fields/vlm/README.md)主线第 7 个节点"MoE + 原生分辨率 + 长思维链 RL"的代表，RL 做法沿用 [Kimi k1.5](../../../llm/papers/arxiv-2501.12599/README.md)。自述局限：模型规模不足以处理高度专门或强依赖语言的问题；注意力参数只相当于 3B 模型，长上下文在极长输入上不够。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2504.07491（Kimi Team 等 95 位作者；当前 v3，2025-06）· [全文 PDF](https://arxiv.org/pdf/2504.07491v3) · 月之暗面（Moonshot AI，Kimi Team）
- 方向：[视觉语言模型](../../fields/vlm/README.md)、[LLM 强化学习](../../../llm/fields/posttraining/rl/README.md)
