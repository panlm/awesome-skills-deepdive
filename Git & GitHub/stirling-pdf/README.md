# Stirling PDF

> 通过 Stirling-PDF API 操作 PDF 文件：合并、拆分、转换、OCR、压缩、签名、涂黑等 60+ 工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Stirling PDF |
| **作者** | angusthefuzz |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/angusthefuzz-stirling-pdf |

## 功能概述
- 页面操作：合并多个 PDF、拆分、旋转、提取指定页面、重新排序
- 格式转换：Word/Excel/图片/HTML → PDF，PDF → Word/图片/文本
- 内容处理：压缩文件大小、OCR 识别使扫描件可搜索、添加水印和印章
- 安全功能：添加/移除密码保护、涂黑敏感内容、清除元数据/脚本
- 签名功能：为 PDF 添加电子签名
- 60+ 工具通过 REST API 提供，支持直接 curl 调用
- 提供 Node.js 封装脚本简化常用操作

## 使用场景
- AI Agent 在工作流中自动处理 PDF（如合并报告、压缩文件、OCR 扫描件）
- 自动化批量 PDF 处理流水线（格式转换、添加水印、密码保护）
- 需要自托管 PDF 处理服务以确保数据安全的企业场景

## 依赖和前提条件
- 自托管的 Stirling-PDF 实例
- 环境变量 `STIRLING_PDF_URL`：实例 URL（默认 `http://localhost:8080`）
- 环境变量 `STIRLING_API_KEY`：API 密钥（如启用认证）
- `node`、`curl`

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
