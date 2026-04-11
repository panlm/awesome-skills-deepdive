# 🔭 Grafana Lens

**为 OpenClaw 提供原生 Grafana 可观测性能力 — 查询指标、日志与链路追踪，创建仪表板，管理告警规则，推送自定义数据，以及通过 Alloy 管理数据采集管线。**

> 社区开发的 OpenClaw 插件，非 Grafana Labs 官方产品。

| 信息 | 详情 |
|------|------|
| **作者** | awsome-o |
| **版本** | 0.5.0 |
| **来源** | [ClawHub](https://clawskills.sh/skills/awsome-o-grafana-lens) \| [GitHub](https://github.com/openclaw/skills/tree/main/skills/awsome-o/grafana-lens) |
| **原始 README** | [ORIGINAL_README.md](./ORIGINAL_README.md) |

---

## 功能概述

- **18+ 组合式 Agent 工具** — 支持 PromQL/LogQL/TraceQL 查询、创建仪表板、设置告警、共享面板截图、安全检查、事件调查、推送自定义指标、管理 Alloy 数据采集管线等
- **SRE 事件调查** — 多信号分诊（`grafana_investigate`），基于 7 天基线的 z-score 异常评分，季节性对比，告警疲劳检测
- **完整 OTLP 可观测栈** — Metrics → Prometheus、Logs → Loki、Traces → Tempo，推送模式无需抓取，数据即时可用
- **安全监控** — 6 项威胁评估：Prompt 注入检测、成本异常、工具循环、会话枚举、Webhook 错误、卡住会话
- **12 个预置仪表板模板** — LLM 指挥中心、成本智能、安全概览、SRE 运维等
- **🆕 Alloy 管线管理** — 29 个预构建 Alloy 管线配方，覆盖 5 大类（指标、日志、链路追踪、基础设施、性能剖析），用自然语言描述监控需求即可完成 Alloy 配置
- **自定义数据观测站** — 通过对话将任意外部数据（日历事件、Git 提交、健身数据、财务指标）推送至 Grafana
- **兼容所有数据源** — 不限于 OpenClaw 指标，可查询 Grafana 中配置的任何 Prometheus 或 Loki 数据源

---

## 使用场景

### 场景一：AI Agent 成本与性能全栈监控
用自然语言查询 Agent 当天 LLM Token 花费，创建按模型分类的延迟与成本趋势仪表板，设置每日云成本超限告警，并通过分布式链路追踪调试慢请求。

### 场景二：基础设施数据采集管线一键部署
使用 `alloy_pipeline` 工具，通过选择预构建配方（PostgreSQL、MySQL、Redis、Docker、Kubernetes 等）快速建立数据采集管线，自动生成 Alloy 配置、样例查询和仪表板模板。支持日志处理（JSON 解析、标签提取、结构化元数据）、多租户路由和尾部采样。

### 场景三：安全事件快速分诊
收到告警后，`grafana_investigate` 并行收集指标、日志和链路追踪，生成假设并给出具体的工具调用参数进行深入排查。支持 RED 方法分析、异常检测、告警疲劳评估和事后复盘模板。

---

## 依赖和前提条件

- **Grafana 实例** — 需要配置 `grafana.url`
- **Grafana API Key** — 需要 Editor 或 Admin 权限，配置为 `grafana.apiKey`
- **可选：LGTM 堆栈** — Grafana + Prometheus + Loki + Tempo + OTel Collector（推荐使用 `grafana/otel-lgtm` Docker 镜像）
- **可选：Grafana Alloy** — 用于数据采集管线管理，需要配置 `ALLOY_URL` 和 `ALLOY_CONFIG_DIR`

---

## Alloy 管线管理（v0.5.0 新增）

本版本重大更新引入了 Grafana Alloy 数据采集管线管理能力：

| 类别 | 配方数量 | 示例 |
|------|---------|------|
| **指标 (Metrics)** | 11 | node-exporter, postgres, mysql, redis, mongodb, memcached, blackbox, kubernetes-pods/services, scrape-endpoint, self-monitoring |
| **日志 (Logs)** | 10 | docker-logs, file-logs, journal-logs, syslog, kafka-logs, kubernetes-logs, gelf-logs, faro-frontend, loki-push-api, secret-filter |
| **链路追踪 (Traces)** | 4 | application-traces, otlp-receiver, service-graph, span-metrics |
| **基础设施 (Infra)** | 4 | docker-metrics, elasticsearch-exporter, kafka-exporter, continuous-profiling |

核心组件包括：
- `alloy-client.ts` — Alloy API 客户端，支持配置推送与健康检查
- `config-builder.ts` — 类型安全的 Alloy 配置生成器
- `pipeline-store.ts` — 管线元数据持久化与状态管理
- `alloy-service.ts` — Alloy 服务层，串联管线生命周期管理

---

## 包含文件（144 个）

<details>
<summary>点击展开完整文件列表</summary>

**根目录文件：**
- `SKILL.md` — 技能定义与 Agent 指令
- `README.md` — 项目说明（英文原版已重命名为 ORIGINAL_README.md）
- `_meta.json` — 版本与发布元数据
- `index.ts` — 插件入口
- `llms.txt` — LLM 友好的技能描述
- `openclaw.plugin.json` — 插件配置
- `package.json` — NPM 包配置
- `tsconfig.json` — TypeScript 配置

**参考文档 (references/)：**
- `agent-metrics.md` — Agent 指标参考
- `alloy-components.md` — 🆕 Alloy 组件参考
- `alloy-pipelines.md` — 🆕 Alloy 管线参考
- `dashboard-composition.md` — 仪表板组合参考
- `external-data.md` — 外部数据推送参考
- `sre-investigation.md` — SRE 调查参考

**Alloy 管线 (src/alloy/)：**
- `alloy-client.ts` / `.test.ts` — Alloy API 客户端
- `config-builder.ts` / `.test.ts` — 配置生成器
- `pipeline-helpers.ts` — 管线辅助函数
- `pipeline-store.ts` / `.test.ts` — 管线状态存储
- `types.ts` — Alloy 类型定义
- `recipes/` — 29 个预构建配方（指标 11 + 日志 10 + 追踪 4 + 基础设施 4）

**核心服务 (src/services/)：**
- `alloy-service.ts` — 🆕 Alloy 服务层
- `alert-webhook.ts` — 告警 Webhook
- `custom-metrics-store.ts` — 自定义指标存储
- `lifecycle-telemetry.ts` — 生命周期遥测
- `metrics-collector.ts` — 指标收集器
- `model-pricing.ts` — 模型定价
- `otel-logs.ts` / `otel-metrics.ts` / `otel-traces.ts` / `otel-resource.ts` — OTLP 数据层
- `otlp-json-writer.ts` — OTLP JSON 写入
- `redact.ts` — 数据脱敏
- `sdk-compat.ts` — SDK 兼容层

**Agent 工具 (src/tools/)：**
- `alloy-pipeline.ts` — 🆕 Alloy 管线管理工具
- `query.ts` / `query-logs.ts` / `query-traces.ts` — 数据查询
- `create-dashboard.ts` / `update-dashboard.ts` / `get-dashboard.ts` — 仪表板管理
- `create-alert.ts` / `check-alerts.ts` — 告警管理
- `investigate.ts` — SRE 调查
- `security-check.ts` — 安全检查
- `push-metrics.ts` — 指标推送
- `annotate.ts` / `search.ts` / `share-dashboard.ts` — 其他工具
- `explain-metric.ts` / `explore-datasources.ts` / `list-metrics.ts` — 指标探索
- `query-guidance.ts` / `resolve-panel.ts` / `health-context.ts` / `instance-param.ts` — 辅助工具

**仪表板模板 (src/templates/)：**
- 12 个 JSON 模板（cost-intelligence, genai-observability, http-service, llm-command-center 等）

</details>

---

## 安全状态

| 检查项 | 状态 |
|--------|------|
| VirusTotal | ✅ Benign |
| OpenClaw 安全检查 | ⚠️ Unknown |
| **综合评级** | **Tier 2 — 部分验证** |

> ClawHub 页面未显示完整安全状态信息，建议用户安装前自行审查代码。

---

## 安装

```bash
# 通过 ClawHub CLI
clawhub install awsome-o/grafana-lens

# 或通过 OpenClaw CLI
openclaw skills install awsome-o/grafana-lens
```

---

*本 README 由 awesome-skills-deepdive 项目自动生成 (2026-04-11)*
