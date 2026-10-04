# Momentum Contrast for Unsupervised Visual Representation Learning

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1911.05722)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：无监督表示学习在 NLP 中很成功（GPT、BERT），视觉仍以有监督预训练为主；作者认为原因之一是语言有离散词表可以建字典，图像是连续的高维信号。把对比学习看作字典查找，就需要一个又大又一致的字典。
- **核心方法**：用一个队列保存过去若干批的 key，字典大小（K = 65536）因此与批大小（256）解耦；key 编码器的参数取 query 编码器的动量滑动平均（m = 0.999），让队列里的 key 来自缓慢变化的同一个编码器。m 取 0.9 时精度降到 55.2%，m = 0 时训练不收敛。ResNet-50 线性评测 60.6%；迁移到 PASCAL VOC、COCO 等 7 个检测与分割任务时，可以超过 ImageNet 有监督预训练。预训练数据从 ImageNet 换成 10 亿张 Instagram 图像（IG-1B），提升稳定但较小，作者认为大数据可能没有被充分利用。
- **为什么在这个库里**：[视觉表征方向](../../fields/visual-representation/README.md)主线第 4 个节点，[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 对比学习（队列加动量编码器）"一行；"动量编码器给目标"被 DINO 的教师网络沿用，结论中建议的"遮蔽自编码"前置任务后来由同一组作者的 [MAE](../mae/README.md) 实现。[判断] 以检测迁移而不是线性评测为主要论据，是 FAIR 中 He、Girshick 一支的协议偏好（见入门页"主要路线与团队偏好"）。优先级：必读。

## 身份信息

- 稳定标识：arxiv:1911.05722 · [全文 PDF](https://arxiv.org/pdf/1911.05722) · Facebook AI Research（FAIR） · CVPR 2020
- 方向：multimodal/visual-representation
