# Golden Master

> 黄金镜像测试 — 确保系统配置一致性

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Golden Master |
| **作者** | leegitw |
| **ClawHub** | https://clawskills.sh/skills/leegitw-golden-master |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/leegitw/golden-master |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- source-of-truth
- technical-writing
- Role: Help users establish and validate source-of-truth relationships between files
- Understands: Stale documentation causes real problems — wrong instructions, broken examples, confused users
- Approach: Cryptographic checksums create verifiable links; validation is cheap, staleness is expensive
- Boundaries: Identify relationships and staleness, never auto-modify files without explicit request

## 依赖和前提条件
- Data handling**: This skill operates within your agent's trust boundary. All file analysis
- "Check if derived files are current"

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23