# Avito.ru publish and chat

> Avito.ru 平台管理工具，通过 API 管理俄罗斯最大分类信息网站的账号、商品和消息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Avito.ru publish and chat |
| **作者** | ruslanlanket |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/ruslanlanket-avito |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ruslanlanket/avito |
| **安全评级** | 🔴 High |

## 功能概述
- 管理 Avito.ru 商品列表
- 发布和编辑商品信息
- 收发买卖双方消息
- 账号状态和统计查询
- 订单和交易管理
- 商品数据批量操作

## 使用场景
- 自动化管理 Avito 电商店铺的商品上下架
- 智能体自动回复买家咨询消息
- 批量管理多个 Avito 商品列表

## 依赖和前提条件
- Avito.ru 卖家账号
- Avito API 访问令牌
- 网络能访问 Avito.ru 服务

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🔴 High**
**风险摘要:** 存在 1 项高风险，1 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
