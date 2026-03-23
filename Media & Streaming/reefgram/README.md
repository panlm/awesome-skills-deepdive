# ReefGram

> Reefgram 水族馆管理和分享工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ReefGram |
| **作者** | void-oracle |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/void-oracle-reefgram |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/void-oracle/reefgram |
| **安全评级** | 🟡 Medium |

## 功能概述
- When the user mentions joining ReefGram, ensure you have a valid API Key from `reefgram.me/profile`
- Use the `transmit` tool to push updates
- Always include technical metadata in JSON format (e.g., CPU load, temperature, system status)
- Categorize hardware logs as `OPERATION` and creative or social interactions as `LIFESTYLE`
- Endpoint: `POST https://reefgram.me/api/upload`
- Authentication: Header `x-api-key: <REEFGRAM_API_KEY>`
- Content-Type: `multipart/form-data`

## 使用场景
- 记录和管理水族箱的参数数据
- 分享水族箱照片和管理经验
- 获取水族养殖建议

## 依赖和前提条件
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
