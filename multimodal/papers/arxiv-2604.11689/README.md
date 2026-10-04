# LARY: A Latent Action Representation Yielding Benchmark for Generalizable Vision-to-Action Alignment

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2604.11689)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：机器人动作数据稀缺，人类动作视频量大却没有动作标注；把视觉信号转成与本体无关的"潜在动作"是利用这些视频的关键，但潜在动作表示能否支撑控制，缺少严格的评测。
- **核心方法**：提出 LARY 基准，从两个层面评测：高层语义动作（做什么：151 个动作类别的分类，用注意力探针）与低层机器人控制（怎么做：回归动作轨迹）；数据含 100 多万段视频（1000 小时）、62 万图像对和 59.5 万条运动轨迹，覆盖多种本体与环境。比较 11 个模型：专门的具身潜在动作模型、通用视觉编码器（语义级如 DINOv3、V-JEPA 2，像素级如 FLUX.2、Wan2.2），以及作者把 LAPA 训练方式嫁接到冻结通用编码器上得到的"通用 LAM"。结论：没有动作监督的通用视觉基础模型稳定优于专门的具身 LAM；潜空间（语义）表示比像素空间更贴近物理动作空间。
- **为什么在这个库里**：[机器人侧世界模型入门页](../../../robotics-embodied/fields/world-models/README.md)"从内部看"一节与[基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"⑥ 评估与分析"一行；与 [Reconstruction or Semantics?](../arxiv-2605.06388/README.md) 从两个角度得出同一结论：语义特征比重建特征更适合接到动作上。做不好的场景：评测用离线探针和回归，不是闭环控制成功率；作者指出专门的 LAM 会因数据少或过早约束到低层控制而出现表示坍缩，并单列了长尾类别的误差分析（Sec.5.1、Sec.6）。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2604.11689 · [全文 PDF](https://arxiv.org/pdf/2604.11689) · 美团（LongCat 团队）
- 方向：multimodal/world-models
