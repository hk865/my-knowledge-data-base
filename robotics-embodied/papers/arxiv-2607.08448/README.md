# Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents

> 状态：文献卡 · 2026 · [原文](https://arxiv.org/abs/2607.08448)

- **解决什么**：冻结动作策略在长程任务、扰动或失败后容易失效，怎样由通用Agent组织它已有的局部能力。
- **核心方法**：相对直接运行VLA，把接触动作封装成短时可重试原语，与解析工具、任务记忆和失败经验一起交给冻结Agent调度。
- **为什么在这个库里**：完整具身Agent与动作模型相接的近期主读入口，连接[基线表](../../fields/embodied-agents/BASELINES.md)中的技能接口、反馈与记忆。优先级：必读。 [技术精读](reading.md)。
