# staratheris-arya-model-router

> Token-saver router: elige modelo (cheap/default/pro) y usa sub-agentes para tareas pesadas. Incluye compresión/briefing opcional.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | staratheris-arya-model-router |
| **作者** | staratheris |
| **ClawHub** | https://clawskills.sh/skills/staratheris-staratheris-arya-model-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/staratheris/staratheris-arya-model-router |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- Mantener el chat diario barato.
- Escalar a un modelo superior solo cuando la tarea lo amerite.
- Evitar pasar contexto enorme al modelo caro: primero crear un **brief**.
- El agente principal (main) se mantiene en un modelo económico.
- Para tareas pesadas, el router recomienda (o ejecuta) **sub-agentes** con un modelo superior.
- cheap: `openai/gpt-4o-mini`

## 依赖和前提条件

- 无特殊依赖

## 安全状态

| 来源 | 评级 |
|---|---|
| VirusTotal | 🟢 Benign |
| OpenClaw | 🟢 Benign |

> ClawHub 安全扫描已通过，跳过详细审计。

---

> 本文档由 awesome-skills-deepdive skill 自动生成，仅供参考。
> 生成时间: 2026-04-01 04:47 UTC
