# KallyAI Executive Assistant

> KallyAI 执行助理——AI 电话代理，处理出站和入站电话

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | KallyAI Executive Assistant |
| **作者** | sltelitsyn |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/sltelitsyn-kallyai |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sltelitsyn/kallyai |
| **安全评级** | 🟡 Medium |

## 功能概述
- 自动处理出站电话（外呼）
- 接听和处理入站电话
- 语音识别和自然语言理解
- 电话会议安排和日程管理
- 通话记录和摘要生成

## 使用场景
- 自动打电话预约餐厅或医院
- 智能接听来电并记录留言
- 批量外呼进行客户回访

## 依赖和前提条件
- API Key（KallyAI）、电话服务集成

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
