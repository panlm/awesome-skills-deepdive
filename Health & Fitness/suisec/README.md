# Sui Sec

> 瑞士安全合规检查工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Sui Sec |
| **作者** | k66inthesky |
| **类目** | 健康与健身 |
| **ClawHub** | https://clawskills.sh/skills/k66inthesky-suisec |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/k66inthesky/suisec |
| **安全评级** | 🟢 Low |

## 功能概述
- Inject `--dry-run` and `--json` flags into the command
- Detect the sender address from the simulation output
- Parse Balance Changes and Object Changes
- Audit against the user's declared SUI intent
- "I want to transfer 10 SUI to 0xABC..."
- "I want to mint an NFT for 0.01 SUI"
- "I want to call the swap function, exchanging 100 USDC for SUI"
- Inform the user: "SuiSec audit passed. Dry-run results are consistent with your intent. Ready to execute."

## 使用场景
- 执行瑞士标准的安全合规检查
- 生成安全合规性评估报告
- 管理安全策略和审计记录

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `main.py`
- `package.json`
- `setup.sh`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
