# Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models

> 状态：文献卡 · 2025 · [原文](https://arxiv.org/abs/2502.19417)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：机器人难以执行"做个不要番茄的素三明治"这类开放指令，也难以在执行中接受人的纠正。
- **核心方法**：分层 VLA：高层 VLM（PaliGemma-3B）约 1 Hz 读取指令、图像与用户插话，输出原子语言指令和口头回应，低层 [π0](../arxiv-2410.24164/README.md) 执行；高层用大模型合成的人机对话数据训练。三个平台上指令准确率比 GPT-4o 做高层高约 40%；没有记忆，长上下文指令做不好。
- **为什么在这个库里**：[具身 Agent](../../fields/embodied-agents/README.md)主线第 4 步：高层从冻结的通用大模型变成训练过的 VLM。优先级：必读。
