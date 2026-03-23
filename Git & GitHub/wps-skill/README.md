# Wps Skill

> WPS Office 自动化操作 Skill，支持文档创建、格式转换和批量处理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Wps Skill |
| **作者** | lilei0311 |
| **版本** | 1.0.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/lilei0311-wps-skill |

## 功能概述
- 创建 Word、Excel、PPT 文档（支持带初始内容创建）
- 打开已有 WPS 文档
- 列出指定目录中的文档文件
- 格式转换：在 PDF、Word、Excel 等格式间互转
- 批量转换整个目录下的文档格式
- 通过 OpenClaw Agent 自然语言指令操作 WPS

## 使用场景
- 通过 AI Agent 自然语言指令批量创建和管理办公文档
- 将目录下的所有文档批量转换为 PDF 格式
- 日常办公文档的自动化创建和格式转换

## 依赖和前提条件
- 系统已安装 **WPS Office**
- Python 依赖：`pyautogui`、`pyperclip`、`Pillow`（`pip install pyautogui pyperclip Pillow`）
- macOS 需要授予自动化权限
- 可选配置 `config.json` 中的默认保存路径和 WPS 安装路径

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
