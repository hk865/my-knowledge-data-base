# 数据与数据集模块导航

[返回总导航](00-learning-navigation.md)

## 先读两分钟

这里按可独立学习的小问题拆成四个模块。每个模块都有一张浓缩图、两张分步图、详细解释和相关论文的指定片段阅读。图像、文本与IMU共享同一训练闭环；坐标、时间和标签的具体含义决定它们的差别。

1. [样本接口与数据集选择](modules/data/01-data-contracts.md)：x、y、mask、meta，四种规模，怎样选数据
2. [划分同步与最小数据管道](modules/data/02-data-pipeline.md)：先分组再切窗，训练统计、同步、增强、collate和缓存
3. [图像与文本分类的小规模实践](modules/data/03-classification-labs.md)：CIFAR-10与IMDb，各自的输入编码与共同的CE闭环
4. [IMU窗口怎样对应一个位移标签](modules/data/04-imu-lab.md)：EuRoC短窗回归，时间边界、坐标变换、参考状态与可观性

## 共享的数据目录

- [十五个代表数据集的选型说明](catalog/dataset-selection.md)
- [机器可读JSON](catalog/datasets.json)与[可筛选CSV](catalog/datasets.csv)
- [官方来源和核验范围](catalog/dataset-sources.json)

三个实验都是计划，没有下载大型数据或训练实测；16GB显存可行性是小模型估算。相关论文只对注明章节作针对性阅读，不声称完整复现。核验日期为2026-10-01。
