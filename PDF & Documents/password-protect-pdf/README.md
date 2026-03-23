# Protect PDF with password

> 为 PDF 文件添加密码保护

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Protect PDF with password |
| **作者** | crossservicesolutions |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/crossservicesolutions-password-protect-pdf |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/crossservicesolutions/password-protect-pdf |
| **安全评级** | 🟡 Medium |

## 功能概述
- 为 PDF 设置打开密码
- 配置 PDF 权限密码
- 支持多种加密级别
- 批量处理多个 PDF 文件

## 使用场景
- 为包含敏感信息的 PDF 文件设置密码保护
- 批量为归档文档添加访问密码

## 依赖和前提条件
- API 密钥
- Bearer Token
- Python 运行环境

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `examples`
- `requirements.txt`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23