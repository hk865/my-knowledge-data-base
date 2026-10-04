# Seccomp BPF (SECure COMPuting with filters)

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://docs.kernel.org/userspace-api/seccomp_filter.html
- 类型：官方技术文档，非论文
- 日期：动态资料，无固定发表日期
- 日期依据：滚动内核文档页，无可见固定发布日期
- [原文入口](https://docs.kernel.org/userspace-api/seccomp_filter.html)
- 阅读版本：2026-10-04所见动态官方页面；未固定不可变版本
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

seccomp 以系统调用号/参数等元数据过滤调用，缩小暴露内核面；原文明说 syscall filtering 不是完整沙箱，逻辑行为与信息流还需其他加固/LSM。

- 实际阅读范围：introduction_what_it_isnt_usage
- 证据边界：BPF 过滤器不能任意解引用用户指针；不能把它直接写成路径级业务授权器。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://docs.kernel.org/userspace-api/seccomp_filter.html](https://docs.kernel.org/userspace-api/seccomp_filter.html)

只保留公开原文链接，不镜像第三方全文。
