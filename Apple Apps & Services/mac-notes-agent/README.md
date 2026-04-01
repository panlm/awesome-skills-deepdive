# mac-notes-agent

> 读取和管理 macOS 备忘录应用中的笔记

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | mac-notes-agent |
| **作者** | swancho |
| **ClawHub** | https://clawskills.sh/skills/swancho-mac-notes-agent |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/swancho/mac-notes-agent |
| **许可证** | CC-BY-NC-4.0 |
| **安全评级** | 🟡 Medium |

## 功能概述
- Apple Notes에 노트를 생성/조회/수정/삭제/검색할 수 있습니다.
- 내부 구현은 `osascript`(AppleScript)를 통해 Notes 앱을 제어하는 Node.js CLI입니다.
- macOS (Notes 앱 설치되어 있어야 함)
- Node.js (OpenClaw와 동일 환경)
- title "오늘 회의 메모" \
- body "첫 줄\n둘째 줄\n셋째 줄" \

## 依赖和前提条件
- macOS with the built-in Notes app
- Node.js
- `osascript` available on PATH (default on macOS)

## 包含文件
- `ORIGINAL_README.md` — 原始说明文档
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `cli.js` — 脚本文件

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 包含可执行脚本 |
| SEC-02 数据外泄 | 🟡 Medium | 向外部 API 发送数据 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在中等风险项，建议审查相关配置和权限

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23