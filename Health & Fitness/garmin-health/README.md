# ⌚ Garmin Health Analysis — Garmin 健康数据分析

## 描述

连接 Garmin Connect 获取健康指标数据，支持自然语言查询，可生成交互式 HTML 健康数据仪表板。支持 20+ 种指标，包括睡眠、Body Battery、HRV、VO2 Max 等。

## 功能特点

- **自然语言查询**：直接用自然语言询问健康数据，如"我昨晚睡得怎么样？"
- **20+ 健康指标**：睡眠阶段、Body Battery、HRV、VO2 Max、训练准备度、身体成分、SPO2 等
- **FIT/GPX 文件分析**：下载并分析运动轨迹、海拔、配速等数据
- **交互式仪表板**：使用 Chart.js 生成 HTML 可视化图表
- **自动监控**：支持通过 Cron 任务定期检查健康状态

## 使用方法

```bash
# 安装依赖
pip3 install garminconnect fitparse gpxpy

# 配置凭证（三种方式之一）
# 方式 A：在 ~/.clawdbot/clawdbot.json 中配置
# 方式 B：设置环境变量
export GARMIN_EMAIL="your@email.com"
export GARMIN_PASSWORD="your-password"
```

### 查询示例

- "我昨晚的睡眠得分和各阶段分布"
- "这周的 Body Battery 趋势"
- "过去一个月的所有运动记录"
- "生成 90 天的 HRV 趋势图"

## 安全评估

- **VirusTotal**: ⚠️ 未验证
- **OpenClaw**: ⚠️ 未验证
- **风险说明**: 需要 Garmin Connect 账户凭证（邮箱和密码）

## 附加资源

- [GitHub 源码](https://github.com/openclaw/skills/tree/main/skills/eversonl/garmin-health-analysis)
- [ClawHub 页面](https://clawskills.sh/skills/eversonl-garmin-health-analysis)
- [Garmin Connect MCP Server](https://github.com/eversonl/garmin-health-mcp-server)
