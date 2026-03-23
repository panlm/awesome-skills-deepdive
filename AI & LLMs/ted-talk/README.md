# TED Talk

> 搜索和获取 TED 演讲内容，提取文稿和关键要点

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TED Talk |
| **作者** | leegitw |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/leegitw-ted-talk |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leegitw/ted-talk |
| **安全评级** | 🟢 Low |

## 功能概述
- 搜索和获取 TED 演讲内容
- 提取演讲文字稿和字幕
- 按主题、演讲者等条件筛选
- 获取演讲摘要和关键要点
- 支持多语言演讲内容检索
- 适用于学习、研究和内容创作

## 使用场景
- 快速检索特定主题的 TED 演讲作为学习资源
- 提取 TED 演讲文稿用于内容创作和引用
- 为团队分享和培训寻找优质演讲素材

## 依赖和前提条件
- Bash/Shell 环境

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
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
