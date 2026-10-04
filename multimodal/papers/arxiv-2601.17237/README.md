# C-RADIOv4 (Tech Report)

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2601.17237)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多教师蒸馏得到的"聚合式"主干（把几个训练目标不同的编码器的特征蒸馏进一个学生）要随教师更新；上一代的教师 DFN CLIP、DINOv2、SAM 已被 SigLIP 2、DINOv3、SAM 3 超过。
- **核心方法**：沿用 [AM-RADIO](../arxiv-2312.06709/README.md) 与 RADIOv2.5 的框架，教师换成 SigLIP2-g-384、DINOv3-7B、SAM3。训练分辨率从两档改为在低、高两组中随机采样。为了不让学生模仿教师的固定模式噪声（SigLIP 2 特征图边缘的"空洞"、SAM 窗口边界的伪影、DINOv3-H+ 时常出现的大幅值噪声块），对学生和每个教师施加互相独立的随机平移，只在对齐后的位置上算损失。摘要向量的损失按各教师嵌入的角度离散度归一化，否则 DINOv3 会主导损失、压过 SigLIP 2。发布 412M（SO400M）与 631M（H）两个尺寸，带 ViTDet 窗口模式以加速高分辨率推理，许可允许商用。H 版线性探针 ADE20K 55.20，DINOv3-7B 为 55.9，参数约为后者的十分之一；ImageNet k 近邻 86.59（Table 1）。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 多教师蒸馏"一行的 2026 年版本；[入门页](../../fields/visual-representation/README.md)主线第 8 个节点"组合从拼接移到蒸馏"的证据，它的三个教师正好是本方向三条路线（图文对比、自蒸馏、分割监督）的当前代表。自述：SAM3 当教师在所选 benchmark 上没有带来提升，保留它是为了能替换 SAM3 的视觉编码器；"更好的教师带来更好的学生"仍然成立。代码与模型已发布。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2601.17237 · [全文 PDF](https://arxiv.org/pdf/2601.17237) · NVIDIA · 技术报告
- 方向：multimodal/visual-representation、cross-domain/knowledge-distillation
