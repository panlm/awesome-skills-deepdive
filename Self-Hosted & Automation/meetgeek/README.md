# meetgeek

> 从 CLI 查询 MeetGeek 会议智能 - 摘要、转录、行动项

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | meetgeek |
| **作者** | nexty5870 |
| **ClawHub** | https://clawskills.sh/skills/nexty5870-meetgeek |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nexty5870/meetgeek |
| **安全评级** | 🟡 Medium |

## 功能概述
- 列出最近会议记录
- 获取 AI 摘要和行动项
- 获取完整转录文本
- 获取会议高亮内容
- 跨会议自然语言搜索
- 支持文件导出

## 使用场景
- 快速查看最近会议摘要和行动项
- 搜索特定话题的讨论内容
- 导出会议转录文本

## 依赖和前提条件
- `meetgeek-cli`（npm 全局安装）
- MeetGeek API Key

## 包含文件
- `SKILL.md` — 技能定义和命令参考
- `meetgeek.sh` — CLI 封装脚本

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 通过 meetgeek CLI 操作 |
| SEC-02 数据外泄 | 🟢 Safe | 从 MeetGeek 读取数据到本地 |
| SEC-03 凭证获取 | 🟡 Medium | MeetGeek API Key 存储在本地 |
| SEC-04 供应链风险 | 🟡 Medium | npm 包依赖（meetgeek-cli） |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅导出文件到指定路径 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 只读 API 操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可获取完整会议转录（可能含敏感内容） |
| SEC-10 混淆/反分析 | 🟢 Safe | 简单 CLI 封装 |

**综合评级: 🟡 Medium**
**风险摘要:** 访问第三方会议 API 获取可能敏感的通话数据，依赖 npm 包

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
