# Prompt Compression

> 本地运行的 Prompt 压缩工具，在 AI 开发迭代循环前减少输入 token 消耗

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Prompt Compression |
| **作者** | trinitybotserver |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/trinitybotserver-compression |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/trinitybotserver/compression |
| **安全评级** | 🟡 Medium |

## 功能概述
- 在 AI 开发循环运行前压缩 prompt/指令文件以减少输入 token
- 自动创建 .bak 备份文件，支持即时回滚
- 完全本地运行，不调用任何模型或外部 API
- 支持 balanced（平衡）和 aggressive（激进）两种压缩模式
- 提供 PowerShell 和 bash 两种安装方式
- 包含 ClawHub 打包工具和安全扫描脚本

## 使用场景
- 在长 prompt 迭代开发中减少 API 调用成本
- 压缩大型指令文件以适应模型上下文窗口限制
- 在 CI/CD 管道中自动化 prompt 优化流程

## 依赖和前提条件
- bash 4+
- jq（JSON 处理）
- bc（数学计算）
- PowerShell（Windows 用户可选）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 6 项中风险。命令执行：存在命令执行相关引用；数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌

---
> 本文档由 awesome-skills-deepdive skill 自动生成
