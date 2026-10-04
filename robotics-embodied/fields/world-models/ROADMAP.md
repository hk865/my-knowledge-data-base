# 世界模型（机器人侧）：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

前五步从状态估计与 MPC 出发，第六步比较近期设计。每一步都先读材料，再做一个能检验理解的小练习。

1. **把世界模型当成学到的状态方程。** 读[讲义](../world-models.md)第一至六节。放在第一步，因为 RSSM 的先验与后验就是滤波的预测与校正，"想象中学策略"与"部署时规划"两条路线分别对应基于模型的策略训练与 MPC，先建立这个对应，后面的论文都是在换表示、换用法。练习：写出 RSSM 与卡尔曼滤波逐项对应的表，标出哪一项在 RSSM 里是学出来的。
2. **在想象中学策略，以及它在真机上的代价。** 读 [DreamerV3 精读](../../../multimodal/papers/dreamerv3/reading.md)，再读 [World Models](../../papers/arxiv-1803.10122/README.md) 与 [DayDreamer](../../papers/arxiv-2206.14176/README.md) 两张卡。放在这里，因为这条线直接连接真机上的强化学习，而 World Models 的 τ 实验是"模型被策略钻空子"最清楚的例子。练习：对照四足训练中策略利用奖励漏洞的例子，说明 World Models 里 τ 调低为什么会让梦中得分升高、真实得分下降。
3. **部署时在特征空间里规划。** 读 [DINO-WM](../../../multimodal/papers/arxiv-2411.04983/README.md) 与 [V-JEPA 2](../../papers/arxiv-2506.09985/README.md)（JEPA 指在特征空间预测未来的联合嵌入预测架构）。放在这里，因为它们把 MPC 的结构原样搬到学到的潜空间里，规划耗时（53 秒、16 秒每个动作）直接表明离闭环控制还有多远。练习：给定四足控制频率，估算 V-JEPA 2-AC 式规划需要快多少倍才能闭环使用。
4. **视频世界模型怎样为 VLA 服务。** 读 [Veo 评估器](../../papers/arxiv-2512.10675/README.md) 与 [Ctrl-World](../../papers/arxiv-2510.10125/README.md)，可对照 [UniSim](../../papers/arxiv-2310.06114/README.md)。放在这里，因为这是 2025 年后有直接实验支撑的一条新用途，需要先有 [VLA 方向](../vla/README.md)的背景。练习：Pearson 0.92 能保证什么、不能保证什么？设计一个排名正确但单个策略成功率估计很差的例子。
5. **世界模型与动作模型合并。** 读 [Zero-WAM 精读](../../papers/zero-wam/reading.md)，再看 [EVA](../../../multimodal/papers/arxiv-2603.17808/README.md) 与 [Hydra-0](../../../multimodal/papers/arxiv-2608.18077/README.md) 的卡片。放在最后，因为它要求同时理解视频预测、动作解码和训练—部署的差异。练习：画出 Zero-WAM 训练时与部署时的数据流，标出视频预测误差从哪里传到动作。

读完后可以去[多模态的世界模型方向](../../../multimodal/fields/world-models/README.md)看视频生成一侧，再读观点页[《生成收敛》](../../../perspectives/generative-convergence.md)的"从视频生成到世界模型"一节。

## 第六步：把模型名字换成可检验的设计选择

第三步的 DINO-WM → [V-JEPA 2](../../papers/arxiv-2506.09985/README.md)（2025）之后，优先读 [JEPA-WMs 系统研究](../../papers/arxiv-2512.24497/README.md)（TMLR 2026）。它把编码器、训练展开、本体状态和规划器分别做对照。练习：固定任务和数据量，只改一个变量，预测会先影响表示误差还是规划成功率；注意仿真与真实图像数据的选择可能不同。

随后选读 [Cosmos Policy](../../papers/arxiv-2601.16163/README.md)（2026），与第五步的 Zero-WAM 对照"预测器如何与策略结合"；再读 [The Planning Limits of Latent World Models](../../papers/arxiv-2609.39235/README.md)（2026-09），把训练预测长度、规划展开长度、目标距离和反馈间隔画成四个独立量。

检验（示例设置）：预测器训练看 5 步，测试也只展开 5 步，却拿 20 步后的图像作目标。分别尝试扩大网络、延长测试展开、改成近处子目标；先写下每项修改修的是哪种失败，再设计有准确动力学作对照的实验。专家子目标是额外输入，比较时必须把它的获取成本单列。

视频模型平台的代际变化单独看[多模态世界模型](../../../multimodal/fields/world-models/README.md)，部署控制的选型仍落回动作接口、闭环证据与端到端延迟。
