# envios

> 阿根廷物流配送管理技能，涵盖配送区域、时间和问题处理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | envios |
| **作者** | jalfargentina |
| **ClawHub** | https://clawskills.sh/skills/jalfargentina-envios |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jalfargentina/envios |
| **安全评级** | 🟢 Low |

## 功能概述
- 阿根廷全国配送（除火地岛）
- CABA/GBA 当日送达（King Flex 摩托）
- 内陆地区快递配送（Andreani/OCA）
- 按区域的预计配送时间表
- 地址验证（Google Maps）
- 损坏包裹处理流程

## 使用场景
- 客户咨询配送时间和覆盖范围
- 处理包裹延迟或损坏投诉
- 验证客户配送地址

## 依赖和前提条件
- 无（纯知识型 Skill）

## 包含文件
SKILL.md（完整配送知识库）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无代码执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 未获取凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 纯知识内容 |
| SEC-10 混淆/反分析 | 🟢 Safe | 西班牙语文本完全可读 |

**综合评级: 🟢 Low**
**风险摘要:** 纯知识型配送指南，零风险

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
