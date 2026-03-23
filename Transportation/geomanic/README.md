# Geomanic

> 查询和管理 Geomanic GPS 出行数据——隐私优先的 GPS 追踪服务

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Geomanic |
| **作者** | weltspion |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/weltspion-geomanic |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/weltspion/geomanic |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询个人 GPS 出行记录和轨迹
- 管理位置数据（添加、查看、删除）
- 隐私优先的设计保护位置数据安全
- 支持出行统计和分析

## 使用场景
- 回顾和分析过去一周的出行轨迹
- 管理个人位置数据的隐私设置

## 依赖和前提条件
- API Key（Geomanic）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
