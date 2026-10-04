# 评估：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [全部文献](PAPERS.md)

五步，每步先读、再做一道检验题。检验题都能用纸笔或一个小脚本完成，答案的依据在所列原文里。

## 第一步：把一个评测拆成四个部件

读：[入门页](README.md)"什么是评测"，[MMLU](../../papers/arxiv-2009.03300/README.md) 与 [SWE-bench](../../papers/arxiv-2310.06770/README.md) 的文献卡。

检验题：分别写出 MMLU 与 SWE-bench 的题目分布、接入方式、判分器、汇总统计。然后回答：MMLU 为什么故意不提供训练集？这个设计假设了训练语料里没有什么？SWE-bench 换一个脚手架，四个部件中哪一个变了，为什么分数可以差十倍？

## 第二步：检验一个裁判

读：[MT-Bench 与 Chatbot Arena 精读](../../papers/llm-judge/reading.md)第 3–4 节，[AlpacaEval-LC](../../papers/arxiv-2404.04475/README.md)。

检验题：取 20 道开放题，各准备两份质量相近的回答，让任意一个 LLM 当裁判，先按 A、B 顺序判一次，再交换顺序判一次，记录判决翻转的比例；再把其中一份回答在不增加信息的前提下改写得更长，看裁判是否改判。对照 MT-Bench 的 Table 2、Table 3，说明你的翻转率对应它的哪一种偏差，以及 MT-Bench 报告的"约 85% 一致"是在哪个子集上算的。

## 第三步：量一次污染

读：[GSM1k](../../papers/arxiv-2405.00332/README.md)、[LiveCodeBench](../../papers/arxiv-2403.07974/README.md)、[Oren 等](../../papers/arxiv-2310.17623/README.md)。

检验题：三种检测办法（重新出题、按时间切分、检验题目顺序的似然）各需要什么前提，各自检测不到哪种污染？假设你要检查一个开源模型是否见过某个公开的选择题集，只有模型权重、没有训练数据，你会选哪一种，需要准备什么？再读 [DeepSeek-R1](../../../llm/papers/arxiv-2501.12948/README.md) 的去污染说明，指出 10-gram 过滤为什么挡不住改写过的题。

## 第四步：把评测当奖励，预测会出什么问题

读：[入门页](README.md)"评测怎样进入训练"，[IFEval](../../papers/arxiv-2311.07911/README.md)，[Tülu 3](../../../llm/papers/arxiv-2411.15124/README.md) 的 RLVR 一节，[RL 方向](../../../llm/fields/posttraining/rl/README.md)的奖励黑客案例。

检验题：IFEval 的判分器是一组字符串与计数检查。如果把它直接当 RL 奖励，列出三种模型可能学会的捷径（提示：宽松判定会删掉首行和末行；"至少出现 3 次"不检查语义）。Tülu 3 的模型 IFEval 80 分上下、IFEval-OOD 只有 20–30 分，这说明奖励教会了什么、没教会什么？再对照 Kimi K2 附录 F.3：一组禁止免责声明的评分细则，会让模型在模糊问题上表现出什么行为？

## 第五步：评测的生命周期与隐藏

读：[SWE-bench Verified](../../papers/openai-swe-bench-verified/README.md) → [Verified 退役说明](../../papers/openai-swe-bench-verified-retired/README.md)，[HLE](../../papers/arxiv-2501.14249/README.md)，[The Leaderboard Illusion](../../papers/arxiv-2504.20879/README.md)。

检验题：用入门页"为什么评测数据被隐藏"一表，为 SWE-bench 设计一个不容易被污染、也不容易被钻空子的后继版本：题目从哪来、测试怎样写才既不过窄也不过宽、公开哪些、隐藏哪些。然后说明你的设计放弃了什么（提示：外部复核、题量、维护成本）。最后回答：Arena 上"私下测 10 个变体只公布最好的"为什么会抬高排名，它和在测试集上调超参数是不是同一件事？

## 保留边界

记录原文支持的事实、自己的解释和仍需实验验证的假设；没有独立运行实验时，不写成已复现。各领域的评测（角色扮演、安全、代码规范、科研、金融、医疗、法律）怎样拆成同样的四个部件，在[各领域的评测](domains.md)里继续。
