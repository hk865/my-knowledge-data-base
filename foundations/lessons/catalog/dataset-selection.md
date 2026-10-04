# 十五个代表数据集的选型目录

[数据模块目录](../04-data-and-datasets.md)


以下共 15 个代表项，包括配套模块中的图像、文本与IMU三个实验。形状是进入模型前的建议接口，不保证与下载文件逐字节一致。loss 为本讲义建议，官方 benchmark 的评价协议应单独遵循。

### 图像里的类别 位置与像素

**1 CIFAR-10。** 用 `[3,32,32]→类别` 建立最小闭环；CE 配 accuracy。保留官方划分，检查重复图；见[图像实践](../modules/data/03-classification-labs.md)。它的低分辨率不代表实际相机难度。

**2 ImageNet ILSVRC2012。** 用 `[3,H,W]→1000类` 学分类/迁移学习；固定 resize/crop 后可形成 `[3,224,224]`，224 是预处理选择。CE 配 top-1/top-5。本阶段宜冻结预训练骨干练分类头；不建议先从头训全量。[官方入口](https://www.image-net.org/download.php)列出下载及非商业研究/教育访问条件，部分获取需要登录或申请。

**3 COCO。** 用图像配 `boxes[N,4]`、`classes[N]`、实例 mask 或 captions；检测通常联合分类与框回归，分割可用 BCE/CE 加 Dice，caption 是 token CE。训练按 image ID 分组，同图的多个标注不能分到两边。框原格式是像素 `[x,y,width,height]`，不是右下角坐标；类别 ID 映射需显式保存。看 AP 或任务官方指标，不能只看分类 accuracy。[官方格式](https://github.com/cocodataset/cocodataset.github.io/blob/master/dataset/format-data.htm)与[使用条款](https://github.com/cocodataset/cocodataset.github.io/blob/master/dataset/termsofuse.htm)说明：标注 CC BY 4.0，图像权利另按来源处理。

### 文本里的类别 下一个词与答案位置

**4 IMDb。** `ids[L]→正/负`，CE 配 accuracy/F1；按影评分组，词表只由训练集拟合，见[文本实践](../modules/data/03-classification-labs.md)。电影影评上的情感判断不能直接当机器人指令理解。

**5 WikiText-2。** 文本块 `ids[L]→next_ids[L]`，带因果遮罩和 padding mask，token CE 配 perplexity；保留官方 train/validation/test，文章段落不得跨集合。选择 raw 还是已分词版本会改变任务。[Salesforce 数据卡](https://huggingface.co/datasets/Salesforce/wikitext)确认版本与字段，但许可证标签写 CC BY-SA 3.0/GFDL、正文写 4.0，存在不一致，实际使用前核实所选版本，不擅自合并成一个结论。

**6 SQuAD 2.0。** 输入问题与上下文，标签为答案 span 及是否不可回答；先做起止位置 CE 和无答案判定，而非完整聊天系统。文本字符偏移必须映射到 token；截断后消失的答案不能标成任意位置。按文章/段落防泄漏，以官方 EM/F1 评价；测试标签不公开。[官方页](https://rajpurkar.github.io/SQuAD-explorer/)提供训练、开发集及 CC BY-SA 4.0 说明。

### 运动估计里的传感器 真值与参考系

**7 EuRoC。** `[L,6]` 或双目加 IMU 可做局部运动回归/VIO；位移 Huber 加旋转几何误差是可能设计。按序列/环境划分，真值覆盖、外参和同步先检查，见[IMU实践](../modules/data/04-imu-lab.md)。

**8 TUM VI。** 双目图像和六轴 IMU，可用于 VIO、光度/惯性一致性及有真值区间的监督。官方数据相机20Hz、IMU200Hz，图像有16位强度版本。room 序列全程有真值，多数其他序列仅首尾有；中间不能硬插成“真值标签”。按场景/序列划分，轨迹评价限 GT 有效部分，数据 CC BY 4.0。[官方说明](https://cvg.cit.tum.de/data/datasets/visual-inertial-dataset)

**9 KITTI。** 车载图像、LiDAR 与定位信息适合视觉/激光里程计、深度和检测，但这是多个子任务集合。[odometry](https://www.cvlibs.net/datasets/kitti/eval_odometry.php)中的相邻图像/点云可对应相对位姿监督；需要 IMU/OXTS 时要核对 [raw data](https://www.cvlibs.net/datasets/kitti/raw_data.php)，不能假设 odometry 压缩包就是高频 IMU 数据。按 drive/路线划分，坐标外参遵循所选包；评价用相应 benchmark。官网标为 [CC BY-NC-SA 3.0](https://www.cvlibs.net/datasets/kitti/index.php)。

**10 RoNIN。** 手机惯性窗可做人体平面速度/位移和朝向学习，常用速度 MSE/Huber，最终评价轨迹误差。GT 跟踪手机绑在身体上，采集 IMU 的另一台手机可自由手持，标签不等于手持手机自身轨迹。按人、设备、序列组织测试，区分 seen/unseen subjects。[官方页](https://ronin.cs.sfu.ca/)限定研究用途；[README](https://ronin.cs.sfu.ca/README.txt)写公开327序列、同步数据200Hz，并明确 `ekf_ori` 不应在测试使用，不能把可读取字段都当可用输入。

**11 OxIOD。** 即 Oxford Inertial Odometry Dataset，不是本目录之外另一个“Oxford惯性数据集”。手机惯性窗配姿态/位置，可做行人局部运动回归，先选 Huber；按人、携带方式、手机和完整轨迹检查泛化。158序列、多种携带方式是论文描述，不代表每种组合数量均衡。[官方入口](https://deepio.cs.ox.ac.uk/)及[作者论文](https://arxiv.org/abs/1809.07491)可核查；官网本次直接读取不稳定，搜索可见下载入口，具体包内字段/单位及独立许可证未确认，不提供伪精确列号。

### 从人体运动到机器人动作

**12 AMASS。** 主要是人体模型参数序列，不是原生六轴 IMU。常见学习接口是 `[L,J,3]` 关节位置或 `[L,J,3,3]` 旋转，需由选定人体模型转换。可做动作预测、运动先验，位置 L1/Huber 配 MPJPE，旋转用几何误差；按人、动作和原始来源划分。合成 IMU 需要传感器放置、重力、差分和噪声模型，不能把其结果当真实 IMU。[官方页](https://amass.is.tue.mpg.de/)要求注册，[许可](https://amass.is.tue.mpg.de/license.html)限制为规定的非商业用途及再分发；帧率和模型版本要逐文件保存。

**13 Open X-Embodiment。** 是异构机器人数据集合，episode 中含图像、任务文字、状态与动作等，字段随子集变化。可从一个子集做行为克隆：连续动作 MSE/分布 NLL，动作离散成 token 后才用 CE。不要把 RT-X 模型的7维动作说明误当所有原始数据同一种动作语义。按 embodiment、任务、场景、episode 检查划分，闭环成功率比离线动作误差更接近控制目标。[官方仓库](https://github.com/google-deepmind/open_x_embodiment)提供 RLDS 接口及许可说明，具体来源数据仍需逐子集核对。

**14 robomimic。** 更适合先从单一操作任务理解示范：HDF5 按 demo 存 `obs`、`actions[T,A]` 等；先挑 Lift 的 low_dim，小型 MLP/RNN 做行为克隆，MSE 或策略 NLL。按完整 demo 划分，检查示范者和初始状态；离线 loss 之外再看仿真成功率。[官方格式](https://robomimic.github.io/docs/datasets/overview.html)要求按其动作规范，不能把归一化动作当 SI 单位。官方链接的 [v1.5 数据仓库](https://huggingface.co/datasets/robomimic/robomimic_datasets/tree/main/v1.5)标 MIT；该说明不应外推到框架支持的所有外部数据。环境版本变动可能影响复现。

**15 D4RL及其迁移入口。** 离线 RL 数据典型记录 `(s,a,r,s',terminated,truncated)`，不同环境维度不同。行为克隆可先用动作 MSE；真正离线 RL 还涉及价值学习与分布外动作约束，不能只换一个 MSE 名字。按 episode 划分，不能跨终止边界拼 transition；任务评价通常看回报及规定的归一化得分。[维护方仓库](https://github.com/Farama-Foundation/D4RL)已说明数据迁移到 Minari，默认数据 CC BY 4.0、例外另列；新实验记录数据 ID、版本和环境版本，不照搬旧安装教程。


核验日期2026-10-01。任务/loss/划分为教学建议；许可只记录官方页面事实及未确认项。
