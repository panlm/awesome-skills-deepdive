# Word Automation

> 通过 Windows COM 接口自动化 Word/WPS 文档操作，支持读取、替换、插入、合并、拆分及导出等功能

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Word Automation |
| **作者** | fadeloo |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/fadeloo-tiangong-wps-word-automation |

## 功能概述
- 读取 Word/WPS 文档的文本内容
- 查找并替换文档中的文本
- 插入段落、标题、页眉、页脚和分页符
- 合并多个文档为一个或拆分单个文档
- 导出文档为 PDF 或 TXT 格式
- 添加或替换文档中的图片
- 仅适用于单文档操作，不支持批量处理

## 使用场景
- 需要自动化处理 Windows 上的 Word/WPS 文档（如批量修改模板内容、导出 PDF）
- 文档内容替换和格式化场景（如合同模板填充、报告生成）

## 依赖和前提条件
- Windows 操作系统，已安装 **Microsoft Word** 或 **WPS Writer**
- Python 环境
- `pywin32` 库（`python -m pip install pywin32`）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive skill 自动生成
