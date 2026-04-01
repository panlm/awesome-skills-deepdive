# Agent Registry

> Agent 懒加载注册表——将上下文窗口中的 Agent 令牌开销减少 70-90%

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Registry |
| **作者** | matrixy |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/matrixy-agent-registry |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-registry |
| **安全评级** | 🔴 High |

## 功能概述
- 从"全量加载"转为"按需加载"：仅在需要时才加载相关 Agent
- 实测 140 个 Agent 场景下节省 83% 令牌（16.4k → 2.7k）
- 内置 BM25 搜索引擎：自动分析用户输入并匹配相关 Agent
- UserPromptSubmit Hook 实现完全自动的 Agent 发现
- 索引一次后按需加载，启动速度大幅提升
- 解决 Agent 数量增长导致的上下文窗口膨胀问题

## 使用场景
- 安装了大量 Agent/Skill 的环境下优化上下文窗口利用率
- 减少每次对话的令牌消耗，降低 API 调用成本
- 加速 Agent 系统启动时间，改善用户体验

## 依赖和前提条件
- Node.js / npm（Bun 运行时）
- install.sh 安装脚本

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
