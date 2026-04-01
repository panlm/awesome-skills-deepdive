# Pincer

> 安全优先的 Skill 安装包装器，在安装前扫描恶意软件、提示注入和可疑模式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Pincer |
| **作者** | panzacoder |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/panzacoder-pincer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/panzacoder/pincer |
| **安全评级** | 🔴 High |

## 功能概述
- 在安装 Skill 前进行全面安全扫描
- 检测恶意软件、提示注入和可疑代码模式
- 集成 mcp-scan 进行深度安全分析
- 可替代 clawhub install 进行更安全的 Skill 管理
- 支持仅扫描模式（pincer scan）不执行安装
- 应对 ClawHub 生态中已知的恶意 Skill 攻击活动

## 使用场景
- 在安装社区 Skill 前进行安全审查，防止信息窃取
- 定期扫描已安装的 Skill 检查安全风险
- 在团队中推行安全的 Skill 安装流程

## 依赖和前提条件
- mcp-scan 工具
- clawhub CLI

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
