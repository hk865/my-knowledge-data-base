# VideoPhy: Evaluating Physical Commonsense for Video Generation

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2406.03520)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：文本到视频模型被寄望成为"物理世界的通用模拟器"，但 FVD 这类指标需要参考视频、偏向画质、检测不出不现实的运动，衡量不了生成的视频是否符合物理常识。
- **核心方法**：用 GPT-4 生成并经人工筛选出 688 条描述，按材料交互分成固体—固体、固体—流体、流体—流体三类，交给 12 个开源与闭源模型生成视频，由人判断"是否遵循描述"和"是否符合物理常识"。两项同时满足的比例最好的 CogVideoX-5B 也只有 39.6%；固体—固体交互（球落地弹起、锤子敲钉）最差；常见失败是认不清物体的材料（刚体随时间变形）、违反质量守恒与牛顿定律。另训练了自动评估器 VideoCon-Physics，代替昂贵的人工评测。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)"从测量看"一表中"文本条件下的物理常识"这一协议的代表；与用真实视频续写的 [Physics-IQ](../arxiv-2501.09038/README.md)、用合成规律做分布外测试的 [PhyWorld](../arxiv-2411.02385/README.md) 互补。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2406.03520 · [全文 PDF](https://arxiv.org/pdf/2406.03520v2) · UCLA、Google Research
- 方向：multimodal/world-models、multimodal/generation、cross-domain/evaluation
