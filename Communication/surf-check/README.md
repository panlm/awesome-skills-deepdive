# Surf Check

> 冲浪条件预报决策引擎，分析浪况数据输出是否适合冲浪的判断与告警

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Surf Check |
| **作者** | kevinmcnamee |
| **版本** | 0.2.2 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/kevinmcnamee-surf-check |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kevinmcnamee/surf-check |
| **安全评级** | 🔴 High |

## 功能概述
- 获取指定海滩的实时浪况和天气数据
- 分析浪高、周期、风向等关键冲浪参数
- 输出明确的「可冲浪/不可冲浪」决策建议
- 支持多个冲浪点的条件对比
- 可配置个人偏好的浪况阈值
- 定时检查并在条件达标时主动告警

## 使用场景
- 冲浪爱好者每日检查最佳冲浪时段
- 出行前快速评估多个海滩的冲浪条件
- 设置浪况告警在理想条件出现时收到通知

## 依赖和前提条件
- 冲浪预报数据源访问（如 Surfline 等）
- 指定冲浪地点坐标或名称

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `scripts`
- `src`
- `tsconfig.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
