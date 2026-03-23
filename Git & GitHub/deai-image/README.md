# Deai Image

> 检测并移除 AI 生成图片的指纹特征，通过 7 阶段处理管道将 AI 图片转化为类似人类拍摄的照片

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Deai Image |
| **作者** | swaylq |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/swaylq-deai-image |

## 功能概述
- 7 阶段处理管道：元数据清除 → 胶片颗粒 → 色彩调整 → 模糊/锐化 → 缩放 → JPEG 重压缩 → 最终清理
- 支持 Midjourney、DALL-E 3、Stable Diffusion、Flux、Firefly 等主流 AI 模型生成的图片
- 提供三种处理强度：light（保质量）、medium（平衡）、heavy（最大绕过率 65-80%）
- 完全剥离 EXIF 标签和 C2PA 水印等元数据（100% 有效）
- 支持批量处理整个目录的图片
- 同时提供 Python 版和 Bash 版脚本

## 使用场景
- 对 AI 生成的创意图片进行后处理，消除 AI 检测器的识别特征
- 批量处理 AI 图片集合，用于个人创意项目或学术研究

## 依赖和前提条件
- ImageMagick 7.0+
- ExifTool
- Python 3.7+ 及 Pillow、NumPy（Python 版）
- Debian/Ubuntu: `sudo apt install imagemagick libimage-exiftool-perl python3 python3-pip && pip3 install Pillow numpy`
- macOS: `brew install imagemagick exiftool python3 && pip3 install Pillow numpy`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要提权或管理员权限 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 4 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
