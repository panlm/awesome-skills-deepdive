# WeChat Moments Copy Generator

> 一键生成微信朋友圈爆款文案，助力个人品牌和社交传播

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | WeChat Moments Copy Generator |
| **作者** | user520512 |
| **版本** | 1.0.0 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/user520512-moments-copy |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/user520512/moments-copy |
| **安全评级** | 🟢 Low |

## 功能概述
- 根据主题生成吸引眼球的朋友圈文案
- 多种文案风格切换（励志、搞笑、文艺等）
- 自动添加热门话题标签
- 配图建议和排版优化
- 支持产品推广和个人生活分享场景
- 文案字数和格式自动适配朋友圈限制

## 使用场景
- 微商产品推广文案的快速生成
- 旅行、美食等生活分享的创意文案撰写
- 个人品牌日常运营的内容输出

## 依赖和前提条件
- OpenClaw 运行环境
- 微信账号（用于发布）

## 包含文件
- `ORIGINAL_README.md`
- `README.md`
- `SKILL.md`
- `_meta.json`
- `package.json`
- `src`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
