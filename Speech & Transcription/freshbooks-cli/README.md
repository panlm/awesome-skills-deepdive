# freshbooks-cli

> 通过 FreshBooks CLI 管理发票、费用和客户

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | freshbooks-cli |
| **作者** | haseebuchiha |
| **ClawHub** | https://clawskills.sh/skills/haseebuchiha-freshbooks-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/haseebuchiha/freshbooks-cli |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- client-id "<FRESHBOOKS_CLIENT_ID>" \
- client-secret "<FRESHBOOKS_CLIENT_SECRET>" \
- lines '[{"name":"Web Services","qty":1,"unitCost":{"amount":"15000.00","code":"USD"}},{"name":"App Services","qty":1,"unitCost":{"amount":"15000.00","code":"USD"}}]'
- All output is JSON to stdout. Pipe to `jq` for filtering: `freshbooks clients list | jq '.clients[].organization'`
- Money values are `{"amount": "string", "code": "USD"}`. The amount is always a string like `"30000.00"`, never a number. Do not use parseFloat on money.
- Tokens auto-refresh. If refresh fails, re-run `freshbooks auth login --client-id <id> --client-secret <secret> --manual`.

## 依赖和前提条件
- 
- client-id "<FRESHBOOKS_CLIENT_ID>" \
- client-secret "<FRESHBOOKS_CLIENT_SECRET>" \
- manual

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23