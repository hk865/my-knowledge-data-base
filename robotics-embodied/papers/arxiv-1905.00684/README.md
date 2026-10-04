# DS-VIO: Robust and Efficient Stereo Visual Inertial Odometry based on Dual Stage EKF

> 状态：文献卡 · 2019 · [原文](https://arxiv.org/abs/1905.00684)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：滤波式双目 VIO（视觉惯性里程计，一句话：融合相机与 IMU 估计机器人的位姿轨迹）要在精度和计算量之间取舍：状态向量越大越准，也越慢。
- **核心方法**：把 EKF（扩展卡尔曼滤波）拆成两级：第一级只融合加速度计与陀螺仪，第二级再融合双目相机与 IMU，以此保持较低的状态维度。在 EuRoC 数据集上与 OKVIS、ROVIO、VINS-Mono、S-MSCKF（同为紧耦合滤波式双目 VIO，是最接近的对照）比较，RMS 误差相当或更低，计算效率与以往滤波方法相当。
- **为什么在这个库里**：[状态估计与建图](../../fields/localization-mapping/README.md)方向滤波式 VIO 的一个工程变体，可与 [ESKF 技术参考](../eskf/README.md)对照看「状态里放什么、分几级融合」这一设计选择。优先级：存档。

## 身份信息

- 稳定标识：arxiv:1905.00684
- 作者：Xiaogang Xiong、Wenqing Chen、Zhichao Liu、Qiang Shen
- 全文：[arXiv PDF](https://arxiv.org/pdf/1905.00684)
- 方向：[状态估计与建图](../../fields/localization-mapping/README.md)
