# Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.05904)

[返回大语言模型目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：SFT 数据里含有基座没学过的新事实时，会不会让模型更容易编造。
- **核心方法**：在闭卷问答（EntityQuestions）上，用作者提出的 SliCK 方法按 PaLM 2-S 基座能否答对，把微调样本分成 Known 与 Unknown，控制 Unknown 的比例做微调。发现 Unknown 样本比 Known 样本拟合得慢得多；一旦被拟合，它们会线性地增加模型在已有知识上的幻觉；最好的开发集表现出现在拟合了大部分 Known、只拟合了少数 Unknown 的时候，因此早停能降低风险。作者自述：只用了一个模型；结论来自闭卷问答，长文本生成中过滤 Unknown 样本的做法还要另行验证（§11）。
- **为什么在这个库里**：后训练总览"SFT 学不到新知识，反而可能增加幻觉"的直接证据，[SFT Baseline 表](../../fields/posttraining/sft/BASELINES.md)"数据内容"一格；Llama 3 按"让模型知道自己知道什么，而不是添加知识"构造事实性数据时引用了它。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2405.05904 · [全文 PDF](https://arxiv.org/pdf/2405.05904) · Technion、Google Research
- 方向：llm/posttraining/sft
