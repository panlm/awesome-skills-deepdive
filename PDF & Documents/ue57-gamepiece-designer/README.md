# UE5.7 Gamepiece Designer

> 游戏棋子/角色设计工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | UE5.7 Gamepiece Designer |
| **作者** | jdqconsulting |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/jdqconsulting-ue57-gamepiece-designer |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jdqconsulting/ue57-gamepiece-designer |
| **安全评级** | 🟢 Low |

## 功能概述
- 游戏角色和棋子设计
- 可视化设计编辑
- 自定义属性和参数
- 导出多种格式

## 使用场景
- 为桌游设计自定义的游戏棋子和角色
- 创建游戏原型中的角色视觉设计

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `README.md`
- `SKILL.md`
- `Templates`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23