# network-scanner

> 扫描本地网络设备和端口

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | network-scanner |
| **作者** | florianbeer |
| **ClawHub** | https://clawskills.sh/skills/florianbeer-network-scanner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/florianbeer/network-scanner |
| **许可证** | 未指定 |
| **安全评级** | 🔴 High |

## 功能概述
- Safety First: Includes built-in protection against accidentally scanning public IP ranges or networks without proper private routing — preventing abuse reports from hosting providers.
- Trusted networks (configured in `networks.json`) skip route verification since you've explicitly approved them.
- Markdown (default):
- Last scan: 2026-01-28 00:10*
- 2 devices found*
- JSON (--json):

## 依赖和前提条件
- `sudo` access recommended for MAC address discovery

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 需要 sudo 权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 包含网络探测功能 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🔴 High**
**风险摘要:** 存在多项高风险问题，使用前需仔细评估

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23