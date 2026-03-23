# contract diagram

> 合同结构可视化工具，将合同关系图表化

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | contract diagram |
| **作者** | nonlinear |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/nonlinear-contract-diagram |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/nonlinear/contract-diagram |
| **安全评级** | 🟡 Medium |

## 功能概述
- 将合同条款关系可视化
- 生成合同结构图表
- 识别关键条款和依赖关系
- 支持多方合同关系展示

## 使用场景
- 将复杂的商业合同可视化为结构图便于审查
- 展示多方合约的权利义务关系

## 依赖和前提条件
- GitHub API
- Webhook 配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `github-markdown.css`
- `index.html`
- `marked.min.js`
- `mermaid.min.js`
- `serve.sh`
- `server.js`
- `styles.css`

## 详细安全审计
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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23