# salute speech

> Salute Speech 语音识别和合成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | salute speech |
| **作者** | chorus12 |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/chorus12-salute-speech |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/chorus12/salute-speech |
| **安全评级** | 🟡 Medium |

## 功能概述
- API Key: Environment variable `SALUTE_AUTH_DATA` must be set (Base64-encoded `client_id:client_secret` or raw authorization key from https://developers.sber.ru/studio/)
- SSL note: The script disables SSL verification by default (`verify_ssl=False`) because Sber's certificate chain is non-standard. This is expected
- Token is valid for ~30 minutes; the script fetches a new one each run
- Large files (>1 hour) may need `--max-wait-time` increased beyond 300s
- The `callcenter` model is optimized for telephony audio (8kHz, mono)
- Profanity filter is disabled by default (`enable_profanity_filter=False`)
- The script uses normalized text by default (numbers as digits, abbreviations expanded). Raw text is also available in the JSON output

## 使用场景
- 执行高精度的语音识别
- 支持多语言语音合成
- 实时语音转文字处理

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `salute_transcribe.py`

## 安全状态
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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，3 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
