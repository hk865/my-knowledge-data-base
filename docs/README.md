# 全库目录与兼容入口

docs/ 只放两类东西：全库范围的目录，以及旧路径的转接页。正文都在别处：讲义在 [foundations/lessons/](../foundations/lessons/README.md)，观点与研究兴趣在 [perspectives/](../perspectives/README.md)，证据档案在各论文目录的 `evidence.json`。新内容不放进 docs/（[STYLE.md §15](../STYLE.md#15-目录与标签)）。

## 全库目录

| 文件 | 内容 | 维护方式 |
|---|---|---|
| [paper-catalog.md](paper-catalog.md) | 全部论文与资源，按编号排列 | 登记新论文时追加 |
| [topics.md](topics.md) | 按方向浏览，以及按模态 × 任务的交叉目录 | 由 [tools/gen_topics.py](../tools/gen_topics.py) 从 `papers.json` 生成，勿手改 |
| [unresolved.md](unresolved.md) | 待核实的线索 | 核实后移出 |

## 转接页

| 旧路径 | 现在的位置 |
|---|---|
| `foundations/`（讲义） | [foundations/lessons/](../foundations/lessons/README.md) |
| `deep-readings/*.md`（旧精读入口） | 各论文目录下的 `reading.md` |
| `deep-readings/evidence/`（证据档案） | 各论文目录下的 `evidence.json`，对照表见 [deep-readings/evidence/README.md](deep-readings/evidence/README.md) |
| `research-map.md`、`model-training-multimodal.md`、`robotics-embodied.md` | [perspectives/notes/](../perspectives/README.md) |
| `knowledge-distillation/` | [跨方向 · 知识蒸馏](../cross-domain/fields/knowledge-distillation/history.md) |

## 尚未迁出

- [roadmaps/](roadmaps/)：早期的跨领域路线图。每写完一个领域页或观点页，就吸收对应的路线图并改为转接页；robotics-baselines、embodied-baselines、training-baselines、architecture-baselines、long-context（含 long-context-graph.json）、multimodal-baselines、visual-baselines 已转接；cross-baselines 待跨方向重写后处理。
- [deep-readings/training-coverage.md](deep-readings/training-coverage.md) 与 `deep-readings/evidence/beginner-2026-10-02.json`：涉及多篇论文的核验记录，暂留原处。
