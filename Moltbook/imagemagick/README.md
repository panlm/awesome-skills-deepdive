# imagemagick

> 使用 ImageMagick 进行图像处理的综合技能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | imagemagick |
| **作者** | kesslerio |
| **ClawHub** | https://clawskills.sh/skills/kesslerio-imagemagick |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kesslerio/imagemagick |
| **安全评级** | 🟢 Low |

## 功能概述
- 背景去除（支持自定义颜色和容差）
- 图像缩放和格式转换（PNG/WebP/JPG/GIF）
- 水印叠加
- 缩略图批量生成
- 色彩调整（亮度、对比度、灰度）

## 使用场景
- 图像背景去除
- 批量图像格式转换
- 为图像添加水印

## 依赖和前提条件
- ImageMagick（convert 命令）

## 包含文件
- `SKILL.md — 使用说明`
- `ORIGINAL_README.md — 快速入门`
- `scripts/remove-bg.sh — 背景去除脚本`
- `skill.json — 元数据`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | Shell 脚本调用 ImageMagick convert 命令 |
| SEC-02 数据外泄 | 🟢 Safe | 仅本地文件处理 |
| SEC-03 凭证获取 | 🟢 Safe | 不涉及凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 依赖系统级 ImageMagick |
| SEC-05 文件系统篡改 | 🟡 Medium | 读写图像文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 不涉及 LLM |
| SEC-07 越权操作 | 🟢 Safe | 仅文件转换操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 脚本简洁透明 |

**综合评级: 🟢 Low**
**风险摘要:** 标准图像处理工具封装，行为安全透明

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
