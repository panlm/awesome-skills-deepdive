# Ultimate Fork and Skill Scanner

## 标题和描述

**Fork and Skill Scanner Ultimate** (v1.1.1) — 扫描 GitHub Fork 和 ClawHub 技能，发现有价值的变更、创新和增强功能。每次运行可分析多达 1,000 个 Fork。

- **作者**: @globalcaos
- **分类**: Git & GitHub
- **许可证**: MIT
- **安装**: `clawhub install globalcaos/fork-and-skill-scanner-ultimate`

## 功能特点

- **大规模 Fork 扫描**: 每次运行可分析多达 1,000 个 GitHub Fork
- **三阶段过滤漏斗**:
  1. **Bash 预过滤** — 几秒内丢弃不活跃和完全相同的 Fork，不浪费 Token
  2. **子智能体深度分析** — 通过并行智能体检查存活的 Fork：diff 质量、新模式、性能变化
  3. **可操作报告** — 只有值得关注的 Fork 才会通过，通过 WhatsApp 推送
- **每日技能评审**: 每天评审 10 个 ClawHub 技能，追踪新趋势
- **Token 高效设计**: Bash 先做繁重工作，智能体只处理有价值的内容
- **仅在有值得报告的内容时才发送报告**

## 使用方法/示例

```bash
# 安装
clawhub install globalcaos/fork-and-skill-scanner-ultimate

# 或使用 npx
npx clawhub@latest install globalcaos/fork-and-skill-scanner-ultimate

# 或粘贴仓库链接到助手聊天
https://github.com/openclaw/skills/tree/main/skills/globalcaos/fork-and-skill-scanner-ultimate
```

### 工作流程
1. 指定要扫描的 GitHub 仓库
2. 技能自动获取并预过滤 Fork 列表
3. 对有价值的 Fork 进行深度分析
4. 生成可操作的报告并推送通知

## 安全评估

| 评估项目 | 状态 | 说明 |
|---------|------|------|
| 源码可用性 | ✅ 可用 | GitHub 仓库源码可审计 |
| 下载量 | 🟡 低 | 新发布的技能，下载量较少 |
| API 访问 | ✅ 只读 | 使用 GitHub 公共 API（只读），无需认证 |
| 子智能体 | ⚠️ 注意 | 通过 OpenClaw sessions_spawn 本地生成子智能体 |
| 外部通信 | ⚠️ 注意 | 报告通过已配置的渠道（如 WhatsApp）发送 |
| 凭据存储 | ✅ 无 | 不存储或请求凭据 |
| 许可证 | ✅ MIT | 开源友好许可 |
| 总体评级 | 🟡 可疑 | 功能合理但涉及子智能体生成和外部消息推送，需谨慎使用 |

**注意事项**:
- 使用 GitHub 公共 API（只读），对公共仓库无需认证
- 子智能体通过 OpenClaw 的 `sessions_spawn` 在本地生成
- 报告通过已配置的消息渠道推送
- 未存储或请求任何凭据
- 建议在使用前审查子智能体的行为范围

## 附加资源列表

- ClawSkills 页面: https://clawskills.sh/skills/globalcaos-ultimate-fork-and-skill-scanner
- GitHub 源码: https://github.com/openclaw/skills/tree/main/skills/globalcaos/fork-and-skill-scanner-ultimate
- 完整项目: https://github.com/globalcaos/clawdbot-moltbot-openclaw
- 版本: v1.1.1
- 发布时间: 2026-02-21
