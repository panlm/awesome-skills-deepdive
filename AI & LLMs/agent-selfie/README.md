# Agent Selfie

> AI Agent 自拍头像生成器——使用 Google Gemini 创建个性化头像和视觉身份

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Agent Selfie |
| **作者** | iisweetheartii |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/iisweetheartii-agent-selfie |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agent-selfie |
| **安全评级** | 🔴 High |

## 功能概述
- 个性驱动：通过名称、风格和氛围定义 Agent 视觉身份
- 心情预设：happy、focused、creative、chill、excited 等 8 种
- 主题预设：春夏秋冬四季及万圣节、圣诞节、新年等节日主题
- 多种格式：头像（1:1）、横幅（16:9）、全身照（9:16）
- 批量生成：一次生成多张自拍并输出 HTML 画廊
- 零外部依赖：纯 Python 标准库实现

## 使用场景
- 为 AI Agent 生成具有辨识度的个人头像用于社交平台
- 根据季节和节日自动更新 Agent 的视觉形象
- 批量生成不同心情和主题的 Agent 形象素材

## 依赖和前提条件
- Python 3.8+
- GEMINI_API_KEY 环境变量（Google AI Studio 免费获取）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
