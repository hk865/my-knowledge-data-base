# Improved Baselines with Visual Instruction Tuning

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2310.03744)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：训练通用视觉助手的最佳配方不清楚：原版 LLaVA 擅长对话、在短答案学术 benchmark 上弱，InstructBLIP 相反；两者结构和数据都不同，差异根源无法判断。
- **核心方法**：在 LLaVA 框架内做受控对照：线性投影换成两层 MLP，视觉塔换成 336 像素的 CLIP ViT-L，加入学术 VQA、OCR、区域级数据，并在短答案题后加格式提示（Answer the question using a single word or phrase）。只加 VQAv2 与格式提示，MME 从 809.6 升到 1323.8。最终只用约 120 万条公开数据（558K 对齐 + 665K 指令），8 张 A100 约 1 天训完，在 12 个 benchmark 中的 11 个领先；LLaVA-1.5-HD 把图切成 224 的格子分别编码以提高分辨率。
- **为什么在这个库里**：[Baseline 页](../../fields/vlm/BASELINES.md)的主基线：此后开源 VLM 的"ViT + MLP + LLM"默认接口。两个发现值得记住：原版 LLaVA 对是非题倾向答"是"，源于训练数据缺这类题；输入提到 448 后详细描述的幻觉显著减少，作者认为分辨率不够看清标注细节时模型学会编。前作见 [LLaVA 精读](../llava/reading.md)。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2310.03744（Haotian Liu 等 4 位作者；当前 v2，2024-05）· [全文 PDF](https://arxiv.org/pdf/2310.03744v2) · University of Wisconsin–Madison、Microsoft Research · CVPR 2024
- 方向：[视觉语言模型](../../fields/vlm/README.md)
