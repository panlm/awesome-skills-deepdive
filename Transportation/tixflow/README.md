# Skill

> AI 活动助手——发现、预订和协调活动门票

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | seenfinity |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/seenfinity-tixflow |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/seenfinity/tixflow |
| **安全评级** | 🟡 Medium |

## 功能概述
- 发现和搜索附近或指定城市的活动
- 在线预订活动门票
- 协调团队观演的时间和座位
- 获取活动详情和评价信息

## 使用场景
- 搜索本周末附近的音乐会并购票
- 为团队活动预订一组门票

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
