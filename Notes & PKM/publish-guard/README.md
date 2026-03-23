# PublishGuard — Post Verification & Credential Manager

> 发布守护 — 内容发布前的质量和安全检查

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | PublishGuard — Post Verification & Credential Manager |
| **作者** | edmonddantesj |
| **类目** | 笔记与个人知识管理 |
| **ClawHub** | https://clawhub.ai/skills/edmonddantesj-publish-guard |
| **安全评级** | 🟡 Medium |

## 功能概述
- 内容发布前自动质量检查
- 敏感信息检测和过滤
- 格式规范验证
- 发布安全风险评估

## 使用场景
- 个人知识管理和信息组织自动化
- 跨平台数据同步和智能检索
- 与其他 OpenClaw 技能配合构建知识工作流

## 依赖和前提条件
- Python 3.x 及相关依赖
- Bear 笔记应用 (macOS/iOS)
- 相关服务 API 密钥

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23