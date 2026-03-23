# Bird DMs

> Bird 附加工具，让 AI 智能体检查和读取 X/Twitter 私信收件箱

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bird DMs |
| **作者** | tolibear |
| **版本** | 1.0.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/tolibear-bird-dms |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tolibear/bird-dms |
| **安全评级** | 🔴 High |

## 功能概述
- 读取 X/Twitter 私信收件箱
- 检查新私信通知
- 浏览私信对话列表
- 获取私信内容详情
- 作为 Bird 工具的扩展模块运行

## 使用场景
- 智能体自动监控 X/Twitter 私信并及时响应
- 定期检查私信收件箱处理用户咨询
- 将 Twitter 私信纳入统一消息管理流程

## 依赖和前提条件
- Bird 主工具已安装和配置
- X/Twitter 账号授权
- Twitter API 或登录凭证

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `dist`
- `package-lock.json`
- `package.json`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
