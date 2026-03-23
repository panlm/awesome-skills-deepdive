# auditing-appstore-readiness

> 审计 iOS 应用的 App Store 合规性和发布准备度

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | auditing-appstore-readiness |
| **作者** | tristanmanchester |
| **ClawHub** | https://clawskills.sh/skills/tristanmanchester-auditing-appstore-readiness |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tristanmanchester/auditing-appstore-readiness |
| **许可证** | 未指定 |
| **安全评级** | 🟢 Low |

## 功能概述
- Native iOS (Swift/Obj‑C, Xcode project/workspace)
- React Native (bare)
- Expo (managed or prebuild)
- Overall verdict: PASS / WARN / FAIL
- Detected project flavour and key identifiers (bundle id, version, build)
- A list of checks with evidence and remediation steps

## 依赖和前提条件
- config generation (`expo prebuild`)
- signing automation (`fastlane match`)
- archiving (`xcodebuild archive`, `eas build`) — creates artefacts and may require signing
- In‑app purchases / subscriptions configured if used

## 包含文件
- `README.md` — 中文说明文档
- `SKILL.md` — 技能定义文件
- `_meta.json` — 元数据
- `references/` — 目录
- `scripts/` — 目录

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无直接命令执行 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API Key/Token |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无提权操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集行为 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码透明可审计 |

**综合评级: 🟢 Low**
**风险摘要:** 低风险技能，可安全使用

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23