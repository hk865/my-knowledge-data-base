# 世界模型（多模态侧）：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

先走五步，从你熟悉的状态方程出发，走到视频生成团队的世界模型和它们的评测。每一步先读材料，再做一个能检验理解的小练习。

1. **把世界模型看成"状态更新 + 渲染"。** 读 [VAE 讲义](../../../foundations/lessons/16-vae.md)，再读 [World Models](../../../robotics-embodied/papers/arxiv-1803.10122/README.md) 卡片和[入门页](README.md)"什么是世界模型"一节。放在第一步，因为后面每篇论文都在替换这里的某个部件（表示、动力学、动作接口），先把三件套和状态方程对上，才看得出谁改了什么。练习：用 x_{t+1} = f(x_t, u_t)、y = h(x) 写出 World Models 中 V、M、C 各自对应哪一项，并说明路砖一例说明 h 的逆（编码器）缺了什么。
2. **潜空间世界模型的完整形态与它的盲点。** 读 [DreamerV3 精读](../../papers/dreamerv3/reading.md)，再读 [DIAMOND](../../papers/arxiv-2405.12399/README.md) 卡片。放在这里，因为 DIAMOND 正是从 Dreamer 一线的盲点（压缩丢掉小细节）出发，两篇连读就是一次"站在现在看过去"。练习：设想 Breakout 的分数只占画面的 1%，说明一个以重建误差训练、带强正则的离散潜变量为什么可能把它丢掉，DreamerV3 又是怎样用"弱正则 + free bits"缓解的。
3. **从视频生成造出可玩的世界。** 先读[扩散讲义](../../../foundations/lessons/17-diffusion.md)，再读 [Genie](../../papers/arxiv-2402.15391/README.md)、[GameNGen](../../papers/arxiv-2408.14837/README.md)、[Genie 2](../../papers/genie-2-blog/README.md)、[Genie 3](../../papers/genie-3-blog/README.md)。放在这里，因为这是 2024 年后世界模型的主力形态，需要先懂扩散怎样以条件生成一帧。练习：画出 GameNGen 训练时与生成时上下文帧的来源，标出噪声增广在哪一步起作用；再说明为什么屏幕上的弹药数字同时是"要画对的东西"和"模型的记忆"。
4. **用专项考题检验"世界模拟器"。** 读 [Sora 技术报告卡](../../papers/sora-tech-report/README.md)，再读 [Physics-IQ](../../papers/arxiv-2501.09038/README.md)、[PhyWorld](../../papers/arxiv-2411.02385/README.md)、[VideoPhy](../../papers/arxiv-2406.03520/README.md)。放在生成之后，因为这些评测是针对上一步那类模型设计的，读过生成一侧才知道它们在测哪个部件。练习：Physics-IQ 中真实感与物理理解的相关 r = −0.46 且不显著，说明这对"用 FVD 或人工辨真伪挑世界模型"意味着什么；再用 PhyWorld 的"颜色 > 大小 > 速度 > 形状"预测一个视频模型可能出现的物体变形。
5. **不画像素的另一条路。** 读 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) 卡片和 [Cosmos](../../papers/arxiv-2501.03575/README.md) 卡片，再转到[机器人侧的世界模型页](../../../robotics-embodied/fields/world-models/README.md)。放在最后，因为它要求同时理解生成一侧的代价（慢、物理不准）和规划一侧的需求（快、目标明确）。练习：按 V-JEPA 2-AC 每个动作 16 秒、Cosmos 每个动作 4 分钟，估算一次 10 步抓放各要多久，并说明 V-JEPA 2 为此放弃了什么（提示：结果能不能被人直接看懂、目标怎样给出）。

## 续篇：把生成接口与控制证据重新接起来

先读 [Dreamer 4](../../papers/arxiv-2509.24527/README.md)（必读），把第二步的 RSSM 与它的因果分词器、Transformer 动力学逐项对照；再读 [Cosmos-Predict2.5](../../papers/arxiv-2511.00062/README.md)（选读），最后读 [Cosmos 3](../../papers/arxiv-2606.02800/README.md)（必读）。这一顺序依次解决“复杂状态能否扩展”“视频怎样被控制”“同一个网络怎样同时预测状态与动作”。

练习：写出三个条件任务：p(未来视频｜历史、动作)、p(动作｜前后视频)、p(未来视频、动作｜历史、指令)。在 Cosmos 3 Fig.4 上标出三者分别给什么加噪；再说明 Dreamer 4 的想象强化学习需要其中哪些接口、还缺哪种奖励信息。最终分别记录视频误差、模型内回报和真实环境成功率，不把它们合成一个“世界模型分数”。

读完后可以去观点页[《生成收敛》](../../../perspectives/generative-convergence.md#从视频生成到世界模型)看"视频团队为什么转去做世界模型"的跨领域论证。
