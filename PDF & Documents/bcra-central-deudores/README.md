# Central de Deudores BCRA

> 阿根廷央行债务人查询工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Central de Deudores BCRA |
| **作者** | ferminrp |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/ferminrp-bcra-central-deudores |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ferminrp/bcra-central-deudores |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询 BCRA 中央债务人系统
- 债务信息检索
- 信用状态报告
- 数据格式化输出

## 使用场景
- 查询个人或企业在阿根廷央行的债务记录
- 生成信用状态报告用于风险评估

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`

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