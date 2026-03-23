# Email Capture Generator

> 使用经过验证的 5 段式转化框架构建高转化率的引流磁铁、挤压页和邮件捕获漏斗

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Email Capture Generator |
| **作者** | cameron-jovan |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/cameron-jovan-email-capture-generator |

## 功能概述
- 基于 5 段式转化框架生成页面：Hook（英雄区）→ Value（价值展示）→ Proof（社会证明）→ Urgency（紧迫感）→ Reassurance（信任保障）
- 生成包含邮件输入框和 CTA 按钮的注册表单
- 自动生成感谢页面和交付自动化钩子
- 支持多种引流磁铁类型：电子书、清单、模板、网络研讨会等
- 提供模板变量系统，方便快速替换标题、利益点、CTA 文案等
- 内置社会证明区块（订阅者数量、用户评价）

## 使用场景
- 快速为新产品或内容创建专业的邮件列表注册着陆页
- 为网络研讨会或免费资源构建完整的邮件捕获漏斗

## 依赖和前提条件
- 无外部依赖（纯模板/框架指导型 Skill）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
