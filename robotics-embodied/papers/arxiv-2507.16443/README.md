# VGGT-Long: Chunk it, Loop it, Align it -- Pushing VGGT's Limits on Kilometer-scale Long RGB Sequences

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2507.16443)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：VGGT 在 24 GiB 的 RTX 4090 上只能处理 60–80 张图，KITTI 一条序列约 4600 帧；MASt3R-SLAM 在 KITTI 上约 100 帧后跟踪停滞。
- **核心方法**：把序列切成重叠块分别跑 VGGT，相邻块用置信度加权的 Sim(3) 对齐，用 DINOv2 检索回环，最后对块级 Sim(3) 做全局优化，不需要标定或重训。KITTI 全序列平均 26.358 m，与 DPV-SLAM++ 的 25.749 m 相当；去掉 Seq 01 后 19.298 m，带回环的 ORB-SLAM2 为 9.464 m；VGGT、CUT3R、Fast3R 在 KITTI 上显存溢出。原文 Fig.8 写明同一车道反向行驶时 RGB 回环检测失败；每块 2.6–2.8 秒。
- **为什么在这个库里**：[定位与建图](../../fields/localization-mapping/README.md)阶段 5 中"长序列"问题的修补；MASt3R-Fusion 报告它在 KITTI-360 上的误差为轨迹长度的 2.91%。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2507.16443 · [全文 PDF](https://arxiv.org/pdf/2507.16443v2) · Kai Deng、Zexin Ti、Jiawei Xu、Jian Yang、Jin Xie（南开大学、南京大学）
- 发表：ICRA 2026（arXiv comments）
- 方向：robotics/localization-mapping
