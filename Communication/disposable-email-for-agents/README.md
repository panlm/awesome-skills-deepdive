# Disposable Email For Agents

> 为 AI 智能体提供一次性邮箱服务，可创建临时邮件地址用于注册、验证等场景

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Disposable Email For Agents |
| **作者** | prashantrohilla-max |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/prashantrohilla-max-disposable-email-for-agents |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/prashantrohilla-max/disposable-email-for-agents |
| **安全评级** | 🟢 Low |

## 功能概述
- 即时创建临时邮件地址
- 接收和读取邮件内容
- 自动提取验证码和确认链接
- 邮箱到期自动销毁
- 支持多个临时邮箱并行使用
- 无需注册真实邮箱账号

## 使用场景
- 智能体自动注册网站账号时的邮箱验证
- 测试邮件发送功能时的接收端
- 保护隐私避免暴露真实邮箱地址

## 依赖和前提条件
- OpenClaw 环境已配置
- 一次性邮箱服务 API 访问权限

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖；混淆/反分析：使用编码/解码操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
