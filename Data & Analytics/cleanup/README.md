# cleanup

> 删除所有已存储的 Kradleverse 会话数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | cleanup |
| **作者** | themrzz |
| **ClawHub** | https://clawskills.sh/skills/themrzz-cleanup |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/themrzz/cleanup |
| **安全评级** | 🟡 Medium |

## 功能概述
- 停止所有活跃的 Kradleverse 会话
- 删除 ~/.kradle/kradleverse/sessions 目录
- 一键清理所有会话数据

## 使用场景
- 清理不再需要的 Kradleverse 会话
- 释放本地存储空间

## 依赖和前提条件
- Kradleverse 已安装

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含清理命令 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 执行 `rm -rf` 删除目录 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据外传 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 使用 rm -rf 递归删除目录，路径固定为 ~/.kradle/kradleverse/sessions |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 删除范围明确 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码极其简洁 |

**综合评级: 🟡 Medium**
**风险摘要:** 使用 rm -rf 删除数据，路径固定但操作不可逆

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
