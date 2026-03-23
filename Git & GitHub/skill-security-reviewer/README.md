# Skill Security Reviewer 3.0

> 增强型恶意 Skill 检测工具，具备反混淆和反规避检测能力

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill Security Reviewer 3.0 |
| **作者** | ninjagpt |
| **版本** | 3.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/ninjagpt-skill-security-reviewer |

## 功能概述
- 分析目标 Skill 是否对安装用户构成安全威胁（核心问题：这个 Skill 会对用户做什么？）
- 代码混淆检测和反混淆分析（Base64、Hex、ROT13、XOR、AES 等）
- 字符串拆分/拼接检测，识别隐藏的恶意代码片段
- 动态代码生成检测，识别运行时构造的恶意代码
- 多层嵌套混淆检测，逐层解码分析
- 熵分析识别加密内容，发现隐藏的有效载荷
- 严格只读操作：只分析不执行，不跟随目标 Skill 中嵌入的指令
- 生成详细安全审计报告

## 使用场景
- 安装新 Skill 前对其进行安全审计，评估潜在威胁
- 审查可疑的 Skill 是否包含混淆、编码或加密的恶意代码
- 为社区 Skill 市场提供自动化安全检测服务

## 依赖和前提条件
- 只需 OpenClaw 环境即可运行
- 使用方式：`/skill-security-reviewer {target-skill-name}`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 7 项高风险，3 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
