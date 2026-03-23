# icom-7610

> 控制 ICOM IC-7610 业余无线电收发信机

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | icom-7610 |
| **作者** | morozsm |
| **ClawHub** | https://clawskills.sh/skills/morozsm-icom-7610 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/morozsm/icom-7610 |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Hamlib (rigctl): `brew install hamlib`
- curl: usually pre-installed
- python3: usually pre-installed
- pyserial (only for serial power on): `pip3 install pyserial`
- wfview (optional, for LAN control): [wfview.org/download](https://wfview.org/download)
- H "Content-Type: text/xml" \

## 依赖和前提条件
- 
- wfview** (optional, for LAN control): [wfview.org/download](https://wfview.org/download)
- Advantages over serial:**
- No USB cable needed — Ethernet only
- Power on works with simple `set_powerstat 1` (no raw CI-V / pyserial needed)

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
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