# FOSMVVM Fields Generator

> 自动生成带验证规则的 FOSMVVM Fields 协议定义和 FormField 表单字段配置

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | FOSMVVM Fields Generator |
| **作者** | foscomputerservices |
| **版本** | 2.0.6 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/foscomputerservices-fosmvvm-fields-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/foscomputerservices/fosmvvm-fields-generator |
| **安全评级** | 🟢 Low |

## 功能概述
- 生成 FOSMVVM Fields 协议代码
- 自动添加字段验证规则
- 支持多种 FormField 类型定义
- 验证逻辑自动绑定
- Swift 代码格式化输出
- 支持自定义验证规则扩展

## 使用场景
- iOS/macOS 开发中快速生成表单模型代码
- FOSMVVM 架构项目的字段定义自动化
- 减少重复性的表单验证代码编写

## 依赖和前提条件
- FOSMVVM 框架项目环境
- Swift 开发环境
- OpenClaw 环境已配置

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `reference.md`

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
