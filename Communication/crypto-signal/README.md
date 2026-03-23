# Crypto Signal

> AI 驱动的加密货币情报系统，从 50+ Telegram 群组中提取趋势话题、交易警报和市场信号

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Crypto Signal |
| **作者** | qiantanxiaohai |
| **版本** | 0.1.1 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/qiantanxiaohai-crypto-signal |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/qiantanxiaohai/crypto-signal |
| **安全评级** | 🟢 Low |

## 功能概述
- 聚合 50+ Telegram 加密货币群组的实时信息
- AI 分析趋势话题和热门币种
- 交易信号识别与警报推送
- 市场情绪分析与量化评分
- 自定义关注币种和关键词过滤
- 历史信号回溯与准确率统计

## 使用场景
- 加密货币交易者获取实时市场情报
- 监控 Telegram 群组中的交易信号和项目动态
- 追踪市场热点和新兴代币趋势

## 依赖和前提条件
- Telegram 账号及 API 凭据
- OpenClaw 环境已配置
- 已加入相关 Telegram 加密货币群组

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `crypto-signal.py`
- `install.sh`

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
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
