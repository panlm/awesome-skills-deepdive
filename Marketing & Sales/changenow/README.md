# Changenow

> ChangeNow 加密货币兑换工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Changenow |
| **作者** | yakelb0815 |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/yakelb0815-changenow |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yakelb0815/changenow |
| **安全评级** | 🟢 Low |

## 功能概述
- 加密货币即时兑换
- 汇率查询和比较
- 交易状态追踪
- 多种加密货币支持

## 使用场景
- 快速进行加密货币兑换交易
- 查询和比较不同加密货币的兑换汇率

## 依赖和前提条件
- API 密钥
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23