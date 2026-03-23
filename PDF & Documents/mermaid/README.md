# Mermaid Diagrams

> Mermaid 图表渲染和生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mermaid Diagrams |
| **作者** | jarekbird |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/jarekbird-mermaid |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jarekbird/mermaid |
| **安全评级** | 🟡 Medium |

## 功能概述
- 将 Mermaid 语法转换为可视化图表
- 支持流程图、序列图、甘特图等多种类型
- 自动渲染并输出为图片格式
- 集成到文档生成工作流中

## 使用场景
- 将代码中的 Mermaid 语法自动渲染为流程图
- 为技术文档生成架构图和时序图

## 依赖和前提条件
- OAuth 认证
- npm
- GitHub API

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `generate-test.sh`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23