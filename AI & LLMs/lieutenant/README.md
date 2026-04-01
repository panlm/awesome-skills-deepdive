# Lieutenant - AI Agent Security

> AI 代理安全防护系统，提供实时威胁检测和行为监控

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Lieutenant - AI Agent Security |
| **作者** | jd-delatorre |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/jd-delatorre-lieutenant |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jd-delatorre/lieutenant |
| **安全评级** | 🔴 High |

## 功能概述
- 实时监控 AI 代理的行为并检测异常操作
- 提供多层安全防护机制防止恶意利用
- 检测并阻止 Prompt 注入攻击
- 监控文件系统访问和命令执行行为
- 提供详细的安全事件日志和审计跟踪
- 支持自定义安全策略和告警规则
- 与 OpenClaw 生态系统深度集成

## 使用场景
- 为生产环境中的 AI 代理部署安全防护层
- 实时检测和阻止 AI 代理的异常或危险操作
- 安全合规审计中监控 AI 系统的行为轨迹

## 依赖和前提条件
- OpenClaw 运行环境
- 安全策略配置

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
