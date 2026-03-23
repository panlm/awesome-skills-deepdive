# agent-browser-clawdbot

> 面向 AI 代理优化的无头浏览器自动化 CLI，使用可访问性树快照和 ref 引用选择元素

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | agent-browser-clawdbot |
| **作者** | matrixy |
| **ClawHub** | https://clawskills.sh/skills/matrixy-agent-browser-clawdbot |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-browser-clawdbot |
| **安全评级** | 🟡 Medium |

## 功能概述
- 基于可访问性树的确定性元素选择
- 完整浏览器导航（打开/后退/前进/刷新）
- 交互操作（点击/填充/悬停/拖拽）
- 会话隔离，支持多用户场景
- 状态持久化（保存/加载 cookies）
- 网络控制（拦截/模拟请求）
- 截图和 PDF 生成

## 使用场景
- 自动化多步骤 Web 工作流
- 需要确定性元素选择的浏览器测试
- Web 数据采集和表单填充

## 依赖和前提条件
agent-browser CLI 工具

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 大量 shell 命令执行指令（agent-browser open/click/fill 等） |
| SEC-02 数据外泄 | 🟡 Medium | 可通过网络请求转发数据，cookies 持久化可能泄露会话 |
| SEC-03 凭证获取 | 🟡 Medium | 状态持久化涉及 cookies/localStorage，可包含凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 agent-browser 外部 CLI |
| SEC-05 文件系统篡改 | 🟡 Medium | 截图/PDF 保存到文件系统 |
| SEC-06 Prompt 注入 | 🟡 Medium | 浏览器操作可能被恶意页面利用 |
| SEC-07 越权操作 | 🟡 Medium | 网络控制可拦截/修改请求 |
| SEC-08 持久化机制 | 🟡 Medium | 状态持久化（save/load auth.json） |
| SEC-09 信息采集 | 🟡 Medium | 可获取页面内容、cookies、localStorage |
| SEC-10 混淆/反分析 | 🟢 Safe | 指令清晰无混淆 |

**综合评级: 🟡 Medium**
**风险摘要:** 浏览器自动化工具本质上可执行广泛操作，需谨慎使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
