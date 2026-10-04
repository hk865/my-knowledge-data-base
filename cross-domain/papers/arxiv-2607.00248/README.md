# Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.00248)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：字节跳动 Seed 团队的 Seed2.0 系列（Pro / Lite / Mini，用于豆包等产品；模型卡 2026-06-30 发布于官网与 arXiv）怎样为大规模线上部署的用户体验与"真实世界的复杂任务"做优化（§1）。
- **核心方法**：§1 把智能体"会做竞赛题、却做不完实际任务"的差距归为两点：真实任务跨越长程与多个阶段，现有智能体难以自己搭工作流、在长时间尺度上积累经验；真实知识高度专业化、长尾。对应地，Seed 从真实用户需求出发选取或构建评测，搭成科学发现、Vibe Coding、上下文学习、真实任务四个维度的评测体系，并写明它"既是 benchmark 套件，也是迭代开发的指南"（§1、§6）。图 1 的企业使用场景分布中，社交陪伴是较小的一类。§4.1 的中文复杂指令遵循内部评测（912 例、17 个加权维度）上 Seed2.0 Pro 75.26%，比 Seed1.8 高 2.37 个百分点，提升最大的是语气控制（+15.16 个百分点，包括傲娇、阴阳怪气这类风格）。§1 自述与 Claude 在编码上差距明显（SWE-Evo、NL2Repo），与 Gemini 在长尾知识上差距明显；§4 写明仓库级代码生成与长程上下文整合仍难。
- **为什么在这个库里**：[思考笔记](../../../perspectives/notes/model-behavior.md)第 4 条豆包的官方对照：语气、风格是它明确优化并评测的维度，陪伴是使用场景之一，但模型卡没有"默认以情绪回应"的表述，也没有迎合评测。[观点页](../../../perspectives/eval-shapes-models.md)里作为"评测体系就是开发指南"的直接自述。后续版本 Seed2.1 只有[官方发布博客](https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity)（2026-06-23），写明评测以真实工作流和众包开发者盲评为先。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2607.00248 · [全文 PDF](https://arxiv.org/pdf/2607.00248) · [官方页面](https://seed.bytedance.com/en/public_papers/seed2-0-model-card-towards-intelligence-frontier-for-real-world-complexity)
- 作者：ByteDance Seed
- 开放情况：官方模型卡；模型未开放权重。
- 方向：cross-domain/evaluation、cross-domain/agents
