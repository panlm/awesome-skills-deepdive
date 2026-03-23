# Bookkeeper

> 预算记账自动化元技能，通过编排 Gmail、OCR 等工具实现自动记账

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Bookkeeper |
| **作者** | h4gen |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/h4gen-bookkeeper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/h4gen/bookkeeper |
| **安全评级** | 🔴 High |

## 功能概述
- 自动从 Gmail 提取收据和发票
- OCR 识别纸质收据内容
- 自动分类和记录交易
- 编排多个子技能协同工作
- 生成财务汇总报告

## 使用场景
- 自动扫描邮箱中的电子收据并录入账本
- 拍照上传纸质收据自动识别金额和类别
- 月末自动汇总所有支出生成分类报告

## 依赖和前提条件
- Gmail 访问权限、OCR 服务、多个子技能

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🔴 High | 需要安装外部包且含管道安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 3 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
