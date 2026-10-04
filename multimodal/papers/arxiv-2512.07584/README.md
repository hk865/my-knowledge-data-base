# LongCat-Image Technical Report

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2512.07584)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多语言写字（尤其是中文生僻字）、写实度、部署成本与开放程度；摘要指出同类模型常用接近 200 亿参数或更大的 MoE。
- **核心方法**：60 亿参数的混合 MM-DiT，用 Qwen2.5-VL-7B 作文生图与编辑共用的条件编码器，VAE 沿用 FLUX.1-dev；提示里引号内要写出来的文字改为逐字编码，减轻模型的记忆负担。预训练与中期训练剔除全部 AI 生成图像（作者发现少量混入就会让成图带"塑料感"），RL 阶段反过来把一个 AIGC 检测器当作奖励模型之一，另有畸变检测、人类偏好与 OCR 奖励，策略优化用 DPO、GRPO 与自研的 MPO。按 Qwen-Image 的 ChineseWord 协议，三级生僻字准确率 70.3%（同表 Seedream 4.0 为 2.3%、Qwen-Image 6.1%、HunyuanImage 3.0 4.1%）。开放最终模型、中期检查点与训练代码。
- **为什么在这个库里**：说明"写不对字"这个长尾可以靠编码方式与数据攻下来，不只靠规模；把 AIGC 检测器当奖励，是判别器以奖励的形式回到训练中的一例（见[入门页](../../fields/generation/README.md)批注）。[Baseline 页](../../fields/generation/BASELINES.md)部件 6、7。优先级：存档。

## 身份信息

- 稳定标识：arxiv:2512.07584 · [全文 PDF](https://arxiv.org/pdf/2512.07584v1) · 美团 LongCat 团队 · 公开权重与训练代码
- 方向：multimodal/generation
