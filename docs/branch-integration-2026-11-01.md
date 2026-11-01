# 知识库分支整合审计：2026-11-01

范围仅为 hk865/my-knowledge-data-base。基线 main 为 `f0e77f099918ee84345b55b6e186404c14db4cc4`。盘点 17 个主题分支：5 个此前已并入，12 个仍有独有资料，共吸收 13 个原始提交。全部原始分支保留，没有删除或强制推送。逐分支完整提交与合并提交见[结构化记录](branch-integration-2026-11-01.json)。

## 逐分支处置

| 分支 | 原始分支提交 | 分类 | 本次吸收提交数 |
|---|---|---|---:|
| `embodied-agents-2026-10-06` | [`98378d8`](https://github.com/hk865/my-knowledge-data-base/commit/98378d80b76a6ad41464d5ffe52c1e8071225752) | 此前已并入 | 0 |
| `phase3` | [`2352c92`](https://github.com/hk865/my-knowledge-data-base/commit/2352c92ebcef6f3cbb02762e9ec96e2926665faf) | 此前已并入 | 0 |
| `phase3-expand-2026-10-04` | [`536a982`](https://github.com/hk865/my-knowledge-data-base/commit/536a982e2b46abae7c93992d868361d9c8d9dcf5) | 此前已并入 | 0 |
| `research-action-priors-2026-10-09` | [`2fd4703`](https://github.com/hk865/my-knowledge-data-base/commit/2fd4703e218bb91ba280a22740c372b5fa16bee0) | 此前已并入 | 0 |
| `research-daily-2026-10-08` | [`1041255`](https://github.com/hk865/my-knowledge-data-base/commit/10412550b111eede6489b20490c4c161f27aa4a0) | 此前已并入 | 0 |
| `research-daily-2026-10-09` | [`7908e62`](https://github.com/hk865/my-knowledge-data-base/commit/7908e62575c94106892a46e1bd430f22d37e245a) | 独有资料已整合 | 1 |
| `research-daily-2026-10-10` | [`9b824bb`](https://github.com/hk865/my-knowledge-data-base/commit/9b824bbe2c3b07ea397024d48c2e6441b6629462) | 独有资料已整合 | 1 |
| `research-daily-2026-10-12` | [`ab6820c`](https://github.com/hk865/my-knowledge-data-base/commit/ab6820cbeb413949f0713549ce1ffc685c543dcb) | 独有资料已整合 | 1 |
| `research-daily-2026-10-13` | [`2b6655b`](https://github.com/hk865/my-knowledge-data-base/commit/2b6655bbbadbc62be19d2c1ece0b7a9bea9d838d) | 独有资料已整合 | 1 |
| `research-daily-2026-10-14` | [`51e31fb`](https://github.com/hk865/my-knowledge-data-base/commit/51e31fb6cf8e932be38ea4c7f964fdfbf18c91fd) | 独有资料已整合 | 1 |
| `research-daily-2026-10-15` | [`3c69e71`](https://github.com/hk865/my-knowledge-data-base/commit/3c69e71b5819d5f7566b3a7ca147774935794f8c) | 独有资料已整合 | 1 |
| `research-daily-2026-10-16` | [`5983238`](https://github.com/hk865/my-knowledge-data-base/commit/59832382f3f5ddfd1ecb63cb7fa06c11a79981a2) | 独有资料已整合 | 1 |
| `research-daily-2026-10-17` | [`f51626a`](https://github.com/hk865/my-knowledge-data-base/commit/f51626a7b5eff0e933f7b8bd190cb679a7498171) | 独有资料已整合 | 1 |
| `research-dynamic-slam-2026-10-31` | [`83a9e9e`](https://github.com/hk865/my-knowledge-data-base/commit/83a9e9e0370fc8b3d1600bc26ab57287762ab4b0) | 独有资料已整合 | 1 |
| `research-embodied-papers-2026-11-01` | [`09e68a9`](https://github.com/hk865/my-knowledge-data-base/commit/09e68a92eca0fbed5dc0c219f148c252043a223d) | 独有资料已整合 | 1 |
| `research-robot-agent-tools-2026-10-24` | [`0b4534e`](https://github.com/hk865/my-knowledge-data-base/commit/0b4534ebbe20c90f565d5b3e744c6f3854751339) | 独有资料已整合 | 2 |
| `research-weekly-2026-10-18` | [`948fb98`](https://github.com/hk865/my-knowledge-data-base/commit/948fb982019fdf4996991ad5508db309fa4f0aff) | 独有资料已整合 | 1 |

“此前已并入”按提交祖先关系判定，并非仅凭文件名相同。未发现仅内容重复但历史未合入的独立分支；也未发现需要搁置的实验、私人内容或语义矛盾分支。12 个独有分支均以保留历史的 merge commit 合入整合分支。

## 合并中处理的冲突

1. 动态 SLAM 与 Agent 工具专题共同追加 index.json/CSV：按规范路径求并集，保留双方入口。
2. 机械臂资料包与 SLAM 同时从原 main 分配 p612 等目录编号：不拼接冲突编号，先保留 SLAM 注册，再用现有注册工具登记机械臂 12 篇和周整理 3 篇，重新生成唯一编号与分类目录。
3. 六篇已有文献卡新增解读，按 source.json 刷新阅读入口。SayCan、Harness VLA、RoboSkill 原有正文不覆盖，补充解读另存。
4. README 与领域目录保留双方新增导航，只重新计算生成计数，没有选择一方覆盖研究结论。

原先 611 项资源加 SLAM 14 项、机械臂 12 项、周整理 3 项，得到 **640 项**。论文资料包的 21 篇解读仍全部可访问。周整理分支原有三张文献卡此前未登记，此次补齐正式目录、控制方向和内容索引；其余短报候选继续保持候选状态。

## 原始资料与许可边界

每日短报、周整理与公开证据快照保留原日期和来源。周整理页面追加本次入库补记，原来未完整处理的候选不会因合并而成为“已全文精读”。本次没有重新做论文实验，也没有修改用户已审阅结论。

本次没有新发布 PDF、模型、训练轨迹、私人对话、账户、密钥或运行日志。机械臂 21 份 PDF 留在本地，官方原文与许可核查见[资料包](../robotics-embodied/fields/embodied-agents/reading-pack-2026-10-30/README.md)。

## 验证

仓库 24 项注册与同步回归测试通过；注册与同步 dry-run 均无遗漏。发布前另核对全部 JSON、规范路径、唯一资源标识及目录编号、JSON/CSV一致性、相对链接、来源正文保留和新增内容敏感模式。结构化记录保存最终检查数量。推送采用普通快进，若远程 main 前进则重新检查，遵守远程保护规则。
