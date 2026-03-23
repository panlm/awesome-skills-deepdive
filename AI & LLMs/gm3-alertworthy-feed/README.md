# GM3 Alertworthy Feed

> 智能过滤和推送值得关注的新闻和信息流

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | GM3 Alertworthy Feed |
| **作者** | bigbadman-lab |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/bigbadman-lab-gm3-alertworthy-feed |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bigbadman-lab/gm3-alertworthy-feed |
| **安全评级** | 🟡 Medium |

## 功能概述
- 基于 AI 智能判断信息的重要程度和值得关注度
- 从多个信息源聚合内容并进行过滤
- 自动识别和推送高价值、值得警觉的新闻
- 支持自定义关注主题和过滤规则
- 提供简洁的摘要和重要性评分

## 使用场景
- 每日自动筛选重要新闻，避免信息过载
- 监控特定领域的关键动态和突发事件
- 为决策者提供经过 AI 筛选的高质量信息流

## 依赖和前提条件
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
