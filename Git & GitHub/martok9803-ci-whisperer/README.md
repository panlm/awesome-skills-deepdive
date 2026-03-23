# CI Whisperer

> 分析 GitHub Actions 构建失败日志，定位根因并提出最小修复方案，像资深工程师做"CI 验尸"。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CI Whisperer |
| **作者** | martok9803 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/martok9803-martok9803-ci-whisperer |

## 功能概述
- 接受工作流运行 URL、运行 ID 或 PR 编号作为输入
- 通过 GitHub CLI（`gh`）获取运行元数据和失败日志
- 生成"CI 验尸报告"：失败的 Job/Step、错误摘录、根因分析
- 按可能性排序列出修复选项，附带置信度评级
- 默认只读模式，不推送代码或创建分支
- 可选 PR 修复模式（需用户明确请求 + 环境变量 `CI_WHISPERER_WRITE=1`）

## 使用场景
- CI 构建失败时快速定位根因，不用手动翻阅大量日志
- 为新加入团队的开发者解释 CI 失败原因和修复方法
- 自动化处理频繁的 CI 失败并可选生成修复 PR

## 依赖和前提条件
- GitHub CLI（`gh`）已安装并认证
- 可选环境变量：`CI_WHISPERER_WRITE=1`（启用 PR 修复模式）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
