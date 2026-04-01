# testflight-seat-monitor

> 监控 TestFlight 应用版本更新和测试状态

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | testflight-seat-monitor |
| **作者** | jon-xo |
| **ClawHub** | https://clawskills.sh/skills/jon-xo-testflight-monitor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jon-xo/testflight-monitor |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- 🔍 Smart Lookups - Maps cryptic TestFlight codes → readable app names
- 🔕 Silent by Default - Only alerts when slots actually open (no spam)
- 📦 Batch Monitoring - Check multiple apps in one run
- 📊 State Tracking - Detects status changes (full → available)
- ⚙️ Configurable - CLI-based config, customizable intervals
- 🎯 Community Data - Uses 800+ app names from awesome-testflight-link

## 依赖和前提条件
- OpenClaw** (agent runtime)
- `curl` (fetch pages)
- `jq` (JSON processing)
- `bash` (macOS/Linux)

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `config/` — 目录
- `lib/` — 目录
- `manifest.json` — 配置/数据文件
- `testflight-monitor.sh` — 脚本文件
- `tools/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟡 Medium | 包含持久化配置 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23