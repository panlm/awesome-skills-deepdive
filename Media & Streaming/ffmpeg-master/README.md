# Donson Intelligent Editing

> Use when performing video/audio processing tasks including transcoding, filtering, streaming, metadata manipulation, or complex filtergraph operations with FFmpeg.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Donson Intelligent Editing |
| **作者** | liudu2326526 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/liudu2326526-ffmpeg-master |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/liudu2326526/ffmpeg-master |
| **安全评级** | 🟢 Low |

## 功能概述
- video processing
- audio conversion
- filter_complex
- hardware acceleration
- Stream Mapping: Always use `-map` for complex files to ensure you get the right audio/subtitle tracks.
- Seeking: Put `-ss` *before* `-i` for fast seeking (input seeking), or *after* `-i` for accurate seeking (output seeking)

## 使用场景
- 多媒体内容管理
- 流媒体服务控制
- 媒体库组织和搜索

## 包含文件
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。混淆/反分析：使用编码/解码操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23