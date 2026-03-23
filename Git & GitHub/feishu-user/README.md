# feishu-user

> 使用用户访问令牌（User Access Token）进行飞书文档操作，支持读取、创建、写入和追加文档

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | feishu-user |
| **作者** | hacksing |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/hacksing-feishu-user |

## 功能概述
- 使用用户身份（User Access Token）调用飞书开放 API 操作云文档
- 支持文档的读取、创建、写入（覆盖）和追加内容
- 支持 Block 级操作：列出所有 Block、获取/更新/删除特定 Block
- 提供 FeishuClient 类和便捷函数两种调用方式
- 内置 Token 自动刷新脚本（feishu_token.py），缓存到本地配置
- Token 通过 OAuth 授权码流程获取，支持自动续期

## 使用场景
- 以个人身份操作飞书云文档，适合需要访问用户个人文档空间的场景
- 在 AI Agent 中集成飞书文档读写能力，自动化文档内容管理

## 依赖和前提条件
- Python 3 + `requests` 库（`pip install requests`）
- 飞书开放平台应用凭证：APP_ID、APP_SECRET
- 需开启权限：`docx:document`、`drive:drive.search:readonly`、`search:docs:read`
- OAuth 授权回调 URL（REDIRECT_URI）

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
