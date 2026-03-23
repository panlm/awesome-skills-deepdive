# Paid Advertising

> 为个人创业者规划、投放和优化付费广告活动的完整指南

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Paid Advertising |
| **作者** | jk-0001 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/jk-0001-paid-advertising |

## 功能概述
- 评估是否已准备好投放付费广告（漏斗就绪检查）
- 多平台对比选择指南：Google Ads、Facebook/Instagram、LinkedIn、YouTube、Twitter 等
- 广告活动结构设计：账户、广告系列、广告组、广告素材层级
- 广告文案和创意撰写指导
- 受众定位和预算分配策略
- 转化追踪设置和效果优化方法
- 各平台的典型 CPC 参考和优劣势分析

## 使用场景
- 首次投放付费广告时，决定选择哪个平台和如何分配预算
- 优化现有广告活动的投放效果和投资回报率
- 学习从零开始设置 Google/Facebook 广告系列

## 依赖和前提条件
- 无技术依赖，作为策略指导型 skill 运行
- 建议搭配 unit-economics skill 使用（确保 LTV > CAC）
- 建议至少有 $500-1000 的测试预算

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23