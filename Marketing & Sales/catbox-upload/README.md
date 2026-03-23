# Upload files to catbox.moe (permanent) or litterbox.catbox.moe (temporary).

> Catbox 文件上传工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Upload files to catbox.moe (permanent) or litterbox.catbox.moe (temporary). |
| **作者** | microck |
| **类目** | Marketing & Sales |
| **ClawHub** | https://clawskills.sh/skills/microck-catbox-upload |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/microck/catbox-upload |
| **安全评级** | 🟢 Low |

## 功能概述
- 文件上传到 Catbox 平台
- 生成分享链接
- 支持多种文件格式
- 快速文件分发

## 使用场景
- 快速上传文件到 Catbox 获取分享链接
- 批量上传营销素材便于团队共享

## 依赖和前提条件
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `requirements.txt`
- `upload.py`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 存在 1 项高风险，0 项中风险。数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23