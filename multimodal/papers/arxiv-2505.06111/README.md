# UniVLA: Learning to Act Anywhere with Task-centric Latent Actions

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2505.06111)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：通用机器人策略大多靠扩大带动作标注的数据来提升，因此被绑在单一本体上，难以从不同本体、视角和人类视频里学到可迁移的知识。
- **核心方法**：先学"以任务为中心的潜在动作"（latent action：从相邻两帧的变化里无监督推断出的离散动作代码）：在 DINOv2 特征空间里用逆动力学编码、前向动力学解码，经 VQ-VAE 离散化，并以语言指令为条件把与任务无关的变化分到另一组代码；再以 Prismatic-7B VLM（与 [OpenVLA](../../../robotics-embodied/papers/openvla/README.md) 相同的底座）预测潜在动作 token，部署时用轻量解码器把潜在动作映射成具体机器人的动作。LIBERO 平均 95.2%（OpenVLA 76.5%，Fig.1）；预训练算力不到 OpenVLA 的 1/20，下游数据为其 1/10。
- **为什么在这个库里**：[机器人侧世界模型基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)"③ 动作接口"一行：用潜在动作把没有动作标注的视频接进策略学习。[What Do LAMs Learn?](../arxiv-2506.15691/README.md) 从理论上说明了它用 DINO 特征和语言条件去除干扰的必要性，[LARY](../arxiv-2604.11689/README.md) 系统比较了这类潜在动作表示。做不好的场景：潜在动作的粒度和码本大小固定；主要在单臂操作上评测，双臂人形和灵巧手需要更细的动作空间；依赖语言标注（Limitations 段）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2505.06111 · [全文 PDF](https://arxiv.org/pdf/2505.06111) · 香港大学、OpenDriveLab、智元机器人（AgiBot） · RSS 2025
- 方向：multimodal/world-models、robotics/embodied-policies
