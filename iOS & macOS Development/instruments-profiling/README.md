# instruments-profiling

> 使用 Instruments/xctrace 对 macOS/iOS 原生应用进行性能分析

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | instruments-profiling |
| **作者** | steipete |
| **ClawHub** | https://clawskills.sh/skills/steipete-instruments-profiling |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/steipete/instruments-profiling |
| **安全评级** | 🟢 Low |

## 功能概述
- Time Profiler 模板使用指南
- xctrace CLI 命令参考
- 正确选择目标二进制文件的关键技巧
- 堆栈数据导出和后处理
- Instruments UI 工作流程
- iOS 设备特定注意事项

## 使用场景
- 诊断应用启动慢或卡顿问题
- 分析 CPU 热点函数
- 导出性能数据进行自动化比较

## 依赖和前提条件
- macOS + Xcode
- xcrun 命令行工具

## 包含文件
SKILL.md（完整性能分析指南）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅提供 xctrace 命令参考，不自动执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据外传 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅指导写入 trace 文件到 /tmp |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 需要开发者工具权限说明 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 纯指南内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯知识型性能分析指南，零代码执行风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
