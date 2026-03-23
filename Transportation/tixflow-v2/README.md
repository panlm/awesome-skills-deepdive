# TixFlow

> AI 活动助手 V2——升级版的活动发现、预订和协调功能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TixFlow |
| **作者** | seenfinity |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/seenfinity-tixflow-v2 |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/seenfinity/tixflow-v2 |
| **安全评级** | 🟡 Medium |

## 功能概述
- 增强的活动搜索和推荐功能
- 更流畅的门票预订体验
- 智能活动推荐基于个人偏好
- 改进的团队协调功能

## 使用场景
- 根据个人兴趣获取个性化的活动推荐
- 管理多人活动的门票和协调信息

## 依赖和前提条件
- API Key（Tixflow）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
