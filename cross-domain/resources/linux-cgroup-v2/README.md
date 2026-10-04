# Control Group v2

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://docs.kernel.org/admin-guide/cgroup-v2.html
- 类型：官方技术文档，非论文
- 日期：动态资料，无固定发表日期
- 日期依据：页首保留 Date: October, 2015；正文声明未来接口变化须更新本页，不能把现页全内容归为 2015 年固定版本
- [原文入口](https://docs.kernel.org/admin-guide/cgroup-v2.html)
- 阅读版本：2026-10-04所见动态官方页面；未固定不可变版本
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

cgroup 将进程分层组织，以 controller 分配/约束系统资源；下层不能取消上层资源限制。

- 实际阅读范围：authoritative_intro_core_controller_model
- 证据边界：不是通用用户—动作—资源授权框架。 不能绝对说它与安全无关：资源耗尽防御及部分 controller 有安全用途；这里反对的是把资源分组当作充分数据隔离。 未声称逐条审核全部 controller 文档。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://docs.kernel.org/admin-guide/cgroup-v2.html](https://docs.kernel.org/admin-guide/cgroup-v2.html)

只保留公开原文链接，不镜像第三方全文。
