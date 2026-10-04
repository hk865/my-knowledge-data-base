# Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers

> 状态：文献卡 · 2024 · [原文](https://arxiv.org/abs/2405.12424)

[返回机器人与具身目录](../../README.md) · [原文与阅读记录](source.json)

- **解决什么**：强化学习训练的四足控制器在实测中看起来很鲁棒，但它的弱点分布在高维、按时间展开的长尾状态里，随机测试很难找到。
- **核心方法**：把「找出让机器人摔倒的扰动序列」本身写成一个强化学习问题：训练一个对抗策略（adversary，一句话：专门学习怎样让被测策略失败的另一个策略），在观测、速度命令和未被观测的外力三类空间里施加幅度与变化率都受限的扰动，并用 Lipschitz 正则让扰动平滑、接近真实情况（§IV-A、IV-B）。找到的攻击再混入原本的域随机化（domain randomization，一句话：训练时随机改变摩擦、质量、外力等仿真参数）里微调原策略（§IV-C）。被攻击的对象包括 [Miki 等 2022](../arxiv-2201.08117/README.md) 的感知行走策略：以 5% 的概率遇到学到的对抗者做微调后，实机在湿滑白板和软垫上更稳，命令跟踪精度与微调前相比没有显著变化（§V-B、Table III）。
- **为什么在这个库里**：[四足故障后恢复](../../../perspectives/notes/quadruped-recovery.md)四类解法中「场景」一类：主动搜出让策略失败的长尾情况，再把它们按小比例加回训练分布；它同时报告了加回之后原有的命令跟踪能力没有明显下降。优先级：选读。
