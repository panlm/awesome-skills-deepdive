# Greek Compliance Aade

> 希腊税务合规工具，集成 AADE/TAXIS 系统处理增值税、薪资、社保等

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Greek Compliance Aade |
| **作者** | satoshistackalotto |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/satoshistackalotto-greek-compliance-aade |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/satoshistackalotto/greek-compliance-aade |
| **安全评级** | 🔴 High |

## 功能概述
- 处理希腊增值税（VAT）申报和计算
- 集成 AADE/TAXIS 税务系统
- 管理薪资和 EFKA 社保缴纳
- 处理市政税和其他地方税种
- 生成合规性报告

## 使用场景
- 希腊企业的月度增值税申报和提交
- 计算和管理员工薪资及社保缴纳

## 依赖和前提条件
- AADE/TAXIS 系统凭证

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，5 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
