# GDPR Cookie Consent

> GDPR Cookie 合规管理工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | GDPR Cookie Consent |
| **作者** | metehan777 |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/metehan777-gdpr-cookie-consent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/metehan777/gdpr-cookie-consent |
| **安全评级** | 🟡 Medium |

## 功能概述
- Your website has visitors from the EU
- Your website has visitors from California
- You use cookies for analytics (Google Analytics)
- You use cookies for advertising (Google Ads, Facebook Pixel)
- You use third-party services that set cookies
- You process any personal data via cookies
- GDPR: Up to €20 million or 4% of global annual turnover
- CCPA: $2,500 - $7,500 per violation

## 使用场景
- 管理网站的 Cookie 同意设置
- 确保 GDPR 隐私合规性
- 生成隐私政策和同意记录

## 依赖和前提条件
- Node.js / npm

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
