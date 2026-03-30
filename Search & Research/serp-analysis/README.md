# SERP Analysis — 搜索结果页分析

> **作者**: [aaron-he-zhu](https://github.com/aaron-he-zhu) · **版本**: v4.1.0 · **许可证**: Apache-2.0

分析搜索引擎结果页面（SERP），映射排名因素、SERP 特性和 AI Overview 模式。识别排名页面成功的原因、哪些内容格式占据主导地位，以及 SERP 特性机会在哪里。

## 功能概述

- 🔍 **SERP 组成分析**: 映射结果页的所有元素（AI Overview、广告、精选摘要、PAA、知识面板等）
- 📊 **排名因素识别**: 分析 Top 10 结果的域名权重、反向链接、内容长度等指标
- ⭐ **SERP 特性映射**: 识别精选摘要、"大家也在问"、知识面板等特性的获取策略
- 🤖 **AI Overview 分析**: 检查 AI 生成答案的触发条件、引用来源和内容模式
- 🎯 **搜索意图检测**: 从 SERP 组成确认用户意图（信息型/导航型/交易型）
- 📐 **内容格式建议**: 基于 SERP 现状推荐最优内容格式
- 📈 **真实难度评估**: 综合 DA、PA、反向链接等计算排名难度分数（1-100）
- 🆚 **多关键词/多地区对比**: 支持跨关键词、跨地区、移动端 vs 桌面端的 SERP 对比

## 使用场景

1. **内容创作前调研**: 在为目标关键词撰写内容前，先分析 SERP 了解哪些格式和深度的内容能排名，避免盲目创作
2. **竞争对手排名分析**: 理解为什么某个竞争对手排在你前面，找到可以超越的具体切入点
3. **SERP 特性抢占**: 识别精选摘要和 AI Overview 的获取机会，这些特性的竞争通常低于争夺第一名

## 依赖和前提条件

- **运行环境**: Claude Code ≥1.0, skills.sh marketplace, ClawHub marketplace, Vercel Labs skills ecosystem
- **系统依赖**: 无需安装系统包
- **允许工具**: WebFetch（用于抓取搜索结果数据）
- **可选集成**: MCP 网络访问用于 SEO 工具、Search Console、AI Monitor 集成
- **无集成时**: 用户手动提供关键词、SERP 截图、Top 10 排名 URL 等，skill 仍可正常工作
- **所属套件**: [SEO & GEO Skills Library](https://github.com/aaron-he-zhu/seo-geo-claude-skills)（共 20 个 SEO/GEO 技能）

## 包含文件

| 文件 | 说明 |
|------|------|
| `SKILL.md` | 主技能定义文件，包含 8 步分析流程和验证检查点 |
| `_meta.json` | 元数据（版本历史、发布信息） |
| `references/analysis-templates.md` | 每个分析步骤的详细输出模板 |
| `references/example-report.md` | 完整示例报告（"how to start a podcast" 关键词 SERP 分析） |
| `references/serp-feature-taxonomy.md` | SERP 特性完整分类、触发条件、AI Overview 框架、意图信号和波动性评估 |

## 安全审计结果

| 检查项 | 评级 | 发现 |
|--------|------|------|
| SEC-01 命令执行 | 🟢 通过 | 纯指令/模板型 skill，无 shell 命令 |
| SEC-02 数据外泄 | 🟢 通过 | 无外部网络请求，仅通过 WebFetch 读取搜索结果 |
| SEC-03 凭证获取 | 🟢 通过 | 不触碰任何凭证或密钥 |
| SEC-04 供应链风险 | 🟢 通过 | 无软件包安装操作 |
| SEC-05 文件系统篡改 | 🟢 通过 | 不修改系统文件，仅生成分析报告 |
| SEC-06 Prompt 注入 | 🟢 通过 | 指令清晰透明，无隐藏行为 |
| SEC-07 越权操作 | 🟢 通过 | 操作范围与声称的 SERP 分析功能一致 |
| SEC-08 持久化机制 | 🟢 通过 | 无 cron、后台进程或持久化行为 |
| SEC-09 信息采集 | 🟢 通过 | 不收集系统/环境元数据 |
| SEC-10 混淆/反分析 | 🟢 通过 | 所有指令清晰可读，无编码或间接执行 |

**综合评级: 🟢 Safe (安全)**

**ClawHub 状态**: VirusTotal: Benign | OpenClaw: Unknown

**风险摘要**: 该 skill 为纯文本指令型，仅提供 SERP 分析模板和工作流程指导，无命令执行、无凭证读取、无系统修改。使用 WebFetch 工具获取搜索结果数据，属于正常的 SEO 分析操作范围。
