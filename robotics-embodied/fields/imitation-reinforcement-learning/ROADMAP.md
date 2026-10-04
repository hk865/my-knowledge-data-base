# 模仿学习与机器人强化学习：学习路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

五步。前两步分别建立模仿与强化的基线，第三步看两者在腿足上的组合，第四步看模仿怎样规模化，第五步看 RL 怎样接回模仿之上。

## 第一步：把两种训练信号的机制理顺

读[讲义](../imitation-reinforcement-learning.md)第 2–6 节（模仿）与第 7–13 节（强化），基础概念回到 [05b 强化学习](../../../foundations/lessons/05b-reinforcement-learning.md)。

为什么在这里：后面每篇论文都要回答"训练信号从哪来、更新了哪些参数"。讲义第 13 节的六类诊断（任务与奖励、信用分配、探索、课程、恢复、仿真迁移）是读后面论文时的检查表。

## 第二步：读模仿与强化各自的基线

依次读：
1. [DAgger](../../papers/arxiv-1011.0686/README.md)：复合误差的定理；
2. [PPO 精读](../../../llm/papers/ppo/reading.md)：RL 一侧；
3. [Diffusion Policy 精读](../../papers/diffusion-policy/reading.md)：多峰动作；
4. [ACT](../../papers/arxiv-2304.13705/README.md)：动作分块。

为什么在这里：DAgger 说明了模仿为什么会累积误差，PPO 说明了 RL 的更新怎样保持稳定、又不管什么（探索）；后两篇是模仿一侧的两种实用修法。

## 第三步：看腿足上的组合，RL 出教师、模仿出学生

读 [Lee 2020](../../papers/arxiv-2010.11251/README.md)，再读[运动控制入门页](../control-locomotion/README.md)第 3 节与第 6 节，以及"[为什么绕不开模仿学习](../control-locomotion/README.md#为什么绕不开模仿学习)"一节；可选 [OmniH2O](../../papers/arxiv-2406.08858/README.md)（人形上模仿教师与直接 RL 的对照）和 [AMP](../../papers/arxiv-2104.02180/README.md)（只用状态的动作模仿）。

为什么在这里：这是 DAgger 在机器人上最成功的落地形式，专家换成了仿真里的特权教师；也是四足 RL 实践中最常见的部署结构。读完会看到，腿足"以 RL 为主"只说对了一半：RL 的起点和学生一侧都靠模仿。

## 第四步：看模仿怎样规模化，以及它的上限

依次读 [RT-1](../../papers/arxiv-2212.06817/README.md) → [Open X-Embodiment](../../papers/arxiv-2310.08864/README.md) → [Octo](../../papers/arxiv-2405.12213/README.md)，VLA 结构的细节转到 [VLA 方向](../vla/README.md)。

为什么在这里：这一段把数据推到十几万到上百万条轨迹，同时写清了模仿的上限：RT-1 自述不能超过示范者，也做不出全新动作。第五步的论文都从这个上限出发。

## 第五步：看 RL 怎样接回模仿之上

先读 [HIL-SERL](../../papers/arxiv-2410.21845/README.md)，再读 [DPPO](../../papers/arxiv-2409.00588/README.md)，最后读 [π*0.6](../../papers/arxiv-2511.14759/README.md)；可选 [SimpleVLA-RL](../../papers/arxiv-2509.09674/README.md)。

为什么在这里：
- HIL-SERL 是"同样多的人类数据，模仿还是 RL"的直接对照，最能说明 RL 补的是什么；
- DPPO 和 π*0.6 分别回答 RL 怎样接到生成式策略和大模型上；
- SimpleVLA-RL 对照 LLM 后训练的做法。

读完回到[入门页](README.md)的"当前开放问题"，其中奖励来源、长时域、人工纠正的质量都还没有解决。

## 第六步：用 2025–2026 的工作决定自己的改进接口

第五步建立了 RL 回到模仿之上的问题，接着读一组有明确分工的论文：

1. [π*0.6](../../papers/arxiv-2511.14759/README.md)（2025）与 [RL Token](../../papers/arxiv-2604.23073/README.md)（2026）对照，优先级：必读。前者从经验分轮更新大策略，后者冻结底座、在线更新小头。练习：把采集、奖励、人类介入、可训练参数与部署切换列成五行；再解释各自的成功率和吞吐量在测哪一段任务。
2. [EgoScale](../../papers/arxiv-2602.16710/README.md)（2026），优先级：选读。接第四步的跨机器人示范，标出人类动作估计、重定向、人机对齐与任务微调四处的数据成本；训练数据更多并不等价于完全免示范。
3. [Generate, Track, Improve](../../papers/arxiv-2609.31577/README.md)（2026），优先级：足式支线选读。对照 [AME-2](../../papers/arxiv-2601.08485/README.md)，一个把 RL 用于参考生成器，一个让学生策略结合教师监督与 RL。检验：如果低层控制器固定，哪些错误仍有可能靠高层更新修好？

读论文时保留仿真、真实关键阶段、真实整项任务三种证据口径；跨口径的数字不拼成统一排行榜。
