# Capability Scope Expansion Watcher

> 检测技能跨版本的渐进式能力范围扩张——发现通过小幅、看似合理的更新逐步扩大权限的模式，这些更新单独看不触发警报，但累积后大幅扩展了攻击面。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Capability Scope Expansion Watcher |
| **作者** | andyxinweiminicloud |
| **版本** | 1.1.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-capability-scope-expansion-watcher |

## 功能概述
- 追踪技能跨版本的能力范围演变历史
- 计算每个版本的权限增量（声明的和实际的）
- 评估自初始版本以来的累积范围扩张
- 分析步长模式，识别渐进式权限蠕变
- 检测风险等级矛盾（v1.1 新增功能）
- 支持指定版本范围评估累积扩张程度
- 识别已安装技能列表中哪些技能发生了权限漂移

## 使用场景
- 定期审计已安装技能的版本更新，检测隐蔽的权限扩张
- 在技能升级前对比新旧版本的权限范围变化
- 安全团队对 Agent 生态系统中的"温水煮青蛙"式攻击进行防御

## 依赖和前提条件
- curl
- Python 3

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。信息采集：大量系统信息采集

---
> 本文档由 awesome-skills-deepdive skill 自动生成
