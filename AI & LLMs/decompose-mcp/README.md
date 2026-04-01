# Decompose Mcp

> 将任意文本分解为分类语义单元（权限级别、风险类别、关注度评分、实体提取），无需 LLM，确定性运行

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Decompose Mcp |
| **作者** | echology-io |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/echology-io-decompose-mcp |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/echology-io/decompose-mcp |
| **安全评级** | 🟡 Medium |

## 功能概述
- 将文本分解为结构化语义单元，标注权限级别（mandatory、directive、permissive 等）
- 识别风险类别：安全关键、安全性、合规、财务、合同等
- 计算 0-10 的关注度评分（权限权重 × 风险乘数）
- 提取标准引用（ASTM、ASCE、IBC、OSHA、ISO 等）
- 识别财务数据（金额、百分比、保留金、违约金）
- 支持 URL 内容获取和分解，处理 HTML、Markdown 和纯文本
- 完全本地运行，无需 LLM，输出确定性结果

## 使用场景
- 在发送文档给 LLM 前进行预处理，标注关键合规和安全要求
- 分析合同和规范文档，自动提取强制性条款和风险要素
- 从技术规范中提取标准引用、截止日期和财务条款

## 依赖和前提条件
- Python 3
- pip install decompose-mcp
- 可选：配置 MCP Server 集成

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
