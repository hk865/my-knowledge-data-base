# On scalable oversight with weak LLMs judging strong LLMs

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2407.04622)

[返回跨方向方法目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：可扩展监督（scalable oversight）要让较弱的监督者也能准确监督更强的 AI。辩论（debate）方案设想两个同样强的 AI 互相反驳，帮较弱的裁判选出正确答案；此前用 LLM 做的实验主要只在一个带信息不对称的抽取式问答任务（QuALITY）上。本文用较弱的 LLM 代替人类裁判，在更多种弱—强差距上检验：辩论是否比单个顾问（consultancy）、比裁判直接作答更能让弱裁判答对。
- **核心方法**：设置与提示沿用 Khan 等（2024）（§3.2），任务扩到 9 个、每个 128 题（§1），题目都改成二选一，分三类（§3.1、Table 1）：抽取式（QuALITY、BoolQ、GPQA-extractive，文章只给辩手、不给裁判，形成信息不对称）、封闭式（MMLU、GSM8KQA、PrOntoQA、TruthfulQA、GPQA）、多模态（MMMU）。协议六种（Figure 1）：裁判直接作答（看或不看文章）、指定立场的顾问与辩论，以及新加的开放顾问与开放辩论——由顾问或主辩手自己选立场，用来测"强模型本身选错时，弱裁判会不会被它说服"。辩手和顾问用 Gemini Pro 1.5，裁判用 Gemma 7B、GPT-3.5、Gemini Pro 1.0、Pro 1.5（§3.3）；只做推理时评测，不训练辩手（§3.2）。结果：辩论在所有任务类型上都胜过指定立场的顾问；抽取式任务上辩论胜过不看文章的直接作答，但不如看文章作答；封闭式任务上相对直接作答的优势很小或没有；轮数、best-of-N、裁判 few-shot 几乎不影响结果，裁判用思维链反而有害或无显著作用（§4.1）。开放顾问中，无论顾问选对选错，裁判都同样容易被说服；开放辩论中，主辩手选错时裁判准确得多（§4.2、Figure 3）。更强的辩手（Elo 更高）带来更高的裁判准确率，但幅度小于只做 QuALITY 的前作（§4.3、Figure 4）。
- **为什么在这个库里**：[评估方向](../../fields/evaluation/README.md)批注把它列为"GPQA 服务的可扩展监督问题"的入口，[各领域的评测](../../fields/evaluation/domains.md)用它指向"弱模型监督强模型"的问题。可与本方向基线 [MT-Bench 与 Chatbot Arena](../llm-judge/README.md) 对照读：后者检验强裁判与人类偏好的一致率，本篇让裁判弱于被评模型，只有在信息不对称的任务上辩论才明显有帮助。作者写明结论只适用于推理时，辩论作为训练协议是否有效没有直接证据（§1）。优先级：选读。

## 身份信息

- 稳定标识：arxiv:2407.04622 · [全文 PDF](https://arxiv.org/pdf/2407.04622) · Google DeepMind · 当前版本 v2（2024-07-12，修正 Figure 3、新增 Figure A.9）
- 方向：cross-domain/model-science、cross-domain/evaluation
