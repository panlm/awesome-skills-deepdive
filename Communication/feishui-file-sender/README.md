# feishui-file-sender

> 通过飞书频道发送文件，利用 message 工具的 filePath 参数实现文件传输

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | feishui-file-sender |
| **作者** | josephyb97 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/josephyb97-feishui-file-sender |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/josephyb97/feishui-file-sender |
| **安全评级** | 🟢 Low |

## 功能概述
- 通过飞书频道发送本地文件
- 支持多种文件格式传输
- 使用 message 工具 filePath 参数
- 支持指定目标频道或用户
- 文件发送状态确认

## 使用场景
- 在飞书群组中分享文件和文档
- 自动化工作流中的飞书文件分发
- 向飞书用户发送生成的报告文件

## 依赖和前提条件
- 飞书应用凭据和频道权限
- OpenClaw 飞书插件已配置
- 待发送文件的本地路径

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。越权操作：涉及权限相关操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
