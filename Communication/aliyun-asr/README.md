# Aliyun Asr

> "Pure Aliyun ASR skill for voice message transcription, supports multiple channels including Feishu"

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Aliyun Asr |
| **作者** | jixsonwang |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jixsonwang-aliyun-asr |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jixsonwang/aliyun-asr |
| **安全评级** | 🟡 Medium |

## 功能概述
- ✅ 纯ASR识别: 只进行语音到文本的转换，不生成任何语音回复
- ✅ 多通道支持: 支持飞书(Feishu)、Telegram、WhatsApp等所有OpenClaw支持的语音消息通道
- ✅ 自动集成: 无需额外配置，语音消息自动被识别并作为文本消息处理
- 开通 [智能语音交互(NLS)](https://nls-portal.console.aliyun.com/) 服务
- 在RAM控制台创建子用户并分配 `AliyunNLSFullAccess` 权限
- 在NLS控制台创建应用，获取 AppKey

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `__init__.py`
- `_meta.json`
- `aliyun_pure_asr.py`
- `example-config.json`
- `handle_media.py`
- `index.js`
- `main.py`
- `package.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 4 项中风险。数据外泄：存在外部 API 调用；凭证获取：需要 API 密钥或令牌；文件系统篡改：存在文件系统操作

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23