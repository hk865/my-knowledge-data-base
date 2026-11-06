# ORB-SLAM3 与 VINS-Mono的尺度 初始化和地图后端

> 状态：技术对比 · 草稿 · 未复现

## 一句话

纯视觉、双目和视觉惯性解决的是“观测从哪里来、尺度能否恢复”；VO、局部优化和地图后端解决的是“历史信息保留多久、何时重新使用”。ORB-SLAM3与VINS-Mono都用几何优化，但在输入配置、初始化以及历史观测的保留方式上选择不同。

## 先把传感器配置与地图能力分开

VO即视觉里程计，核心任务是持续估计相对运动；视觉SLAM在此基础上维护可重复关联的地图，利用旧区域中的观测定位和纠正漂移。VIO即视觉惯性里程计，表示联合使用相机和IMU。因而，“有没有IMU”和“有没有长期地图”是两条独立的分类轴。

ORB-SLAM3的单目和双目模式都是纯视觉，但仍可建图、回环和重定位；加IMU的模式才是视觉惯性。VINS-Mono以单目加IMU的局部VIO估计为核心，完整系统还带回环和全局位姿图。单看“ORB有因子图、VINS有窗口”会漏掉二者都采用局部优化、也都管理长期约束这一点。[O1、V1]

| 配置 | 米制尺度来自哪里 | 启动时需要解决什么 | 保留历史的方式 |
|---|---|---|---|
| ORB-SLAM3纯单目 | 视觉几何保留一个整体尺度自由度 | 两视图恢复运动与点，随后视觉BA | 关键帧、三维点与观察关系构成持久地图 |
| ORB-SLAM3纯双目 | 已标定双目基线 | 左右图匹配与三角化，建立首张地图 | 同样可重用地图、回环和重定位 |
| ORB-SLAM3单目惯性 | 视觉运动与有物理单位的IMU联合约束 | 先建立视觉地图，再估尺度、重力、速度与偏置 | 局部惯性优化与持久地图结合 |
| ORB-SLAM3双目惯性 | 双目已经提供尺度 | 继续初始化重力、速度和偏置，尺度固定 | 局部惯性优化与持久地图结合 |
| VINS-Mono | 单目视觉与IMU联合约束 | 视觉SfM后做视觉惯性对齐 | 有界局部窗口加长期关键帧位姿图 |

BA即束调整：联合优化相机位姿和三维点，使预测投影与实际图像观测一致。持久地图指旧关键帧和地图点在退出当前局部优化后仍可再次参与数据关联，长期内存并不只是一条轨迹。

## 纯视觉已经可以做什么

### 单目缺的是整体尺度 不是一切三维信息

在常见的单目几何模型中，像素满足 $u=\pi(RP+t)$。将所有三维点与平移同时乘上正数 $s$，有

$$\pi(R(sP)+st)=\pi(s(RP+t))=\pi(RP+t).$$

同一段视频可以由整体放大后的场景和运动生成。因此单目在合适视差下可恢复结构、旋转和平移方向，却保留一个整体尺度自由度。继续移动能改善三角化和相对结构，这个全局尺度对称性仍然成立。若任务只要求返回旧地点或在图像中对准目标，相对几何已经有价值；若要输出米制距离，则需额外约束。

ORB-SLAM3源码中的对应过程很具体：`MonocularInitialization()`先匹配两帧并调用两视图重建，`CreateInitialMapMonocular()`建立关键帧和三维点、做初始BA，再按中值深度规范化尺度。这个规范化只是选择地图单位。[O2]

### 双目基线已经是一次已知运动

已校准的双目把同一时刻两台相机的相对位置作为已知基线。对于校正后的平行针孔相机，深度近似为 $Z=f_xB/d$，其中 $B$ 是米制基线、$d$ 是左右视差。它在启动阶段就提供尺度。

**示例数值。** $f_x=400$像素、$B=0.1$米、视差20像素时，$Z=2$米。若视差误差为1像素，一阶深度误差约为 $f_xB/d^2=0.1$米。双目“尺度已知”与“每个点深度都准确”是两件事，远点的小视差会放大误差。

源码 `StereoInitialization()`直接把有效双目深度反投影为地图点，纯双目分支没有单目惯性初始化中的尺度求解。它可以在相机静止时利用左右基线启动，但仍需要可靠标定、足够有效特征和匹配；双目惯性模式还要满足自身的IMU启动条件。[O3]

## VIO初始化增加的是哪些未知量

单目加IMU时，尺度、重力方向、初始速度、陀螺和加速度偏置互相耦合。把它们全部交给任意初值的非线性优化，容易落入较差解。两套系统都先利用视觉几何建立初值，再让IMU补上米制运动与惯性状态。

**ORB-SLAM3的组织方式**是“视觉MAP → 固定视觉轨迹的惯性MAP → 联合视觉惯性MAP”。MAP即最大后验估计，将测量似然与先验一起优化。第二步显式估计尺度、重力方向、偏置与速度，并使用预积分协方差和偏置先验。双目惯性将尺度固定为1，从这组未知量中去掉尺度。论文后续还细化尺度与重力，以改善低激励时的收敛。[O1 §V-B]

**VINS-Mono的组织方式**是“视觉SfM → 陀螺偏置估计 → 线性求速度/重力/尺度 → 固定重力模长的细化 → 紧耦合非线性优化”。SfM即从多幅图像恢复运动和结构。初始化的视觉轨迹先保持任意尺度，与IMU预积分对应后再恢复尺度；所核对代码在初始化重传播时暂用零加速度偏置，进入联合VIO后再估计该偏置；ORB-SLAM3的惯性MAP初始化则显式引入偏置先验。两者在求解方式、先验使用和状态组织上不同。[V1 §V、V2]

“有IMU”提供恢复尺度所需的信息来源，运动激励决定其中一些未知量能否被区分。持续静止或纯旋转无法建立通常的单目三角化基线，长期缺乏变化的平移加速度也会削弱尺度辨识。已知电机命令可作为运动模型输入，但命令对应的目标位移不是实际位移测量；可靠编码器、固定基座机械臂的标定运动学，或经过检验的轮地/足地约束，才会进一步提供米制运动证据。这是可观测性层面的区别，不依赖前端使用ORB还是KLT。

KLT是根据局部亮度变化跟踪图像特征位移的光流方法。VINS-Mono用KLT做相邻帧跟踪，ORB-SLAM3主要匹配二进制ORB描述子。二者都需要几何一致性与三角化条件，前端选择本身不会消除尺度自由度。

## 两种后端主要差在怎样使用历史

### ORB-SLAM3把地图当作可再次访问的状态

在纯视觉局部BA中，源码从当前关键帧的共视邻居选取局部位姿和地图点，再把其他观察这些点的关键帧作为固定边界加入约束。共视指不同关键帧看到了同一批三维点。视觉惯性局部优化则围绕时间相邻的关键帧和IMU约束展开，同时保留地图中的视觉观察。

因此“时间很久以前，但现在又看见”的地图点能够直接参与当前匹配与优化。追踪丢失后的重定位也直接利用地图中的三维点；回环和Atlas地图合并进一步纠正地图状态。Atlas是管理多张已建地图并在识别出重叠区域时合并它们的结构。[O1 §III、V-C、VI；O4]

### VINS-Mono把局部细节与全局漂移分开管理

局部滑窗联合优化最近若干帧的位姿、速度、偏置、视觉逆深度及配置允许的外参。旧变量退出窗口时，边缘化把它们对保留变量的影响压成先验。逆深度用深度的倒数参数化三维点，通常依附某个观测帧。

长期部分保留关键帧与位姿约束，并通过回环构建全局位姿图。位姿图主要优化节点之间的相对运动一致性，局部BA则还利用原始视觉投影与IMU残差。VINS-Mono的长期关键帧图支持场景检索与全局一致性，但它没有把全部历史图像观测和三维点持续作为一个统一大BA重新求解。[V1 §VI–VIII；V3]

源码还把两种回环反馈分开：常规4自由度图优化更新图中的关键帧位姿，计算旋转/平移漂移修正量，并应用到后续关键帧和最新输出；它本身不把全部图优化结果直接写回局部窗口的位姿、速度和偏置。若开启`FAST_RELOCALIZATION`，时间戳仍在局部窗口内的回环匹配会另外形成重投影因子，影响窗口内共享的位姿、逆深度与外参，并把求得的回环相对位姿回传给全局图。[V5]

两种组织方式都兼顾实时性与长期约束。关键差别是：重访时，旧观测通过持久地图点直接参与局部估计，还是主要通过重定位约束与长期位姿图传递信息。比较时应看“保留了哪些变量与观测、旧信息怎样再次进入目标函数”，而不仅是有没有因子图。

## 位姿修正后 以前的观测到底改不改

需要把三类对象分开。

1. **原始测量。** 像素位置、左右视差、IMU采样等保留其采集时的值。
2. **被估计的状态。** 相机位姿、地图点坐标、速度与偏置会被优化更新。
3. **由状态转换得到的世界系表示。** 将深度点、语义实例或点云变换到世界坐标的结果，需要随着位姿或地图修正而更新。

视觉BA的残差可写为 $r_{ij}=u_{ij}-\pi(T_{CW,i}P_{W,j})$。优化改变 $T$ 和 $P$，从而改变预测投影；测量 $u$ 保持不变。源码也是把关键帧保存的图像特征作为边的`measurement`，把位姿和地图点作为待估计顶点。[O5]

**示例数值。** 某帧相机原来位于世界系 $x=2$米，一条深度观测表示目标在相机前方3米，回投的世界位置是5米。回环将该帧位姿修正为1.5米，同一条局部观测回投后变为4.5米；相机系的3米测量保持不变。这只演示单条观测的回投，多个视角融合后的地图点还要由联合约束决定。

对应的刚性修正为

$$P_W^{new}=T_{WC}^{new}(T_{WC}^{old})^{-1}P_W^{old}.$$

ORB-SLAM3回环实现明确先调整关键帧位姿，再通过参考关键帧把地图点从旧世界表示带到新世界表示；纯单目还可能包含尺度修正，使用的是Sim(3)，即旋转、平移与尺度的相似变换。[O6]

[建议] 对额外构建的点云、语义和动态实例层，保留原始局部观测、时间戳及参考关键帧，或采用以关键帧为锚的子地图。这样图优化后能重投影或更新子地图，动态轨迹也能区分“物体真实移动”和“地图坐标被纠正”。旧相对运动因子则应保留其测量含义；把每轮优化后的相对位姿重新当成同一个因子的测量，会改变原来的估计问题。

## 回环 重定位与BoW分别做哪一步

**重定位**是在当前定位丢失或未知时，把当前观测对齐到已有地图，恢复当前位置。**回环**是在持续运行中认出重访区域，添加跨时间约束并纠正累计漂移。二者可共享地点检索和几何验证，但目标与触发条件不同。

BoW即词袋：把许多局部视觉描述子量化成词，再汇总为整幅图像的稀疏词频或加权直方图。ORB描述子本身是二进制串，局部匹配常用Hamming距离，即不同二进制位的数量；图像级BoW评分又是另一层。DBoW2的L1评分把归一化直方图的距离转成相似度。将整个图像称为one-hot向量，会丢掉同一幅图中多个视觉词和各自权重的信息。[O7]

ORB-SLAM3重定位的实际链条是：BoW找候选关键帧 → ORB匹配建立当前2D特征与地图3D点的对应 → PnP/RANSAC求位姿并排外点 → 重投影优化和补充匹配。PnP是用三维地图点与二维图像点求相机位姿。BoW解决“去哪找”，几何求解回答“具体在哪、匹配是否成立”。[O8]

VINS-Mono的局部KLT跟踪与回环检索也分工不同：回环使用关键帧的BRIEF描述子和DBoW2检索，再进行几何验证与约束构建。BRIEF与ORB同属二进制局部描述子，前端用了KLT不妨碍长期模块另用描述子检索。[V4]

## 批注

**易误读**

- 纯双目属于纯视觉输入，但ORB-SLAM3仍运行完整地图和回环逻辑；“纯视觉”与“只有VO”不应互换。
- 双目惯性已从基线获得尺度，仍要初始化重力、偏置与速度；“不用估单目尺度”不等于“无需惯性初始化”。双目的米制尺度也不直接给出地球坐标原点或绝对朝向。
- VINS-Mono中的视觉SfM是VIO初始化分支，不是关闭IMU后继续输出纯VO的自动降级模式；失败时仍会滑窗重试或重新初始化。
- VINS-Mono论文强调IMU激励条件，但当前官方源码中`initialStructure()`的低激励检查只告警，拒绝初始化的语句被注释；物理可观测条件与某版代码的硬门控是不同事实。[V2]
- 论文VINS-Mono初始化叙述与当前代码的点数、视差阈值和相对位姿求解器存在差异；这里保留流程级比较，不把某一版阈值当成算法定义。
- 视觉惯性系统用重力约束横滚和俯仰后，长期漂移校正常采用位置与偏航的4自由度位姿图；这与纯单目中需要处理尺度的Sim(3)情况不同。4自由度是模型选择，不保证真实尺度或横滚俯仰误差严格为零。
- VINS-Mono论文§VII-C叙述固定旧回环帧姿态；所核对实现却把`relo_Pose`注册为待优化参数，旧帧全局位姿用于事后求坐标修正，不宜把论文叙述逐字当成当前代码行为。[V5]
- ORB-SLAM3源码中地图点顶点的`setMarginalized(true)`是图求解器对消元次序的设置，不能单凭这个标记判断它采用VINS那样的固定时滞历史先验。
- 原始采样与优化派生量应分开：外参或偏置更新后，去畸变坐标、射线、IMU预积分等派生量可能重新计算，像素与IMU原始采样仍保存其测量值；数据关联和离群点选择也可被复核。

**与已有精读的互补关系**

- ORB-SLAM3已有精读重点解释MAP初始化、中期关联、Atlas和地图焊接；本页只把这些机制放到“纯单目/双目/VIO”的输入差异与观测更新问题中对照。
- VINS-Mono文献卡提供系统主线；本页补充滑窗先验与全局位姿图的分工，并区分论文条件和当前公开代码行为。

**未核实 / 待验证**

- 本页是论文与公开源码的阅读分析，未编译或运行两套系统，也未核验它们在当前相机、动作数据或Dynanavi中的实际表现；任何项目接口建议均为建议。
- 当前项目是否已有回环、重定位、地图修正通知或可更新语义层，需要另查项目代码；上述能力不能由论文存在而推断为项目已经实现。
- 本文的尺度与电机段是根据观测模型作出的可观测性分析，不是两篇论文验证过的电机控制实验；控制是否成功也不能单独证明存在显式公制地图。

**论文与源码**

- O1：[ORB-SLAM3论文v2](https://arxiv.org/pdf/2007.11898v2)，重点§III–VI。
- O2：[单目初始化与尺度规范化](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/Tracking.cc#L2448-L2625)。
- O3：[双目初始化](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/Tracking.cc#L2335-L2447)；[IMU初始化](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/LocalMapping.cc#L1173-L1320)。
- O4：[视觉局部BA的关键帧选取](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/Optimizer.cc#L1116-L1195)；[局部惯性BA](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/Optimizer.cc#L2383-L2510)。
- O5：[重投影边使用固定图像观测](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/Optimizer.cc#L1285-L1325)。
- O6：[回环修正关键帧与地图点](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/LoopClosing.cc#L969-L1110)；[位姿图后按参考帧更新地图点](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/Optimizer.cc#L1738-L1778)。
- O7：[BoW从多个描述子累计权重](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/Thirdparty/DBoW2/DBoW2/TemplatedVocabulary.h#L1066-L1110)；[L1评分](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/Thirdparty/DBoW2/DBoW2/ScoringObject.cpp#L22-L75)；[ORB的Hamming距离](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/ORBmatcher.cc#L2058-L2078)。
- O8：[重定位候选与PnP求解](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4/src/Tracking.cc#L3609-L3745)。
- V1：[VINS-Mono论文v1](https://arxiv.org/pdf/1708.03852v1)，重点§V–VIII。
- V2：[初始化视觉结构与激励告警](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/vins_estimator/src/estimator.cpp#L218-L361)；[视觉惯性对齐](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/vins_estimator/src/initial/initial_aligment.cpp#L3-L206)；[当前代码的相对位姿筛选](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/vins_estimator/src/estimator.cpp#L442-L473)。
- V3：[两种边缘化分支](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/vins_estimator/src/estimator.cpp#L825-L999)；[全局4DoF位姿图](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/pose_graph/src/pose_graph.cpp#L403-L542)。
- V4：[关键帧BRIEF提取](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/pose_graph/src/keyframe.cpp#L13-L117)；[DBoW2类型](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/pose_graph/src/pose_graph.h#L22-L81)；[BRIEF词袋查询](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/pose_graph/src/pose_graph.cpp#L304-L324)。
- V5：[全局图优化后的drift修正](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/pose_graph/src/pose_graph.cpp#L549-L573)；[修正最新输出](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/pose_graph/src/pose_graph_node.cpp#L201-L226)；[局部重定位投影因子](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/vins_estimator/src/estimator.cpp#L769-L799)；[局部重定位后计算坐标修正](https://github.com/HKUST-Aerial-Robotics/VINS-Mono/blob/90dabb5ec79946ae42fd2e1e91d4e69aabe1e25d/vins_estimator/src/estimator.cpp#L598-L616)。
