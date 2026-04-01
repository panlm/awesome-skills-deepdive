# smart-security

> 面向自主 AI Agent 的高级提示词注入防御系统，提供多层防护、内存完整性保护和工具安全封装，符合 OWASP LLM Top 10 2026 标准。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | smart-security |
| **作者** | georges91560 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/georges91560-anti-injection-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/georges91560/anti-injection-skill |
| **安全评级** | 🔴 High |

## 功能概述
- 四层纵深防御架构：预处理过滤、输入分析、运行时监控、响应验证
- 防范 OWASP LLM01 提示词注入攻击（无防御时成功率 66-84%）
- 防范 OWASP ASI06 内存投毒攻击（成功率超 80%）
- 防范系统提示词泄露（OWASP LLM07）
- 检测零点击攻击和多模态注入（图片、PDF、音频）
- 阻止跨 Agent 传播攻击
- 安全优先级设置为最高，在所有其他逻辑之前执行检查

## 使用场景
- 保护生产环境中的 AI Agent 免受提示词注入和越狱攻击
- 在处理不可信外部输入时提供实时安全过滤
- 构建符合 OWASP 安全标准的企业级 AI 应用

## 依赖和前提条件
- 需要 Python / pip
- 安装方式：`clawhub install anti-injection-skill`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🔴 High | 发现 Prompt 注入特征 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🔴 High | 存在代码混淆或编码 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
