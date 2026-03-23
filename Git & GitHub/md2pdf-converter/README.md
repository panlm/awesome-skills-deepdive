# Markdown to PDF Converter (v2.0)

> 离线 Markdown 转 PDF 工具，完整支持 Unicode、中文字体和 3660 个彩色 Emoji。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Markdown to PDF Converter (v2.0) |
| **作者** | tianxingleo |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/tianxingleo-md2pdf-converter |

## 功能概述
- 将 Markdown 文档转换为专业排版的 PDF
- 完整的 Unicode 支持（中文、日文、韩文）
- 完整的 Emoji 支持（Twemoji 14.0.0，3660 个彩色 PNG）
- 支持所有 Emoji 变体（肤色、发型、地区旗帜等）
- 首次运行后可完全离线工作
- 专业 PDF 布局，含页码、代码高亮、表格和引用块
- 使用 Python 生成精确的 Emoji 映射表

## 使用场景
- 将含中文和 Emoji 的 Markdown 报告转换为可分享的 PDF
- 在离线环境下批量生成专业格式的文档
- 为团队文档或技术报告生成带完整 Emoji 渲染的 PDF

## 依赖和前提条件
- Pandoc（通用文档转换器）
- WeasyPrint（CSS 转 PDF 渲染器）
- Python 3（用于 Emoji 映射生成）
- wget（仅首次运行时下载 ~150MB Emoji 资源）
- 首次运行会下载 Twemoji 14.0.0 到 `~/.cache/md2pdf/emojis/`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。命令执行：存在命令执行相关引用；供应链风险：需要安装外部依赖；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive skill 自动生成
