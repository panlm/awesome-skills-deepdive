# Qr Generator

> 二维码生成工具，支持多种数据类型编码

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Qr Generator |
| **作者** | autogame-17 |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/autogame-17-qr-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/autogame-17/qr-generator |
| **安全评级** | 🟢 Low |

## 功能概述
- 生成标准二维码图像
- 支持 URL、文本、联系信息等编码
- 自定义二维码大小和颜色
- 输出多种图片格式

## 使用场景
- 为产品页面生成二维码用于线下推广
- 批量生成活动签到二维码

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `index.js`
- `package-lock.json`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；混淆/反分析：使用编码/解码操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23