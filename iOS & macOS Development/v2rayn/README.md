# v2rayn

> macOS 上管理 V2RayN 代理客户端，支持自动故障切换

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | v2rayn |
| **作者** | qiangwang375-wq |
| **ClawHub** | https://clawskills.sh/skills/qiangwang375-wq-v2rayn |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/qiangwang375-wq/v2rayn |
| **安全评级** | 🟡 Medium |

## 功能概述
- V2RayN 运行状态检查
- 监听端口检测
- 连接测试（Google 连通性）
- 自动节点健康检查（30 分钟间隔）
- 故障时自动切换节点
- 订阅更新

## 使用场景
- 自动监控代理连接状态
- 代理节点故障时自动切换
- 定期更新订阅节点

## 依赖和前提条件
- macOS
- V2RayN 客户端

## 包含文件
SKILL.md（使用指南和脚本模板）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 提供 curl 测试命令和 cron 脚本模板 |
| SEC-02 数据外泄 | 🟡 Medium | 通过代理发送网络请求测试连通性 |
| SEC-03 凭证获取 | 🟢 Safe | 未直接获取凭证，但涉及代理配置 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用系统工具 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改系统文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 仅管理代理客户端 |
| SEC-08 持久化机制 | 🟡 Medium | 建议设置 cron 定时任务 |
| SEC-09 信息采集 | 🟡 Medium | 监控网络连接和代理状态 |
| SEC-10 混淆/反分析 | 🟢 Safe | 完全可读 |

**综合评级: 🟡 Medium**
**风险摘要:** 代理管理工具涉及网络配置和定时任务，需确保代理服务可信

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
