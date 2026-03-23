# DrawThings Image Generation

> 通过 API 使用 DrawThings（Stable Diffusion）在 Mac 本地生成图片，支持 MLX/CoreML 加速

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | DrawThings Image Generation |
| **作者** | dustinparsons |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/dustinparsons-drawthings |

## 功能概述
- 通过文本提示词生成图片，支持自定义步数、CFG Scale、尺寸和采样器
- 批量生成多张变体图片（--batch-size）
- 内置预设配置：快速（8步 UniPC）、高质量（30步 DPM++）、NFT 优化
- 可复现生成（通过指定 seed 值）
- 兼容 Automatic1111 API 接口
- 生成的 PNG 图片自动嵌入提示词和参数元数据

## 使用场景
- 在 Mac 上利用本地 GPU 加速批量生成 AI 图片，无需云端 API
- AI Agent 自动化执行图片生成工作流，测试不同模型和参数组合

## 依赖和前提条件
- macOS + DrawThings 应用（本地 Stable Diffusion 实现）
- 环境变量 `DRAWTHINGS_URL`（默认 http://127.0.0.1:7860）
- Python 3

## 安全状态
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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
