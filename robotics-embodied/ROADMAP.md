# 机器人与具身系统：路线图

[领域总目录](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md)

## 分方向路线

- [感知与传感器](fields/perception/ROADMAP.md)
- [状态估计与建图](fields/localization-mapping/ROADMAP.md)
- [导航与规划](fields/navigation-planning/ROADMAP.md)
- [运动控制与腿足运动](fields/control-locomotion/ROADMAP.md)
- [模仿学习与机器人强化学习](fields/imitation-reinforcement-learning/ROADMAP.md)
- [视觉语言动作模型](fields/vla/ROADMAP.md)
- [世界模型与行动预测](fields/world-models/ROADMAP.md)
- [具身Agents](fields/embodied-agents/ROADMAP.md)

## 有基础以后：把历史接到 2025–2026

按想解决的问题选一行，先读左侧基线，再读右侧后续；每个方向的具体优先级、证据和边界放在它自己的路线图。

| 方向 | 历史问题的入口 | 近期出口 |
|---|---|---|
| [感知](fields/perception/ROADMAP.md) | FM-Fusion 的串联；DA2 / FoundationStereo 的深度 | SAM 3、DA3；Fast-FoundationStereo、LAS2 的实时化 |
| [定位与建图](fields/localization-mapping/ROADMAP.md) | ORB-SLAM3 / VINS-Mono；前馈模型的尺度与漂移 | MASt3R-Fusion（2025）、VGGT-SLAM 2.0 / AMB3R-SLAM（2026） |
| [导航与规划](fields/navigation-planning/ROADMAP.md) | R2R 的任务假设；NaVILA 的分层接口 | DualVLN（2025）、ABot-N1 / Robostral Navigate（2026） |
| [运动控制](fields/control-locomotion/ROADMAP.md) | RMA / Miki 的感知；OmniH2O 的跟踪 | AME-2、SONIC、三维结构穿越、Generate, Track, Improve |
| [模仿与强化](fields/imitation-reinforcement-learning/ROADMAP.md) | DAgger 的反馈；HIL-SERL 的真机学习 | π*0.6（2025）、RL Token / EgoScale（2026） |
| [VLA](fields/vla/ROADMAP.md) | OpenVLA / π0 的动作生成 | 2025–2026 的连续执行、记忆、经验学习和可复现评测 |
| [世界模型](fields/world-models/ROADMAP.md) | Dreamer；DINO-WM 的潜空间规划 | V-JEPA 2、JEPA-WMs、Cosmos Policy 与规划范围诊断 |
| [具身 Agent](fields/embodied-agents/ROADMAP.md) | SayCan 的技能边界与验证 | Hi Robot（2025）；EmbodiedSkills、RoboSkill、MEMORA（2026） |

有足式 RL 经验时，可先走“AME-2 → 感知可靠性 → 生成器后训练”这条短线，再展开 VLA 与世界模型。保留旧论文的原因是它们定义了接口和失败来源；近期论文的价值是改了其中哪一处。

## 已有完整技术路线

- [robotics-baselines](../docs/roadmaps/robotics-baselines.md)
- [embodied-baselines](../docs/roadmaps/embodied-baselines.md)
- [embodied-agents](roadmaps/embodied-agents.md)

路线中的相邻关系通常表示学习顺序、共享问题或可比较的机制。除非原文与证据明确说明，不解释为直接算法继承。
