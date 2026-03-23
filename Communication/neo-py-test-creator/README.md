# Skill

> 自动分析 Python 函数并生成 pytest 兼容的单元测试模板，提升测试覆盖率

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Skill |
| **作者** | martinforsulu |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/martinforsulu-neo-py-test-creator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/martinforsulu/neo-py-test-creator |
| **安全评级** | 🔴 High |

## 功能概述
- 自动解析 Python 函数签名和文档字符串
- 生成 pytest 兼容的测试用例模板
- 覆盖正常输入、边界值和异常场景
- 支持 mock 和 fixture 的自动生成
- 测试文件结构自动组织
- 支持参数化测试生成

## 使用场景
- 为新编写的 Python 模块快速生成测试框架
- 提升现有项目的单元测试覆盖率
- 代码审查时自动补充缺失的测试用例

## 依赖和前提条件
- Python 3.x 运行环境
- pytest 库已安装
- 待测试的 Python 源代码文件

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
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
