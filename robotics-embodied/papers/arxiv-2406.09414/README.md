# Depth Anything V2

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.09414)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：真实深度标注本身有噪声：深度传感器测不准透明物体，立体匹配怕无纹理和重复纹理，SfM 怕动态物体；基于扩散的深度方法细节好但慢。
- **核心方法**：把全部真实标注换成 59.5 万张合成图，用 ViT-G 教师为 6200 万张真实无标注图打伪标签，再训练 2500 万到 13 亿参数的学生。NTIRE 2024 透明表面挑战零样本 δ1：MiDaS 0.259、V1 0.535、V2 0.836；V100 上 Small 60 ms、Large 213 ms，扩散方法为 2.1–5.2 s。原文写明常规基准上与 V1 相当、两个数据集略差，在 NYUv2/KITTI 上训练的度量模型对透明物体不鲁棒，合成训练集不够多样。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 6 的深度节点，"站在现在看过去"表中"传感器真值在透明物体上是错的"一行的依据。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2406.09414 · [全文 PDF](https://arxiv.org/pdf/2406.09414v2) · Lihe Yang、Bingyi Kang、Zilong Huang、Zhen Zhao、Xiaogang Xu等（HKU、TikTok）
- 发表：NeurIPS 2024
- 方向：robotics/perception
