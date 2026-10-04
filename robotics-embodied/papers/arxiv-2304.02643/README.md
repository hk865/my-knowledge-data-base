# Segment Anything

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2304.02643)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：建立一个按提示（点、框、文字）输出任意物体掩码的通用分割模型。
- **核心方法**：重图像编码器每张图只跑一次，之后提示编码器与掩码解码器在浏览器中约 50 ms 出一个掩码；在 1100 万张图、11 亿个掩码的 SA-1B 上训练。原文写明会漏掉细结构、偶尔幻觉出小的不连通块、边界不如 zoom-in 方法锐利，用重编码器时整体不是实时，不清楚怎样用提示实现语义与全景分割。
- **为什么在这个库里**：[感知方向](../../fields/perception/README.md)阶段 6 的掩码来源；FM-Fusion 中 SAM 占每帧 464.4 ms，且跨视角掩码不一致。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2304.02643 · [全文 PDF](https://arxiv.org/pdf/2304.02643) · Alexander Kirillov、Eric Mintun、Nikhila Ravi、Hanzi Mao、Chloe Rolland等（Meta AI Research, FAIR）
- 发表：未核实（本轮未查正式发表处）
- 方向：robotics/perception
