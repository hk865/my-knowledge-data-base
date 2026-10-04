# Vision Transformers Need Registers

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.16588)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：DINOv2 的冻结特征分割、深度都很强，却和依赖注意力图的无监督物体发现方法（LOST）不兼容，表现只与有监督主干相当；原始的 DINO 没有这个问题。
- **核心方法**：先找原因：有监督（DeiT-III）、图文（OpenCLIP）、自监督（DINOv2）训练的大 ViT，都会在信息量低的背景处出现一小部分 token（约占 2%），输出范数约为其他 token 的 10 倍；它们丢掉了原图块的局部信息，被模型挪去存放全局信息，只出现在 ViT-L 及更大的模型、训练进行到约三分之一之后。修法是在输入序列里加几个不对应任何图块、输出时丢弃的"寄存器" token（默认 4 个，计算量增加不到 2%）。伪影完全消失，注意力图与特征图变平滑，密集预测变好；LOST 在 DINOv2 上的 VOC2007 corloc 从 35.3 升到 55.4。加 1 个寄存器就拿到密集任务的大部分收益，ImageNet 分类则随寄存器增多继续变好。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"架构 = 加寄存器 token"一行。它说明 DINO 标题里的"涌现性质"与模型规模、训练长度绑在一起（[DINO 精读](../dino/reading.md)"局限与后续"第 3 条），也说明这类伪影在有监督、图文、自监督三种训练信号下都会出现；[DINOv3](../arxiv-2508.10104/README.md) 训练时沿用 4 个寄存器。附录观察到 [MAE](../mae/README.md) 没有这种伪影，作者推测与它只有逐块的局部损失有关。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2309.16588 · [全文 PDF](https://arxiv.org/pdf/2309.16588) · FAIR Meta、Univ. Grenoble Alpes / Inria · ICLR 2024
- 方向：multimodal/visual-representation
