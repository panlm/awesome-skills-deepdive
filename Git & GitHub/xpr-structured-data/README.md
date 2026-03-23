# XPR Structured Data

> CSV 解析、JSON 转 CSV 和 SVG 图表生成工具，处理结构化数据并创建可视化图表

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | XPR Structured Data |
| **作者** | paulgnz |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/paulgnz-xpr-structured-data |

## 功能概述
- 解析 CSV 文本为 JSON 对象数组（自动检测分隔符：逗号、制表符、分号、管道符）
- 处理带引号的字段（含嵌入逗号和换行符）
- 将 JSON 数据转换为 CSV 格式输出
- 生成 SVG 图表进行数据可视化
- 支持分页和预览功能（返回列信息、行数和前 5 行预览）
- 提供 `limit` 参数控制返回数据量

## 使用场景
- 快速解析和转换 CSV/JSON 格式的结构化数据
- 将数据转换为 SVG 图表进行可视化展示
- 处理各种分隔符格式的表格数据

## 依赖和前提条件
- 无外部依赖，纯脚本实现

## 安全状态
## 详细安全审计
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
> 本文档由 awesome-skills-deepdive skill 自动生成
