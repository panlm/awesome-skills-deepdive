# Chief Editor

> 专业主编 AI 助手，支持个性化写作偏好和多源知识整合的内容创作工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Chief Editor |
| **作者** | teamolab |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/teamolab-chief-editor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/teamolab/chief-editor |
| **安全评级** | 🟢 Low |

## 功能概述
- 扮演专业主编角色，根据用户个性化写作偏好进行内容创作
- 支持读取附件文件和知识库文档，整合多源信息
- 自动识别文档中的 URL 并抓取补充内容（最多 5 个关键链接）
- 通过 wiki_retriever 工具从知识库中检索相关文档
- 用户写作偏好优先级最高，覆盖系统提示和其他指令
- 支持模板变量替换（如 $DATE$、$GET_USER_TEMPLATE$ 等）

## 使用场景
- 基于知识库文档和附件资料，自动生成专业文章或报告
- 根据用户偏好风格进行内容改写和编辑
- 整合多个信息源（文件、URL、知识库）创建综合性内容

## 依赖和前提条件
- 无外部依赖，纯指令型 Skill
- 需要配合知识库和文档工具使用

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
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。数据外泄：存在外部 API 调用；Prompt 注入：存在可疑 Prompt 模式

---
> 本文档由 awesome-skills-deepdive skill 自动生成
