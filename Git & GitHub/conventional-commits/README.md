# Conventional Commits

> 按照 Conventional Commits 规范格式化提交消息，确保提交遵循标准格式以支持自动化工具、变更日志生成和语义化版本管理。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Conventional Commits |
| **作者** | bastos |
| **版本** | 2.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/bastos-conventional-commits |

## 功能概述
- 强制执行 Conventional Commits 规范的提交消息格式：`<type>[scope]: <description>`
- 支持完整的提交类型：feat、fix、docs、style、refactor、perf、test、build、ci、chore、revert
- 可选 Scope 提供代码库区域的上下文信息
- 支持 Body（详细描述）和 Footer（Breaking Changes、Issue 引用等）
- 与语义化版本关联：feat → MINOR、fix → PATCH、BREAKING CHANGE → MAJOR
- 提供清晰的描述规范：祈使语气、小写开头、不加句号

## 使用场景
- 在创建 Git 提交时自动生成符合 Conventional Commits 规范的消息
- 团队协作中统一提交消息格式，便于自动生成 CHANGELOG
- 结合 CI/CD 工具链实现基于提交消息的自动语义化版本发布

## 依赖和前提条件
- Git
- 无额外依赖

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成
