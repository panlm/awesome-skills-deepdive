# habib-pdf-to-json

> PDF 转 JSON — 从 PDF 文档提取结构化数据

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | habib-pdf-to-json |
| **作者** | dbmoradi60 |
| **类目** | 日历与日程管理 |
| **ClawHub** | https://clawhub.ai/skills/dbmoradi60-habib-pdf-to-json |
| **安全评级** | 🟢 Low |

## 功能概述
- PDF 文档内容提取
- 结构化 JSON 数据输出
- 表格和文本识别
- 批量 PDF 处理

## 使用场景
- 日常事务调度和时间管理自动化
- 工作流程编排和任务协调
- 与其他 OpenClaw 技能配合构建自动化流程

## 依赖和前提条件
- Python 3.x 及相关依赖

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23