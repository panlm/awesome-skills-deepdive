# Living Room Smoke Detector

> 客厅烟雾/火灾检测器，通过 Dirigera 空气传感器监测 PM2.5 和 CO2，超标时持续播报警报。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Living Room Smoke Detector |
| **作者** | maverick-2 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/maverick-2-living-room-smoke-detector |

## 功能概述
- 每 5 分钟直接查询 Dirigera 智能家居中枢的 ALPSTUGA 空气传感器
- 检测危险阈值：PM2.5 > 250 µg/m³ 或 CO2 > 2000 ppm
- 超标时在 Mac 扬声器上持续播放语音警报
- 空气质量恢复正常后自动停止警报
- 仅保留最新一次读数，简洁的状态管理
- 作为常规烟雾报警器的辅助备份

## 使用场景
- 在家中部署额外的烟雾/火灾检测层，作为传统报警器的智能补充
- 通过定时任务持续监测室内空气质量并在异常时自动告警
- 为 Mac 用户提供基于语音播报的紧急通知

## 依赖和前提条件
- IKEA Dirigera 智能家居中枢和 ALPSTUGA 空气传感器
- Python 3
- macOS（使用 Mac 扬声器播放警报）
- Dirigera API 访问令牌

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive skill 自动生成
