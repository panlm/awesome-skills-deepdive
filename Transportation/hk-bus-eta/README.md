# Hong Kong Bus ETA | 香港巴士預計到達時間

> 香港巴士到站时间查询（KMB/CTB/LWB），支持模糊站名匹配和多巴士公司

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Hong Kong Bus ETA | 香港巴士預計到達時間 |
| **作者** | tomfong |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/tomfong-hk-bus-eta |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tomfong/hk-bus-eta |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询九巴（KMB）、城巴（CTB）、龙运（LWB）的实时到站时间
- 支持中英文模糊站名匹配搜索
- 同时显示多家巴士公司的到站信息
- 获取巴士路线和站点详细信息

## 使用场景
- 在香港等车时查看下一班巴士的预计到站时间
- 搜索到达某目的地的巴士路线和换乘方案

## 依赖和前提条件
- Node.js / npm（使用公开 API）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成
