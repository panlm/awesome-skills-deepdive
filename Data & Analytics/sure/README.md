# sure

> 从 Sure 个人财务面板获取财务报告

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sure |
| **作者** | bt0r |
| **ClawHub** | https://clawskills.sh/skills/bt0r-sure |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bt0r/sure |
| **安全评级** | 🟢 Low |

## 功能概述
- 列出所有账户余额
- 获取财务报告数据
- 通过 API Key 认证

## 使用场景
- 查看个人财务账户汇总
- 集成财务数据到自动化工作流

## 依赖和前提条件
- `SURE_API_KEY` 和 `SURE_BASE_URL` 环境变量
- Sure 应用实例

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，API 使用方法 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅使用 curl 调用 API |
| SEC-02 数据外泄 | 🟢 Safe | 仅与用户指定的 Sure 实例通信 |
| SEC-03 凭证获取 | 🟢 Safe | 从环境变量读取 API Key |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 只读 API 调用 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 获取财务数据（敏感信息） |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码极其简洁 |

**综合评级: 🟢 Low**
**风险摘要:** 简洁的财务数据 API 客户端，注意财务数据的敏感性

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
