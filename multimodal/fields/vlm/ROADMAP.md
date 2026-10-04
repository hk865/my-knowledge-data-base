# 视觉语言模型：阅读与问题路线

[回到入门](README.md) · [Baseline](BASELINES.md) · [论文目录](PAPERS.md)

六步。前两步建立基线和它的对照，第三步先学会怀疑分数，再看分辨率和训练流程两条主线，最后接到机器人。

## 第一步：基线的数据流与冻结日程

读 [LLaVA 精读](../../papers/llava/reading.md)，再读 [LLaVA-1.5](../../papers/arxiv-2310.03744/README.md)。

为什么在这里：此后几乎所有开源 VLM 都是"ViT + MLP + LLM"，先把这条最简单的路看清，后面每篇都能读成"改了哪个部件"（[Baseline 页](BASELINES.md)）。LLaVA-1.5 是同一结构上的受控对照，告诉你 MLP、分辨率、格式提示各值多少。

检验题：
1. 画出一张图和一个问题进入 LLaVA 的数据流，标出两个训练阶段里各自更新的参数。损失算在哪些 token 上？
2. 336 像素、14 像素切块的 CLIP 给出多少个视觉 token？换成 448 像素呢？（答案：576；1024。）
3. 为什么原版 LLaVA 对是非题倾向答"是"，LLaVA-1.5 用什么办法修正？

## 第二步：被放弃的两种接法

读 [Flamingo](../../papers/arxiv-2204.14198/README.md) 与 [BLIP-2](../../papers/arxiv-2301.12597/README.md)。

为什么在这里：知道 LLaVA-1.5 赢了谁、为什么赢，才能判断今天的 DeepStack、SVA 是不是在重走老路。两篇都冻结 LLM，消融里最重要的东西（Flamingo 的交错网页数据与零初始化门控，BLIP-2 的第一段表征学习）也值得记住。

检验题：
1. Flamingo 的 tanh 门控在初始化时让模型等于什么？去掉它会怎样？
2. BLIP-2 每张图给 LLM 多少个视觉向量？与 LLaVA-1.5 的 576 个相比，省下了什么、丢掉了什么？
3. BLIP-2 自述不会上下文学习，它给的原因与 Flamingo 的 M3W 消融有什么关系？

## 第三步：先学会怀疑分数

读 [POPE](../../papers/arxiv-2305.10355/README.md)、[MMStar](../../papers/arxiv-2403.20330/README.md)、[Cambrian-1](../../papers/arxiv-2406.16860/README.md) 第 3.1 节。

为什么在这里：后面的模型论文都用 benchmark 说话。MMMU、MathVista 这类题开不开图差距很小，是非题一律答"是"能拿一半分，学术分高也不等于用户喜欢。先建立这些判断，再读模型论文才不会被数字带着走。

检验题：
1. 一个模型 POPE 准确率 50%、"是"的比例 99%，说明什么？为什么 POPE 同时报 F1？
2. 给你一个新 benchmark，设计一个最便宜的实验判断它是否需要看图。
3. MMStar 用什么标准剔除题目？为什么要用 8 个 LLM 而不是 1 个？

## 第四步：看得清——分辨率与 token 预算

读 [Qwen2-VL](../../papers/arxiv-2409.12191/README.md)、[InternVL 1.5](../../papers/arxiv-2404.16821/README.md)，对照 [DeepSeek-VL2](../../papers/arxiv-2412.10302/README.md) 与 [Molmo](../../papers/arxiv-2409.17146/README.md) 的切块。

为什么在这里：2024 年开源模型追上闭源模型，最大的一步是分辨率。读完能解释为什么 InfoVQA 随 token 数从 28.9 涨到 77.3，而 MMMU 不动。

检验题：
1. 一张 1344×896 的图，在 Qwen2-VL（14 像素块、2×2 合并）里得到多少个视觉 token？在 InternVL 1.5（448 切块、每块 256 个 token、加一张缩略图）里呢？（答案：96×64/4 = 1536；3×2 块加缩略图共 7 块，7×256 = 1792。）
2. 切块边缘会丢什么信息？Molmo 怎样补？
3. 为什么把小图放大过头反而让 OCRBench 下降？

## 第五步：训练流程是 LLM 后训练的镜像

读 [DeepSeek-VL](../../papers/arxiv-2403.05525/README.md) 第 3.2 节、[InternVL 2.5](../../papers/arxiv-2412.05271/README.md) 第 4.3 节、[Kimi-VL](../../papers/arxiv-2504.07491/README.md) 第 2.3 节与 RL 部分、[Qwen3-VL](../../papers/arxiv-2511.21631/README.md) 第 4 节；对照 [LLM 后训练](../../../llm/fields/posttraining/README.md)。

为什么在这里：结构收敛之后，差距来自数据和训练日程。把每一段对到 LLM 一侧，能预判 VLM 会踩哪些坑。

检验题：
1. 列出语言能力被挤掉、复读、过度思考、奖励被钻空子四个坑，各写出 VLM 一侧的论文出处和 LLM 一侧的对应现象。
2. DeepSeek-VL 与 DeepSeek-VL2 的文本比例为什么不同？两者的基座有什么区别？
3. Qwen3-VL 为什么要用通用 RL 去"纠正"计数和读表？这说明 SFT 数据可能有什么问题？

## 第六步：接到机器人

读 [OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md)与 [VLA 方向](../../../robotics-embodied/fields/vla/README.md)主线历史第 2–5 节。

为什么在这里：VLA 的骨干就是 VLM，冻结视觉塔、空间接地、语言能力被挤掉三个坑原样传到动作上。

检验题：
1. OpenVLA 的底座与 LLaVA-1.5 有哪两处不同？冻结视觉编码器对成功率有什么影响？
2. Molmo 的"指向"和 Qwen2.5-VL 的绝对像素坐标，哪一个更容易接到机械臂的抓取点上？各自缺什么？
