# iDRAC

> |

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | iDRAC |
| **作者** | eddygk |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/eddygk-idrac |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/eddygk/idrac |
| **安全评级** | 🟡 Medium |

## 功能概述
- Check server hardware status, health, or temperatures
- Query CPU, memory, storage/RAID details
- Monitor system sensors (fans, voltage, thermal)
- Perform power operations (status, on, off, graceful shutdown, force restart)
- Check BIOS/firmware versions or system inventory
- View system event logs (SEL) or lifecycle controller logs

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23