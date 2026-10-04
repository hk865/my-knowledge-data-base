# Histograms of Oriented Gradients for Human Detection

> 状态：文献卡 · 2005 · [原文](https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：为稳健的视觉目标识别找一套好的特征。作者以线性 SVM 行人检测为测试场景：人的姿态、衣着和背景变化很大，特征要在杂乱背景和困难光照下把人形干净地分出来。
- **核心方法**：在检测窗口上划出密集、均匀的小格（cell），统计每格内梯度方向的直方图，再在相互重叠的块（block）内做局部对比度归一化，拼成一个长向量交给线性 SVM。逐项消融的结论是：细尺度梯度（最简单的一维 [−1, 0, 1] 模板、不做平滑效果最好）、细的方向分箱、较粗的空间分箱、重叠块内的高质量归一化，四者都重要。与此前最好的 Haar 小波检测器相比，误检率降低一个数量级以上；在原 MIT 行人库上近乎完美分离，作者因此另建了 1800 多张标注人像、姿态与背景变化更大的 INRIA 行人库。
- **为什么在这个库里**：[视觉表征方向](../../fields/visual-representation/README.md)主线的起点：特征由人设计，只有最后的分类器在学习；[Baseline 页](../../fields/visual-representation/BASELINES.md)"原点"一行。"固定特征加线性分类器"的形式后来原样保留在线性评测协议里，只是特征换成了学到的。它的 [−1, 0, 1] 梯度算子与浅层卷积的结构对应见 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 6 节。作者自述的下一步（局部空间不变性更强的部件模型、加入运动信息）中，前者由 DPM 接上。优先级：选读。

## 身份信息

- 稳定标识：doi:10.1109/CVPR.2005.177 · [作者主页 PDF](https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf) · INRIA Rhône-Alps · CVPR 2005，第 1 卷，886–893 页
- 方向：multimodal/visual-representation、robotics/perception
