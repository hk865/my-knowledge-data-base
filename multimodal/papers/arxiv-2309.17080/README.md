# GAIA-1: A Generative World Model for Autonomous Driving

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2309.17080) · 技术报告

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：自动驾驶要预测"自车做某个动作之后世界会怎样"。作者认为此前的世界模型依赖标注数据、多在仿真里验证，而且表示维度低，生成不出足够逼真的未来，用不到真实驾驶上。
- **核心方法**：把视频、文本、动作都变成离散 token，像语言模型一样用 6.5B 参数的自回归 Transformer 预测下一个图像 token，再用 2.6B 的视频扩散解码器把 token 还原成高分辨率视频。图像分词器在压缩时回归 DINO 特征，让 token 更偏语义而不是高频细节。训练数据是 Wayve 在伦敦采集的 4700 小时自有驾驶数据。用小模型拟合的幂律准确预测了最终模型的验证交叉熵。可以用动作让自车驶出车道、用文字改天气或加一辆公交车，生成数据里没有的场景。作者写明的局限：自回归生成不是实时；采样时用 argmax 会陷入重复循环，直接从分布里采又会取到尾部 token、把模型带出分布。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)主线第 3 个节点中驾驶一支的代表：公司用自有车队数据、把 LLM 的"下一个 token + 规模定律"搬到驾驶视频上；与学术界在 nuScenes 上做的 [OccWorld](../arxiv-2311.16038/README.md) 对照（像素 token 对 3D 占据 token）。评测以定性示例为主，这一点本身是"评测偏向画面"的例子。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2309.17080 · [全文 PDF](https://arxiv.org/pdf/2309.17080v1) · Wayve
- 方向：multimodal/world-models、multimodal/generation
