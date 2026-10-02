# 视觉语言模型 阅读导航

本页是阅读导航，汇集已有讲解、论文与阅读路线；它本身不是本方向的独立教学讲义。

[返回领域总目录](../../README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 先理解什么

视觉语言模型让图像信息影响语言输出。阅读时先识别视觉编码器、连接器和语言模型，再看哪些参数训练、使用什么样的图文或指令数据。

## 一个容易混淆的边界

能描述图像不等于能可靠测距、定位或操纵机器人。VLM到VLA还需要明确动作表示与执行接口。

## 入门任务

给一张图和一个问题画出数据流，标出LLaVA两阶段中冻结和训练的部分。

## 具体讲解入口

[打开已有独立讲解](../../../docs/foundations/05c-transfer-meta-learning.md)。保留原讲义位置和完整正文，不把此导航页计为新的精读。

## 从已有讲解开始

1. [Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md)
2. [Visual Instruction Tuning](../../papers/llava/README.md)
3. [OpenVLA: An Open-Source Vision-Language-Action Model](../../../robotics-embodied/papers/openvla/README.md)
