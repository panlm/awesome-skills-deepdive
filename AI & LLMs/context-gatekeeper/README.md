# context-gatekeeper

> Keeps the conversation token-friendly by summarizing recent exchanges, surfacing pending actions, and delivering a compact briefing for each turn before calling the model. Trigger this skill whenever you need to prune a bloated thread or keep the next prompt lean.

## 基本信息

| 项目 | 内容 |
|---|---|
| **名称** | context-gatekeeper |
| **作者** | davienzomq |
| **ClawHub** | https://clawskills.sh/skills/davienzomq-context-gatekeeper |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/davienzomq/context-gatekeeper |
| **安全评级** | 🟢 ClawHub Verified (Benign) |

## 功能概述

- `--history`: caminho do arquivo com o log das trocas (cada linha deve ser `ROLE: texto`). Usa STDIN se omitido.
- `--summary`: destino do resumo (substitui o arquivo se já existir).
- `--max-summary-sents`: limite de sentenças resumidas (padrão 6).
- `--max-recent-turns`: quantas trocas finais aparecerão na seção "Últimos turnos" (padrão 4).
- Monte um cron/loop leve que chame o script antes de cada resposta automática.
- Guarde um paralelo `context/pending-tasks.md` e copie a seção "Pendências" do resumo para lá.

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
