# Cacheforge Setup

> CacheForge 环境配置和部署工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Cacheforge Setup |
| **作者** | tkuehnl |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/tkuehnl-cacheforge-setup |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tkuehnl/cacheforge-setup |
| **安全评级** | 🟡 Medium |

## 功能概述
- Set up CacheForge for the first time
- Register a new CacheForge account
- Connect their LLM API provider to CacheForge
- Get a CacheForge API key
- Preset default base URLs:
- openrouter → `https://openrouter.ai/api/v1`
- anthropic → `https://api.anthropic.com`
- custom → `https://api.fireworks.ai/inference/v1`

## 使用场景
- 配置和部署缓存服务环境
- 初始化缓存集群设置
- 管理缓存服务的配置参数

## 依赖和前提条件
- Python / pip
- API Key

## 包含文件
- `CHANGELOG.md`
- `ORIGINAL_README.md`
- `SECURITY.md`
- `SKILL.md`
- `TESTING.md`
- `_meta.json`
- `setup.py`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，1 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
