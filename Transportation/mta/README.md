# NYC MTA Transit

> 纽约 MTA 公共交通——实时地铁到达、公交预测、服务告警和站点信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | NYC MTA Transit |
| **作者** | brianleach |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/brianleach-mta |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianleach/mta |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询纽约地铁的实时到达时间
- 获取公交车的到站预测
- 查看 MTA 服务告警和延误信息
- 搜索站点和路线信息
- 支持 GTFS-RT 实时数据流

## 使用场景
- 查看时代广场站接下来的地铁到达时间
- 检查纽约地铁的实时服务状态
- 获取某公交路线的实时车辆位置

## 依赖和前提条件
- API Key（MTA）

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
