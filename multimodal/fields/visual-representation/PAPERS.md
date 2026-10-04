# 视觉表征论文目录

[入门页](README.md) · [Baseline](BASELINES.md) · [路线图](ROADMAP.md)

按[入门页](README.md)主线历史的阶段排列。有单篇目录的链接到目录；没有的链接到原文，并注明"无单篇目录"，它们的原文摘录在 [synthesis.csv](synthesis.csv) 中。"格"指它在 [Baseline 表](BASELINES.md)中的行。跨方向的论文只列与本方向相关的那一面，不重复计数。

## 0 起点：手工特征（1980–2010）

- [Neocognitron](https://www.cs.princeton.edu/courses/archive/spr08/cos598B/Readings/Fukushima1980.pdf) · 1980 · NHK 放送科学基础研究所 · 无单篇目录 · 格：原点之前（交替的特征提取层与池化层）
- [Gradient-Based Learning Applied to Document Recognition](https://leon.bottou.org/papers/lecun-98h)（LeNet） · 1998 · 无单篇目录，原文未核实（只核对了题录） · 格：原点之前（卷积加梯度训练）
- [Histograms of Oriented Gradients for Human Detection](../../papers/hog/README.md)（HOG） · 2005 · INRIA · 文献卡 · 格：原点（手工特征 + 线性 SVM）
- [Object Detection with Discriminatively Trained Part Based Models](https://cs.brown.edu/people/pfelzens/papers/lsvm-pami.pdf)（DPM） · 2010 · University of Chicago 等 · 无单篇目录 · 格：原点（可变形部件）

## 1 ImageNet 与 AlexNet（2009–2014）

- [ImageNet: A Large-Scale Hierarchical Image Database](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf) · 2009 · Princeton · 无单篇目录 · 格：数据 = 百万级标注图像
- [ImageNet Classification with Deep Convolutional Neural Networks](../../papers/alexnet/README.md)（AlexNet） · 2012 · University of Toronto · 文献卡 · 格：训练信号 = 人工标签 + 深层 CNN
- [Visualizing and Understanding Convolutional Networks](https://arxiv.org/abs/1311.2901) · 2013 · NYU · 无单篇目录 · 格：评测协议 = 诊断工具（入门页"从内部看"）
- [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575)（ILSVRC 综述） · 2014 · Stanford 等 · 无单篇目录 · 格：数据 = 年度竞赛

## 2 预训练加微调（2013–2014）

- [Rich feature hierarchies for accurate object detection and semantic segmentation](https://arxiv.org/abs/1311.2524)（R-CNN） · 2013 · UC Berkeley · 无单篇目录 · 格：读出接口 = 检测数据上微调整个主干
- [Deformable Part Models are Convolutional Neural Networks](https://arxiv.org/abs/1409.5403) · 2014 · UC Berkeley · 无单篇目录 · 格：读出接口（DPM 展开为 CNN）

## 3 CNN 内部加深（2014–2019）

- [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)（VGG） · 2014 · Oxford · 无单篇目录 · 格：架构 = 3×3 卷积堆深
- [Going Deeper with Convolutions](https://arxiv.org/abs/1409.4842)（GoogLeNet） · 2014 · Google · 无单篇目录 · 格：架构 = Inception 模块
- [Deep Residual Learning for Image Recognition](../../papers/arxiv-1512.03385/README.md)（ResNet） · 2015 · Microsoft Research · 文献卡 · 格：架构 = 残差连接；第一个基线
- [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597) · 2015 · University of Freiburg · 无单篇目录 · 格：架构 = 编码–解码 + 跨层拼接
- [You Only Look Once: Unified, Real-Time Object Detection](../../../robotics-embodied/papers/arxiv-1506.02640/README.md)（YOLO） · 2015 · University of Washington 等 · 文献卡（主页面在[机器人感知方向](../../../robotics-embodied/fields/perception/README.md)） · 格：架构 = 面向端侧
- [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861) · 2017 · Google · 无单篇目录 · 格：架构 = 面向端侧
- [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946) · 2019 · Google Research · 无单篇目录 · 格：架构 = 面向端侧

## 4 拿掉标签：对比学习（2019–2020）

- [Momentum Contrast for Unsupervised Visual Representation Learning](../../papers/arxiv-1911.05722/README.md)（MoCo） · 2019 · FAIR · 文献卡 · 格：训练信号 = 对比学习（队列 + 动量编码器）
- [A Simple Framework for Contrastive Learning of Visual Representations](../../papers/arxiv-2002.05709/README.md)（SimCLR） · 2020 · Google Research · 文献卡 · 格：训练信号 = 对比学习（大批量 + 投影头）

## 5 ViT 与它的配方（2020–2021）

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../../papers/vit/README.md)（ViT） · 2020 · Google Research · 逐步教学版精读 · 格：架构 = 切块 Transformer；数据 = JFT-300M；第二个基线的结构
- [Training data-efficient image transformers & distillation through attention](../../papers/arxiv-2012.12877/README.md)（DeiT） · 2020 · Facebook AI、Sorbonne · 文献卡 · 格：训练配方 = 强增强与正则 + 蒸馏 token
- [How to train your ViT? Data, Augmentation, and Regularization in Vision Transformers](../../papers/arxiv-2106.10270/README.md)（AugReg） · 2021 · Google Research · 文献卡 · 格：数据 = ImageNet-21K；训练配方 = 系统扫描

## 6 对 ViT 的四种回答（2021–2022）

- [Learning Transferable Visual Models From Natural Language Supervision](../../papers/clip/README.md)（CLIP） · 2021 · OpenAI · 逐步教学版精读（主页面在[图文对齐方向](../alignment/README.md)） · 格：训练信号与数据 = 图文对比；第三个基线之一
- [Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision](../../papers/arxiv-2102.05918/README.md)（ALIGN） · 2021 · Google Research · 文献卡（主页面在图文对齐方向） · 格：数据 = 18 亿噪声图文对
- [Emerging Properties in Self-Supervised Vision Transformers](../../papers/dino/README.md)（DINO） · 2021 · FAIR、Inria · 技术精读 · 格：训练信号 = 自蒸馏
- [BEiT: BERT Pre-Training of Image Transformers](../../papers/arxiv-2106.08254/README.md) · 2021 · 哈尔滨工业大学、Microsoft Research · 文献卡 · 格：训练信号 = 遮蔽预测离散视觉 token
- [Masked Autoencoders Are Scalable Vision Learners](../../papers/mae/README.md)（MAE） · 2021 · FAIR · 技术精读 · 格：训练信号 = 遮蔽重建像素
- [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)（ConvNeXt） · 2022 · FAIR、UC Berkeley · 无单篇目录 · 格：架构 = 现代化 CNN；训练配方 = Transformer 式配方

## 7 DINOv2 与冻结即用（2023）

- [Sigmoid Loss for Language Image Pre-Training](../../papers/arxiv-2303.15343/README.md)（SigLIP） · 2023 · Google DeepMind · 文献卡（主页面在图文对齐方向） · 格：训练信号 = 逐对 sigmoid
- [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](../../papers/arxiv-2301.08243/README.md)（I-JEPA） · 2023 · Meta FAIR 等 · 文献卡 · 格：训练信号 = 表示空间预测
- [DINOv2: Learning Robust Visual Features without Supervision](../../papers/arxiv-2304.07193/README.md) · 2023 · Meta AI Research、Inria · 文献卡 · 格：训练信号、数据、训练配方各一行；第三个基线之一
- [Vision Transformers Need Registers](../../papers/arxiv-2309.16588/README.md) · 2023 · Meta FAIR、Inria · 文献卡 · 格：架构 = 寄存器 token

## 8 DINOv2 之后：做 VLM 的眼睛与密集特征（2024–2026，入门页主线尚未展开）

- [Eyes Wide Shut? Exploring the Visual Shortcomings of Multimodal LLMs](../../papers/arxiv-2401.06209/README.md)（MMVP） · 2024 · NYU、Meta FAIR、UC Berkeley · 文献卡（主页面在图文对齐方向） · 格：评测协议 = CLIP 盲对
- [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](../../papers/arxiv-2406.16860/README.md) · 2024 · NYU · 文献卡（主页面在 [VLM 方向](../vlm/README.md)） · 格：评测协议 = 以问答比较视觉骨干
- [SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](../../papers/arxiv-2502.14786/README.md) · 2025 · Google DeepMind · 文献卡（主页面在图文对齐方向） · 格：训练信号 = 对比 + 描述与定位 + 自蒸馏
- [Scaling Language-Free Visual Representation Learning](../../papers/arxiv-2504.01017/README.md)（Web-SSL） · 2025 · Meta FAIR、NYU · 文献卡 · 格：数据 = 与 CLIP 同数据；评测协议 = 问答
- [Perception Encoder: The best visual embeddings are not at the output of the network](../../papers/arxiv-2504.13181/README.md) · 2025 · Meta FAIR · 文献卡 · 格：读出接口 = 中间层 + 对齐；训练配方 = 强化的对比配方
- [DINOv3](../../papers/arxiv-2508.10104/README.md) · 2025 · Meta AI Research · 文献卡 · 格：训练信号 = Gram anchoring；数据 = LVD-1689M
- [C-RADIOv4 (Tech Report)](https://arxiv.org/abs/2601.17237) · 2026 · NVIDIA · 无单篇目录，只核对了摘要与 Table 1 · 格：训练信号 = 多教师蒸馏（SigLIP 2、DINOv3、SAM 3）
- [V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482) · 2026 · Meta FAIR · 无单篇目录，只核对了摘要与 Fig.2 · 格：训练信号 = 密集预测损失 + 多层自监督
- [RADIO1D: Elastic Representations for Condensed Vision Modeling](https://arxiv.org/abs/2607.03624) · 2026 · NVIDIA · 无单篇目录，只核对了摘要与 Fig.1 · 格：读出接口 = 可变长 1D token

## 表征分析与诊断（跨阶段）

- [ImageNet-trained CNNs are biased towards texture; increasing shape bias improves accuracy and robustness](https://arxiv.org/abs/1811.12231) · 2019 · University of Tübingen · 无单篇目录 · 格：评测协议 = 线索冲突诊断
- [Similarity of Neural Network Representations Revisited](https://arxiv.org/abs/1905.00414)（CKA） · 2019 · Google Brain · 无单篇目录 · 格：评测协议 = 表示相似度
- [Do Vision Transformers See Like Convolutional Neural Networks?](https://arxiv.org/abs/2108.08810) · 2021 · Google Research · 无单篇目录 · 格：评测协议 = CKA、注意力距离与探针

## 跨方向交叉引用（归属其他方向，在此不展开）

- [VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](../../papers/arxiv-2203.12602/README.md) · 2022 · 文献卡（[视频与时序方向](../video-temporal/README.md)） · 格：训练信号（视频）= 管道遮蔽重建
- [Revisiting Feature Prediction for Learning Visual Representations from Video](../../papers/arxiv-2404.08471/README.md)（V-JEPA） · 2024 · 文献卡（视频与时序方向） · 格：训练信号（视频）= 特征预测
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](../../../robotics-embodied/papers/arxiv-2506.09985/README.md) · 2025 · 文献卡（机器人侧世界模型方向） · I-JEPA 一支在机器人规划上的延伸
- [Visual Instruction Tuning](../../papers/llava/README.md)（LLaVA） · 2023 · 技术精读（VLM 方向） · 格：读出接口 = 倒数第二层网格特征
- [OpenVLA 精读](../../../robotics-embodied/papers/openvla/reading.md) · 2024 · 技术精读（[VLA 方向](../../../robotics-embodied/fields/vla/README.md)） · 格：读出接口 = 两种编码器拼接并微调
- [DINO-WM](../../papers/arxiv-2411.04983/README.md)、[Back to the Features](../../papers/arxiv-2507.19468/README.md)、[Reconstruction or Semantics?](../../papers/arxiv-2605.06388/README.md) · 2024–2026 · 文献卡（[世界模型方向](../world-models/README.md)） · 格：读出接口 = 冻结特征作为世界模型状态空间
- [Depth Anything](../../../robotics-embodied/papers/arxiv-2401.10891/README.md) · 2024 · 文献卡（机器人感知方向） · 用 DINOv2 特征对齐损失训练深度模型，是冻结大编码器在几何任务上的下游
