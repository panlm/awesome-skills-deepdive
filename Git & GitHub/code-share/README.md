# Code Share

> 通过 GitHub Gist 分享代码，替代聊天中的内联代码块，适用于超过 10 行的代码输出或需要保持格式的场景。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Code Share |
| **作者** | jeromestein |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/jeromestein-code-share |

## 功能概述
- 自动判断代码长度：10 行以内使用内联代码块，超过 10 行自动创建 Gist
- 默认创建 Secret Gist，除非用户明确要求公开
- 敏感数据扫描：自动检测并替换 API Key、Token、密码等敏感信息为占位符
- 更新模式：可对已分享的 Gist 进行原地更新（保持同一 URL，新建修订版本）
- 验证 GitHub CLI 认证状态，引导用户完成 `gh auth login`
- 返回简短摘要 + Gist URL，避免在聊天中粘贴大段重复代码

## 使用场景
- 在 Discord/聊天中分享超过 10 行的代码时自动创建 Gist 链接
- 需要保持代码格式和高亮的场景，提供可复制的分享链接
- 迭代修改代码时保持同一 Gist URL，方便协作追踪

## 依赖和前提条件
- GitHub CLI（`gh`）已安装并认证
- `gh` 需具有 gist 权限 scope

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
