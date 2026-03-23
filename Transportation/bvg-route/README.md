# BVG (Berliner Verkehrsbetriebe) Route Planner

> 柏林公共交通（BVG）路线规划工具，使用 v6.bvg.transport.rest API

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | BVG (Berliner Verkehrsbetriebe) Route Planner |
| **作者** | jaysonsantos |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/jaysonsantos-bvg-route |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jaysonsantos/bvg-route |
| **安全评级** | 🟢 Low |

## 功能概述
- 柏林公共交通路线规划和导航
- 获取地铁、公交、电车的实时出发时间
- 查询站点信息和换乘方案
- 支持地址和坐标搜索

## 使用场景
- 规划从柏林亚历山大广场到勃兰登堡门的公交路线
- 查看柏林某地铁站接下来的出发时刻

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
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；混淆/反分析：使用编码/解码操作

> 本文档由 awesome-skills-deepdive skill 自动生成
