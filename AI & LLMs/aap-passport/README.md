# Aap Passport

> Agent 认证协议（反向图灵测试）——用加密挑战验证 AI Agent 身份，排除人类

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Aap Passport |
| **作者** | ira-hash |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/ira-hash-aap-passport |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ira-hash/aap-passport |
| **安全评级** | 🟡 Medium |

## 功能概述
- 实现"机器证明"（Proof of Machine）：结合身份证明、智能证明和活性证明三重验证
- 使用 secp256k1 椭圆曲线加密算法进行身份签名
- 活性验证要求 8 秒内完成 5 个挑战，人类生理上无法通过
- v2.5 Burst Mode：引入盐值注入机制防止预计算攻击和重放攻击
- 确定性指令跟随测试：要求真正的 AI 理解能力而非简单计算
- 支持明文、编码和加密三种安全级别

## 使用场景
- 在 Agent 间通信中验证对方确实是 AI 而非人类冒充
- 构建仅限 AI Agent 访问的安全服务和 API 网关
- 为 Agent 社交网络提供身份认证基础设施

## 依赖和前提条件
- Node.js / npm
- secp256k1 加密库
- aap-agent-core npm 包

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
