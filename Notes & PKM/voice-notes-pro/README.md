# Voice Notes Pro

> 专业语音笔记 — 语音转文字记录和智能管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Voice Notes Pro |
| **作者** | toniaczlog |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/toniaczlog-voice-notes-pro |
| **安全评级** | 🟡 Medium |

## 功能概述
- 语音转文字记录功能
- 语音笔记分类和管理
- 关键词提取和搜索
- 多语言语音识别支持

## 使用场景
- 通过 AI Agent 快速创建和管理笔记内容
- 搜索和检索历史笔记信息
- 笔记自动分类、标注和整理

## 依赖和前提条件
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。越权操作：需要提权或管理员权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23