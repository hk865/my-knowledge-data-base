# Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2209.03003)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：扩散与流模型生成一个样本要反复调用网络解 ODE/SDE，比 GAN、VAE 这类一步模型慢得多；扩散方法的设计空间超参繁多、理解不足；生成建模与域迁移（例如人脸变猫脸）通常分开处理。
- **核心方法**：从两个分布各取一点，用直线 Xₜ = tX₁ + (1−t)X₀ 连起来，让网络回归速度 X₁ − X₀（一个普通的最小二乘问题），得到的 ODE 称为整流流。再用训练好的流生成"噪声–样本"配对重新训练（reflow），路径越来越直，直到一步 Euler 也能用；配对之上还可以蒸馏。CIFAR-10 上 1-整流流用自适应求解器 FID 2.58；2-整流流蒸馏后一步生成 FID 4.85、召回率 0.50，作者称为当时一步扩散与流模型的最好结果。代价写在实验里：reflow 改善约 80 步以下的结果，却因速度估计误差累积使多步结果变差（自适应求解器下 FID 2.58 → 3.36 → 3.96），作者也不建议做太多次 reflow。论文未声明代码发布。
- **为什么在这个库里**：[Baseline 页](../../fields/generation/BASELINES.md)部件 4"直线路径"与部件 5"少步采样"两格的交叉点；[SD3](../arxiv-2403.03206/README.md) 的"整流流"指的就是这条直线路径。见 [DDPM 精读](../ddpm/reading.md)"局限与后续"第 6 条。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2209.03003 · [全文 PDF](https://arxiv.org/pdf/2209.03003) · University of Texas at Austin
- 方向：multimodal/generation
