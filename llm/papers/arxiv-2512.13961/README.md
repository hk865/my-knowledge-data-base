# Olmo 3

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.13961)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：开源权重的推理模型越来越强，但数据、中间检查点与训练代码不公开，研究者无法检查"某个能力从哪个阶段、哪批数据来"；AI2 要给出从预训练到 RL 全流程完全公开的 7B 与 32B 模型。
- **核心方法**：预训练在 Dolma 3 上进行（约 5.93T token 的混合），中段训练用 100B token 的数学、代码与推理数据（Dolmino），长上下文阶段再用 50B（7B）或 100B（32B）token 把窗口从 8K 扩到约 65K（Longmino，主要是 olmOCR 处理的科学 PDF）。Think 模型的后训练沿用 [Tulu 3](../arxiv-2411.15124/README.md) 的 SFT → DPO → RLVR 三段：DPO 用"Delta Learning"构造偏好对（被选回答来自较强模型、落选回答来自较弱模型），作者报告在同样数据上 DPO 能带来 SFT 带不来的提升；RL 改用 GRPO 的一组修改（OlmoRL）：丢掉零梯度题组、主动补采样、token 级损失、不除以标准差、放宽裁剪上界、不加 KL、截断重要性采样，并靠完全异步、连续批处理与训练中途更新推理权重把 RL 提速约 4 倍。另训练 RL-Zero 版本（基座上直接 RL），用来研究预训练数据对 RLVR 的影响；作者写明，中段训练数据若含评测内容，随机的"伪奖励"会和真奖励一样有效，因此要严格去污染。全部训练约 56 天、1024 块 H100，预训练占九成以上，后训练（SFT、DPO、RL）约 9 天；v2 报告的 Olmo 3.1 Think 32B 又在 224 块 GPU 上多跑了 21 天 RL。
- **为什么在这个库里**：[强化学习方向](../../fields/posttraining/rl/README.md)与[后训练总览](../../fields/posttraining/README.md)中 AI2 路线的最新节点（Tulu 3 用 PPO，Olmo 3 改用 GRPO 变体），[偏好学习方向](../../fields/posttraining/preferences/README.md)"DPO 仍是开放团队主力"的证据，[预训练方向](../../fields/pretraining/README.md)完全公开数据的一线。优先级：选读。

## 批注

**易误读**
- "预训练占九成以上"是 7B/32B 规模、完全公开配方下的算力分配，不能和 DeepSeek-V3.2"后训练超过预训练成本的 10%"直接对比：两者的模型规模、RL 时长与成本口径都不同。

**未核实 / 待验证**
- OlmoRL 各项修改的单独消融数字未核对；Olmo 3.1 的分数取自 v2 的表 1，未逐项对照。

## 身份信息

- 稳定标识：arxiv:2512.13961 · [全文 PDF](https://arxiv.org/pdf/2512.13961) · Allen Institute for AI（Team Olmo，66 位作者）；v1 2025-12-15，v2 2026-04-14
- 方向：llm/pretraining、llm/posttraining/sft、llm/posttraining/preferences、llm/posttraining/rl
