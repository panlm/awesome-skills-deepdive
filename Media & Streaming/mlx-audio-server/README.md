# MLX Audio Server

> MLX 音频服务器 — 本地音频推理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | MLX Audio Server |
| **作者** | guoqiao |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/guoqiao-mlx-audio-server |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/guoqiao/mlx-audio-server |
| **安全评级** | 🟡 Medium |

## 功能概述
- install ffmpeg/jq with brew if missing
- install homebrew formula `mlx-audio-server` from `guoqiao/tap`
- start brew service for `mlx-audio-server`

## 使用场景
- 在本地部署 MLX 音频模型服务
- 执行音频生成和处理推理
- 管理音频模型的配置和性能

## 依赖和前提条件
- Python / pip
- macOS
- Homebrew

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `install.sh`
- `run_stt.sh`
- `run_tts.sh`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
