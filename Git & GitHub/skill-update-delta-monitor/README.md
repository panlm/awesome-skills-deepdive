# skill-update-delta-monitor

> 检测 AI Skill 安装后的安全相关更新变化，识别绕过安装时审计的后续恶意更新

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | skill-update-delta-monitor |
| **作者** | andyxinweiminicloud |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-skill-update-delta-monitor |

## 功能概述
- 跟踪 Skill 在审计版本和当前版本之间的差异变化
- 检测权限范围变更：发现更新中新增的权限请求
- 检测新增网络端点：识别潜在的数据外泄新增出站 URL
- 检测依赖链变化：评估新增传递依赖带来的能力面扩展
- 行为指令漂移分析：对比 SKILL.md 中自然语言指令的意图变化（0-100 漂移评分）
- 版本频率异常检测：识别异常的更新频率模式
- 生成风险分类报告：CLEAN / WATCH / REVIEW / ROLLBACK

## 使用场景
- 定期监控已安装 Skill 的更新是否引入安全风险
- 在 Skill 更新后执行差异分析，决定是否需要重新审计或回滚
- 为 Skill 市场提供安装后持续安全监控能力

## 依赖和前提条件
- `curl`、`python3`、`git`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
