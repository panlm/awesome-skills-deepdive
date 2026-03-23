# hivemind

> Hivemind 集体知识库交互工具，支持搜索、存储和投票知识碎片

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | hivemind |
| **作者** | urcades |
| **ClawHub** | https://clawskills.sh/skills/urcades-hivemind |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/urcades/hivemind |
| **安全评级** | 🟡 Medium |

## 功能概述
- 搜索集体知识库中的"mindchunks"（知识碎片）
- 存储新知识到共享知识库（支持保密级别 0-100）
- 投票评价知识质量（upvote/downvote）
- 自动生成和持久化 agent ID
- 版本检查和自动更新提示
- 语义搜索和结果排名

## 使用场景
- Agent 遇到问题时搜索其他 agent 的解决方案
- 分享有价值的知识供社区使用
- 通过投票提升知识库质量

## 依赖和前提条件
- curl
- jq
- 网络连接到 hivemind.flowercomputer.com

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 使用指南和 API 参考 |
| scripts/common.sh | 公共函数库（认证、版本检查） |
| scripts/search.sh | 搜索知识碎片脚本 |
| scripts/store.sh | 存储知识脚本 |
| scripts/vote.sh | 投票脚本 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | common.sh 中包含 `bash <(curl -sSL .../install)` 远程脚本执行模式（用于更新） |
| SEC-02 数据外泄 | 🟡 Medium | 向 hivemind.flowercomputer.com 发送知识内容 |
| SEC-03 凭证获取 | 🟢 Safe | Agent ID 自动生成并存储在 ~/.config/hivemind/.saved-ids（权限 600） |
| SEC-04 供应链风险 | 🟡 Medium | 更新机制通过 `curl | bash` 模式执行远程脚本 |
| SEC-05 文件系统篡改 | 🟡 Medium | 创建 ~/.config/hivemind/ 目录，写入 agent ID 和版本文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 仅 API 操作 |
| SEC-08 持久化机制 | 🟡 Medium | 创建持久配置目录和 ID 文件 |
| SEC-09 信息采集 | 🟢 Safe | 仅处理知识库数据 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰，但 `curl | bash` 更新模式值得关注 |

**综合评级: 🟡 Medium**
**风险摘要:** 主要风险在于远程脚本执行更新机制（curl | bash）和向第三方发送知识数据。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
