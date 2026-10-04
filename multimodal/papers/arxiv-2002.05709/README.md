# A Simple Framework for Contrastive Learning of Visual Representations

> 状态：文献卡 · 2020 · [原文](https://arxiv.org/abs/2002.05709)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：不用人工标注学视觉表示：生成式方法逐像素建模代价高，启发式的前置任务限制了通用性，此前的对比学习方法又依赖专门的网络结构或记忆库。
- **核心方法**：同一张图做两次随机增强得到正样本对，批内其余 2(N−1) 个增强视图都作负样本，用归一化、带温度的交叉熵（NT-Xent）训练 ResNet。系统消融得出三点：增强的组合决定任务好坏，其中随机裁剪加颜色失真最关键；骨干与损失之间加一个非线性投影头，投影头之前的表示比投影头之后好 10 个百分点以上，下游使用前者；对比学习比有监督学习更依赖大批量（4096–8192）和更长的训练。4 倍宽 ResNet-50 线性评测 76.5%，与有监督的标准 ResNet-50 相当；标准宽度时为 69.3%，同结构有监督 76.3%；只用 1% 标签微调，top-5 85.8%。
- **为什么在这个库里**：[视觉表征方向](../../fields/visual-representation/README.md)主线第 4 个节点"信号轴从人工标签移到图像自身"的两篇之一，[Baseline 页](../../fields/visual-representation/BASELINES.md)"训练信号 = 对比学习（大批量加投影头）"一行。"不变性的种类由人选的增强决定"后来成为 [I-JEPA](../arxiv-2301.08243/README.md) 的出发点，"训练时用投影头、下游丢掉它"被 DINO 等沿用。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2002.05709 · [全文 PDF](https://arxiv.org/pdf/2002.05709) · Google Research, Brain Team · ICML 2020
- 方向：multimodal/visual-representation
