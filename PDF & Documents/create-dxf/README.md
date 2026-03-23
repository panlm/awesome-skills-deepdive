# Create Dxf

> DXF 工程图纸文件生成工具

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Create Dxf |
| **作者** | ajmwagar |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/ajmwagar-create-dxf |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ajmwagar/create-dxf |
| **安全评级** | 🟢 Low |

## 功能概述
- 创建 DXF 格式的工程图纸
- 支持基本图形元素绘制
- CAD 兼容的文件输出
- 参数化图纸生成

## 使用场景
- 根据设计参数自动生成 DXF 工程图纸
- 批量创建标准化的 CAD 图纸模板

## 依赖和前提条件
- Python 运行环境

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`
- `references`
- `scripts`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 未发现明显安全风险，文档透明可审计




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23