# gotrain

> 纽约 MTA 系统列车出发查询（地铁、LIRR、Metro-North）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gotrain |
| **作者** | gumadeiras |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/gumadeiras-gotrain |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/gumadeiras/gotrain |
| **安全评级** | 🟢 Low |

## 功能概述
- 查询纽约地铁实时出发信息
- 获取 LIRR（长岛铁路）时刻表
- 查看 Metro-North 通勤铁路出发时间
- 支持按站点和线路查询

## 使用场景
- 查看曼哈顿某地铁站接下来的列车出发时间
- 查询 LIRR 从宾夕法尼亚站的下一班出发

## 依赖和前提条件
- Node.js / npm（MTA 公开 API）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖

> 本文档由 awesome-skills-deepdive skill 自动生成
