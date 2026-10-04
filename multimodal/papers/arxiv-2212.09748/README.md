# Scalable Diffusion Models with Transformers

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2212.09748)

[返回多模态目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：从 DDPM 到 LDM，扩散模型都用卷积 U-Net 作主干。U-Net 的归纳偏置是否必要？Transformer 主干能否像在语言与识别里那样，计算量越大效果越好？
- **核心方法**：在 LDM 的潜空间里（256×256×3 的图经现成 VAE 变成 32×32×4），把潜变量切成 p×p 的块作 token，交给标准 ViT 式的 Transformer 去噪；时间步与类别经 adaLN-Zero 注入（自适应层归一化，并把每个残差分支初始化为恒等）。p 减半，token 数变 4 倍，计算量至少变 4 倍。12 个模型中前向 Gflops 与 FID 的相关系数为 −0.93；DiT-XL/2（118.6 Gflops，LDM-4 为 103.6，像素空间 ADM 为 1120）在 ImageNet 256×256 类条件生成上用无分类器引导得到 FID 2.27，此前最好的 LDM 为 3.60。论文只做类条件生成，没有做文本条件；作者把"作为 DALL·E 2、Stable Diffusion 这类系统的主干"列为后续工作。代码公开。
- **为什么在这个库里**：[视觉生成方向](../../fields/generation/README.md)主线第 8 个节点，[Baseline 页](../../fields/generation/BASELINES.md)现代配方中"主干"部件的出处。第一作者 Peebles 后来署名 [Sora 技术报告](../sora-tech-report/README.md)，该报告引用它作主干来源；[VAR](../arxiv-2404.02905/README.md) 把它当作对手比较。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2212.09748 · [全文 PDF](https://arxiv.org/pdf/2212.09748) · UC Berkeley、New York University（第一作者在 Meta AI FAIR 实习期间完成）
- 方向：multimodal/generation
