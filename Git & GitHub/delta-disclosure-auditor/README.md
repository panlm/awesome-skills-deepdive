# Delta Disclosure Auditor

> 验证 Skill 更新是否发布了可审计的变更记录，弥补"注册表显示新版本"与"任何人都能看到变更内容"之间的透明度缺口

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Delta Disclosure Auditor |
| **作者** | andyxinweiminicloud |
| **版本** | 1.1.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-delta-disclosure-auditor |

## 功能概述
- 审计能力声明变更（新增/删除/范围变化是否明确声明）
- 审计依赖变更（新增/删除/版本升级是否披露）
- 审计验证命令变更（测试删减/弱化是否需要明确声明）
- 审计行为范围变更声明（如"新增外部端点"vs"修复拼写错误"）
- 风险分类绑定审计（v1.1）：检查 Skill 风险分类是否与实际能力匹配
- 监管链验证（v1.1）：检查变更是否有加密签名和哈希链
- 更新资格评估（v1.1）：无充分披露的 Skill 不应有资格进行自动更新

## 使用场景
- 对 Skill 生态中的版本更新进行持续安全监控，确保变更透明可追踪
- 评估一个 Skill 是否具备自动更新的资格，基于其披露完整性

## 依赖和前提条件
- curl
- Python 3

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
