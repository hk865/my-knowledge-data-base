# Back to the Features: DINO as a Foundation for Video World Models

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2507.19468)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：像素空间的大规模视频生成模型昂贵，已有的潜空间世界模型又规模小、领域窄；能否在冻结的通用视觉特征上训练一个通用的视频世界模型。
- **核心方法**：编码器用冻结的 DINOv2，只训练一个预测未来帧特征的预测器，在约 6000 万段未经筛选的网络视频上训练；预测器不限定分辨率、帧率和上下文长度。动作条件通过后训练时加入的动作模块实现，而不是像 [DINO-WM](../arxiv-2411.04983/README.md) 那样把动作 token 插进图像块序列（作者认为后者要全量微调，可能破坏已学的视频理解）。VSPW 分割预测（0.5 秒后）mIoU 比第二名高 6.3%；在 IntPhys、GRASP、InfLevel 直觉物理基准上表现强；PushT 规划成功率从从头训练的 46.9% 提到微调后的 59.4%（Table 4）。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"① 表示"一行与入门页第 4 阶段，检验"冻结特征 + 大规模视频预训练"能否带来规划收益。`[判断]` 站在现在看，收益存在但有限：规划只在 PushT、Wall、PointMaze 三个简单环境上评测，作者预计在更接近预训练数据的复杂环境里收益更明显，本文没有验证。DINO-WM 原文在同名 PushT 环境报告 0.90，两文的数据与规划设置没有逐项对齐，不能直接比较。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2507.19468 · [全文 PDF](https://arxiv.org/pdf/2507.19468) · Meta FAIR
- 方向：multimodal/world-models、multimodal/video-temporal
