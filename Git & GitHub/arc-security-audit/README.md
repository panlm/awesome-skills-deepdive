# Security Audit

> 对代理的完整技能栈进行一键式全面安全审计，生成按风险等级排序的综合报告

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Security Audit |
| **作者** | trypto1019 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/trypto1019-arc-security-audit |

## 功能概述
- 一条命令审计所有已安装技能或指定单个技能
- 串联 arc-skill-scanner、arc-trust-verifier 等工具链进行全面扫描
- 评估每个技能的信任度（来源、代码清洁度、二进制存在性）
- 通过 SHA-256 校验和验证二进制完整性
- 生成按风险等级排序的优先级报告，支持 JSON 输出
- 可选生成信任证明（trust attestations）

## 使用场景
- 定期对整个代理技能栈进行安全健康检查
- 安装新技能后立即进行风险评估
- 生成合规所需的安全审计报告

## 依赖和前提条件
- `python3`
- 支持的操作系统：macOS、Linux
- 可选依赖：arc-skill-scanner、arc-trust-verifier

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
