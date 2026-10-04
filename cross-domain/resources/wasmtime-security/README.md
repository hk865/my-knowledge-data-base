# Security

[领域目录](../../README.md) · [原文与阅读记录](source.json)

- 稳定标识：url:https://docs.wasmtime.dev/security.html
- 类型：官方技术文档，非论文
- 日期：动态资料，无固定发表日期
- 日期依据：动态运行时文档，无固定发布日期
- [原文入口](https://docs.wasmtime.dev/security.html)
- 阅读版本：2026-10-04所见动态官方页面；未固定不可变版本
- 来源关系：历史助手引用；仅取得检索摘要，没有原会话直链

## 阅读线索与边界

Wasm 实例以 imports/exports 与外界交互而非原生任意 syscall；Wasmtime 的 WASI 文件接口使用 capability 模型，仅提供显式授予的文件访问。

- 实际阅读范围：webassembly_core_defense_in_depth_filesystem_access
- 证据边界：保护依赖宿主暴露接口；不是把任意原生程序原样装进去的 VM。 运行时实现仍可能有缺陷，文档另外列出纵深缓解。 历史没有恢复独立 WASI 原始链接，不能把此页伪装成那条缺失引用。

这是资料卡，没有独立reading.md，不计为全文精读；用户是否已读未知，未据此推断已采纳任何工程方案。未运行代码、变更安全设置或独立复现实验。

## 核验来源

- [https://docs.wasmtime.dev/security.html](https://docs.wasmtime.dev/security.html)

只保留公开原文链接，不镜像第三方全文。
