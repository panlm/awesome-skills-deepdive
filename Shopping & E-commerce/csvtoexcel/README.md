# csv-to-excel

> CSV 文件转 Excel 格式工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | csv-to-excel |
| **作者** | xuanguan2020 |
| **ClawHub** | https://clawskills.sh/skills/xuanguan2020-csvtoexcel |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xuanguan2020/csvtoexcel |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Detects CSV encoding automatically (UTF-8, GBK, GB2312, UTF-8-SIG)
- Ensures Chinese characters display correctly in Excel
- No manual encoding specification needed
- Header row: Bold white text on blue background
- Borders: Thin borders around all cells
- Column widths: Auto-adjusted based on content (handles Chinese characters properly)

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 依赖外部包 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23