# 视频与时序表征

> 状态：领域入门页 · v2
>
> 速览：
> - 视频比图像多一根时间轴。这个方向研究模型怎样把"时间"放进表征：单帧外观再聚合、光流与 3D 卷积抓局部运动、时空注意力连接跨帧关系，以及视频大模型把成百帧的 token 交给语言模型。
> - 主线是"benchmark 被外观捷径攻破，再换一个更需要时间的 benchmark"：UCF-101 → Kinetics → Something-Something → 视频-文本检索与问答 → 长视频（EgoSchema、Video-MME）。
> - 站在现在看，最大的坑是静态外观偏差：完全不建模时间的 TimeSformer 在 Kinetics 上 76.9%、在 Something-Something v2 上 36.6%；从没见过视频的图像模型 DINOv2 冻结评测 Kinetics 83.4%，高于专门在视频上预训练的 V-JEPA（82.0%）。
> - 视频大模型的核心约束是 token 预算（帧数 × 每帧 token 数）。LLaVA-Video 发现"多帧、每帧少 token"好于"少帧、每帧多 token"，但有下限；所有模型都随视频变长而掉分，Gemini 1.5 Pro 在 Video-MME 上从短视频到长视频降 14.3 个百分点。
> - [判断] 视频理解、视频生成和机器人世界模型用的是同一套时间部件（时空切块、空间与时间分解、时间压缩），卡在同一个缺口上：多长的过去、以什么粒度留在上下文里。

本页属于[多模态总目录](../../README.md)。拆分后的基线见 [Baseline 页](BASELINES.md)，问题路线见[路线图](ROADMAP.md)，收录论文见[论文目录](PAPERS.md)。

**页型说明。** 本页按 STYLE §3（以任务界定的方向）来写，没有用[视觉表征页](../visual-representation/README.md)的 §3.6 变体。原因是视频方向有自己专属的任务与 benchmark（动作识别、时空动作检测、视频问答、长视频理解），而且它的历史正是由 benchmark 的替换推动的；本方向的核心问题恰好是"这些 benchmark 有没有测到时间"，按 §3.1 应当写进历史。视觉表征页"先界定对象、再讲谱系"的做法保留在第一节。

## 这个领域在解决什么

结论：要回答的是"必须看顺序才能答"的问题，而大部分 benchmark 里装的是"看一帧就能答"的问题。

两段 3 秒的视频：一段是把杯子放进盒子，另一段是假装放进去又拿出来。单独看任何一帧都差不多，区分它们要看帧的先后与物体状态的变化。"这个人在滑雪吗"则只要一帧雪地就够。视频理解要解决的是前一类问题；这个领域的大部分历史，是在发现 benchmark 里其实多是后一类问题之后，一次次换题。

**时间进入表征的四种方式**（本方向的方法谱系；训练信号是另一根轴，见下文）：

| 方式 | 时间怎样进入 | 代表 | 换来的 | 代价与做不好的 |
|---|---|---|---|---|
| 单帧外观 + 聚合 | 每帧独立编码，再平均，或交给后面的模型 | 双流的空间流；Lei 等的单帧训练；视频大模型的逐帧编码 | 直接复用图像预训练，便宜 | 分不清顺序和方向（放进与拿出、打开与关上） |
| 局部运动 | 光流（一句话：相邻帧之间每个像素的位移场，预先用传统算法算好），或带时间维的 3D 卷积核 | 双流的时间流、I3D、SlowFast | 抓住几帧之内的运动 | 感受野只有几帧；光流贵，且怕相机运动 |
| 跨帧注意力 | 把视频切成时空块（token），在块之间做注意力，常把空间与时间分开算 | TimeSformer、ViViT，以及 VideoMAE、V-JEPA 的 ViT 主干 | 一层就能读到整个片段 | token 数随帧数线性增长、注意力随 token 数平方增长；TimeSformer 受显存限制最多 96 帧 |
| 语言模型的上下文 | 帧 token 按时间顺序排进语言模型，另加时间位置编码 | Video-LLaVA、LLaVA-Video、Qwen2.5-VL | 开放式问答，可以处理数十分钟的视频 | 帧数 × 每帧 token 数受上下文限制；时间戳要专门编码 |

训练信号一轴依次是：有监督动作标签（Kinetics）→ 遮蔽重建像素（VideoMAE）→ 在特征空间里预测被遮部分（V-JEPA）→ 视频-文本对比与指令数据（InternVideo2、LLaVA-Video）。这条轴与[视觉表征](../visual-representation/README.md)的"训练信号"一轴同构，区别在视频帧之间高度冗余，遮蔽和采样都要专门处理时间。

几个贯穿全页的词。**片段与视图**：从视频里截出的连续若干帧叫一个片段；测试时在不同时间位置截多个片段、每个片段再取几种空间裁剪，每种组合叫一个视图，最终分数取各视图平均，常见的 30 视图就是 10 个片段 × 3 个裁剪（TimeSformer §4.5 的说明）。**帧采样**：均匀稀疏地取几帧，或按固定帧率稠密地取。**token 预算**：视频大模型里每帧变成若干 token，帧数乘以每帧 token 数不能超过语言模型的上下文。

本方向接到三处：[视频生成](../generation/README.md)用同样的时空切块生成视频；[视觉语言模型](../vlm/README.md)把图像版的"编码器 + 投影 + 语言模型"搬到视频；机器人一侧的 [VLA](../../../robotics-embodied/fields/vla/README.md) 与[世界模型](../../../robotics-embodied/fields/world-models/README.md)要决定给策略看多少帧历史。

## 主线历史

每个节点写三件事：上一个节点留下的问题、这一节点改变了什么、它自己做不好的场景。

1. **双流网络（2014，Oxford）：时间 = 预先算好的光流。** 留下的问题：卷积网络在图像上已超过手工特征，搬到视频时却不灵：Karpathy 等（2014）把多帧直接堆进网络，单帧网络与多帧网络表现相近，微调到 UCF-101 后比手工的稠密轨迹特征差约 20%（双流原文 §1.1 的转述）。改变：[Two-Stream](../../papers/arxiv-1406.2199/README.md) 把视频拆成两路，空间流看单帧 RGB（可用 ImageNet 预训练），时间流看堆叠的 10 对光流，两路分数晚融合。UCF-101 三个划分平均 88.0%，与手工特征 IDT（85.9%–87.9%）相当。**做不好**：UCF-101 每个划分只有 9.5K 个训练视频；光流要预先算好；只看单帧的空间流就有 73.0%，说明许多类靠外观就能分。最差的 Hammering 类，空间流把它认成 HeadMassage（都有人脸），时间流认成 BrushingTeeth（都是手上下重复运动），两种线索各有盲区。

2. **Kinetics 与 I3D、Something-Something（2017）：数据规模扩大，benchmark 分成两类。** 留下的问题：UCF-101、HMDB-51 只有约 1 万段视频，各种结构分不出高下；视频能否像 ImageNet 那样靠大数据预训练再迁移。改变：DeepMind 的 Kinetics 有 400 类、约 24 万段训练视频（每段约 10 秒，均已裁剪）。[I3D](../../papers/arxiv-1705.07750/README.md) 把 ImageNet 上的 2D 网络"膨胀"成 3D：N×N 的卷积核变成 N×N×N，权重沿时间复制 N 份再除以 N，使一张图重复成的"静止视频"输出不变；Kinetics 预训练后 UCF-101 达 98.0%。同年 TwentyBN 的 [Something-Something](../../papers/arxiv-1706.04261/README.md) 走反方向：请人按"把某物放进某物""假装把某物放到某物后面"这类模板录视频，同一物体做一组只差细节的动作，专门不让模型靠认物体、看手的位置或相机抖动"作弊"；3D-CNN 在 174 类上 top-1 错误率 88.5%。**做不好**：I3D 自己的表格已经显示 Kinetics 偏外观：逐帧分类再平均的基线有 62.2%；光流单路 63.4%，低于 RGB 单路 71.1%，而在 UCF-101、HMDB-51 上光流更强。作者写道只看光流时人眼也常认不出 Kinetics 的动作，归因于相机运动更多。[判断] 从这里开始 Kinetics 衡量规模与外观，Something-Something v2（SSv2，扩充到约 22 万段的版本）衡量时间，两者经常给出相反的排序：ViViT 观察到此前方法在两者上的相对表现呈反相关（§4.3）。

3. **SlowFast（2018，FAIR）：时间轴不该与空间对称处理。** 留下的问题：3D 卷积把时间当作第三个空间维度；双流还要预先算光流。改变：[SlowFast](../../papers/arxiv-1812.03982/README.md) 的 Slow 路帧率低、通道宽，看"是什么"；Fast 路帧率高 8 倍、通道只有 1/8，约占 20% 计算，看"怎么动"；侧向连接把两路融合，端到端从像素训练。Kinetics-400 上 79.8%（不用 ImageNet 预训练）；Fast 路单独只有 51.7%，加到 Slow 路上提升 3.0 个百分点；AVA 时空动作检测（一句话：在视频里框出每个人并标出他在做的动作）从 19.0 升到 24.2 mAP（平均精度，越高越好），拍手 +27.7、游泳 +27.4 AP。**做不好**：Kinetics 上的增益不大，只看 4 帧的 Slow 路本身已有约 72.6%（由原文"只拼接两路输出 73.5%、比 Slow-only 高 0.9"推得）；AVA 上接电话、躺或睡、射击三类反而略降。作者在正文里点出一个长期被忽视的成本：许多方法测试时用 100 多个视图，SlowFast 自己也用 30 个。

4. **TimeSformer 与 ViViT（2021，FAIR 与 Google）：时间算子换成注意力。** 留下的问题：卷积只看几帧之内，长程依赖要层层聚合；3D CNN 训练很贵。改变：把 [ViT](../../papers/vit/README.md) 搬到视频，每帧切块成 token。所有时空 token 两两做注意力太贵，于是做分解：[TimeSformer](../../papers/arxiv-2102.05095/README.md) 在每层先做时间注意力（只看其他帧同一位置的块），再做空间注意力；[ViViT](../../papers/arxiv-2103.15691/README.md) 比较了四种分解，包括"先逐帧空间编码、再在帧特征上做时间编码"。TimeSformer 在 K400（即 Kinetics-400）上 78.0%，视频训练只用 416 V100 小时（SlowFast 用 3840 小时达 75.6%）。**做不好**：TimeSformer 的消融把外观偏差量化得最干净：只做空间注意力、完全不建模时间，K400 仍有 76.9%，SSv2 只有 36.6%（分解时空注意力 59.5%）。两者都依赖图像预训练：TimeSformer 从零训练 K400 只有 64.8%，ViViT 的最好结果用非公开的 JFT 预训练，并把"去掉对图像预训练的依赖"列为未来工作。TimeSformer 在 SSv2 上要用到 75% 以上的训练数据才超过 3D CNN，显存把它限制在 96 帧以内。

5. **VideoMAE 与 V-JEPA（2022–2024）：训练信号从动作标签移到视频自身。** 留下的问题：视频 Transformer 离不开图像预训练，学到的表征被图像带偏；Kinetics 的标签又奖励外观。改变：南京大学、腾讯与上海 AI 实验室的 [VideoMAE](../../papers/arxiv-2203.12602/README.md) 把 [MAE](../../papers/mae/README.md) 搬到视频，所有帧遮同一位置（管道遮蔽），遮蔽率 90%–95%：视频帧冗余，按图像那样随机遮，模型从相邻帧抄就能补全。ViT-B 在 SSv2 上从零训练 32.6%、ImageNet-21K 有监督预训练 61.8%、VideoMAE 69.6%。Meta 的 [V-JEPA](../../papers/arxiv-2404.08471/README.md) 不重建像素，而是在特征空间里预测被遮的大块时空区域，在约 200 万段公开视频上训练，冻结主干评测 SSv2 71.4%。**做不好**：两篇都写出了 Kinetics 的问题。VideoMAE 发现各遮蔽策略在 K400 上的差距小于 SSv2，认为 Kinetics 视频大多静止、与场景相关；V-JEPA 的冻结评测中，从没训练过视频的图像模型 DINOv2 在 K400 上 83.4%，高于 V-JEPA 的 82.0%，在 SSv2 上只有 50.6%。迁移受域偏移影响：在 SSv2 上，42k 段 SSv2 视频自预训练好于 24 万段 Kinetics 预训练后迁移（68.7% 对 68.5%）。V-JEPA 自述图像分类仍落后于图像模型（ImageNet 77.4% 对 DINOv2 的 86.2%），推测公开视频数据缺少多样性。

6. **视频-语言与"单帧就够"（2022–2023）：任务换成检索与问答，偏差跟着过来。** 留下的问题：动作分类的类别是固定的，目标转向用自然语言检索视频和回答问题（MSRVTT、ActivityNet-QA 等）。发现：UNC 的 [Lei 等](../../papers/arxiv-2206.03428/README.md)只用单帧训练（推理时把几帧拼起来一起送入），在 MSRVTT、DiDeMo、ActivityNet Captions 检索和三个视频问答上达到或超过多帧方法，称之为"静态外观偏差"；他们用 SSv2 的动作模板另建检索任务，单帧模型在那里比 4 帧模型低 10.9 个百分点（R1：检索结果排第一的就是正确视频的比例）。Berkeley 的 [EgoSchema](../../papers/arxiv-2308.09126/README.md) 进一步问"一道题要看多长"：定义时间证书长度（让人确信答案正确所需观看的最少片段总长），在 Ego4D 第一人称视频上建 5000 多道三分钟视频的五选一题，证书中位数约 100 秒，是第二长数据集的 5.7 倍；作为对照，Kinetics 在"类别互斥"的规则下几帧就够。发布时最好的模型不到 33%（随机 20%），人类约 76%。**做不好**：多给帧不一定更好，mPLUG-Owl 在 EgoSchema 上 1 帧 27.0%、5 帧 31.1%、30 帧 20.0%。EgoSchema 的题由 LLM 根据人工旁白生成，作者自述带有 LLM 文本分布偏差与第一人称视频偏差。它和后来的 Video-MME 都要先用"只读题目的语言模型"过滤能盲答的题，说明语言先验本身就是一条捷径。

7. **视频大模型（2023–2025）：时间交给语言模型的上下文，瓶颈变成 token 预算。** 留下的问题：开放式问答与长视频需要语言模型来组织答案，但每帧几百个 token，几十帧就填满上下文。改变：三种做法并行。第一种是先训练视频基础编码器再接语言模型，上海 AI 实验室的 [InternVideo2](../../papers/arxiv-2403.15377/README.md) 训练 6B 参数的视频编码器（遮蔽蒸馏 → 视频-音频-语音-文本对比 → 接语言模型），K400 微调 92.1%。第二种是把图像 VLM 的配方（见 [LLaVA](../../papers/llava/README.md)）直接用于视频：北京大学的 [Video-LLaVA](../../papers/arxiv-2311.10122/README.md) 把图像和视频编码器预先对齐到语言空间、共用一个投影层，每段视频 8 帧；ByteDance 与南洋理工的 [LLaVA-Video](../../papers/arxiv-2410.02713/README.md) 用 GPT-4o 按每秒 1 帧稠密标注 178K 段动态视频，并在帧数与每帧 token 数之间重新分配。第三种是在 VLM 里原生处理长视频：阿里的 [Qwen2.5-VL](../../papers/arxiv-2502.13923/README.md) 训练时动态采样帧率，把位置编码的时间维对齐到绝对时间（上一代 Qwen2-VL 的时间位置只等于帧序号，反映不了事件的快慢），相邻两帧合并成一个 token 块，评测时每段最多 768 帧、视频 token 不超过 24,576。评测随之换成 [Video-MME](../../papers/arxiv-2405.21075/README.md)：900 段 11 秒到 1 小时的视频、2700 道人工题，可另给字幕与音频。**做不好**：所有模型都随视频变长而掉分，Gemini 1.5 Pro 在 Video-MME 上从短视频 81.7% 降到长视频 67.4%，计数是共同瓶颈。早期视频大模型不如直接喂多帧的图像模型（Video-LLaVA 39.9% 对 InternVL-Chat-V1.5 50.7%），Video-LLaVA 自述 8 帧丢失长视频细节。InternVideo2 自述固定分辨率、固定采样率与高度压缩的 token 限制了细节，EgoSchema 60.0% 不及 Gemini 1.5 Pro 的 72.2%；LLaVA-Video 的 7B 模型在 EgoSchema 上偏弱，作者归因于训练数据中第一人称视频比例下降。字幕对长视频帮助最大（Gemini 1.5 Pro 长视频加字幕 +10.1）；[判断] 长视频题里有相当一部分信息走语音与文字通道，而不是画面中的时间变化。

### 后继节点：局部时空特征、明确时间与反复取证（2025–2026）

旧地图的两条末端是 V-JEPA 的视频表征和 Qwen2.5-VL 的长视频问答。它们分别留下“局部细节是否保住”“时间怎样表达”“看过一次不够怎么办”三个问题。

- **[V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) → [V-JEPA 2.1](../../papers/arxiv-2603.14482/README.md)，必读。** 前者扩大图像/视频自监督训练，并分别接理解、预测和规划；后者修正“全局动作识别强、密集空间特征弱”的问题，让可见与被遮 token 都受局部预测约束，并在多层施加监督。看动作分类之外，还要看深度、分割与局部对应。
- **[Qwen3-VL](../../papers/arxiv-2511.21631/README.md)，必读。** 它承接 Qwen2.5-VL 的时间位置设计，把时间片前的文字时间戳和交错时空位置编码配合使用，避免只靠不断增大的绝对位置编号表示长视频。时间表达更明确之后，仍要检查帧采样是否漏掉关键事件。
- **[InternVideo3](../../papers/arxiv-2606.12195/README.md)，选读。** 不再只问“能塞多少帧”，而是把观察、检索结果、工具动作和记忆放在持续更新的上下文里；M²LA（保留 token、压缩注意力缓存状态的方法）降低长上下文成本。视频 agent 的示例展示了反复找证据的用法，系统性量化仍是开放问题。

`[判断]` 这些后继把时间建模分成三层：编码器保留什么局部变化、语言模型怎样知道事件时间、执行系统怎样回看证据。长视频长度和总分无法替代这三层的分别检验。若任务还依赖声音与多人对话，再读 [Qwen3.8-Omni](../../papers/arxiv-2609.25611/README.md)，见 [VLM 方向](../vlm/README.md)的音视频智能体节点。

## 站在现在看过去：四个反复出现的坑

以下四条都是跨论文的 [判断]，支撑与反例列在批注里。

**1. 动作数据集的静态外观偏差。** 证据从 2014 年一直延续到 2024 年：双流的单帧空间流在 UCF-101 上 73.0%；I3D 在 Kinetics 上逐帧平均 62.2%、光流弱于 RGB；TimeSformer 只做空间注意力在 K400 上 76.9%；VideoMAE 说 Kinetics 视频"大多静止"；V-JEPA 中图像模型 DINOv2 在 K400 上胜过所有视频模型。论文当时没写明的经验是：Kinetics 上的领先，相当一部分来自更强的外观表征，所以更大的图像预训练在 Kinetics 上总有用、在 SSv2 上没用（TimeSformer 把 ImageNet-1K 换成 ImageNet-21K，K400 从 75.8% 升到 78.0%，SSv2 两者都是 59.5%）。后来者的应对是同时报告 SSv2，并像 V-JEPA 那样把 K400 和 SSv2 当作"外观"和"运动"两类任务分开讨论。这个坑在别的领域有同构版本：图像分类中的纹理偏向（见[视觉表征页](../visual-representation/README.md)"从测量看"一节），以及视觉问答中的语言先验（Lei 等引用的例子：VQA 的是非题全答"是"就有 87%）。

**2. 帧采样技巧掩盖了弱的时间推理。** 每一代都有一种"采样技巧"让分数上涨而不需要更好的时间建模：多视图测试（SlowFast 指出 100 多个视图的成本被忽视）；单帧训练、推理时多帧集成（Lei 等）；"超过 16 帧就不再涨"的经验，LLaVA-Video 指出那是因为 MSVD、WebVid 这类训练数据太静态；推理时帧数远多于训练帧数反而下降（LLaVA-Video 中 32 帧训练的模型推理改用 110 帧，EgoSchema 从 56.3% 降到 55.2%）；EgoSchema 上 mPLUG-Owl 30 帧反而比 5 帧差 11.1 个百分点。共同点是分数变化来自"采到了哪几帧"，而不是"读懂了顺序"。能区分两者的测试有两类：只留动作、去掉物体的模板任务（Lei 等的 SSv2-Template 检索），以及证书长度长的题（EgoSchema、Video-MME 的长视频档）。

**3. 每帧 token 与帧数的取舍。** 一个手算（示例数值）：1 小时视频按每秒 1 帧取 3600 帧，若每帧 729 个 token（LLaVA-Video 所用 SigLIP 编码器的每帧 token 数），共约 262 万 token；Qwen2.5-VL 评测时的上限是 24,576 个视频 token，取满 768 帧时平均每帧只有 32 个，相当于约每 4.7 秒看一帧。LLaVA-Video 的消融给出取舍的方向：总 token 更少时，"110 帧 × 每帧 169 token"仍好于"32 帧 × 每帧 729 token"，到"440 帧 × 64 token"开始下降；它还报告 Qwen2-72B 在 128 张 H100 上按每帧 729 token 只放得下 8 帧。这和 SlowFast 是同一个思想：语义变化慢可以少看，运动要密看；LLaVA-Video 直接借用了 SlowFast 的名字，给少数帧多 token、其余帧少 token。Qwen2.5-VL 合并相邻两帧、ViViT 用跨两帧的时空管道、V-JEPA 用跨两帧的块，都是先在时间上压缩一半。同一个约束在纯语言模型里表现为长上下文的 KV 缓存成本，见 [LLM 长上下文方向](../../../llm/fields/long-context/README.md)。

**4. 长视频记忆。** EgoSchema 发布时模型不到 33%；两年后 Qwen2.5-VL-72B 报告 test 集 76.2%，与原文人类成绩（约 76%）持平，这个 benchmark 已接近饱和。Video-MME 的长视频档仍在拉开差距：Gemini 1.5 Pro 只有 67.4%，开源模型在计数、动作识别、时间感知上差距最大。InternVideo2 把 EgoSchema 的短板归因于"需要更长的上下文"，Video-MME 的作者建议发展处理长上下文的结构与面向时间推理的训练数据。视频生成和机器人碰到的是同一个缺口：Sora 的长视频会逐渐不连贯（见[观点页](../../../perspectives/generative-convergence.md)）；VLA 一侧，多给策略看几帧历史可能引入虚假相关（见 [VLA 领域页](../../../robotics-embodied/fields/vla/README.md)对 RoboTTT 与 π0.7 的讨论）。

## 技术地基

- **卷积、感受野与 3D 卷积**：I3D、SlowFast 的时间卷积就是在卷积核上多加一维；感受野随深度增长的方式见 [CNN 讲义](../../../foundations/lessons/11-cnn.md)第 2–5 节。
- **注意力的成本与分解**：token 数为 N 时注意力成本随 N² 增长，视频的 N 是"每帧块数 × 帧数"，所以视频 Transformer 都要把空间与时间分开；见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 14 节与 [ViT 卡片](../../papers/vit/README.md)。
- **遮蔽预训练与特征预测**：VideoMAE 重建像素、V-JEPA 预测特征，区别与图像一侧的 MAE 和 DINO 相同；见[预训练目标讲义](../../../foundations/lessons/modules/objectives/03-pretraining-objectives.md)第 5–9 节。
- **位置编码**：视频大模型要同时编码帧内位置与时间，Qwen2.5-VL 把 RoPE 拆成时间、高、宽三部分并让时间部分对齐绝对时间；位置编码的原理见 [Attention 与 Transformer 讲义](../../../foundations/lessons/14-attention-transformer.md)第 8 节。
- **图文对齐与 VLM 结构**：视频大模型沿用"视觉编码器 + 投影 + 语言模型"，见 [CLIP](../../papers/clip/README.md)、[LLaVA](../../papers/llava/README.md) 与[视觉语言模型方向](../vlm/README.md)。

## 主要路线与团队偏好

- **Oxford VGG 与 DeepMind（Zisserman 一系）：双流与光流**（[Two-Stream](../../papers/arxiv-1406.2199/README.md)、[I3D](../../papers/arxiv-1705.07750/README.md)）。押注：运动要单独一路输入，外观可以借 ImageNet。[判断] 同一团队两篇都保留预计算的光流路，I3D 已经是 3D 卷积，仍写明加上光流能大幅提升（§2.4）。代价：光流要预先算，Kinetics 上相机运动使光流变弱。
- **FAIR 视频组：端到端的 RGB 模型，以计算效率为主要论据**（[SlowFast](../../papers/arxiv-1812.03982/README.md)、[TimeSformer](../../papers/arxiv-2102.05095/README.md)）。[判断] 两篇都把成本写进主论点：SlowFast 用"每视图 GFLOPs × 视图数"，TimeSformer 用训练 GPU 小时与推理 TFLOPs。代价：两篇的主战场都在 Kinetics，SSv2 上的优势更小或需要更多数据。同属 Meta 的 LeCun、Assran、Ballas 一支走 JEPA 路线（[V-JEPA](../../papers/arxiv-2404.08471/README.md) → [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)）：在特征空间预测、以冻结评测为主，并在 V-JEPA 2 中接上动作条件预测器做机器人规划；代价是图像任务落后于图像模型，规划慢（V-JEPA 2-AC 每个动作 16 秒）。
- **Google Research：借非公开的大规模图像预训练**（[ViViT](../../papers/arxiv-2103.15691/README.md)）。[判断] ViViT 的 Dehghani、Heigold 也是 [ViT](../../papers/vit/README.md) 的作者，两篇的最好结果都靠 JFT 预训练。代价：外部团队无法复现同一条件，ViViT 自己把去掉图像预训练列为未来工作。
- **南京大学与上海 AI 实验室（王利民一系）：遮蔽视频建模打底，再叠加多种目标与大规模数据**（[VideoMAE](../../papers/arxiv-2203.12602/README.md) → [InternVideo2](../../papers/arxiv-2403.15377/README.md)）。[判断] InternVideo2 的第一阶段直接用 VideoMAE 的后续版本 VideoMAEv2 当教师，两篇都开源代码，并在大量 benchmark 上报告。代价：InternVideo2 自述没有新结构，主要靠规模与数据处理。
- **LLaVA 一系（Chunyuan Li 等，从图像到视频）：用 GPT 合成指令数据**（[LLaVA](../../papers/llava/README.md) → [LLaVA-Video](../../papers/arxiv-2410.02713/README.md)）。[判断] 两篇都让 GPT（先 GPT-4，后 GPT-4o）根据描述写指令数据，同类工作 [Video-LLaVA](../../papers/arxiv-2311.10122/README.md) 也沿用 LLaVA 的结构。代价：LLaVA-Video 自述问答可能受标注者视角影响而有偏，训练数据来源决定了哪些 benchmark 涨得多（它把 VideoMME 的提升归因于数据中的大量 YouTube 视频）。
- **公司 VLM（阿里 Qwen）：把视频做成 VLM 的原生输入**（Qwen2.5-VL）。官方报告写明动态帧率、时间维对齐绝对时间的 MRoPE、合并相邻两帧，以及评测的帧数与 token 上限；训练数据中视频的规模与比例没有写明。

**视频生成团队对时间建模的启示。** 生成方向的机制见[视觉生成方向](../generation/README.md)与[观点页](../../../perspectives/generative-convergence.md)，这里只看时间。官方材料写明的做法有三点。其一，先在时间上压缩：[Sora](../../papers/sora-tech-report/README.md) 的压缩网络同时压缩时间与空间再切成时空 patch，[Wan](../../papers/arxiv-2503.20314/README.md) 与 [Seedance 1.0](../../papers/arxiv-2506.09113/README.md) 的 VAE 都把时间压 4 倍，[HunyuanVideo](../../papers/arxiv-2412.03603/README.md) 的 3D VAE 在时间方向只看过去帧。其二，空间与时间分开处理：Seedance 1.0 的扩散 Transformer 把空间层与时间层解耦。其三，失败集中在长时一致：Sora 的长视频会逐渐不连贯、物体凭空出现，[Veo 3](../../papers/veo3-tech-report/README.md) 的模型卡写明复杂运动中保持一致仍是挑战。[判断] 第一点对应理解一侧的时空管道与相邻帧合并，第二点对应 TimeSformer 的分解注意力；第三点与理解一侧的长视频记忆是同一个缺口的两面，生成团队转向世界模型后，这个缺口变成"离开视野的物体回来时还在不在"（[Genie](../../papers/arxiv-2402.15391/README.md) 只有 16 帧记忆）。

## 用什么衡量进展

benchmark 的替换就是这个方向目标的迁移：

| benchmark | 测的能力 | 已知的口径问题 |
|---|---|---|
| UCF-101、HMDB-51（2012、2011） | 小规模动作分类 | 只有约 1 万段视频；I3D 之后到 98.0% / 80.9%，已饱和 |
| Kinetics-400/600/700（2017 起） | 大规模动作分类，主要是外观 | 图像模型很强；常用 30 视图测试；ImageNet-21K 或 JFT 预训练的收益大于时间建模的收益 |
| Something-Something v2 | 细粒度动作与物体状态变化 | 图像模型弱（DINOv2 冻结 50.6%）；Transformer 需要更多数据 |
| AVA | 时空动作检测 | 动态类别（拍手、游泳）对时间建模最敏感，静态类别几乎不受影响 |
| MSRVTT、DiDeMo、ActivityNet-QA 等 | 视频-文本检索与问答 | 单帧模型就能达到最好（Lei 等）；ActivityNet-QA 的许多题看一帧就能答（LLaVA-Video 举例"球是什么颜色"）；开放式问答用 GPT-3.5 打分（Video-LLaVA），评分模型版本会影响数字 |
| EgoSchema（2023） | 三分钟视频的长时理解 | 题目由 LLM 依据旁白生成，并用语言模型过滤可盲答的题；2025 年已有模型与原文人类成绩持平 |
| Video-MME（2024） | 11 秒到 1 小时，分短中长三档 | "只看画面"与"加字幕""加音频"三种设置差距很大，要分开报告；各模型按官方配置取不同帧数 |

**协议会翻转排名。** 四个例子。①冻结特征：DINOv2 在 K400 上高于 V-JEPA（83.4% 对 82.0%），在 SSv2 上低 20.8 个百分点。②预训练数据：ImageNet-21K 让 TimeSformer 的 K400 涨 2.2 个百分点，SSv2 不变。③输入帧数：单帧模型在 DiDeMo 检索 R1 上比 4 帧的 Frozen 高 16.4，在 SSv2-Template 上低 10.9。④模型类别：Video-MME 上直接输入多帧的图像模型 InternVL-Chat-V1.5（50.7%）高于专门的视频模型 Video-LLaVA（39.9%）。评测协议本身也在变：V-JEPA 用注意力探针（一句话：冻结主干，只训练一个用交叉注意力汇聚所有 token 的小模块）替代平均池化，K400 提高 17 个百分点、SSv2 提高 16.1 个百分点（V-JEPA Table 3），不同论文的"冻结评测"数字因此不能直接比较。

## 当前开放问题

- **怎样证明一个模型真的用了时间？** 现有证据都是间接的：SSv2 类模板任务、证书长度、只做空间注意力的对照。入口：[Revealing Single Frame Bias](../../papers/arxiv-2206.03428/README.md)、[EgoSchema](../../papers/arxiv-2308.09126/README.md)、[TimeSformer](../../papers/arxiv-2102.05095/README.md)。
- **固定 token 预算下，帧数、每帧 token 与帧的挑选怎样分配？** LLaVA-Video 给出"多帧少 token"的方向和下限；Qwen2.5-VL 改为按帧率采样并编码绝对时间。入口：[LLaVA-Video](../../papers/arxiv-2410.02713/README.md)、[Qwen2.5-VL 技术报告](../../papers/arxiv-2502.13923/README.md)、[LLM 长上下文方向](../../../llm/fields/long-context/README.md)。
- **长视频的记忆放在哪里？** 上下文里的帧 token、压缩后的特征，还是外部记忆；Video-MME 长视频档与字幕的贡献说明画面信息还没被充分利用。入口：[Video-MME](../../papers/arxiv-2405.21075/README.md)、[InternVideo2](../../papers/arxiv-2403.15377/README.md)、[Gemini 1.5](../../../llm/papers/arxiv-2403.05530/README.md)。
- **自监督视频表征能否成为行动的状态空间？** V-JEPA 的特征在 SSv2 上远强于图像模型，V-JEPA 2 用它做机器人规划；它的消融也显示只从前几帧预测后面（因果遮蔽）得到的特征更弱。入口：[V-JEPA](../../papers/arxiv-2404.08471/README.md)、[V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)、[多模态世界模型方向](../world-models/README.md)、[机器人世界模型领域页](../../../robotics-embodied/fields/world-models/README.md)。

## 阅读顺序

1. [Two-Stream](../../papers/arxiv-1406.2199/README.md) 与 [I3D](../../papers/arxiv-1705.07750/README.md)：先看清"外观一路 + 运动一路"的分工，以及 I3D Table 2 里光流与 RGB 在不同数据集上的强弱。
2. [SlowFast](../../papers/arxiv-1812.03982/README.md)：把"语义慢、运动快"写成结构，后面视频大模型的 token 分配沿用同一思想。
3. [TimeSformer](../../papers/arxiv-2102.05095/README.md)：重点看 Table 1 只做空间注意力的那一行，它是检验其他所有结论的参照。
4. [VideoMAE](../../papers/arxiv-2203.12602/README.md) 与 [V-JEPA](../../papers/arxiv-2404.08471/README.md)：同一个"遮住再预测"的思路，分别预测像素与特征，对照它们与图像模型在 K400、SSv2 上的差别。
5. [Revealing Single Frame Bias](../../papers/arxiv-2206.03428/README.md) 与 [EgoSchema](../../papers/arxiv-2308.09126/README.md)：学会怀疑 benchmark，掌握时间证书这个工具。
6. [LLaVA-Video](../../papers/arxiv-2410.02713/README.md) 与 [Video-MME](../../papers/arxiv-2405.21075/README.md)：视频大模型的 token 预算与长视频评测；读完可以做[路线图](ROADMAP.md)第 5 步的手算。

## 批注

**后继工作的阅读边界**

V-JEPA 2.1 的模型本体是表征编码器，动作规划要另外接预测器与规划程序；Qwen3-VL 的时间戳是输入表达方式，不能单独证明因果理解；InternVideo3 §5.3 与 §7 明确将更全面的视频 agent 量化留作后续。这些边界分别对应三种任务，比较时应先写出输入、输出与可用工具。

**易误读**

- 双流的 73.0%、83.7%、88.0% 是 UCF-101 三个划分的平均，空间流只训练了最后一层（Table 1a、Table 4）。I3D 的 98.0% 来自 ImageNet + Kinetics 预训练的双流 I3D（Table 5）；I3D 的 62.2% 是表中 Two-Stream 结构的 RGB 单路，原文说明它等价于对 25 帧逐帧分类再平均（Table 2 说明）。
- SlowFast 的 79.8% 不用 ImageNet 预训练，作者另报告有无 ImageNet 预训练差别在 ±0.3% 以内（§4.1）；"Slow-only 约 72.6%"是从 Table 5a 的文字推出，原文没有直接写这个数。
- TimeSformer 的 76.9% / 36.6% 与 78.0% / 59.5% 都是 ImageNet-21K 预训练、8 帧输入的 TimeSformer 在验证集上的视频级准确率（Table 1）。
- V-JEPA 与 DINOv2 的比较是冻结主干加注意力探针，不是微调（Table 6）；DINOv2 原文报告的线性探针为 78.4%，V-JEPA 作者用注意力探针重测得 83.4%（§5.2）。V-JEPA 的 ImageNet 77.4% 为 384 分辨率、单层探针，用两层探针为 77.9%。
- Lei 等的"单帧模型"只在训练时用单帧，推理时用多帧早融合；它比较的是"不建模时间的训练"，不是"只看一帧的推理"（§3、§6）。
- EgoSchema 的 76% 是人类在无约束设置下的成绩（75.0%，先看视频再读题为 76.2%）；Qwen2.5-VL 的 76.2% 是 EgoSchema test 集，两者的样本范围不同，"持平"只是量级上的对照。
- Video-MME 的 Gemini 1.5 Pro 81.7% → 67.4% 是"只看画面"设置；Qwen2.5-VL 的 768 帧与 24,576 token 是它在所有视频评测中设的上限，"平均每帧 32 个 token"是本页的除法，不是原文数字。
- LLaVA-Video Table 8 的消融只用 0–30 秒视频、只用视频数据训练（附录 C），不是主模型的设置；总 token 数 18,590 与 21,632 按原文所列，32 × 729 与 21,632 不完全一致，本页只引用原文的比较结论。

**判断的支撑论文与反例**（各行见 [synthesis.csv](synthesis.csv)）

- "Kinetics 衡量外观、SSv2 衡量时间"：I3D Sec.4 与 Table 2；TimeSformer Table 1、Table 3 与 §4.2 的说明（K400 更偏空间场景信息）；VideoMAE §4.2；V-JEPA Table 6 与 §5.2（它也引用 Sevilla-Lara 等 2021 的结论：许多 Kinetics 标签凭外观就能推断）；ViViT §4.3。反例：SlowFast 在 Kinetics 上仍比对应的 Slow-only 稳定提高 1.7–3.4 个百分点（Fig.2），说明时间在 Kinetics 上并非毫无作用。
- "帧采样技巧掩盖弱的时间推理"：SlowFast §4.1；Lei 等 §5；LLaVA-Video 附录 C（Table 8）；EgoSchema Fig.6。反例：LLaVA-Video 中从 32 帧增加到 110 帧（训练与推理同步）在四个 benchmark 上都提升，说明在动态数据上帧数确实有用。
- "token 取舍与 SlowFast 同一思想"：LLaVA-Video 附录 A.2 写明沿用 SlowFast 的思路；Qwen2.5-VL §2.1 合并相邻两帧；ViViT 管道嵌入。边界：LLaVA-Video 的帧数消融（附录 C、Table 8）只在 0–30 秒的视频上训练、只看四个 benchmark。
- "长视频记忆是共同缺口"：Video-MME Abstract 与 §4.2；InternVideo2 §5.3；EgoSchema 与 Qwen2.5-VL Table 8；生成侧见观点页对 Sora、Genie 的整理。反例：Gemini 1.5 Pro 长视频档 67.4% 仍高于多数开源模型在短视频档的成绩，说明规模化的长上下文模型可以部分弥补。
- 团队偏好："两篇以上、存在替代方案时仍重复同一选择"。Zisserman：Two-Stream §2、I3D §2.4；FAIR：SlowFast §4.1、TimeSformer Table 2；JEPA：V-JEPA §1、V-JEPA 2 卡片；Google：ViT §4.1、ViViT §4.3；王利民：VideoMAE、InternVideo2 §3.1；LLaVA 一系：LLaVA、LLaVA-Video §3。边界：FAIR 的两篇作者不重合（He、Feichtenhofer 与 Bertasius、Torresani），"FAIR 视频组"是按单位而非作者归并，证据偏弱。
- "视频生成团队的启示"：观点页阶段四表格（Sora、Wan、Seedance 1.0、HunyuanVideo、Veo 3 的官方材料）。对应关系是结构上的相似，没有原文说明理解与生成两侧互相借鉴。

**与其他论文的关联**

- VideoMAE 与 V-JEPA 是图像一侧 [MAE](../../papers/mae/README.md) 与 [DINO](../../papers/dino/README.md) 两条训练信号在视频上的延伸，图像侧的协议翻转见[视觉表征页](../visual-representation/README.md)"从测量看"。
- 视频生成的评测指标 FVD 用 I3D 的特征计算（见[观点页](../../../perspectives/generative-convergence.md)），所以 Kinetics 的外观偏差也会带进生成评测；[Video Diffusion](../../papers/video-diffusion/README.md) 是生成侧的入口。
- OpenVLA 只看单帧，π0.7 每路相机最多给 6 帧历史并以一定概率整体丢弃历史训练，RoboTTT 的对照中多给 1 帧历史使一个任务从 57% 降到 39.5%（见 [VLA 领域页](../../../robotics-embodied/fields/vla/README.md)）：机器人一侧对"给多少帧"的争论与本页第二、三个坑相通。
- [Gemini 1.5](../../../llm/papers/arxiv-2403.05530/README.md) 是 Video-MME 与 EgoSchema 上的强对照，它的长上下文做法见 LLM 长上下文方向。

**未核实 / 待验证**

- Something-Something v2 本身没有单独的论文，"约 22 万段"取自 ViViT §4.1 的描述；Kinetics 数据集论文（Kay 等 2017）没有打开，Kinetics 的数字取自 I3D §3。
- Karpathy 等（2014）与 Sevilla-Lara 等（2021）没有打开原文，本页只引用双流、TimeSformer、V-JEPA 对它们的转述。
- Lei 等论文后来的正式发表版本没有核对，本页按 arXiv v1。Video-MME 按 2025 年 5 月的 v3，v1 的表格与模型列表可能不同。
- I3D 计划公开的模型、Something-Something 数据集和 Video-MME 数据的实际发布与许可没有另查。
