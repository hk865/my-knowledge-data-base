# SAM 3: Segment Anything with Concepts

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2511.16719)

[返回机器人与具身目录](../../README.md) · [原文版本与阅读记录](source.json)

- **解决什么**：[SAM](../arxiv-2304.02643/README.md) 与 SAM 2 按点、框分割"这一个东西"，不能按名词短语找出图像和视频里"所有黄色校车"；开放词汇检测器只给框，跨帧身份也不稳定，机器人系统只好把识别、检测、分割、跟踪几个模型串起来。
- **核心方法**：定义"可提示概念分割"（PCS）：提示是名词短语、示例图片或两者结合，输出每个实例的掩码和跨帧一致的 ID。图像级检测器和基于记忆的视频跟踪器共享一个骨干，用一个"存在头"（presence head）把"图里有没有这个概念"和"它在哪里"分开判断；数据引擎产出含困难负样本的 400 万个独特概念标签，并发布 SA-Co 基准。SA-Co/Gold 上 cgF1 54.1，OWLv2 为 24.6，人类为 72.8；H200 上一张含 100 多个物体的图约 30 ms；接上多模态大模型（SAM 3 Agent）后能处理需要推理的分割查询。作者写明细粒度的领域外概念、长短语、需要推理的情形不在当前能力范围内，视频推理时间随物体数增长，拥挤场景做不到实时。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)第 7 阶段的节点：[FM-Fusion](../arxiv-2402.04555/README.md) 用 RAM + Grounding DINO + SAM 拼出开放词汇分割（每帧约 1 秒），SAM 3 把识别、检测、分割、跨帧跟踪收进一个模型；也是 Meta 一系"通用 2D 模型"（Mask R-CNN → SAM → SAM 3）押注的延续。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2511.16719（Meta Superintelligence Labs，Carion、Gustafson 等 38 位作者；v1 2025-11-20，当前 v2 2026-03-28）
- 全文：[arXiv PDF](https://arxiv.org/pdf/2511.16719)
- 方向：[感知](../../fields/perception/README.md)（视觉表征一侧见[视觉表征方向](../../../multimodal/fields/visual-representation/README.md)）
