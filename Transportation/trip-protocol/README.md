# Trip Protocol

> 旅行协议——结构化的旅行计划和信息管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Trip Protocol |
| **作者** | reggie-sporewell |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/reggie-sporewell-trip-protocol |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/reggie-sporewell/trip-protocol |
| **安全评级** | 🟡 Medium |

## 功能概述
- 结构化管理旅行计划和行程
- 统一的旅行信息存储格式
- 行程共享和协作功能
- 旅行数据导入导出

## 使用场景
- 创建结构化的旅行计划文档
- 与旅伴共享和协作编辑行程

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
