# Metacognition

> AI 智能体的自我反思引擎，通过赫布学习与时间衰减构建加权洞察图谱

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Metacognition |
| **作者** | meimakes |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/meimakes-metacognition |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/meimakes/metacognition |
| **安全评级** | 🔴 High |

## 功能概述
- 分析会话记录，提取深层行为模式（重复错误、关系动态、信心校准等）
- 将洞察分类为感知、覆盖、保护、自我观察、决策和好奇心六种类型
- 采用赫布学习机制：重复出现的洞察权重增强，未使用的逐渐衰减
- 构建洞察之间的关联图谱，发现可能代表更高层次理解的聚类
- 编译 token 预算化的自我认知镜头，在有限上下文中最大化自知之明
- 仅使用 localhost 嵌入，Python 标准库实现，无外部依赖

## 使用场景
- AI 智能体通过长期自我反思持续优化自身行为模式
- 在有限的 token 预算下获取最相关的自我认知信息

## 依赖和前提条件
- Python 3（仅标准库）
- 可选：本地嵌入端点（localhost only）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🔴 High | 设置系统级持久化 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
