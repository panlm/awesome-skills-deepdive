# QRdex

> 使用 QRdex.io REST API 创建、管理和追踪二维码

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | QRdex |
| **作者** | sebastienb |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/sebastienb-qrdex |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/sebastienb/qrdex |
| **安全评级** | 🔴 High |

## 功能概述
- 通过 API 批量创建自定义二维码
- 管理已生成的二维码列表
- 追踪二维码扫描统计数据
- 支持动态二维码（可修改目标链接）
- 自定义二维码样式和设计
- 导出和分享二维码图片

## 使用场景
- 批量生成营销活动二维码
- 追踪二维码扫描量和用户转化
- 动态管理和更新二维码目标链接

## 依赖和前提条件
- QRdex.io API 密钥
- QRdex.io 平台账号

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
