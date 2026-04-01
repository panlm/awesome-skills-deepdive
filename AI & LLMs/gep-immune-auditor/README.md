# GEP Immune Auditor

> 基于免疫系统原理的 AI 代理安全审计工具，检测提示注入和越权行为

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | GEP Immune Auditor |
| **作者** | andyxinweiminicloud |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-gep-immune-auditor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/gep-immune-auditor |
| **安全评级** | 🟡 Medium |

## 功能概述
- 模拟免疫系统的"自我/非自我"识别机制来检测异常行为
- 实时监控 AI 代理的操作行为并识别潜在威胁
- 检测 Prompt 注入攻击和恶意指令
- 提供详细的安全审计报告和风险评分
- 支持自定义安全策略和检测规则
- 可与现有 AI 工作流无缝集成

## 使用场景
- 企业 AI 代理部署前的安全合规审计
- 实时监控生产环境中 AI 代理的行为异常
- 评估 AI 系统对 Prompt 注入攻击的防御能力

## 依赖和前提条件
- OpenClaw 运行环境
- API 密钥配置

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 7 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
