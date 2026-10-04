# 2026年10月4日研究短报：怎样从经典基线读到新问题

## 机器人：预测得像，和真正能用来控制，是两道关

机器人需要在动作执行期间继续观察环境，也需要知道预测偏差何时会破坏后面的计划。Fast-FoundationStereo 把高质量立体视觉的计算成本带进讨论；LAS2 把定位与场景表示连接起来；近期世界模型研究则追问，规划器能否找到模型没有在训练中见过、却看起来分数很高的动作序列。[判断] 这些工作的共同价值是把表征质量与闭环使用之间的差距具体化，而不是用新模型名字替换经典基线。

从自己的问题进入即可：[感知路线图](../robotics-embodied/fields/perception/ROADMAP.md)比较准确率与实时预算，[定位与建图路线图](../robotics-embodied/fields/localization-mapping/ROADMAP.md)比较几何一致性与地图维护，[世界模型路线图](../robotics-embodied/fields/world-models/ROADMAP.md)比较预测、规划与策略训练的接口。VLA 的离散或连续动作表示，与动作块如何实时衔接，是相互影响的两个选择，见 [VLA 路线图](../robotics-embodied/fields/vla/ROADMAP.md)。

## 语言模型：更值得追问的往往是数据利用和学习失效条件

同样的训练预算，数据怎么选择、怎样重复使用，会改变训练结果；同样向教师学习，学生是否到达合适的状态、能否在解出答案后停止，也可能决定收益。DataDecide、FineWeb2 与数据受限预训练分别切入小规模选数、多语言清洗与重复利用；OPD II 和 Solving Without Stopping 则提供两种不同的蒸馏诊断。[判断] 这些对照实验值得与大模型技术报告一起读，因为它们更接近可单独检验的训练问题。

具体顺序由[预训练方向](../llm/fields/pretraining/README.md)和 [SFT 路线图](../llm/fields/posttraining/sft/ROADMAP.md)维护。理解优化器与训练阶段的关系，接着看[训练科学](../cross-domain/fields/training-science/README.md)；理解草稿模型怎样降低生成成本，接着看[推理方向](../llm/fields/inference/README.md)。

## 多模态：改变表示空间，与改变生成过程，要分开比较

MeanFlow 改的是生成过程中的速度目标；RAE 改的是生成器工作的表示空间。这两类工作回答不同问题：前者追求用更少的生成步骤完成采样，后者研究视觉表征保留的信息怎样帮助生成。[判断] 先看清被替换的模块，才能判断不同方法是否互补，而不是把所有进展都概括成“更好的扩散”。视频与世界模型还要额外检查时序证据、动作条件和闭环评估。

沿[生成路线图](../multimodal/fields/generation/ROADMAP.md)比较目标与表示，再按问题进入[视频与时序](../multimodal/fields/video-temporal/README.md)、[图文对齐](../multimodal/fields/alignment/README.md)或[世界模型路线图](../multimodal/fields/world-models/ROADMAP.md)。经典讲义承担公式和算例，新论文承担对这些机制的替换、扩展与边界检验。

<details><summary>整理记录</summary>
本日补入的20篇文献卡分别保留官方来源、实际阅读章节与核验边界；文献卡不等于全文精读或复现。
各方向的固定阅读顺序只在方向页和路线图维护，此短报不再另建一份容易失效的全库覆盖表。
同日的[权限与协作短报](2026-10-04.md)和[机制讲义更新记录](2026-10-04-phase3-expansion.md)保留为日期记录。
</details>
