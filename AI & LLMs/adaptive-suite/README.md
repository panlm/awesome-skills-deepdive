# adaptive-suite

> 一个持续自适应的技能套件，让 Agent 扮演全能型编码员、业务分析师、项目经理和数据分析师

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | adaptive-suite |
| **作者** | afajohn |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/afajohn-adaptive-suite |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/afajohn/adaptive-suite |
| **安全评级** | 🟢 Low |

## 功能概述
- 持续搜索发现免费在线工具、API 和开源资源
- 自适应 AI 编码助手：跨多语言和框架，根据用户编码风格动态调整
- 业务分析与项目管理：提供 Agile、Lean 等方法论的战略规划建议
- Web 开发辅助：支持 HTML/CSS/JS 及数据库 Schema 设计
- NAS 元数据扫描器：只读模式采集文件名、元数据和目录结构
- 持续学习机制：从用户交互中改进推荐质量

## 使用场景
- 为个人或小团队提供跨领域的全栈技术支持和项目管理辅助
- 在有限预算下寻找和推荐免费替代方案和开源工具
- 扫描 NAS 存储设备的文件结构并生成元数据报告

## 依赖和前提条件
- Python、Node.js、curl、sqlite3
- FREE_API_KEYS 环境变量

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 3 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive skill 自动生成
