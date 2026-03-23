# Translink CLI

> 查询和解释 Translink SEQ（布里斯班）的 GTFS 静态和实时公共交通数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Translink CLI |
| **作者** | alanburchill |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/alanburchill-translink-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/alanburchill/translink-cli |
| **安全评级** | 🟢 Low |

## 功能概述
- 查询布里斯班及东南昆士兰地区的公共交通数据
- 支持 GTFS 静态时刻表和实时数据
- 排查公共交通问题和延误
- 解释公共交通数据格式

## 使用场景
- 查询布里斯班某站点的下一班公交到达时间
- 排查 Translink 公共交通的实时数据问题

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

> 本文档由 awesome-skills-deepdive skill 自动生成
