# Security Model

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://gvisor.dev/docs/architecture_guide/security
- 类型：官方技术文档，非论文
- 日期：动态资料，无固定发表日期
- 日期依据：动态架构指南，没有可见固定文章发布日期
- [原文入口](https://gvisor.dev/docs/architecture_guide/security/)
- 阅读版本：2026-10-04所见动态官方页面；未固定不可变版本
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

Sentry 重实现应用可见 System API，减少对宿主 API 的直接暴露；VM 则通过 guest OS/虚拟设备改变边界。；资源耗尽仍依赖宿主 cgroup，网络策略需另施加；硬件侧信道不是其一般防护保证。

- 实际阅读范围：threat_model_goals_defense_in_depth_faq
- 证据边界：VM/gVisor 安全性取决于实际暴露面，不能仅凭使用虚拟化硬件排序。 沙箱不是安全架构的替代品，也不会自动禁止已映射文件与网络访问。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://gvisor.dev/docs/architecture_guide/security/](https://gvisor.dev/docs/architecture_guide/security/)

只保留公开原文链接，不镜像第三方全文。
