# Security

> 状态：资料卡 · 动态文档 · [原文](https://docs.wasmtime.dev/security.html)

- **解决什么**：怎样给 WebAssembly 程序提供受限的宿主能力。
- **核心方法**：Wasm 实例以 imports/exports 与外界交互而非原生任意 syscall；Wasmtime 的 WASI 文件接口使用 capability 模型，仅提供显式授予的文件访问。
- **为什么在这个库里**：补充[Agent 权限与协作](../../fields/agents/permissions-isolation-collaboration.md)：区分身份、授权、执行隔离和资源预算，避免把一种机制当作完整安全边界。优先级：选读。
