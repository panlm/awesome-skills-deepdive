# Ham Radio DX Monitor

> 业余无线电 DX 频段监控工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ham Radio DX Monitor |
| **作者** | capt-marbles |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/capt-marbles-ham-radio-dx |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/capt-marbles/ham-radio-dx |
| **安全评级** | 🟢 Low |

## 功能概述
- ea7jxh - dx.ea7jxh.eu:7373 (Europe)
- om0rx - cluster.om0rx.com:7300 (Europe)
- oh2aq - oh2aq.kolumbus.fi:7373 (Finland)
- ab5k - ab5k.net:7373 (USA)
- w6rk - telnet.w6rk.com:7373 (USA West Coast)
- *"Check the DX cluster for new spots"*
- *"What's active on 20 meters?"*
- *"Show me today's DX digest"*

## 使用场景
- 监控 DX 频段的实时活动
- 查询和记录远程通联信息
- 管理业余无线电设备配置

## 依赖和前提条件
- Node.js / npm
- Python / pip

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `dx-monitor.py`

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
