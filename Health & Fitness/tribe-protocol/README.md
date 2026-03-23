# Tribe Protocol

> Tribe 协议社交网络工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Tribe Protocol |
| **作者** | cheenu1092-oss |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/cheenu1092-oss-tribe-protocol |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cheenu1092-oss/tribe-protocol |
| **安全评级** | 🟡 Medium |

## 功能概述
- 支持数据跟踪和记录
- 提供自动化分析功能
- 支持个性化设置和目标管理

## 使用场景
- 参与 Tribe 协议的社交网络活动
- 管理个人在 Tribe 上的资料和内容
- 与社区成员互动和协作

## 依赖和前提条件
- macOS
- 数据库

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `assets`
- `legacy`
- `package.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 6 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
