# Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.16163)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：预训练视频模型学到了物理世界怎样变化，但要把它变成机器人策略，以往要另接动作头、改结构或分多阶段训练。
- **核心方法**：NVIDIA 与 Stanford 把 2B 参数的潜在视频扩散模型 Cosmos-Predict2 直接在目标机器人的示范上做一阶段后训练，不改结构：动作块、本体状态、未来的状态与图像、价值（期望累计回报）都编码成"潜在帧"，和相机帧排在同一段扩散序列里（不够大的低维向量经归一化后复制填满）。同一个模型因此既输出动作，又预测未来和价值，测试时可以对多个候选动作块做 best-of-N 规划。LIBERO 98.5%、RoboCasa 67.1%；真机 ALOHA 四个双臂任务平均 93.6 分，作者报告整体高于 π0.5（例如装糖果进自封袋 85.4 对 61.5，装糖果进碗 89.6 对 95.2 则略低），明显高于 OpenVLA-OFT+ 与 Diffusion Policy；在两个最难的任务上加规划再提高约 12.5 分。作者写明加规划时约 5 秒才出一个动作块，难用于动态任务；有效的规划需要大量 rollout 数据，目前只做一层 best-of-N。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)"世界模型与动作模型合并"的 NVIDIA 版本：[Cosmos](../../../multimodal/papers/arxiv-2501.03575/README.md) 平台论文只列出机器人用途、没有实证，本篇给出了实证；同一个模型兼任策略、世界模型和价值函数，与 [Zero-WAM](../zero-wam/reading.md)、[Hydra-0](../../../multimodal/papers/arxiv-2608.18077/README.md) 对照。第一作者也是 [OpenVLA](../openvla/reading.md) 与 [OpenVLA-OFT](../arxiv-2502.19645/README.md) 的第一作者。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2601.16163（NVIDIA、Stanford，Kim、Gao、Lin 等 11 位作者；v1，2026-01-22）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2601.16163) · [项目页](https://research.nvidia.com/labs/dir/cosmos-policy/)
- 方向：[世界模型（机器人侧）](../../fields/world-models/README.md)（另见[VLA](../../fields/vla/README.md)）
