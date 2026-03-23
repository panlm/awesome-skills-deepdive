# Metra Skill

> 芝加哥 Metra 通勤铁路查询——实时列车到达、车辆追踪和服务告警

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Metra Skill |
| **作者** | brianleach |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/brianleach-metra |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianleach/metra |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询 Metra 列车的实时到达时间
- 追踪列车实时位置
- 获取服务告警和延误通知
- 查看线路时刻表和站点信息

## 使用场景
- 查看芝加哥联合车站接下来的 Metra 列车出发时间
- 检查 Metra 线路的实时服务状态和延误

## 依赖和前提条件
- API Key（Metra）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
