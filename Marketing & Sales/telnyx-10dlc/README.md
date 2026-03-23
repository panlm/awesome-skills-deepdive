# 10dlc Registration

> Register for 10DLC as a sole proprietor to enable SMS messaging in the USA. Use when setting up A2P SMS, registering brands/campaigns, or assigning phone numbers for compliant US messaging. Requires Telnyx CLI.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | 10dlc Registration |
| **作者** | teamtelnyx |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/teamtelnyx-telnyx-10dlc |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teamtelnyx/telnyx-10dlc |
| **安全评级** | 🟡 Medium |

## 功能概述
- Telnyx CLI installed: `npm install -g @telnyx/api-cli`
- API key configured: `telnyx auth setup`
- At least one US phone number
- Telnyx docs: https://developers.telnyx.com/docs/messaging/10dlc
- Support portal: https://support.telnyx.com
- API status: https://status.telnyx.com

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 依赖和前提条件
- Node.js / npm
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config.json`
- `scripts`
- `setup.sh`
- `test.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23