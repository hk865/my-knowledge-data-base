# 世界模型（多模态侧）的基线

[回到入门](README.md) · [阅读路线](ROADMAP.md) · [全部文献](PAPERS.md) · [机器人侧的基线](../../../robotics-embodied/fields/world-models/BASELINES.md)

## 基线是谁、为什么是它

- **[World Models](../../../robotics-embodied/papers/arxiv-1803.10122/README.md)（Ha 与 Schmidhuber，2018）。** 它定义了"学到的世界模型"最早的完整接口：V（VAE，把每帧压成潜变量）+ M（MDN-RNN，按动作预测下一步潜变量的分布）+ C（控制器）。输入是像素与环境动作，输出是下一步的潜变量（可解码回像素），评估看在模型里训练出的控制器回到真实环境的得分。后来以控制为目标的世界模型（Dreamer 一线、DIAMOND）都在替换它的部件。
- **[Genie](../../papers/arxiv-2402.15391/README.md)（Google DeepMind，2024）。** 它定义了视频生成一侧的接口：只用无标注网络视频，视频分词器把帧压成离散 token，潜在动作模型从相邻帧推出一个离散动作，动力学模型按"过去 token + 动作"生成下一帧；评估同时看画质（FVD）与可控性（ΔtPSNR）。之后的可交互世界模型（GameNGen、Genie 2/3、Cosmos）在替换它的生成过程、动作接口与记忆。

两条基线对应入门页"从任务看"中"在模型里训练智能体"和"可玩的交互环境"两类用途。以机器人规划、评估为目标的工作，拆分在[机器人侧的基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)（以 DreamerV3 与 DINO-WM 为基线）。

## 基线的结构拆分

| 部件 | World Models | Genie |
|---|---|---|
| ① 状态表示 | 单帧 VAE 的连续潜变量（32 或 64 维），单独训练 | 时空 Transformer 视频分词器的离散 token |
| ② 动力学与生成过程 | MDN-RNN，输出混合高斯，按温度 τ 采样 | MaskGIT 式掩码预测，逐帧生成 token 再解码 |
| ③ 动作接口 | 环境定义的真实动作 | 无监督学出的 8 个潜在动作 |
| ④ 记忆与上下文 | LSTM 隐状态 | 16 帧 |
| ⑤ 数据 | 随机策略在单个环境里采集 | 3 万小时网络 2D 平台游戏视频（从 20 万小时筛出）、机器人视频 |
| ⑥ 评估 | 控制器在真实环境的得分 | FVD（画质）、ΔtPSNR（可控性）、CoinRun 上的行为克隆 |

## 后续工作在改哪个部件

| 部件 | 改法 | 代表论文 | 改进了什么 / 付出了什么 |
|---|---|---|---|
| ①② | 编码、动力学、奖励联合训练的 RSSM，离散随机潜变量，固定超参 | [DreamerV3](../../papers/dreamerv3/reading.md) | 150 多个任务一套配置；保留哪些细节仍靠调表示正则，每任务单独训练 |
| ① | 对象槽，预测激光雷达深度而不是光流 | [SAVi++](../../papers/arxiv-2206.07764/README.md) | 真实驾驶视频上涌现分割与跟踪；要首帧框与深度监督，物体再出现未建模 |
| ①② | 在对象槽上用 Transformer 自回归 | [SlotFormer](../../papers/arxiv-2210.05861/README.md) | 长时物体动力学好，可做物理问答与规划；只在合成数据上，确定性 |
| ①②③ | 视频、文本、动作统一成 token，自回归 + 视频扩散解码器；分词器回归 DINO 特征 | [GAIA-1](../../papers/arxiv-2309.17080/README.md) | 驾驶场景可用文字与动作编辑，拟合出规模定律；不能实时，评测定性 |
| ① | 3D 占据栅格的 token，同时预测自车轨迹 | [OccWorld](../../papers/arxiv-2311.16038/README.md) | 不用框与地图监督也能规划；新进入的车辆预测不出，长时规划变差 |
| ①③ | BEV 记忆 + 占据与流预测，速度、转向、轨迹等动作条件，接规划 | [Drive-OccWorld](../../papers/arxiv-2408.14197/README.md) | 可控的 4D 占据生成用于端到端规划（只核对了摘要） |
| ②④ | 时空 patch 上的扩散 Transformer，一次生成整段，无逐帧动作 | [Sora 技术报告](../../papers/sora-tech-report/README.md) | 一分钟高清、涌现 3D 一致；物理与长时一致自述不足 |
| ① + ② | 不压成离散潜变量，EDM 扩散逐帧生成像素 | [DIAMOND](../../papers/arxiv-2405.12399/README.md) | Atari 100k 1.46，小细节保真；帧堆叠记忆短 |
| ②④ | 改造 Stable Diffusion，64 帧上下文 + 噪声增广抗漂移 + 解码器微调 | [GameNGen](../../papers/arxiv-2408.14837/README.md) | 20 帧/秒实时 DOOM；3 秒记忆，只能模拟一个游戏 |
| ②③ | 自回归潜空间扩散 + 无分类器引导增强动作可控性，3D 键鼠操作 | [Genie 2](../../papers/genie-2-blog/README.md) | 一致约一分钟；实时版本需蒸馏、画质下降 |
| ②③④ | 文本生成世界，实时 720p，可提示的世界事件 | [Genie 3](../../papers/genie-3-blog/README.md) | 视觉记忆约一分钟、数分钟一致；动作空间有限，文字难以生成 |
| ⑤ + ② | 2000 万小时原始视频筛选，扩散与自回归两套开放权重底座，可后训练加相机与动作条件 | [Cosmos](../../papers/arxiv-2501.03575/README.md) | 开放的通用底座；物体永久性与接触动力学不足 |
| ① | 在自监督表征空间预测，不解码像素；动作条件后训练 | [V-JEPA 2](../../../robotics-embodied/papers/arxiv-2506.09985/README.md)、[DINO-world](../../papers/arxiv-2507.19468/README.md) | 规划快；目标只能是图像，对相机位置敏感 |
| ⑥ | 真实拍摄续写，四项时空指标 | [Physics-IQ](../../papers/arxiv-2501.09038/README.md) | 证明视觉真实感与物理理解不相关；只测续写 |
| ⑥ | 文本描述 + 人工判物理常识，自动评估器 | [VideoPhy](../../papers/arxiv-2406.03520/README.md) | 覆盖材料交互；人工评测有文化偏差 |
| ⑥ + ⑤ | 合成物理规律，分布内、分布外、组合泛化分开测 | [PhyWorld](../../papers/arxiv-2411.02385/README.md) | 揭示案例式泛化与属性优先级；只在 2D 简单场景 |
| ⑥ | 综述驾驶世界模型的生成、规划与评测 | [驾驶世界模型综述](../../papers/arxiv-2501.11260/README.md) | 列出时序记忆、安全验证等开放问题 |
| ①②⑤ | 因果视频分词器 + Transformer 动力学；shortcut forcing 支持少步、带噪历史生成 | [Dreamer 4](../../papers/arxiv-2509.24527/README.md) | 连接离线视频模型与想象强化学习；证据来自 Minecraft 离线协议 |
| ②③⑤ | 统一多种视频生成条件、视频奖励后训练；空间控制支路做外观转移 | [Cosmos-Predict2.5 / Transfer2.5](../../papers/arxiv-2511.00062/README.md) | 控制性与领域适配增强；奖励/偏好不直接测通用物理准确性 |
| ①②③ | AR 推理与扩散生成双流；以加噪对象统一正向动力学、逆动力学与策略 | [Cosmos 3](../../papers/arxiv-2606.02800/README.md) | 共用多模态接口；最终作用仍须在各具身平台和任务上检验 |

以机器人操作为对象的部件改法（冻结 DINOv2 特征规划、潜在动作、物理参数、掩码中间表示、动作可执行性奖励等）见[机器人侧的基线页](../../../robotics-embodied/fields/world-models/BASELINES.md)。

## 批注

**易误读**

- World Models 与 Genie 不是同一问题的前后两版：前者为控制而学模型，后者为生成可交互环境而学模型。本页把它们并列为基线，是因为后续工作分别继承了两者的接口，DIAMOND 处在两者的交汇处（为控制而学，却用了生成一侧的扩散）。
- 表中数字的口径见[入门页](README.md)批注与 [synthesis.csv](synthesis.csv)。

**未核实**

- Drive-OccWorld、DINO-world 只核对了 arXiv 摘要；驾驶综述只核对了摘要与部分结论段。
