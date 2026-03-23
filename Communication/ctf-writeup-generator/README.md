# CTF Writeup Generator

> 自动从 CTF 竞赛解题过程生成专业的 Writeup 报告，包含完整的解题思路和技术细节

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | CTF Writeup Generator |
| **作者** | akhmittra |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/akhmittra-ctf-writeup-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/akhmittra/ctf-writeup-generator |
| **安全评级** | 🔴 High |

## 功能概述
- 自动记录和整理解题步骤
- 生成结构化的 Writeup 报告
- 支持多种 CTF 题目类型（Web、Pwn、Crypto、Reverse 等）
- 自动插入代码片段和截图说明
- Markdown 格式输出便于分享
- 支持团队协作编辑报告

## 使用场景
- CTF 竞赛后快速生成解题报告
- 安全团队知识沉淀与技术分享
- CTF 学习者整理练习笔记

## 依赖和前提条件
- OpenClaw 环境已配置
- CTF 解题过程的原始记录或终端日志

## 包含文件
- `ORIGINAL_README.md`
- `QUICKSTART.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `example_writeup.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
