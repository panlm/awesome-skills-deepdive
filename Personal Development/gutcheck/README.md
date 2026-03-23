# gutcheck

> 直觉检查 — AI 辅助的决策验证和风险评估

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | gutcheck |
| **作者** | allen566 |
| **ClawHub** | https://clawskills.sh/skills/allen566-gutcheck |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/allen566/gutcheck |
| **许可证** | 未指定 |
| **安全评级** | 🟡 Medium |

## 功能概述
- User authentication system with secure registration and login
- Personalized meal tracking with digestive impact assessment
- Food sensitivity identification through data analysis
- Gut health metrics and progress tracking
- Scientifically-backed dietary recommendations
- Access the application at http://localhost:3000

## 依赖和前提条件
- 
- Create a .env file with required environment variables:
- Run the application:

## 包含文件
- `MARKETING_BREAKTHROUGH.md`
- `MARKETING_PROGRESS_SUMMARY.md`
- `PUBLISHING_INSTRUCTIONS.md`
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `educational_content_plan.md`
- `package.json` — 配置/数据文件
- `press_release.md`
- `publish_gutcheck.js` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
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