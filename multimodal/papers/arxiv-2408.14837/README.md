# Diffusion Models Are Real-Time Game Engines

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2408.14837) · ICLR 2025

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：游戏引擎的循环是"按玩家输入更新状态，再把状态渲染成像素"，全部由人写规则。能否让一个神经网络同时学会更新与渲染，并在复杂 3D 游戏里实时、长时间地被人玩下去？作者指出，交互式模拟不只是"很快的视频生成"：动作是边生成边到来的，必须逐帧自回归，而自回归容易漂移发散。
- **核心方法**（GameNGen）：先让 PPO 智能体玩 DOOM，把整个训练过程的轨迹录下来当数据；再把 Stable Diffusion v1.4 改成"以过去 64 帧的潜变量和动作为条件、预测下一帧"（动作嵌入替换文本交叉注意力）。两个关键改动：训练时给上下文帧加随机强度的噪声并告诉模型噪声等级，让它学会修正自己前面生成的错误，缓解自回归漂移；微调自编码器的解码器，修复底部状态栏（HUD）这类小细节。单张 TPU-v5 上 20 帧/秒；人工评测中 1.6 秒片段只有 58% 能认出真游戏。局限是只看得到 3 秒多的历史，靠屏幕上的弹药、血量数字"记住"状态，会学到错误启发式（反复开枪就生成敌人）。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)主线第 5 个节点"可玩的扩散世界模型"的代表，也是"关键符号保持不变"最直接的证据：HUD 数字既是被渲染的对象，又是模型的外部记忆。第四作者 Fruchter 后来与 Parker-Holder 共同署名 [Genie 3 博客](../genie-3-blog/README.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2408.14837 · [全文 PDF](https://arxiv.org/pdf/2408.14837v2) · Google Research、Google DeepMind、Tel Aviv University
- 方向：multimodal/world-models、multimodal/generation
