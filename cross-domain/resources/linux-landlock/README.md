# Landlock: unprivileged access control

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://docs.kernel.org/userspace-api/landlock.html
- 类型：官方技术文档，非论文
- 日期：动态资料，无固定发表日期
- 日期依据：正文 Date 元数据为 August 2026；滚动文档更新时间，不标成论文发表日
- [原文入口](https://docs.kernel.org/userspace-api/landlock.html)
- 阅读版本：2026-10-04所见动态官方页面；未固定不可变版本
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

Landlock 是可叠加 LSM，允许非特权进程收紧自身及后代的访问；路径须同时通过全部 Landlock 层、DAC 和其他 LSM 控制。

- 实际阅读范围：introduction_rules_layering_inheritance_and_abi_caveats
- 证据边界：不能扩大已有权限；操作覆盖取决于运行内核、Landlock ABI 与 handled rights。 不应把 latest 文档所列新 ABI 能力当成任意 Linux 主机已支持。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://docs.kernel.org/userspace-api/landlock.html](https://docs.kernel.org/userspace-api/landlock.html)

只保留公开原文链接，不镜像第三方全文。
