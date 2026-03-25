# leak — 兼容性迁移存根

> 用于从旧版混合 leak 技能迁移到拆分强化技能的兼容性存根。

## 标题和描述

**名称**: leak  
**作者**: eucalyptus-viminalis  
**版本**: 未知  
**Slug**: `eucalyptus-viminalis-leak`

这是一个兼容性存根（compatibility stub），用于帮助用户从旧版混合 leak 技能平滑迁移到新的拆分强化技能。该技能本身不包含实际功能代码。

## 功能特点

- 🔄 **迁移辅助**: 作为旧版 leak 技能的兼容层
- 📦 **存根设计**: 不包含实际功能实现，仅提供迁移路径
- ⚠️ **无 SKILL.md**: 技能源文件缺失，无法获取完整功能描述

## 使用方法/示例

### 安装
```bash
clawhub install eucalyptus-viminalis/leak
```

或使用 npx:
```bash
npx clawhub@latest install eucalyptus-viminalis/leak
```

### 使用说明
该技能为兼容性存根，建议用户直接迁移到对应的拆分强化技能，而非继续使用此存根。

## 安全评估

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | ⚠️ N/A | 无源文件可审计 |
| SEC-02 数据外泄 | ⚠️ N/A | 无源文件可审计 |
| SEC-03 凭证获取 | ⚠️ N/A | 无源文件可审计 |
| SEC-04 供应链风险 | ⚠️ N/A | 无源文件可审计 |
| SEC-05 文件系统篡改 | ⚠️ N/A | 无源文件可审计 |
| SEC-06 Prompt 注入 | ⚠️ N/A | 无源文件可审计 |
| SEC-07 越权操作 | ⚠️ N/A | 无源文件可审计 |
| SEC-08 持久化机制 | ⚠️ N/A | 无源文件可审计 |
| SEC-09 信息采集 | ⚠️ N/A | 无源文件可审计 |
| SEC-10 混淆/反分析 | ⚠️ N/A | 无源文件可审计 |

**综合评级: ⚠️ 无法评估** — SKILL.md 缺失，无法进行完整安全审计。作为兼容性存根，建议用户迁移到正式的拆分强化技能。

## 附加资源列表

- 📦 ClawSkills 页面: https://clawskills.sh/skills/eucalyptus-viminalis-leak
- 🔗 GitHub 源码: https://github.com/clawdbot/skills/tree/main/skills/eucalyptus-viminalis/leak
- 📄 技能文件: `_meta.json`（仅有元数据）

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-25
