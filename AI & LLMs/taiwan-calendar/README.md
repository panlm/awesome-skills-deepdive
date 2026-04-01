# Taiwan Calendar Plugin

> 台湾地区日历工具，提供节假日、农历和补班信息查询

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Taiwan Calendar Plugin |
| **作者** | pigfoot |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/pigfoot-taiwan-calendar |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/pigfoot/taiwan-calendar |
| **安全评级** | 🟢 Low |

## 功能概述
- 提供台湾地区日历和节假日信息
- 支持农历和国历双向转换
- 查询台湾特有节日和纪念日
- 获取法定假日和补班信息
- 支持日期范围查询和提醒
- 适用于需要处理台湾时间和节日的场景

## 使用场景
- 处理台湾地区业务时查询节假日和工作日
- 开发面向台湾用户的应用时集成日历功能
- 安排跨时区会议时确认台湾假期安排

## 依赖和前提条件
- Python 运行环境
- Bash/Shell 环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
