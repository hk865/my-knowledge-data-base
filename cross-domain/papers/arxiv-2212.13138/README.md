# Large Language Models Encode Clinical Knowledge

> 状态：文献卡 · 2022 · [原文](https://arxiv.org/abs/2212.13138)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：医学 LLM 的评估依赖少数自动化基准，缺少同时覆盖执业考试、科研与消费者提问，并由医生评价回答事实性、危害与偏差的标准。
- **核心方法**：组合 MultiMedQA：6 个已有问答数据集（MedQA（美国医师执照考试题）、MedMCQA、PubMedQA、MMLU 临床主题、LiveQA、MedicationQA），加新建的 HealthSearchQA（3,375 条常见健康搜索问题）；并提出由医生与非专业用户沿多个维度（是否与科学共识一致、可能的危害、偏差等）评价长回答的框架。Flan-PaLM（540B）在 MedQA 上 67.6%，比此前最好结果高 17 个百分点以上；但医生评价它的长回答，只有 61.9% 与科学共识一致，29.7% 可能导致有害结果。用少量示例做 instruction prompt tuning（一种参数高效的软提示微调）得到 Med-PaLM 后，这两个数字变为 92.6% 与 5.8%，与医生写的回答（92.9%、6.5%）相当，但整体仍不如医生。
- **为什么在这个库里**：[分任务能力图](../../fields/evaluation/domains.md)"医疗"一节中"考试准确率不等于安全的长回答"的直接证据：同一个模型，选择题拿到当时最好成绩，开放回答的潜在危害率却接近 30%；改变这一点的是一小步领域对齐，而不是更多知识。下一步读 [HealthBench](../arxiv-2505.08775/README.md)，看医生判断怎样被做成大规模 rubric。优先级：必读。

## 身份信息

- 稳定标识：arxiv:2212.13138 · [全文 PDF](https://arxiv.org/pdf/2212.13138) · Google Research、DeepMind
- 发表：Nature 620, 172–180（2023），题名相同；本卡数字取自 arXiv v1
- 方向：cross-domain/evaluation
