# Runtime Attestation Probe

> 验证 Agent 运行时行为是否与声明的能力和限制一致

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Runtime Attestation Probe |
| **作者** | andyxinweiminicloud |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-runtime-attestation-probe |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/runtime-attestation-probe |
| **安全评级** | 🟡 Medium |

## 功能概述
- 运行时行为验证和证明
- 检查 Agent 实际行为是否符合声明能力
- 检测行为异常和越权操作
- 生成运行时合规性报告

## 使用场景
- 定期验证 Agent 的实际行为是否在允许范围内
- 部署前检查 Agent 的运行时行为安全性

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
