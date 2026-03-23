# Colormind

> 通过 Colormind.io API 生成配色方案，支持锁定颜色、图像取色和多种模型选择

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Colormind |
| **作者** | boilerrat |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/boilerrat-colormind |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/boilerrat/colormind |
| **安全评级** | 🟢 Low |

## 功能概述
- 调用 Colormind.io API 生成随机或约束配色方案
- 支持锁定特定颜色槽位，让 AI 填充其余颜色
- 提供多种配色模型（default、ui 等），每日更新
- 通过 ImageMagick 从图像中提取主要颜色生成配色方案
- 输出 JSON 格式结果，支持 --pretty 模式显示 Hex + RGB
- 列出当前可用的配色模型

## 使用场景
- 为 UI 设计快速生成协调的配色方案
- 基于品牌色锁定后自动补充配套颜色
- 从产品图片中提取颜色并生成匹配的设计色板

## 依赖和前提条件
- Node.js（运行脚本）
- ImageMagick `convert` 命令（图像取色功能需要）
- Python3（辅助脚本）
- 网络连接（调用 colormind.io API，注意使用未加密 HTTP）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
