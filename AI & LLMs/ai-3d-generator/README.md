# Ai 3d Generator

> Génération automatique de modèles 3D détaillés à partir de descriptions textuelles.

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Ai 3d Generator |
| **作者** | vonzellu |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/vonzellu-ai-3d-generator |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/vonzellu/ai-3d-generator |
| **安全评级** | 🟢 Low |

## 功能概述
- Utilise trimesh.creation (icosphere, cylinder, cone, torus, box)
- Pour les détails complexes: utiliser des boucles et paramètres
- Résolution élevée: subdivisions=4-5 pour les sphères, sections=32-64 pour cylindres
- Ajouter des détails de surface (panneaux, textures géométriques)
- Structure modulaire avec fonctions réutilisables
- Exporter en STL binaire à la fin

## 使用场景
- 自动化日常任务
- 提升工作效率
- 集成外部服务

## 依赖和前提条件
- Python / pip

## 包含文件
- `SKILL.md`
- `_meta.json`
- `examples`
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
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 2 项中风险。持久化机制：涉及定时或后台任务；信息采集：读取环境变量或系统信息

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23