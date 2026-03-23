# Update Signature Verifier

> 验证 Skill 更新的加密签名连续性，检测密钥变更、签名缺失和未签名更新等供应链攻击风险

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Update Signature Verifier |
| **作者** | andyxinweiminicloud |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-update-signature-verifier |

## 功能概述
- 检查每个版本是否由与初始安装相同的加密密钥签名
- 检测版本间的密钥变更事件（合法轮换 vs 可疑转移）
- 验证每个版本是否存在签名（发现签名缺失的版本）
- 识别未签名的更新，防止通过合法更新渠道的供应链攻击
- 追踪发布者账号变更和构建管道完整性
- 生成签名连续性审计报告

## 使用场景
- 在 Skill 更新时自动验证签名链是否完整，防止恶意版本替换
- 审查已安装 Skill 的历史版本签名，识别可疑的发布者变更
- 供应链安全合规检查，确保更新渠道的加密信任链不断裂

## 依赖和前提条件
- `curl` 命令行工具
- `python3` 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
