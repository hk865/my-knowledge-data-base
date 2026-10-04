# 视频与时序表征 阅读导航

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

视频模型除了表示单帧内容，还要处理跨帧的身份、运动和遮挡。时间信息可以通过输入顺序、时空网络或记忆组织，不应只看生成帧数。

## 一个容易混淆的边界

时间上平滑不代表物理一致，连续帧相关也不代表模型掌握可用于控制的因果动力学。

## 入门任务

检查Video Diffusion在时间维度上怎样共享信息，再列出运动连续性和长程一致性应分别怎样测量。

## 具体讲解入口

[打开已有独立讲解](../../../foundations/lessons/12-rnn.md)。

## 从已有讲解开始

1. [Denoising Diffusion Probabilistic Models](../../papers/ddpm/README.md)
2. [Video Diffusion Models](../../papers/video-diffusion/README.md)
