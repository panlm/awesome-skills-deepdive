# Media Player

> 通用媒体播放控制工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Media Player |
| **作者** | xejrax |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/xejrax-media-player |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xejrax/media-player |
| **安全评级** | 🟢 Low |

## 功能概述
- Play audio/video locally on the host
- 支持通过命令行进行操作控制
- 提供自动化工作流集成

## 使用场景
- 控制本地媒体播放器的播放操作
- 管理播放队列和播放列表
- 支持多种媒体格式播放

## 依赖和前提条件
- 网络连接

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
