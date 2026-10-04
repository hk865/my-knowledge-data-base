# DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2411.04983)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：世界模型多为特定任务、在线学策略而建。作者主张世界模型应当：能用离线收集的轨迹训练；能在测试时直接优化行为；不绑定具体任务。
- **核心方法**：编码器用冻结的 DINOv2 图像块特征，不重建像素；只训练一个因果 ViT 预测器，按动作预测下一帧的整帧块特征（不像 IRIS 那样逐 token 自回归）；测试时把目标图像也编码成特征，用 CEM（交叉熵法：反复采样动作序列、保留最好的一批再重新拟合分布）做模型预测控制，让预测终点接近目标特征。与同样离线、无奖励训练的 IRIS、DreamerV3、TD-MPC2 相比，Push-T 成功率 0.90（DreamerV3 为 0.30），Wall、PointMaze 与 DreamerV3 相当（Table 1）。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)的两条基线之一，定义了"部署时用模型规划"的接口；[DINO-world](../arxiv-2507.19468/README.md)、[LaDi-WM](../arxiv-2505.11528/README.md) 和 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) 都沿"在冻结特征上预测"这条线。做不好的场景：需要状态—动作覆盖充分的离线数据；训练仍需真实动作标注，用不上无动作的网络视频；只在动作空间里规划，没有分层（Limitations 段）。易误读：对比中的 DreamerV3、TD-MPC2 被改成离线、无奖励训练，不是它们的原生设置；TD-MPC2 因此在四个成功率任务上都是 0。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2411.04983 · [全文 PDF](https://arxiv.org/pdf/2411.04983) · 纽约大学 Courant 研究所、Meta AI
- 方向：multimodal/world-models
