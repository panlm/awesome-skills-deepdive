# SkillBench

> 跟踪 Skill 版本、基准测试性能、对比改进效果，获取自我改进信号

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | SkillBench |
| **作者** | g9pedro |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/g9pedro-skillbench |

## 功能概述
- 跟踪 Skill 版本并记录每次使用的基准数据（成功率、耗时、错误类型）
- 自动从 tasktime 拉取任务耗时数据
- 评分和评级系统（A+ 到 D），基于成功率、平均耗时、一致性和趋势
- 版本对比功能：直观比较不同版本的性能差异
- 基线管理和回归检测：设置基线后自动检测性能退化
- 自动化测试：运行冒烟测试和完整测试套件
- 生成 HTML 仪表板、Markdown/JSON 报告和 shields.io 徽章
- CI/CD 集成：提供 GitHub Actions 工作流模板
- 健康监控：定时检查所有 Skill 状态并生成告警
- 与 ClawVault 生态系统集成同步

## 使用场景
- 持续跟踪 AI Agent 使用的各个 Skill 性能，识别需要改进的短板
- 在 Skill 升级后对比新旧版本性能，验证改进效果或检测回归
- 在 CI/CD 流水线中集成 Skill 基准测试，确保代码变更不影响 Skill 性能

## 依赖和前提条件
- 安装 SkillBench CLI：`npm install -g @versatly/skillbench`
- 可选集成 [tasktime](https://clawhub.com/skills/tasktime) 用于自动耗时采集
- 可选集成 [ClawVault](https://clawvault.dev) 用于数据同步

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
