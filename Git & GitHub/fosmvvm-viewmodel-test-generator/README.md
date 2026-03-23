# FOSMVVM ViewModel Test Generator

> 为遵循 FOSMVVM 架构的 ViewModel 自动生成测试文件，支持编码往返、版本稳定性和多语言翻译验证。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | FOSMVVM ViewModel Test Generator |
| **作者** | foscomputerservices |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/foscomputerservices-fosmvvm-viewmodel-test-generator |

## 功能概述
- 为 ViewModel 生成遵循 FOSMVVM 模式的测试文件（`*ViewModelTests.swift`）
- 验证 Codable 编码/解码往返不丢失数据
- 检测 ViewModel 版本结构变化以确保版本稳定性
- 验证所有 `@LocalizedString` 属性在所有支持的 locale 中都有翻译值
- 支持嵌套子 ViewModel 的递归测试
- 提供 `LocalizableTestCase` 协议基础设施，一行代码即可完成全部测试
- 自动生成 YAML 翻译文件用于测试
- 支持 `@LocalizedSubs` 替换行为验证

## 使用场景
- 为新创建的 ViewModel 添加完整的单元测试覆盖
- 确保多语言本地化翻译完整性（如英文/西班牙文）
- 在 Swift Package Manager 项目中验证 ViewModel 数据模型的向后兼容性

## 依赖和前提条件
- Swift 开发环境（macOS 或 Linux）
- FOSFoundation、FOSMVVM、FOSTesting 框架
- SPM（Swift Package Manager）项目结构

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成
