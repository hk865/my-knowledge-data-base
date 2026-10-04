# VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation

> 状态：文献卡 · 2023 · [原文](https://arxiv.org/abs/2312.03275)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：不做任务训练、不预建地图，只用 RGB-D 与里程计在新环境中找到指定类别的物体（零样本 ObjectNav）。
- **核心方法**：用深度建前沿地图（已探索与未探索的边界），用 BLIP-2 计算每帧图像与"前方似乎有某物体"这类提示的相似度，形成语言接地的价值图，选价值最高的前沿走过去，检测到目标后切换为点目标导航。HM3D 成功率 52.5%、SPL 30.4，并在 Spot 上运行。
- **为什么在这个库里**：[导航与规划](../../fields/navigation-planning/README.md)主线第 5 步：VLM 给候选打分、交给几何导航执行的代表。优先级：选读。
