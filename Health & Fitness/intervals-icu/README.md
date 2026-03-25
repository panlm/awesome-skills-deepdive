# 🚴 Intervals.icu API — 训练数据管理

## 描述

Intervals.icu REST API 的完整参考指南，涵盖认证、活动记录、日历事件、健康数据和运动设置。包含所有主要端点的 curl 示例，支持字段过滤、批量操作和训练文件导出。

## 功能特点

- **全面的 API 覆盖**：涵盖运动员资料、活动、训练、事件、健康数据和训练计划
- **读写双向操作**：支持读取和写入所有主要端点
- **批量操作**：支持批量导入/导出数据
- **字段过滤**：精确控制返回的数据字段
- **多格式导出**：支持 Zwift、Garmin 等格式的训练文件导出
- **去重同步**：从外部平台同步已完成的活动并自动去重

## 使用方法

### 认证

```bash
# API Key 方式
curl -H "Authorization: ApiKey API_KEY:YOUR_API_KEY" \
  https://intervals.icu/api/v1/athlete/YOUR_ATHLETE_ID

# Bearer Token 方式（OAuth）
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  https://intervals.icu/api/v1/athlete/YOUR_ATHLETE_ID
```

### 常用操作

- 获取最近的活动记录
- 安排一周的结构化训练
- 记录每日健康指标（睡眠、静息心率等）
- 导出训练计划为设备可用格式

## 安全评估

- **VirusTotal**: ⚠️ 未验证
- **OpenClaw**: ⚠️ 未验证
- **风险说明**: 需要 Intervals.icu 账户的 Athlete ID 和 API Key

## 附加资源

- [GitHub 源码](https://github.com/openclaw/skills/tree/main/skills/pseuss/intervals-icu-api)
- [ClawHub 页面](https://clawskills.sh/skills/pseuss-intervals-icu-api)
- [Intervals.icu 设置页](https://intervals.icu/settings)
