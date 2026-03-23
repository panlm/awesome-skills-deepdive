# dep-audit

> 审计项目依赖中的已知漏洞（CVE），支持 npm、pip、cargo 等包管理器

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | dep-audit |
| **作者** | tkuehnl |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/tkuehnl-dep-audit |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tkuehnl/dep-audit |
| **安全评级** | 🟡 Medium |

## 功能概述
- 扫描项目依赖中的已知安全漏洞
- 支持 npm、pip、cargo 等多种包管理器
- 生成漏洞详情报告（CVE 编号、严重等级）
- 提供修复建议和升级路径

## 使用场景
- 发布前自动审计项目的所有依赖安全性
- 定期检查项目依赖是否存在新发现的漏洞

## 依赖和前提条件
- 对应的包管理器（npm/pip/cargo 等）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；供应链风险：需要安装外部包且含管道安装

> 本文档由 awesome-skills-deepdive skill 自动生成
