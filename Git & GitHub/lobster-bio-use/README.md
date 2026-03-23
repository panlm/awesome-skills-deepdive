# LobsterBio - Use

> 使用 Lobster AI 分析生物数据，包括单细胞/批量 RNA-seq、文献挖掘、数据集发现和可视化。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | LobsterBio - Use |
| **作者** | cewinharhar |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/cewinharhar-lobster-bio-use |

## 功能概述
- 分析单细胞和批量 RNA-seq 数据
- 搜索 PubMed/GEO 数据库查找论文和数据集
- 对生物数据执行质量控制（QC）
- 细胞聚类、寻找标记基因、差异表达分析
- 创建出版质量的可视化图表（UMAP、火山图等）
- 支持 H5AD、CSV、10X、GEO/SRA 等多种数据格式
- 通过自然语言或斜杠命令与 Lobster 专家代理交互

## 使用场景
- 生物信息学研究人员快速分析单细胞测序数据
- 从公开数据库搜索和下载相关数据集进行二次分析
- 生成用于论文发表的高质量生物信息学图表

## 依赖和前提条件
- Lobster AI 已安装并配置（`lobster config-test` 验证）
- 安装方式：`curl -fsSL https://install.lobsterbio.com | bash`（macOS/Linux）
- 或通过 pip：`pip install 'lobster-ai[full]'`
- 需要运行 `lobster init` 配置 API Key 和代理包

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，1 项中风险。数据外泄：大量外部数据传输

---
> 本文档由 awesome-skills-deepdive skill 自动生成
