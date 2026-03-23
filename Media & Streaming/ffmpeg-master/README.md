# Donson Intelligent Editing

> FFmpeg 多媒体处理大师 — 转码、滤镜、流处理

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
- Stream Mapping: Always use `-map` for complex files to ensure you get the right audio/subtitle tracks
- Seeking: Put `-ss` *before* `-i` for fast seeking (input seeking), or *after* `-i` for accurate seeking (output seeking)
- Format Support: Ensure the output container (extension) supports the codecs you've chosen

## 使用场景
- 执行视频和音频格式转换
- 应用复杂的滤镜和特效处理
- 管理流媒体推送和录制

## 依赖和前提条件
- pip / uv 包管理器
- FFmpeg

## 包含文件
- `SKILL.md`
- `_meta.json`

## 安全状态
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
