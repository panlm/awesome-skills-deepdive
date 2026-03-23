# captchas-openclaw

> OpenClaw 集成 CAPTCHAS Agent API 的指导，包含工具注册和验证流程

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | captchas-openclaw |
| **作者** | captchasco |
| **ClawHub** | https://clawskills.sh/skills/captchasco-captchas-openclaw |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/captchasco/captchas-openclaw |
| **安全评级** | 🟢 Low |

## 功能概述
- CAPTCHAS 验证决策（allow/deny/challenge）
- 挑战完成与令牌铸造
- 令牌验证 API
- OpenResponses 工具 Schema
- OpenClaw 插件工具注册示例

## 使用场景
- 为 AI 代理集成人机验证功能
- 在 OpenClaw Gateway 中注册 CAPTCHAS 工具

## 依赖和前提条件
CAPTCHAS_API_KEY, CAPTCHAS_ENDPOINT 环境变量

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 纯 API 文档和 Schema 定义 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 CAPTCHAS API 发送请求 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 CAPTCHAS_API_KEY 环境变量 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部 CAPTCHAS 服务 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | API 调用有明确权限边界 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可传递 signals 对象到外部服务 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰 |

**综合评级: 🟢 Low**
**风险摘要:** API 集成指南，实际风险取决于 CAPTCHAS 服务本身

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
