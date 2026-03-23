# Ulanzi TC001

> Ulanzi TC001 像素时钟控制工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ulanzi TC001 |
| **作者** | felipeouropreto |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/felipeouropreto-ulanzi-tc001 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/felipeouropreto/ulanzi-tc001 |
| **安全评级** | 🟢 Low |

## 功能概述
- language: `english|chinese`
- autobrightness: `auto|manual`
- brightness: `0-100`
- nightbrightness: `0-100`
- switchspeed: `noswitch|10|15|20|25|30|35|40|45|50|55|60`
- scrollspeed: `0-10`
- timezone: `GMT-3` (or `AUTO`)
- timeformat: `HH:mm|HH:mm:ss`

## 使用场景
- 控制 Ulanzi TC001 像素时钟的显示内容
- 自定义像素时钟的动画和文字
- 设置像素时钟的定时显示任务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `SKILL.md`
- `_meta.json`
- `config.json`
- `references`
- `scripts`

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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
