# keepmyclaw

> OpenClaw 工作区加密云备份和恢复

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | keepmyclaw |
| **作者** | ryce |
| **ClawHub** | https://clawskills.sh/skills/ryce-keepmyclaw |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ryce/keepmyclaw |
| **安全评级** | 🟡 Medium |

## 功能概述
- AES-256 零知识加密备份到 Cloudflare R2
- 备份整个 agent 系统（工作区、记忆、skills、cron、凭证）
- 一键恢复到新机器
- 快照列表和清理管理
- Agent 自主注册和设置流程
- 排除 node_modules/.git 等无关文件

## 使用场景
- 定期加密备份 OpenClaw agent 到云端
- 在新机器上一键恢复完整 agent 状态
- 灾难恢复和 agent 迁移

## 依赖和前提条件
- openssl、curl、tar、jq
- Keep My Claw 账户（付费服务：$5/月或 $19/年）

## 包含文件
- `SKILL.md` — 技能定义和详细设置流程
- `scripts/backup.sh` — 执行备份
- `scripts/restore.sh` — 执行恢复
- `scripts/list.sh` — 列出快照
- `scripts/prune.sh` — 清理旧快照
- `scripts/setup.sh` — 初始设置

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | tar 打包、openssl 加密、curl 上传/下载 |
| SEC-02 数据外泄 | 🟡 Medium | 将加密备份上传到 api.keepmyclaw.com（第三方服务） |
| SEC-03 凭证获取 | 🟡 Medium | 读取 ~/.keepmyclaw/config（API Key）和 passphrase；备份包含凭证目录 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖第三方 API（keepmyclaw.com）存储备份 |
| SEC-05 文件系统篡改 | 🟡 Medium | restore 操作将解密内容写回 ~/.openclaw/ |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 操作限制在 ~/.openclaw 和 ~/.keepmyclaw 范围 |
| SEC-08 持久化机制 | 🟡 Medium | 创建 ~/.keepmyclaw/ 持久化配置和密钥 |
| SEC-09 信息采集 | 🟡 Medium | 打包整个 workspace（可能包含敏感文件） |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 加密备份到第三方云服务，虽然零知识加密但仍涉及数据外传，需信任 keepmyclaw.com

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
