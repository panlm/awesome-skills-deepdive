# sprite-sheet

> 精灵图和纹理图集全面指南，涵盖 Rust（Macroquad/Bevy）和 Godot 4.x 的游戏资源管理

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | sprite-sheet |
| **作者** | kjaylee |
| **ClawHub** | https://clawskills.sh/skills/kjaylee-sprite-sheet |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/kjaylee/sprite-sheet |
| **安全评级** | 🟢 Low |

## 功能概述
- 精灵图和纹理图集的核心概念（帧动画、元数据格式）
- Rust Macroquad WASM 就绪的精灵动画实现
- Rust Bevy ECS 架构的纹理图集系统
- Godot 4.x AnimatedSprite2D 和 AtlasTexture 指南
- 工具对比（TexturePacker、Aseprite、Free Texture Packer）
- Unity .meta 文件精灵坐标解析器（Python）
- 完整的代码示例和项目配置

## 使用场景
- 游戏开发中的精灵图资源优化
- 学习不同引擎的纹理图集系统
- Unity 资源迁移和坐标提取

## 依赖和前提条件
- Rust（Macroquad/Bevy 示例）
- Godot 4.x（Godot 示例）
- Python 3 + PyYAML（Unity meta 解析器）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 核心概念和框架实现文档 |
| ORIGINAL_README.md | 项目概述和学习路径 |
| TOOLS_COMPARISON.md | 工具评测和工作流 |
| unity-asset-extraction.md | Unity 资源提取指南 |
| references/macroquad-guide.md | Macroquad 精灵图 API 指南 |
| references/bevy-guide.md | Bevy TextureAtlas 系统指南 |
| references/godot-guide.md | Godot 4.x 精灵指南 |
| examples/rust-macroquad/ | Macroquad 完整动画示例 |
| examples/rust-bevy/ | Bevy ECS 精灵动画示例 |
| examples/unity_meta_parser.py | Unity .meta 文件解析脚本 |
| examples/UNITY_META_EXAMPLES.md | Unity meta 文件示例 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 示例代码为 Rust/GDScript/Python，需用户主动编译运行 |
| SEC-02 数据外泄 | 🟢 Safe | 无网络请求，纯本地操作 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证相关内容 |
| SEC-04 供应链风险 | 🟢 Safe | Rust 依赖通过 Cargo.toml 声明，版本锁定明确 |
| SEC-05 文件系统篡改 | 🟢 Safe | 仅读取 .meta 文件和输出 JSON，无系统文件修改 |
| SEC-06 Prompt 注入 | 🟢 Safe | 纯技术文档和代码示例 |
| SEC-07 越权操作 | 🟢 Safe | 无系统操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 所有代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 高质量的纯教学型技能，包含完整的代码示例和文档，无任何安全风险。

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
