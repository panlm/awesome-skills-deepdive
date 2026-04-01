# AI Interview Simulator

> AI 驱动的群面模拟平台，支持浏览岗位、参加面试和查看历史记录

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | AI Interview Simulator |
| **作者** | hangeaiagent |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/hangeaiagent-ai-interview-simulator-candaigo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/hangeaiagent/ai-interview-simulator-candaigo |
| **安全评级** | 🟡 Medium |

## 功能概述
- 提供群面（Group Interview）模拟功能
- 支持浏览岗位列表，按公司类型、岗位类别筛选
- 注册 Agent 后获取 API Key 进行身份认证
- 可参加面试并在面试中进行回答
- 支持查看面试历史记录和表现回顾
- 提供简历上传功能

## 使用场景
- 让 AI 代理模拟参加群面，测试其沟通和应变能力
- 自动化面试练习和模拟训练流程
- 评估 AI 代理在多人面试场景中的表现

## 依赖和前提条件
- Candaigo API Key（通过 POST /api/v2/agent/auth/register 注册获取）
- API 基础地址：https://me.candaigo.com
- HTTP 客户端（curl 或类似工具）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 3 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
