# NVIDIA Nemotron 3: Efficient and Open Intelligence

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.20856)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：推理与智能体任务要生成很长的输出、读很长的上下文，Transformer MoE 的 KV 缓存随长度增长，吞吐受限；NVIDIA 要给出权重、训练软件、配方与可再分发数据全部公开的高吞吐模型族（Nano、Super、Ultra）。
- **核心方法**：主干以 Mamba-2 层与 MoE 层交错为主，只保留少数自注意力层（Mamba-2 生成时只存固定大小的状态）；注意力层不用 RoPE，由 Mamba 提供隐式位置信息，在 512K 上继续预训练、256K 上 SFT，支持 1M 上下文。Nano（30B 总参数、约 3B 激活）在 8K 输入、16K 输出的推理负载下吞吐是 Qwen3-30B-A3B 的 3.3 倍；1M 长度的 RULER 为 54.19，上一代 Nemotron 2 Nano 为 23.43。Super 与 Ultra 另加 LatentMoE（把 token 投到更小的潜空间里做路由与专家计算，路由参数与 all-to-all 通信约省 4 倍，省下的预算用于更多专家）与 MTP，并用 NVFP4 预训练：权重、激活、梯度都量化到 4 位，最后约 15% 的层、潜空间投影、MTP 与注意力投影保留 BF16；在 Nano 上对照，NVFP4 与 BF16 的损失相对差不到 1%。后训练在数学、代码、软件工程、搜索、工具使用、长上下文等多个环境上同时做 RL，作者写明这比以前分阶段训练更稳定、更不容易奖励黑客；推理时可指定思考 token 上限，到达后插入思考结束符转入作答。
- **为什么在这个库里**：[架构方向](../../fields/architecture/README.md)"固定大小的状态以混合形式存活"一线的最新生产实例；[预训练方向](../../fields/pretraining/README.md)数值精度"BF16 → FP8 → FP4"一节中第一份 FP4 预训练的公开配方；[强化学习方向](../../fields/posttraining/rl/README.md)"多领域同时 RL"一侧的证据，与 DeepSeek-V4、Kimi K3 的"专家加蒸馏"相对。这份是总览白皮书，Nano、Super、Ultra 各有单独报告。优先级：选读。

## 批注

**易误读**
- 3.3 倍吞吐是 Nano 在特定输入输出长度下的对比，不是同等质量下的总成本对比；NVFP4 的"不到 1%"是 Nano 上的损失对照，Super、Ultra 的完整对照在各自报告中。

**未核实 / 待验证**
- Mamba 与注意力层的确切比例在白皮书正文未量化；Nano、Super（arXiv 2604.12374）、Ultra（arXiv 2606.15007）的单独报告本轮未打开。

## 身份信息

- 稳定标识：arxiv:2512.20856 · [全文 PDF](https://arxiv.org/pdf/2512.20856) · NVIDIA，2025-12-24
- 方向：llm/architecture、llm/long-context、llm/pretraining、llm/posttraining/rl
