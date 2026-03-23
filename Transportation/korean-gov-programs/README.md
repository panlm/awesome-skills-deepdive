# Korean Gov Programs

> Collect Korean government support programs (TIPS, Small Business, R&D grants) into structured JSONL files. Supports incremental collection with checkpoints.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Korean Gov Programs |
| **作者** | lifeissea |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/lifeissea-korean-gov-programs |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lifeissea/korean-gov-programs |
| **安全评级** | 🟢 Low |

## 功能概述
- APPEND 전용: 기존 파일 덮어쓰기 절대 없음
- 중복 방지: title 기준 중복 자동 스킵
- 체크포인트: `.checkpoint.json`에 진행 상태 저장 → 재실행 시 이어서 수집
- 딜레이: 요청 간 0.8초 대기 (서버 부하 방지)

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `package.json`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。凭证获取：需要 API 密钥或令牌；持久化机制：涉及定时或后台任务

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23