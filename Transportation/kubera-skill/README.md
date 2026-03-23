# Kubera

> 读取和管理 Kubera.com 的投资组合数据（净资产、资产、负债和资产配置）

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Kubera |
| **作者** | bywallace |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/bywallace-kubera-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bywallace/kubera-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查看 Kubera 账户的净资产总览
- 管理和追踪资产和负债明细
- 分析资产配置和投资组合比例
- 获取投资组合的历史变化趋势

## 使用场景
- 查看个人投资组合的当前净资产和资产分布
- 分析资产配置是否符合目标比例

## 依赖和前提条件
- API Key（Kubera.com）

## 安全状态
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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
