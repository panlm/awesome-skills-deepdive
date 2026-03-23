# Trust Decay Monitor

> 追踪 AI Skill 安全验证结果的时效性衰减，提醒你那个 18 个月前的"已验证"徽章可能已经过期失效

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Trust Decay Monitor |
| **作者** | andyxinweiminicloud |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-trust-decay-monitor |

## 功能概述
- 计算已验证 skill 的信任新鲜度评分（Trust Freshness Score）
- 追踪验证后的时间衰减，基于可配置的衰减曲线
- 监控依赖项变动（dependency churn）：审计后依赖更新次数越多，信任度越低
- 检测生态系统上下文变化：新 CVE、新权限类型、新攻击模式
- 识别域名所有权变更等高风险事件
- 生成信任衰减报告，标记已过期的验证徽章

## 使用场景
- 定期审查已安装 skill 的安全验证是否仍然有效
- 在 skill 市场中评估"已验证"标记的实际可信度
- 供应链安全管理，识别依赖变动导致的信任失效

## 依赖和前提条件
- `curl` 命令行工具
- `python3` 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
