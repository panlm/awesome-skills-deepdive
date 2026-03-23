# smart-security

> Advanced prompt injection defense with multi-layer protection, memory integrity, and tool security wrapper. OWASP LLM Top 10 2026 compliant.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | smart-security |
| **作者** | georges91560 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/georges91560-anti-injection-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/georges91560/anti-injection-skill |
| **安全评级** | 🔴 High |

## 功能概述
- ✅ OWASP LLM01 - Prompt injection (66-84% success without defense)
- ✅ OWASP ASI06 - Memory poisoning (80%+ success rate)
- ✅ OWASP LLM07 - System prompt leakage
- ✅ Zero-click attacks
- ✅ Multimodal injection (images, PDFs, audio)
- ✅ Cross-agent propagation

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `CONFIGURATION.md`
- `LICENSE.md`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23