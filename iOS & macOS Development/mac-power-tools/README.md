# mac-power-tools

> macOS Apple Silicon 本地优化工具套件，含系统清理和模拟计算

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mac-power-tools |
| **作者** | aadipapp |
| **ClawHub** | https://clawskills.sh/skills/aadipapp-mac-power-tools |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aadipapp/mac-power-tools |
| **安全评级** | 🟡 Medium |

## 功能概述
- 本地 trillion swarm 模拟计算
- CoreML 资源预测
- 安全系统清理
- 本地备份功能
- 进程监控
- 本地网络发现
- 自学习历史记录

## 使用场景
- Mac Mini 本地性能优化
- 系统资源监控和清理
- 本地计算模拟

## 依赖和前提条件
- Python 3.10+
- numpy（可选）
- macOS

## 包含文件
SKILL.md, power_tools.py（主工具脚本）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 通过 subprocess 执行系统命令（清理、网络发现等） |
| SEC-02 数据外泄 | 🟢 Safe | 100% 本地运行，无网络请求 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖 numpy，需 pip 安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 写入 ~/.logs/ 和 ~/.config/ 目录 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅用户级操作 |
| SEC-08 持久化机制 | 🟢 Safe | 写入配置文件但无系统级持久化 |
| SEC-09 信息采集 | 🟢 Safe | 收集本地系统指标 |
| SEC-10 混淆/反分析 | 🟡 Medium | 源文件包含 markdown 代码块包装（文件格式异常） |

**综合评级: 🟡 Medium**
**风险摘要:** 本地工具套件，但源文件格式异常（含 markdown 包装），需检查实际执行内容

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
