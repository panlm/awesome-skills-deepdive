# Invoice Generator

> 专业发票自动生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Invoice Generator |
| **作者** | tmigone |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/tmigone-invoice-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tmigone/invoice-generator |
| **安全评级** | 🟡 Medium |

## 功能概述
- 根据模板自动生成标准发票
- 支持自定义公司信息和发票格式
- 自动计算金额、税费和总计
- 导出为 PDF 格式
- 支持多币种和多语言

## 使用场景
- 为客户项目自动生成月度服务发票
- 批量创建标准化的商业发票文档

## 依赖和前提条件
- Node.js
- npm

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package-lock.json`
- `package.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；供应链风险：需要安装外部依赖；文件系统篡改：存在文件系统操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23