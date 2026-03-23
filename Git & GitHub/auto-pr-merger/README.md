# Auto Pr Merger

> 自动化 GitHub PR 工作流：检出分支、运行测试、尝试修复失败并自动合并

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Auto Pr Merger |
| **作者** | autogame-17 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/autogame-17-auto-pr-merger |

## 功能概述
- 使用 `gh pr checkout` 自动检出指定的 GitHub PR
- 运行用户指定的测试命令验证代码质量
- 测试失败时自动读取输出，尝试修复代码并重新测试
- 支持配置最大重试次数（默认 3 次）
- 测试通过后自动使用 `gh pr merge --merge --auto` 合并 PR
- 每次修复后自动提交并推送变更

## 使用场景
- 自动化处理简单的 PR 合并流程，减少人工干预
- 在 CI 环境中对 PR 进行自动化测试和修复尝试
- 批量处理多个待合并的 PR

## 依赖和前提条件
- `gh` CLI 已安装并完成身份验证
- Node.js 运行环境
- 需要指定测试命令（如 `npm test`、`pytest`）

## 安全状态

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
