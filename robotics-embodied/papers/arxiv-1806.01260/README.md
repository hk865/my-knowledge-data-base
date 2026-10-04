# Digging Into Self-Supervised Monocular Depth Estimation

> 状态：文献卡 · 2018 · [原文](https://arxiv.org/abs/1806.01260)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自监督单目深度在相机静止、物体与相机同速运动时违反静态场景假设，产生无穷远深度的空洞；遮挡下平均重投影误差误罚正确深度。
- **核心方法**：三处改进：逐像素取最小重投影误差处理遮挡；自动掩蔽丢掉相机静止、同速运动物体和低纹理区域的像素；先上采样到输入分辨率再算多尺度光度误差。KITTI Eigen 上 AbsRel 0.115（单目训练）、0.106（单目加双目）。原文写明遇到违反朗伯假设的物体会失效，反光、色彩饱和区域学不出好深度，单目训练不保证公制尺度，逐图中值缩放会掩盖尺度不稳定。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 3 无标签深度的节点；[感知讲义](../../fields/perception.md)第六节的光度损失算例即以它为出处。优先级：选读。

## 身份信息

- 稳定标识：arxiv:1806.01260 · [全文 PDF](https://arxiv.org/pdf/1806.01260v4) · Clément Godard、Oisin Mac Aodha、Michael Firman、Gabriel J. Brostow（UCL、Caltech、Niantic）
- 发表：ICCV 2019
- 方向：robotics/perception
