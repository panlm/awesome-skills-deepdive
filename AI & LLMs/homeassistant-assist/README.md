# Home Assistant Assist

> 将 OpenClaw 连接到 Home Assistant，实现智能家居语音和文本控制

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Home Assistant Assist |
| **作者** | developmentcats |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/developmentcats-homeassistant-assist |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/developmentcats/homeassistant-assist |
| **安全评级** | 🟡 Medium |

## 功能概述
- 与 Home Assistant 的 Assist API 深度集成
- 支持通过自然语言控制智能家居设备
- 可查询设备状态、传感器数据和家庭信息
- 支持自动化场景触发和执行
- 提供设备列表浏览和管理功能
- 支持多语言的语音和文本交互
- 可配置自定义 Home Assistant 管道

## 使用场景
- 通过 AI 助手语音控制家中的灯光、空调等设备
- 查询家庭传感器数据如温度、湿度、门窗状态
- 创建和触发智能家居自动化场景

## 依赖和前提条件
- Home Assistant 实例（URL 和长期访问令牌）
- Home Assistant Assist API 启用
- OpenClaw 运行环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
