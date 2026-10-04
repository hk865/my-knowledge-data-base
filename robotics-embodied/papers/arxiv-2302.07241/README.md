# ConceptFusion: Open-set Multimodal 3D Mapping

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2302.07241)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：已有 3D 语义建图局限于闭集，只能推理训练时预先定义的有限概念。
- **核心方法**：用类别无关的区域分割取局部区域，把 CLIP 的全局与局部特征融合成逐像素特征，经 gradslam 融合进 3D 点图，可用文字、图像或声音查询，不需要额外训练。UnCoCo 上 3D mIoU 0.446，OpenSeg-3D 0.289；摘要称长尾概念上 3D IoU 超过有监督方法 40% 以上。原文写明三条局限：百万级点乘高维嵌入、内存大；特征偏向前景、缺组合性、不懂否定；继承基础模型的偏差。逐像素特征离线提取，每张图 10–15 秒（RTX 3090）。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 6 开放词汇建图的节点。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2302.07241 · [全文 PDF](https://arxiv.org/pdf/2302.07241v3) · Krishna Murthy Jatavallabhula、Alihusein Kuwajerwala、Qiao Gu、Mohd Omama、Tao Chen等（MIT、Université de Montréal、University of Toronto、IIIT Hyderabad 等）
- 发表：RSS 2023
- 方向：robotics/perception、robotics/localization-mapping
