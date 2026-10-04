# Do generative video models understand physical principles?

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2501.09038)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视频模型越来越逼真，它们学到的是物理规律，还是只是会画像素的"模式复读机"？此前没有一个用真实视频、能定量回答这个问题的测试。
- **核心方法**（Physics-IQ）：在受控环境里实拍 66 个物理场景、396 段 8 秒视频（固体力学、流体、光学、热学、磁学，例如多米诺骨牌中间放一只橡皮鸭），每个场景录两次以量出物理本身的随机性。让模型看开头、续写后 5 秒，用"动作发生在哪里、何时发生、发生多少"和 MSE 四项指标与真实续写比较，两次真实录制之间的差异记为 100%。被测的 Sora、Runway Gen 3、Pika、Lumiere、Stable Video Diffusion、VideoPoet 中最好的只有 29.5%。同时用多模态大模型二选一辨真伪来测"看起来真不真"：Sora 最难分辨，但视觉真实感与物理理解不显著相关（r = −0.46，p = .249）。
- **为什么在这个库里**：[世界模型方向](../../fields/world-models/README.md)"从测量看"一节排名翻转的主证据：最逼真的模型不是物理最对的模型。末位作者 Geirhos 也是[视觉表征方向](../../fields/visual-representation/README.md)里"ImageNet CNN 靠纹理捷径分类"一文的作者，两项工作用同一种思路：构造专门的诊断测试，看模型依赖的是哪种线索。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2501.09038 · [全文 PDF](https://arxiv.org/pdf/2501.09038v3) · Google DeepMind（第一作者署名 INSAIT，工作在 Google DeepMind 期间完成）
- 方向：multimodal/world-models、multimodal/generation、cross-domain/evaluation
