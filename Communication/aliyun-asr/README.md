# Aliyun Asr

> 阿里云语音识别工具，将语音消息转换为文字，兼容飞书等多渠道音频输入

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Aliyun Asr |
| **作者** | jixsonwang |
| **版本** | 1.0.10 |
| **类目** | Communication |
| **ClawHub** | https://clawskills.sh/skills/jixsonwang-aliyun-asr |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/jixsonwang/aliyun-asr |
| **安全评级** | 🟡 Medium |

## 功能概述
- 调用阿里云 ASR 服务进行语音转文字
- 支持飞书语音消息自动转录
- 兼容多种音频格式和渠道来源
- 支持中文普通话和多种方言识别
- 实时和离线两种转录模式
- 转录结果带时间戳和置信度

## 使用场景
- 飞书群聊中的语音消息自动转为文字方便查阅
- 会议录音批量转录生成文字记录
- 多渠道语音内容的统一文字化处理

## 依赖和前提条件
- 阿里云账号及 ASR 服务开通
- 阿里云 AccessKey ID 和 Secret
- 飞书应用凭证（如需飞书集成）

## 包含文件
- `README.md`
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
