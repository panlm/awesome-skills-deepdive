# Expanso json-to-yaml

> JSON 数据转换为 YAML 格式

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Expanso json-to-yaml |
| **作者** | aronchick |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/aronchick-expanso-json-to-yaml |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aronchick/expanso-json-to-yaml |
| **安全评级** | 🟢 Low |

## 功能概述
- JSON 到 YAML 的精确转换
- 保持数据结构完整性
- 支持复杂嵌套结构
- 输出格式规范的 YAML

## 使用场景
- 将 JSON 配置文件转换为 YAML 格式
- 在不同配置格式间迁移数据

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
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23