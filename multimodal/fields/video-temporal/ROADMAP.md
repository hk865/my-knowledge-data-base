# 视频与时序表征：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

视频模型除了表示单帧内容，还要处理跨帧的身份、运动和遮挡。时间信息可以通过输入顺序、时空网络或记忆组织，不应只看生成帧数。

## 第二步：沿具体文章拆机制

[Denoising Diffusion Probabilistic Models](../../papers/ddpm/README.md) → [Video Diffusion Models](../../papers/video-diffusion/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

检查Video Diffusion在时间维度上怎样共享信息，再列出运动连续性和长程一致性应分别怎样测量。

## 第四步：保留边界

时间上平滑不代表物理一致，连续帧相关也不代表模型掌握可用于控制的因果动力学。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
