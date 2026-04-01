# Astrai Inference Router

> 通过 Astrai 智能路由器转发所有 LLM 调用，节省 40%+ API 成本，内置隐私控制和 GDPR 合规功能。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Astrai Inference Router |
| **作者** | beee003 |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/beee003-astrai-inference-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/beee003/astrai-inference-router |
| **安全评级** | 🟡 Medium |

## 功能概述
- 智能路由：根据任务类型（代码、研究、聊天、创意）自动选择最优模型
- 成本优化：贝叶斯学习寻找满足质量阈值的最低成本提供商
- 自动故障转移：熔断器机制在提供商宕机时自动切换
- PII 保护：个人身份信息在发送到提供商前自动剥离
- EU 路由：一键配置 GDPR 合规的欧洲专属路由
- 预算上限：设置每日支出限额，防止成本失控
- 实时追踪：查看每个请求节省了多少成本

## 使用场景
- 企业用户需要降低 LLM API 成本同时保证输出质量
- 欧洲用户需要 GDPR 合规的 AI 推理路由方案
- 需要高可用性的 LLM 服务，支持多提供商自动故障转移

## 依赖和前提条件
- 需要 `ASTRAI_API_KEY` 和 `ANTHROPIC_API_KEY` 环境变量
- 包含 `plugin.py` 和 `config.example.toml` 配置文件

## 安全状态
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
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

---
> 本文档由 awesome-skills-deepdive skill 自动生成
