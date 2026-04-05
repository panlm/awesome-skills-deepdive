# jubjub

> 跨平台内容发布与团队协作平台，支持一键发布至 TikTok、Instagram、YouTube 等 8 大平台，每次发布自动生成区块链所有权证明。

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | jubjub |
| **作者** | aquaflans |
| **ClawHub** | https://clawskills.sh/skills/aquaflans-jubjub |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aquaflans/jubjub |
| **安全评级** | 🟡 Medium (中风险) |

## 功能概述

- 支持向 TikTok、Instagram、YouTube、Facebook、LinkedIn、Vimeo、Vimeo OTT、Mux 共 8 个平台发布视频内容
- 工作区（Workspace）管理：创建、更新、删除工作区，支持生成分享邀请链接
- 内容管理：创建、编辑、删除内容项，支持标签、语言、儿童内容标记等设置
- 团队协作：14 个团队管理工具，支持邀请、角色分配（OWNER/ADMIN/MANAGER/EDITOR/PUBLISHER/VIEWER）、权限管理
- 内置通信系统：支持作用域消息（团队/工作区/内容级别）、线程回复、审批决策流程
- 每次发布自动在 Base 区块链上生成不可篡改的所有权证明记录
- 支持定时发布（需包含时区偏移的 ISO 8601 格式）
- 支持通过 x402（USDC on Base）或 MPP（USDC on Tempo）进行按次付费

## 使用场景

- 内容创作者需要将同一视频同时发布到多个社交平台，并追踪发布状态
- 团队协作管理视频内容的审核、审批和发布流程
- 需要区块链验证的内容所有权证明和发布历史记录

## 依赖和前提条件

- 需要 `JUBJUB_API_KEY` 环境变量（在 jubjubapp.com → Profile → Agents → Create New Agent 获取）
- 平台连接需要用户在浏览器中完成 OAuth 授权（TikTok/Instagram/YouTube/Facebook/LinkedIn/Vimeo）
- Mux 和 Vimeo OTT 使用 API Token 连接
- 视频上传需要用户在浏览器中操作上传界面
- 免费版工作区 7 天后过期，Creator ($39 AUD/月) 和 Studio ($199 AUD/月) 提供永久工作区

## 安全状态 (ClawHub)

| 来源 | 评级 |
|---|---|
| VirusTotal | ⚪ Unknown |
| OpenClaw | ⚪ Unknown |

> ⚠️ ClawHub 页面无法访问（404），安全状态未知，已执行完整安全审计。

## 详细安全审计

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 通过 | 纯 REST API 工具定义，无 shell 命令或本地代码执行 |
| SEC-02 数据外泄 | 🟡 警告 | 核心功能即为向 8 个外部平台发送视频内容，所有数据经由 api.jubjubapp.com 中转 |
| SEC-03 凭证获取 | 🟡 警告 | 需要 JUBJUB_API_KEY 环境变量，管理 8 个平台的 OAuth 凭证，通过 credentials_connect 发起授权流程 |
| SEC-04 供应链风险 | 🟡 警告 | 依赖商业第三方服务 api.jubjubapp.com，集成 Base 区块链支付（x402 USDC）和 MPP 支付协议 |
| SEC-05 文件系统篡改 | 🟢 通过 | 无本地文件系统操作，媒体上传通过浏览器进行 |
| SEC-06 Prompt 注入 | 🟢 通过 | API 工具定义清晰，无动态代码执行或注入向量 |
| SEC-07 越权操作 | 🟡 警告 | 包含团队所有权转移工具（teams_transfer），支持 6 级角色体系的权限管理 |
| SEC-08 持久化机制 | 🟢 通过 | 无本地持久化，所有状态存储在 jubjubapp.com 云端，免费版工作区有 7 天 TTL |
| SEC-09 信息采集 | 🟡 警告 | 支持通过邮箱搜索用户资料（profiles_search），批量获取最多 50 个用户信息（profiles_batch），可访问团队活动日志 |
| SEC-10 混淆/反分析 | 🟢 通过 | 无混淆，文档详尽清晰，工具描述透明 |

**综合评级: 🟡 Medium (中风险)**

**风险摘要:** 这是一个商业内容发布平台的 skill，核心功能涉及向多个外部平台发送数据、管理 OAuth 凭证、区块链支付集成和用户信息检索，属于功能驱动的中等风险，未发现恶意行为模式。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 安全审计基于 SKILL.md 静态分析，不代表运行时行为。
> 生成时间: 2026-04-05T03:01:00Z
