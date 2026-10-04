# 视频与时序表征的基线

> 状态：Baseline 页 · v2

[入门页](README.md) · [路线图](ROADMAP.md) · [论文目录](PAPERS.md)

## 基线是谁、为什么是它

结论：本方向有两个基线。I3D 定义了 2017–2021 年视频表征的实验骨架（在 Kinetics 上训练片段分类器、多视图测试、再迁移到小数据集）；Video-LLaVA 与 LLaVA-Video 式的"逐帧图像编码 + 投影 + 语言模型"定义了 2023 年以后视频大模型的骨架。

| 基线 | 定义了什么 | 为什么后来者拿它当参照 |
|---|---|---|
| [I3D](../../papers/arxiv-1705.07750/README.md)（2017，DeepMind 与 Oxford），前身是 [Two-Stream](../../papers/arxiv-1406.2199/README.md)（2014） | 接口：一个固定长度的片段（I3D 训练用 64 帧、25 帧/秒）→ 一个动作类别。结构：ImageNet 2D 网络膨胀成 3D 卷积，RGB 与光流两路。训练与评测：Kinetics 预训练，再在 UCF-101、HMDB-51 上微调；测试时多片段、多裁剪取平均 | SlowFast、TimeSformer 在同一 Kinetics 协议下以它为对照（TimeSformer Table 2 直接比较训练 GPU 小时）；VideoMAE、ViViT 的 3D 块嵌入沿用"把 2D 权重沿时间扩展"的初始化思路并与之比较；视频生成的 FVD 指标用 I3D 特征计算 |
| [Video-LLaVA](../../papers/arxiv-2311.10122/README.md)（2023，北京大学）与 [LLaVA-Video](../../papers/arxiv-2410.02713/README.md)（2024，ByteDance 与 NTU） | 接口：若干帧 + 一句问题 → 一段文字回答。结构：每帧用图像编码器（LanguageBind 或 SigLIP）编码，经一个小投影层变成 token，按时间顺序排进语言模型。训练：图像与视频指令数据混合。评测：零样本多选题与 GPT 打分的开放式问答 | Video-MME 把 Video-LLaVA 列为代表性开源视频模型；LLaVA-Video 在同一结构上只改数据与 token 分配；Qwen2.5-VL 在同一骨架上改帧率采样与时间位置编码 |

## 基线的结构拆分

结论：一个视频模型可以拆成六个可替换的部件；两个基线的差别集中在"时间算子"和"每帧表示"两格：前者在网络内部建模时间，后者把时间交给语言模型的注意力。

| 部件 | 含义 | 片段分类基线（I3D） | 视频大模型基线（Video-LLaVA / LLaVA-Video） |
|---|---|---|---|
| 帧采样 | 取哪些帧、多密、测试时取几次 | 训练 64 帧连续片段；测试处理全部帧（I3D §5）；同类方法普遍用多片段 × 多裁剪 | Video-LLaVA 每段均匀取 8 帧；LLaVA-Video 主模型 64 帧 |
| 时间算子 | 帧与帧之间在哪里、用什么交换信息 | 3D 卷积（时间维的卷积核）+ 预计算光流一路 | 网络内部不建模时间，逐帧独立编码，由语言模型的注意力读帧序列 |
| 每帧表示与 token 预算 | 每帧变成多少数，总量受什么限制 | 卷积特征图，最后池化成一个向量 | 每帧数百个 token；帧数 × 每帧 token 数受语言模型上下文与显存限制 |
| 预训练信号 | 主干的权重从哪里学来 | ImageNet 初始化 + Kinetics 动作标签 | 已与语言对齐的图像（或视频）编码器 + GPT 合成的指令数据 |
| 数据 | 训练用什么视频 | Kinetics：400 类、约 24 万段、每段约 10 秒、已裁剪 | 图像指令数据 + 视频指令数据（LLaVA-Video-178K：178,510 段 0–3 分钟视频） |
| 评测协议 | 好坏怎样定义 | 微调后 top-1 准确率 | 零样本多选准确率；开放式问答用 GPT 打分 |

部件之间有依赖：时间算子越重（3D 卷积、全时空注意力），能放进去的帧越少（TimeSformer 受显存限制最多 96 帧）；时间交给语言模型之后，帧数与每帧 token 数直接争夺同一个上下文；评测协议又决定了哪个部件看起来重要（Kinetics 上换更大的图像预训练比改时间算子收益更大，SSv2 上相反）。

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| 时间算子 | 预计算光流作为第二路输入，晚融合 | [Two-Stream](../../papers/arxiv-1406.2199/README.md) | UCF-101 88.0%，追平手工特征；代价：光流要预先算，只看单帧的空间流就有 73.0%，数据集偏外观 |
| 时间算子 | 2D 网络膨胀成 3D 卷积，保留光流路 | [I3D](../../papers/arxiv-1705.07750/README.md)（基线） | Kinetics 74.2%，迁移后 UCF-101 98.0%；代价：Kinetics 上光流单路（63.4%）弱于 RGB 单路（71.1%） |
| 时间算子 | 双速率：低帧率宽通道 + 高帧率窄通道，侧向连接 | [SlowFast](../../papers/arxiv-1812.03982/README.md) | 不用光流，K400 79.8%，AVA 19.0 → 24.2 mAP；代价：Kinetics 上增益只有 1.7–3.4 个百分点，仍用 30 视图测试 |
| 时间算子 | 时空自注意力，空间与时间分开算 | [TimeSformer](../../papers/arxiv-2102.05095/README.md) | 训练 416 V100 小时达 75.8%（SlowFast 3840 小时 75.6%），可读 96 帧；代价：离不开图像预训练（从零 64.8%），SSv2 上需要大量数据 |
| 时间算子 / 帧采样 | 时空管道切块；四种空间/时间分解，包括"先逐帧编码、再时间编码" | [ViViT](../../papers/arxiv-2103.15691/README.md) | K400 80.0%（JFT 版 84.9%）；代价：依赖非公开 JFT，SSv2 上细粒度运动仍是短板 |
| 预训练信号 | 管道遮蔽、90%–95% 遮蔽率，重建像素 | [VideoMAE](../../papers/arxiv-2203.12602/README.md) | 不用图像预训练，ViT-B SSv2 69.6%，3.5k 段视频也能训练；代价：跨数据集迁移受域偏移影响 |
| 预训练信号 / 评测协议 | 在特征空间预测被遮的时空块；冻结主干 + 注意力探针评测 | [V-JEPA](../../papers/arxiv-2404.08471/README.md)；后续 [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) 加动作条件预测器 | 冻结评测 SSv2 71.4%，比图像模型高 20 个百分点以上；代价：K400 与 ImageNet 上不如 DINOv2 |
| 预训练信号 / 数据 | 未遮 token 对齐两个教师 → 视频-音频-语音-文本对比 → 接语言模型；6B 编码器 | [InternVideo2](../../papers/arxiv-2403.15377/README.md) | K400 92.1%、SSv2 77.5%；代价：无新结构，编码器只看 8 帧，EgoSchema 60.0% 不及 Gemini 1.5 Pro |
| 每帧表示 / 预训练信号 | 图像与视频编码器预先对齐到语言空间，共用投影层，图像视频联合训练 | [Video-LLaVA](../../papers/arxiv-2311.10122/README.md)（基线） | 联合训练使 MSVD-QA 64.8% → 70.7%；代价：只取 8 帧，长视频丢细节；Video-MME 39.9% |
| 数据 / 每帧表示 | 1 fps 稠密采样、GPT-4o 合成动态视频的指令数据；慢帧多 token、快帧少 token | [LLaVA-Video](../../papers/arxiv-2410.02713/README.md)（基线） | 72B 版 Video-MME 70.5%；"多帧少 token"在总 token 更少时更好；代价：440 帧 × 64 token 开始下降，推理帧数远多于训练时会掉分 |
| 帧采样 / 时间位置 | 动态帧率采样；位置编码的时间维对齐绝对时间；相邻两帧合并 | [Qwen2.5-VL 技术报告](../../papers/arxiv-2502.13923/README.md) | Video-MME 73.3%、LVBench 47.3%、Charades-STA mIoU 50.9；代价：每段最多 768 帧、24,576 个视频 token，训练视频数据规模未公开 |
| 时间算子（反向检验） | 只用单帧训练，推理时多帧早融合 | [Revealing Single Frame Bias](../../papers/arxiv-2206.03428/README.md) | 在多个视频-文本 benchmark 上达到最好，揭示静态外观偏差；代价：SSv2-Template 检索比 4 帧模型低 10.9（R1） |
| 评测协议 | 用模板与"假装"动作采集，迫使模型看物体状态变化 | [Something-Something](../../papers/arxiv-1706.04261/README.md) | 成为检验时间建模的标准数据集；代价：标签有歧义，需报告 top-K |
| 评测协议 | 时间证书长度；语言模型过滤可盲答的题；三分钟第一人称视频 | [EgoSchema](../../papers/arxiv-2308.09126/README.md) | 发布时模型不到 33%、人类约 76%；代价：题目由 LLM 依据旁白生成，2025 年已有模型与人类成绩持平 |
| 评测协议 | 11 秒到 1 小时三档时长，可加字幕与音频，人工标注 | [Video-MME](../../papers/arxiv-2405.21075/README.md) | 量化了"随时长掉分"（Gemini 1.5 Pro 短 81.7% → 长 67.4%）；代价：各模型帧数不统一，三种模态设置要分开报告 |

生成方向的视频模型在同样几个部件上做了对应的选择（时间压缩、空间与时间分层），见[入门页](README.md)"视频生成团队对时间建模的启示"一段与[视觉生成方向](../generation/README.md)。

## 2025–2026 后继部件

| 部件 | 旧问题 → 新机制 | 代表 | 证据边界 |
|---|---|---|---|
| 预训练信号与局部读出 | 全局表征强但局部约束不足 → 图像/视频规模化后增加密集、多层预测 | [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) → [V-JEPA 2.1](../../papers/arxiv-2603.14482/README.md) | 表征评测、动作条件预测器与机器人规划分开 |
| 时间位置 | 绝对时间编号外推难 → 文字时间戳与交错时空位置编码 | [Qwen3-VL](../../papers/arxiv-2511.21631/README.md) | 时间表达改善，帧采样遗漏仍存在 |
| 缓存与执行 | 长视频和工具记录昂贵 → 保留token的缓存压缩与迭代取证 | [InternVideo3](../../papers/arxiv-2606.12195/README.md) | GQA转换路线有架构边界；视频agent主要为定性案例 |

## 批注

**易误读**

- I3D 的 74.2% 是 ImageNet 初始化后在 Kinetics 上训练的双流 I3D；不用 ImageNet 初始化为 71.6%（I3D Table 3）。
- SlowFast 的 79.8% 与 TimeSformer 的 78.0% 用的是不同的视图数与预训练（前者 30 视图、无 ImageNet；后者 3 个空间裁剪、ImageNet-21K），表中数字只用于说明各篇自己的改进幅度。
- InternVideo2 的 92.1% 是 6B 模型、16 帧输入的端到端微调结果；EgoSchema 60.0% 是接入 VideoChat2-HD 之后的对话模型（InternVideo2 Table 2、Table 14）。
- Qwen2.5-VL 与 LLaVA-Video 的 Video-MME 分数都是"不加字幕"设置；两者取帧数不同（768 帧上限对 64 帧）。

**与其他论文的关联**

- "逐帧图像编码 + 投影 + 语言模型"来自图像一侧的 [LLaVA](../../papers/llava/README.md)，见[视觉语言模型方向](../vlm/README.md)。
- VideoMAE、V-JEPA 的训练信号对应图像一侧的 [MAE](../../papers/mae/README.md) 与 [DINO](../../papers/dino/README.md)，见[视觉表征方向](../visual-representation/README.md)的方法谱系。
- 机器人策略要决定给多少帧历史，见 [VLA 领域页](../../../robotics-embodied/fields/vla/README.md)。

**未核实 / 待验证**

- LLaVA-Video 主模型配置中每帧 token 数的写法（论文正文给出的元组与附录的 729 不一致），本页没有引用主模型的每帧 token 数。
