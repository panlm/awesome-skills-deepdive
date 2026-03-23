# subreddit-scout

> 为产品或话题智能匹配高相关度的 subreddit 社区，总结版规并生成增值型首帖建议

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | subreddit-scout |
| **作者** | xammarie |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/xammarie-subreddit-scout |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xammarie/subreddit-scout |
| **安全评级** | 🟢 Low |

## 功能概述
- 根据产品特征智能匹配相关 subreddit
- 自动抓取并总结目标 subreddit 的社区规则
- 分析社区氛围和内容偏好
- 生成符合社区调性的增值型首帖建议
- 评估各 subreddit 的活跃度和受众匹配度
- 避免纯广告内容，确保帖子提供真实价值

## 使用场景
- 新产品推广时寻找合适的 Reddit 社区并制定发帖策略
- 内容营销团队批量调研 Reddit 渠道机会
- 独立开发者在 Reddit 做产品冷启动推广

## 依赖和前提条件
- Reddit 账户或 API 访问
- 产品或话题的描述信息

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
