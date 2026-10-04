# -*- coding: utf-8 -*-
"""Step 2: regenerate docs/topics.md from papers.json (topic sections, tag vocabulary,
modality x task cross directory). Idempotent: re-running on its own output gives the same file.
Run from anywhere: python tools/gen_topics.py"""
import sys
import json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODALITY = ["text", "image", "video", "audio", "action", "state", "code", "multimodal", "tabular"]
TASK = ["understanding", "generation", "decision", "evaluation", "analysis"]

VOCAB_HEAD = "## 标签词表"
CROSS_HEAD = "## 按模态与任务的交叉目录"

VOCAB = """## 标签词表

模态和任务类型不建目录，用 `papers.json` 的 `modality_tags`、`task_tags` 表达（[STYLE.md §15](../STYLE.md#15-目录与标签)）。一篇论文可以有多个标签。文末的[按模态与任务的交叉目录](#按模态与任务的交叉目录)由脚本从这两个字段生成。

| 字段 | 标签 | 含义 |
|---|---|---|
| modality_tags | text | 自然语言文本 |
| | image | 单帧视觉输入，包括 RGB、深度图、高程图等几何感知 |
| | video | 时序视觉输入，包括视频和 3D 占据序列 |
| | audio | 语音与音频 |
| | action | 机器人动作、控制指令、运动轨迹 |
| | state | 本体状态、IMU、力觉等传感器时序 |
| | code | 源代码 |
| | multimodal | 视觉与语言（或音频）联合建模，例如图文对齐、VLM、VLA、语言条件的世界模型；视觉与惯性的传感器融合记为 image + state |
| | tabular | 结构化表格特征，词表的补充项，目前只有 [Model Compression](paper-catalog.md#p140) 使用 |
| task_tags | understanding | 理解、表示、判别、状态估计与建图 |
| | generation | 生成文本、图像、视频、动作序列，包括预测未来观测或未来表征的世界模型 |
| | decision | 决策、控制、规划、Agent 行动 |
| | evaluation | 评估方法、benchmark、评审模型 |
| | analysis | 分析模型本身：机制、探针、规模与训练规律、表示空间比较 |

task 标签写论文的方法服务于哪类任务；论文的主要贡献是分析或评估时，加 analysis 或 evaluation。
"""

SUBTOPICS_NEW = {
    "模型科学": "细分：机制可解释性；知识存储、定位与编辑；探针分析；推理忠实性；层冗余与模式坍缩；开放模型与可复现性",
    "训练科学": "细分：规模定律；优化地形；训练动态；双下降；本征维度与参数有效性；遗忘",
}


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if '-h' in sys.argv or '--help' in sys.argv:
        print(__doc__)
        return
    papers = json.load(open(os.path.join(REPO, "papers.json"), encoding="utf-8"))
    tax = json.load(open(os.path.join(REPO, "taxonomy.json"), encoding="utf-8"))
    label2id = {}
    for dom in tax["domains"]:
        for t in dom["topics"]:
            label2id[t["label"]] = t["id"]
    label2id["模型科学"] = "cross-domain/model-science"
    label2id["训练科学"] = "cross-domain/training-science"

    def plist(topic):
        ps = [p for p in papers if topic in p["topic_paths"]]
        ps.sort(key=lambda p: p["catalog_anchor"])
        return ["- [%s](paper-catalog.md#%s)" % (p["title"], p["catalog_anchor"]) for p in ps]

    path = os.path.join(REPO, "docs", "topics.md")
    text = open(path, "rb").read().decode("utf-8")
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = text.replace("\r\n", "\n").split("\n")
    if lines and lines[-1] == "":
        lines.pop()

    # drop previously generated cross directory (idempotency)
    if CROSS_HEAD in lines:
        i = lines.index(CROSS_HEAD)
        lines = lines[:i]
        while lines and lines[-1] == "":
            lines.pop()

    # drop previously generated vocabulary section
    if VOCAB_HEAD in lines:
        i = lines.index(VOCAB_HEAD)
        j = i + 1
        while j < len(lines) and not lines[j].startswith("## "):
            j += 1
        del lines[i:j]

    # rename 机制与可信解释 -> 模型科学
    for k, ln in enumerate(lines):
        if ln.startswith("### 机制与可信解释（"):
            lines[k] = "### 模型科学（0）"
            if lines[k + 2].startswith("细分："):
                lines[k + 2] = SUBTOPICS_NEW["模型科学"]

    # insert 训练科学 after 模型科学 if missing
    if not any(ln.startswith("### 训练科学（") for ln in lines):
        k = next(i for i, ln in enumerate(lines) if ln.startswith("### 模型科学（"))
        j = k + 1
        while j < len(lines) and not lines[j].startswith("### ") and not lines[j].startswith("## "):
            j += 1
        lines[j:j] = ["### 训练科学（0）", "", SUBTOPICS_NEW["训练科学"], "", ""]

    # Materialize newly registered taxonomy topics inside their existing domain.
    for dom in tax["domains"]:
        for topic in dom["topics"]:
            if any(re.match(r"^### " + re.escape(topic["label"]) + r"（\d+）$", ln) for ln in lines):
                continue
            siblings = {x["label"] for x in dom["topics"]}
            positions = [i for i, ln in enumerate(lines)
                         if any(ln.startswith("### " + label + "（") for label in siblings)]
            if not positions:
                continue
            j = max(positions) + 1
            while j < len(lines) and not lines[j].startswith("## "):
                j += 1
            lines[j:j] = ["### " + topic["label"] + "（0）", "",
                          "细分：" + "；".join(topic.get("subtopics", [])), "", ""]

    # regenerate every topic section's count + list
    out = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^### (.+)（\d+）$", ln)
        if m and m.group(1) in label2id:
            label = m.group(1)
            items = plist(label2id[label])
            out.append("### %s（%d）" % (label, len(items)))
            i += 1
            body = []
            while i < len(lines) and not lines[i].startswith("### ") and not lines[i].startswith("## "):
                body.append(lines[i])
                i += 1
            # keep body prefix (blank + 细分 + blank) and trailing blank lines; replace list lines
            pre = []
            for b in body:
                if b.startswith("- ["):
                    break
                pre.append(b)
            trail = 0
            for b in reversed(body):
                if b == "":
                    trail += 1
                else:
                    break
            pre = pre[: len(pre)]
            # pre already ends with the blank after 细分 (and maybe trailing blanks when list empty)
            while pre and pre[-1] == "":
                pre.pop()
            out.extend(pre + [""] + items + [""] * max(trail, 1) if items else pre + [""] * max(trail, 2))
            continue
        out.append(ln)
        i += 1
    lines = out

    # vocabulary section after the nav line
    nav = next(i for i, ln in enumerate(lines) if ln.startswith("[论文总目录](paper-catalog.md)"))
    vocab_lines = VOCAB.rstrip("\n").split("\n")
    lines[nav + 1:nav + 1] = [""] + vocab_lines

    # orthogonal tag lines for modality / task now point to the vocabulary
    for k, ln in enumerate(lines):
        if ln.startswith("- modality："):
            lines[k] = "- modality：" + ", ".join(MODALITY) + "（定义见文首「标签词表」）"
        elif ln.startswith("- task："):
            lines[k] = "- task：" + ", ".join(TASK) + "（定义见文首「标签词表」）"

    # cross directory
    cells = {(m, t): [] for m in MODALITY for t in TASK}
    for p in sorted(papers, key=lambda p: p["catalog_anchor"]):
        for m in p["modality_tags"]:
            for t in p["task_tags"]:
                cells[(m, t)].append(p)
    cross = ["", CROSS_HEAD, "",
             "本节由脚本从 `papers.json` 的 `modality_tags` × `task_tags` 生成，不手工编辑。"
             "一篇论文按它的每个标签组合出现，所以各格相加大于论文总数。格中数字是篇数，点击跳到对应小节。",
             "",
             "| 模态 \\ 任务 | " + " | ".join(TASK) + " |",
             "|---|" + "---:|" * len(TASK)]
    for m in MODALITY:
        row = []
        for t in TASK:
            n = len(cells[(m, t)])
            row.append("[%d](#x-%s-%s)" % (n, m, t) if n else "·")
        cross.append("| " + m + " | " + " | ".join(row) + " |")
    for m in MODALITY:
        for t in TASK:
            ps = cells[(m, t)]
            if not ps:
                continue
            cross += ["", '<a id="x-%s-%s"></a>' % (m, t), "",
                      "### %s × %s（%d）" % (m, t, len(ps)), ""]
            cross += ["- [%s](paper-catalog.md#%s)" % (p["title"], p["catalog_anchor"]) for p in ps]
    lines += cross

    open(path, "wb").write((nl.join(lines) + nl).encode("utf-8"))

    # summary
    print("matrix:")
    print("%-11s" % "", " ".join("%13s" % t for t in TASK))
    for m in MODALITY:
        print("%-11s" % m, " ".join("%13d" % len(cells[(m, t)]) for t in TASK))


if __name__ == "__main__":
    main()
