# FOSMVVM ViewModel Test Generator

> Generate ViewModel tests with codable round-trip, versioning stability, and multi-locale translation verification.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | FOSMVVM ViewModel Test Generator |
| **作者** | foscomputerservices |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/foscomputerservices-fosmvvm-viewmodel-test-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/foscomputerservices/fosmvvm-viewmodel-test-generator |
| **安全评级** | 🟡 Medium |

## 功能概述
- Creating tests for new ViewModels
- Adding test coverage to existing ViewModels
- Verifying localization completeness across locales
- Testing ViewModels with embedded/nested child ViewModels
- Verifying `@LocalizedSubs` substitution behavior
- Codable encoding/decoding

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 包含文件
- `SKILL.md`
- `_meta.json`
- `reference.md`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。混淆/反分析：存在代码混淆或编码

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23