# design-assets

> 创建和编辑图形设计资源：图标、网站图标、图片和色彩系统

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | design-assets |
| **作者** | cmanfre7 |
| **ClawHub** | https://clawskills.sh/skills/cmanfre7-design-assets |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/cmanfre7/design-assets |
| **安全评级** | 🟢 Low |

## 功能概述
- 从 1024x1024 源图生成全套 iOS/macOS/Android 图标
- 生成 Favicon 全套尺寸（16/32/180/192/512 + .ico）
- SVG 图标和 Logo 创建
- 色彩系统和调色板生成
- 使用 sips（macOS）和 ImageMagick 处理
- OG Image 社交分享图生成

## 使用场景
- 新项目图标和 Favicon 批量生成
- 品牌设计资源批量处理
- 跨平台图标适配

## 依赖和前提条件
- macOS sips（可选）
- ImageMagick（可选）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，包含生成脚本模板 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 执行 sips 和 ImageMagick，参数为固定图片处理命令 |
| SEC-02 数据外泄 | 🟢 Safe | 纯本地图片处理 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证操作 |
| SEC-04 供应链风险 | 🟢 Safe | 仅使用系统工具 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅在指定输出目录创建图片 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯本地图片处理工具，无安全风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
