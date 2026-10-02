# 视觉语言模型：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

## 第一步：限定问题

视觉语言模型让图像信息影响语言输出。阅读时先识别视觉编码器、连接器和语言模型，再看哪些参数训练、使用什么样的图文或指令数据。

## 第二步：沿具体文章拆机制

[Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md) → [Visual Instruction Tuning](../../papers/llava/README.md) → [OpenVLA: An Open-Source Vision-Language-Action Model](../../../robotics-embodied/papers/openvla/README.md)

这个次序是教学建议，表示先理解的概念与后续比较对象，不表示作者之间存在直接技术继承。

## 第三步：做能检验理解的工作

给一张图和一个问题画出数据流，标出LLaVA两阶段中冻结和训练的部分。

## 第四步：保留边界

能描述图像不等于能可靠测距、定位或操纵机器人。VLM到VLA还需要明确动作表示与执行接口。

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。
