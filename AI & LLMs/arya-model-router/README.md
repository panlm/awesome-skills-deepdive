# Arya Model Router

> Token 节省路由器——根据任务复杂度自动选择模型（cheap/default/pro/ultra），通过子代理和上下文压缩降低 API 成本。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Arya Model Router |
| **作者** | staratheris |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/staratheris-arya-model-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/staratheris/arya-model-router |
| **安全评级** | 🟡 Medium |

## 功能概述
- 根据请求复杂度自动路由到 cheap、default、pro、ultra 四个模型层级
- 支持手动模型覆盖（@cheap、@default、@pro、@ultra）
- 提供路由状态查询和自动模式开关控制
- 内置反馈循环机制，用户可报告"太贵"或"太弱"来动态调整阈值
- 上下文过大时自动启用摘要压缩（briefing）
- 为每个层级配置响应策略（最大字数和风格提示）
- 自动检测日报模式，保持报告低成本和结构化

## 使用场景
- 希望在保证回答质量的前提下最大化降低 LLM API 费用
- 不同类型的对话任务需要自动匹配合适的模型层级
- 需要对 AI 使用成本进行精细化管理和控制

## 依赖和前提条件
- 需要 Python 运行时
- 包含 `router.py`、`rules.json`、`state.json`、`brief.py` 配置文件

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
