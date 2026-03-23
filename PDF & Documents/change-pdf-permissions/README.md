# Change permissions of PDF

> 修改 PDF 文件的权限设置

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Change permissions of PDF |
| **作者** | crossservicesolutions |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/crossservicesolutions-change-pdf-permissions |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/crossservicesolutions/change-pdf-permissions |
| **安全评级** | 🟡 Medium |

## 功能概述
- 设置 PDF 的打印权限
- 控制 PDF 的编辑权限
- 配置复制和提取权限
- 批量修改权限设置

## 使用场景
- 限制分发 PDF 的打印和编辑权限
- 为不同受众设置不同的 PDF 访问权限

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
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23