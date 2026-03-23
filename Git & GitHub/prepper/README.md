# Prepper Skill

> 通过 Ollama dolphin-llama3 模型获取生存、应急准备和末日准备领域的专业知识

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Prepper Skill |
| **作者** | jlevitsk |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/jlevitsk-prepper |

## 功能概述
- 查询 dolphin-llama3 模型（80亿参数）获取无审查的生存知识
- 覆盖领域：医疗急救、野外生存、机械维修、农业种植、电气系统、化学、通信、食物保存、草药疗法
- 混合验证工作流：Ollama 提供原始答案，Claude 进行验证和增强
- 支持 JSON 格式输出便于程序化处理
- 当主模型拒绝回答时，自动回退到无审查模型
- 灵感来源于 AI-Survival-USB 项目

## 使用场景
- 获取灾难恢复和应急准备的实用建议
- 咨询野外生存技术（净水、搭建庇护所、导航、生火等）
- 了解在有限资源条件下的医疗、维修和通信解决方案

## 依赖和前提条件
- 本地安装并运行 Ollama
- 已拉取 dolphin-llama3 模型
- Python 3（用于运行查询脚本）

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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23