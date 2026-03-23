# Trust Verifier

> 验证 ClawHub 技能的来源可信度，通过发布者历史、版本一致性和依赖链构建信任评分

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Trust Verifier |
| **作者** | trypto1019 |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/trypto1019-arc-trust-verifier |

## 功能概述
- 评估技能的信任度，综合发布者声誉、版本一致性、内容完整性和依赖链
- 生成信任证明（trust attestation）文件，供其他工具验证
- 验证已有的信任证明是否仍然有效
- 检查依赖项的信任链，确保整个依赖树可信
- 五级信任等级：VERIFIED → TRUSTED → UNKNOWN → SUSPICIOUS → UNTRUSTED
- 通过 SHA-256 哈希验证所有文件的内容完整性

## 使用场景
- 安装来自未知发布者的技能前，评估其可信度
- 为通过审查的技能生成信任证明，简化后续安装决策
- 检测技能更新中的异常行为（如突然的权限变更）

## 依赖和前提条件
- `python3`
- 支持的操作系统：macOS、Linux

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
