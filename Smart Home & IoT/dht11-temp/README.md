# dht11-temp

> 使用 DHT11 传感器读取温湿度数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | dht11-temp |
| **作者** | noahseeger |
| **ClawHub** | https://clawskills.sh/skills/noahseeger-dht11-temp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/noahseeger/dht11-temp |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Wiring (adjust pin as needed):
- Important: The 10K pull-up resistor must be connected between DATA and VCC (5V)!
- Line 1: Temperature (°C)
- Line 2: Humidity (%)
- /30 * * * * sudo python3 ~/scripts/dht/main.py >> /var/log/dht.log 2>&1

## 依赖和前提条件
- Wiring (adjust pin as needed):**
- VCC     → 5V (Pin 2 oder 4)
- DATA    → GPIO <PIN> + 10K Pull-Up Widerstand → 5V
- GND     → GND (Pin 6)
- Important:** The 10K pull-up resistor must be connected between DATA and VCC (5V)!

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 需要 sudo 权限 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23