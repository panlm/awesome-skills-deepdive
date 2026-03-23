# pancake-skills

> Tương tác với Pancake Platform API để quản lý pages, conversations, messages, customers, statistics, tags, posts, users. Sử dụng khi cần (1) Quản lý pages và tạo access token, (2) Xử lý conversations và messages, (3) Quản lý thông tin customers, (4) Xem statistics và analytics, (5) Quản lý tags và posts, (6) Quản lý users/staff, (7) Upload media content, (8) Chat plugin operations.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | pancake-skills |
| **作者** | suminhthanh |
| **类目** | 营销与销售 |
| **ClawHub** | https://clawskills.sh/skills/suminhthanh-pancake-skills |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/suminhthanh/pancake-skills |
| **安全评级** | 🟡 Medium |

## 功能概述
- Write Protection: All write operations require `CONFIRM_WRITE=YES`
- Token Security: Tokens are URL-encoded automatically
- Validation: Clear error messages for missing required parameters
- Bảo vệ ghi: Tất cả thao tác ghi yêu cầu `CONFIRM_WRITE=YES`
- Bảo mật token: Token được URL-encode tự động
- Xác thực: Thông báo lỗi rõ ràng khi thiếu tham số bắt buộc

## 使用场景
- 营销活动管理和执行
- 客户获取和转化
- 销售流程优化

## 包含文件
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
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
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23