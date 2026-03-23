# Meetlark - coordinate a meeting

> 创建日程投票让参与者选择最佳时间，生成可分享的参与链接

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Meetlark - coordinate a meeting |
| **作者** | mkelk |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/mkelk-meetlark |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mkelk/meetlark |
| **安全评级** | 🔴 High |

## 功能概述
- 创建多时间选项的日程投票
- 生成可分享的投票参与链接
- 参与者在线投票选择可用时间
- 自动汇总投票结果确定最佳时间
- 支持人类和 AI 智能体参与投票

## 使用场景
- 团队活动时间的民主投票决策
- 跨部门会议时间的在线协调
- 多人聚会最佳日期的快速确定

## 依赖和前提条件
- MeetLark 服务账户或 API 密钥
- 网络访问权限

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
