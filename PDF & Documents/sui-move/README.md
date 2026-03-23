# Sui Move

> Sui 区块链 Move 语言开发工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sui Move |
| **作者** | easonc13 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/easonc13-sui-move |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/easonc13/sui-move |
| **安全评级** | 🟡 Medium |

## 功能概述
- Sui Move 智能合约开发辅助
- Move 语言代码分析
- 合约部署和测试
- Sui 生态集成

## 使用场景
- 辅助开发和调试 Sui Move 智能合约
- 自动化 Move 合约的测试和部署

## 依赖和前提条件
- GitHub API

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `setup.sh`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23