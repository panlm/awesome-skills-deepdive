# mlx-stt

> 使用 Apple MLX 框架进行本地语音转文字

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mlx-stt |
| **作者** | guoqiao |
| **ClawHub** | https://clawskills.sh/skills/guoqiao-mlx-stt |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/guoqiao/mlx-stt |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- "/mlx-stt <audio>"
- "Transcribe ..."
- "Convert audio to text ..."
- First run could be a little slow, since it will need to download model.
- The transcript result will be printed to stdout.

## 依赖和前提条件
- `mlx`: macOS with Apple Silicon
- `ffmpeg`: convert audio format when needed
- `mlx_audio`: do the real job

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `install.sh` — 脚本文件
- `mlx-stt.sh` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23