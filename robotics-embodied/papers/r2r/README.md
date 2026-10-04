# Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments

> 状态：技术精读 · 2017 · [原文](https://arxiv.org/abs/1711.07280)

[返回机器人与具身目录](../../README.md)

- **解决什么**：视觉问答、图像描述都只对一张固定图像作答，模型输出不会改变它下一步看到什么；已有的指令导航研究又多在合成渲染环境里，物体和指令都简单。
- **核心方法**：提出视觉语言导航（VLN）任务：把 Matterport3D 真实建筑扫描做成可交互的视点图模拟器，发布 Room-to-Room（R2R）数据集——人写的自由文本指令、真实全景图像、按建筑划分出训练中从未见过的测试建筑——并给出带注意力的序列到序列 LSTM 基线。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)方向 VLN 基准的源头；后来的统一 VLA（如 [Qwen-VLA](../arxiv-2605.30280/README.md)）仍报告 R2R 指标。优先级：必读。

## 阅读入口

- [技术精读](reading.md)
- [图解与说明](figures/README.md)
- [原文版本与阅读记录](source.json)

## 身份信息

- 稳定标识：arxiv:1711.07280（Anderson 等 9 位作者；CVPR 2018 Spotlight）
- 全文：[arXiv PDF v3](https://arxiv.org/pdf/1711.07280v3)
- 方向：[导航与规划](../../fields/navigation-planning/README.md)
