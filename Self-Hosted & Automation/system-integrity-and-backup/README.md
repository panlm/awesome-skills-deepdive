# system-integrity-and-backup

> 希腊法律合规的加密备份、完整性验证和数据保留管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | system-integrity-and-backup |
| **作者** | satoshistackalotto |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-system-integrity-and-backup |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/system-integrity-and-backup |
| **安全评级** | 🟡 Medium |

## 功能概述
- AES-256 加密备份（全量和增量）
- SHA-256 完整性验证和哈希注册表
- 希腊法律数据保留要求（5-20 年）
- 备份验证（恢复测试，不覆盖生产数据）
- 审计日志（通过/失败永久记录）
- 版本化和可回滚的数据库迁移
- "无静默失败"原则

## 使用场景
- 希腊会计事务所的法规合规数据备份
- 企业级数据完整性验证和审计
- 灾难恢复和恢复测试

## 依赖和前提条件
- jq、openssl、tar
- OPENCLAW_DATA_DIR、OPENCLAW_ENCRYPTION_KEY 环境变量

## 包含文件
- `SKILL.md` — 完整技能定义和命令参考
- `EVALS.json` — 评估数据
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | openssl 加密/解密、tar 打包、完整性检查命令 |
| SEC-02 数据外泄 | 🟡 Medium | 可导出加密备份到外部存储（/mnt/external） |
| SEC-03 凭证获取 | 🟡 Medium | 需要 OPENCLAW_ENCRYPTION_KEY 环境变量（明确要求不存磁盘） |
| SEC-04 供应链风险 | 🟢 Safe | 仅标准系统工具 |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建/管理备份文件和审计日志 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟡 Medium | 可删除过期备份（需人工审批） |
| SEC-08 持久化机制 | 🟡 Medium | 创建备份文件和哈希注册表 |
| SEC-09 信息采集 | 🟡 Medium | 完整性检查扫描所有数据文件 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯 SKILL.md 指令，无代码 |

**综合评级: 🟡 Medium**
**风险摘要:** 企业级备份和完整性管理，涉及加密操作和文件系统管理，但安全实践良好

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
