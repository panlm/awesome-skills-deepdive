# App Store Screenshot Generation

> 使用 each::sense AI 生成 App Store 和 Google Play 应用商店截图素材

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | App Store Screenshot Generation |
| **作者** | eftalyurtseven |
| **版本** | 1.0 |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/eftalyurtseven-app-store-screenshot-generation |

## 功能概述
- 生成 iOS App Store 截图（iPhone 6.7" 1320x2868、iPad 12.9" 2064x2752）
- 生成 Google Play Store 截图（Android 手机 1080x1920）
- 支持设备边框渲染、功能高亮标注和宣传文案叠加
- 生成多语言本地化版本的截图素材
- 支持生活场景类截图（如机场持机场景）
- 提供深色/浅色模式变体和 A/B 测试变体
- 支持应用预览缩略图和入门引导序列截图

## 使用场景
- 移动应用开发者为 App Store 和 Google Play 准备上架截图
- 批量生成多语言版本的应用商店展示图片
- 快速迭代不同创意方案，进行 A/B 测试优化下载转化率

## 依赖和前提条件
- 环境变量 `EACHLABS_API_KEY`（each::sense API 密钥）
- 网络访问 `https://sense.eachlabs.run`

## 安全状态

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，0 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
