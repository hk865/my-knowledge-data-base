# Imagen Video: High Definition Video Generation with Diffusion Models

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2210.02303)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：把 Imagen 的文本到图像级联扩散扩到高清视频：此前的 Video Diffusion（多位作者相同，2022）主要在 64×64 上评测，生成的是低分辨率短片段。
- **核心方法**：沿用 [Video Diffusion](../video-diffusion/README.md) 的时空分解 3D U-Net，把它做成 1 个基础模型 + 3 个空间超分 + 3 个时间超分共 7 个扩散模型的级联（合计 116 亿参数），以冻结的 T5-XXL 为文本编码器，图像与视频联合训练；最终生成 1280×768、24 帧/秒、约 5.3 秒的视频。基础模型用时间注意力抓长程依赖，超分模型改用时间卷积、最高分辨率处改为全卷积以省内存；再用渐进蒸馏把每级采样压到 8 步。作者以偏见与滥用风险为由不发布模型。
- **为什么在这个库里**：[观点页：生成收敛](../../../perspectives/generative-convergence.md)"视频生成的四种基本做法"中"时空分解 U-Net + 级联"的代表，也是 Google 视频生成从 Video Diffusion 到 Veo 的中间一站；它自述的限制（单次约 5.3 秒、高分辨率阶段放弃注意力）正是后来潜空间与 Transformer 路线要解决的。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2210.02303 · [全文 PDF](https://arxiv.org/pdf/2210.02303) · Google Research（Brain Team）
- 方向：multimodal/generation、multimodal/video-temporal
