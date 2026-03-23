# google-analytics-api

> 通过 Maton 网关集成 Google Analytics Admin 和 Data API

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | google-analytics-api |
| **作者** | rich-song |
| **ClawHub** | https://clawskills.sh/skills/rich-song-google-analytics-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/rich-song/google-analytics-api |
| **安全评级** | 🟡 Medium |

## 功能概述
- 管理 Google Analytics 账户和属性（Admin API）
- 运行分析报告（Data API）：会话、用户、页面浏览等
- 创建和管理数据流
- 通过 Maton 网关进行 OAuth 托管认证
- 支持转化事件、自定义维度/指标
- 实时报告和漏斗分析

## 使用场景
- 程序化获取 Google Analytics 报告数据
- 管理多个 GA4 属性和数据流
- 自动化分析报告生成

## 依赖和前提条件
- `MATON_API_KEY` 环境变量（maton.ai 注册获取）
- Google Analytics 账户和 OAuth 连接

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，API 使用指南 |
| LICENSE.txt | 许可证 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 使用 curl 调用 API |
| SEC-02 数据外泄 | 🟡 Medium | 数据通过 Maton 网关（gateway.maton.ai）代理到 Google |
| SEC-03 凭证获取 | 🟡 Medium | 通过 Maton 代理管理 Google OAuth，API Key 从环境变量读取 |
| SEC-04 供应链风险 | 🟡 Medium | 完全依赖 Maton (maton.ai) 作为 API 代理，所有请求经过第三方 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 在 OAuth 授权范围内 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可查询 GA 分析数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 所有 API 调用通过 Maton 第三方网关代理，数据和凭证经过第三方服务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
