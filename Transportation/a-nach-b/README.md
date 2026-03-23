# A nach B - AT Public Transport Service (VOR)

> 奥地利公共交通查询工具，通过 VOR AnachB API 获取实时出发信息、路线规划和站点搜索

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | A nach B - AT Public Transport Service (VOR) |
| **作者** | manmal |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/manmal-a-nach-b |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/manmal/a-nach-b |
| **安全评级** | 🟢 Low |

## 功能概述
- 查询奥地利全境公共交通路线和换乘方案
- 获取指定站点的实时出发时刻表
- 支持地理坐标和站点名称搜索最近站点
- 获取站点详细信息（ID、坐标、交通方式）
- 支持地铁、公交、电车、火车等多种交通方式

## 使用场景
- 在奥地利旅行时查询维也纳到萨尔茨堡的公共交通方案
- 查看某个站点接下来半小时的实时出发列表
- 根据当前位置搜索附近的公共交通站点

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
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

> 本文档由 awesome-skills-deepdive skill 自动生成
