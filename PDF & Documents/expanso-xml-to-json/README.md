# Expanso xml-to-json

> XML 数据转换为 JSON 格式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Expanso xml-to-json |
| **作者** | aronchick |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/aronchick-expanso-xml-to-json |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-xml-to-json |
| **安全评级** | 🟢 Low |

## 功能概述
- XML 文档解析和转换
- 处理属性和命名空间
- 支持复杂 XML 结构
- 输出标准 JSON 格式

## 使用场景
- 将旧系统的 XML 数据转换为 JSON 格式
- 解析 XML API 响应为更易处理的 JSON

## 依赖和前提条件
- 无特殊依赖

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `pipeline-cli.yaml`
- `pipeline-mcp.yaml`
- `skill.yaml`
- `test`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；越权操作：涉及权限相关操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23