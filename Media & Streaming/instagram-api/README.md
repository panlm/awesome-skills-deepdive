# Instagram Api

> Instagram API 集成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Instagram Api |
| **作者** | lifeissea |
| **类目** | 媒体与流媒体 |
| **ClawHub** | https://clawskills.sh/skills/lifeissea-instagram-api |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lifeissea/instagram-api |
| **安全评级** | 🟡 Medium |

## 功能概述
- Graph API Explorer: https://developers.facebook.com/tools/explorer/
- 장기 토큰(Long-lived token)으로 교환: 60일 유효
- Instagram은 공개 URL로만 미디어 업로드 가능 (로컬 파일 직접 업로드 불가)
- 이 스킬은 Imgur를 통해 임시 공개 URL 생성
- 릴스 동영상 처리에는 수분 소요될 수 있음
- API 호출 실패 시 `~/logs/sns/` 로그 확인

## 使用场景
- 通过 API 管理 Instagram 内容发布
- 获取 Instagram 账号数据和分析
- 自动化 Instagram 社交媒体运营

## 依赖和前提条件
- OAuth

## 包含文件
- `SKILL.md`
- `_meta.json`
- `scripts`

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
