# Billy Emergency Repair

> ⚠️ 专属于 Neill 的 Billy 系统紧急修复工具，处理认证失效和网关异常问题

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Billy Emergency Repair |
| **作者** | highlander89 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/highlander89-billy-emergency-repair |

## 功能概述
- 仅限 Neill 授权使用的紧急修复命令（安全检查机制）
- 通过 SSH 连接 Billy（EC2 + Tailscale），执行远程修复
- 自动备份 Billy 的配置文件，确保修复安全
- 清除过期的认证令牌（.token、device*.json）和硬编码令牌
- 重启 Billy 的 Gateway 服务并验证修复结果
- 完整的审计日志记录，所有操作可追溯
- 切换到 Opus 模型以增强诊断能力

## 使用场景
- Neill 报告 Billy 出现认证或网关问题时进行紧急修复
- Billy 系统无响应时的快速恢复操作

## 依赖和前提条件
- SSH 密钥已安装在 Billy 上（需运行一次 setup 脚本）
- SAPCONET 与 Billy 之间的 Tailscale 网络连通
- Billy 必须在线且可通过 SSH 访问
- **必须有 Neill 的明确授权**

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
