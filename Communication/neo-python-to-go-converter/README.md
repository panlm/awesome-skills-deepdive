# Skill

> 自动将 Python 代码转换为性能优化的 Go 语言代码，实现跨语言迁移

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | martinforsulu |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/martinforsulu-neo-python-to-go-converter |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/martinforsulu/neo-python-to-go-converter |
| **安全评级** | 🟢 Low |

## 功能概述
- Python 代码自动转换为 Go 代码
- Go 语言性能优化建议
- 类型推断和静态类型转换
- Go 语言惯用写法适配
- 并发模式自动转换（goroutine）
- 依赖包映射和替代建议

## 使用场景
- 将 Python 原型代码转换为高性能 Go 生产代码
- 微服务从 Python 迁移到 Go 的代码转换
- 学习 Go 语言时参照已有 Python 代码进行对照

## 依赖和前提条件
- Go 语言开发环境（go 1.18+）
- Python 3.x 运行环境
- 待转换的 Python 源代码

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `assets`
- `package.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
