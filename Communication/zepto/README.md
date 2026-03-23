# Zepto

> 秒速在 Zepto 平台下单外卖杂货，语音说出需求即可获取支付链接完成购买

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Zepto |
| **作者** | bewithgaurav |
| **版本** | 1.0.6 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/bewithgaurav-zepto |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/bewithgaurav/zepto |
| **安全评级** | 🔴 High |

## 功能概述
- 自然语言描述需求自动生成购物清单
- 在 Zepto 平台自动搜索和添加商品到购物车
- 生成一键支付链接简化结账流程
- 支持地址管理和配送时间选择
- 智能匹配商品处理缺货替代建议
- 语音下单全流程支持

## 使用场景
- 忙碌时快速语音下单日常生活杂货
- 智能助手定期自动补货常用消耗品
- 不方便操作手机时通过语音完成购物

## 依赖和前提条件
- Zepto 账户
- Zepto 服务覆盖区域的配送地址
- 有效的支付方式

## 包含文件
- `ORIGINAL_README.md`
- `PARSER-USAGE.md`
- `PUBLISH_CHECKLIST.md`
- `README.md`
- `SECURITY.md`
- `SKILL.md`
- `ZEPTO_AUTH.md`
- `_meta.json`
- `package.json`
- `test-ops.js`
- `zepto-agent.js`
- `zepto-ops.js`
- `zepto-parser.js`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
