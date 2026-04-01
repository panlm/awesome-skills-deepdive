# Ai 3d Generator

> 从文本描述自动生成详细的 3D 模型并导出 STL 文件

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
- 将自然语言描述转换为参数化 3D 模型
- 使用 LLM（Kimi/Gemini）生成 Python/Trimesh 建模代码
- 支持多种基础几何体：球体、圆柱、圆锥、圆环、立方体
- 高分辨率输出：球体细分 4-5 级，圆柱截面 32-64 段
- 自动导出 STL 二进制格式文件
- 提供 Prompt 模板实现模块化和可复用的建模脚本

## 使用场景
- 通过自然语言描述快速生成 3D 打印用的 STL 模型
- 为原型设计自动生成参数化 3D 零件
- 批量生成具有表面细节和几何纹理的复杂 3D 模型

## 依赖和前提条件
- Python 3 运行环境
- trimesh 库（`pip install trimesh`）
- numpy 库
- LLM API 访问（Kimi 或 Gemini）

## 安全状态
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
> 本文档由 awesome-skills-deepdive skill 自动生成
