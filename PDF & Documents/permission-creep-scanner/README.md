# Permission Creep Scanner

> 权限蔓延扫描工具，检测过度权限

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Permission Creep Scanner |
| **作者** | andyxinweiminicloud |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/andyxinweiminicloud-permission-creep-scanner |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/permission-creep-scanner |
| **安全评级** | 🔴 High |

## 功能概述
- 扫描检测过度权限配置
- 权限蔓延趋势分析
- 生成权限优化建议
- 定期审计报告

## 使用场景
- 定期扫描系统账户检测不必要的权限积累
- 生成权限审计报告并提供收敛建议

## 依赖和前提条件
- API 密钥
- Python 运行环境
- OpenAI API
- AWS

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 发现直接命令执行指令 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🔴 High | 涉及危险文件操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🔴 High | 大量系统信息采集 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 5 项高风险，2 项中风险。命令执行：发现直接命令执行指令；数据外泄：大量外部数据传输




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23