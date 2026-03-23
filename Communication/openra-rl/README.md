# OpenRA-RL

> 玩《命令与征服：红色警戒》即时战略游戏，建造基地、训练军队、击败 AI 对手

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenRA-RL |
| **作者** | yxc20089 |
| **版本** | 1.1.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/yxc20089-openra-rl |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/yxc20089/openra-rl |
| **安全评级** | 🔴 High |

## 功能概述
- 自动进行《红色警戒》即时战略对战
- 建造基地、采集资源、发展经济
- 训练和指挥多兵种军队作战
- 制定战术策略击败 AI 对手
- 支持 OpenRA 开源游戏引擎
- 实时决策与微操控制

## 使用场景
- AI 智能体自主玩即时战略游戏进行强化学习
- 测试 AI 在复杂实时策略环境中的决策能力
- 游戏 AI 研究与娱乐演示

## 依赖和前提条件
- 安装 OpenRA 游戏引擎
- 配置游戏环境和 AI 接口
- 足够的计算资源运行游戏实例

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，2 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
