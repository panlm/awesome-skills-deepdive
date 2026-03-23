# Entur Travel

> 使用 Entur API 规划挪威公共交通出行，覆盖所有运营商

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Entur Travel |
| **作者** | mmichelli |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/mmichelli-entur-travel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/mmichelli/entur-travel |
| **安全评级** | 🟢 Low |

## 功能概述
- 规划挪威全境公共交通路线
- 覆盖所有挪威交通运营商（NSB、Ruter 等）
- 查询实时出发时间和换乘信息
- 支持按地点名称和坐标搜索

## 使用场景
- 规划奥斯陆到卑尔根的公共交通路线
- 查看挪威某城市的公交实时出发时刻

## 依赖和前提条件
- Node.js / npm（Entur 公开 API）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

> 本文档由 awesome-skills-deepdive skill 自动生成
