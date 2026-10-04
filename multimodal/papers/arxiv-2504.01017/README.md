# Scaling Language-Free Visual Representation Learning

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2504.01017)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：视觉自监督模型做视觉语言模型的视觉输入时（尤其 OCR 与图表问答）不如 CLIP，这通常被归因于语言监督带来的语义；但两者的训练数据也不同：CLIP 用数十亿网页图文对，自监督多用 ImageNet 或分布与它相近的上亿张图。差距究竟来自语言还是数据？
- **核心方法**：在同一份 MetaCLIP 数据（20 亿样本，MC-2B）上训练两类模型：自监督只用其中的图像（主要是 DINOv2 式的 Web-DINO，也训练了 MAE），CLIP 用图文对；模型从 1B 扩到 7B 参数。评测以 Cambrian-1 的 16 项视觉问答为主（冻结编码器，固定 Llama-3 8B 做视觉指令微调），同时保留 ImageNet 线性、ADE20K 分割、深度等经典协议。结果：Web-DINO 的平均、OCR 与图表、视觉中心类问答随模型增大近似对数线性上升，到 7B 仍未饱和；CLIP 约 3B 后基本饱和。同等条件下 CLIP 在 OCR 与图表见长，Web-DINO 在视觉中心类见长。只保留含图表、表格、文档的 1.3% 图像训练 2B 模型，OCR 与图表反超用全量图文对训练的 CLIP 4.3 个百分点，平均问答高 0.7。
- **为什么在这个库里**：[Baseline 页](../../fields/visual-representation/BASELINES.md)"数据 = 与 CLIP 同数据的对照"与"读出接口 = 以问答为评测协议"两行；它把"自监督特征不适合做 VLM 输入"拆成数据与规模问题，是入门页趋势 2"与语言对齐"的边界证据（[DINO 精读](../dino/reading.md)"局限与后续"第 6 条、[MAE 精读](../mae/reading.md)第 3 条）。自述局限：没有语言就不能直接零样本分类；只用一个固定的语言模型；更大或未筛选的数据留待以后。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2504.01017 · [全文 PDF](https://arxiv.org/pdf/2504.01017) · FAIR Meta、New York University、Princeton University
- 方向：multimodal/visual-representation
