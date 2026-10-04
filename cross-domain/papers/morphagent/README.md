# Metamorphic Testing of Multi-Agent LLM Systems: A Trace-Based Behavioral Oracle Framework

> 状态：文献卡 · 2026 · [原文](https://ieeexplore.ieee.org/abstract/document/11662476/)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：多智能体 LLM 系统的输出不确定，智能体之间的交互又会产生涌现行为，传统的测试预言（oracle，判断一次运行结果对不对的依据）因此失效。摘要称本文用基于执行轨迹的行为分析来处理这个预言问题。
- **核心方法**：把蜕变测试（metamorphic testing：不看标准答案，而检查输入做某种变换后，前后两次运行应满足的关系）用到 agent 的执行轨迹上。框架 MORPHAGENT 记录结构化轨迹（规划步骤、工具调用、消息往来、最终输出），对源运行施加变换后再运行一次，检查三类关系：目标保持（输入扰动后目标仍达成）、协作一致（替换或重排智能体后，委派与通信模式仍一致）、工具使用完整（改写提示后，工具调用序列语义等价）。摘要报告：在代码生成、研究综述、客服、数据分析四个多智能体基准和三个 LLM 后端上，共 2,840 对源—后续运行；人为注入的行为故障检出 82.0%，其中协作故障 90.3%、目标偏离故障 81.7%，误报率 6.1%；在已有的多智能体框架中发现 14 个此前未报告的行为异常。
- **为什么在这个库里**：[Agent 方向](../../fields/agents/README.md)批注把它与 [Agentic property-based testing](../agentic-property-based-testing/README.md) 一起列为"从测试一侧加强验证"的例子：二者都不依赖逐题的标准答案，一个检查对一类输入都该成立的性质，一个检查变换前后两条轨迹之间的关系。[评估方向](../../fields/evaluation/README.md)"捷径与裁判偏差"一节写到裁判只读到文字、看不到外部状态，本篇检查的对象正是执行轨迹，而不只是最终回答。优先级：存档。

## 身份信息

- 稳定标识：doi:10.1109/aitest70988.2026.00036 · [IEEE 计算机学会数字图书馆摘要页](https://www.computer.org/csdl/proceedings-article/aitest/2026/056200a185/2jgwiWf2kU0) · Gopalakrishnan Marimuthu（独立研究者，美国佐治亚州亚特兰大） · 2026 IEEE International Conference on Artificial Intelligence Testing (AITest)，pp. 185–192
- 方向：cross-domain/agents、cross-domain/evaluation

## 批注

**易误读**
- 82.0% 是对人为注入（seeded）故障的检出率，不是对真实缺陷的召回率；6.1% 误报率的计算口径摘要没有写明（摘要）。

**未核实 / 待验证**
- 全文未能打开：四个基准与三个 LLM 后端的具体名称、故障注入方式、14 个行为异常分别出现在哪些框架，都只有摘要的概括，未核实。
- 作者与单位取自 IEEE 计算机学会数字图书馆的摘要页，未与全文首页核对。
