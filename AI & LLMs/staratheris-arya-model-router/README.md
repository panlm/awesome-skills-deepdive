# Arya Model Router

> 智能 AI 模型路由器，自动将请求分配到最优 LLM

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Arya Model Router |
| **作者** | staratheris |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/staratheris-staratheris-arya-model-router |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/staratheris/staratheris-arya-model-router |
| **安全评级** | 🟡 Medium |

## 功能概述
- 智能路由 AI 请求到最优模型
- 支持多个 LLM 提供商的负载均衡
- 根据任务类型自动选择合适模型
- 实现成本优化和性能平衡
- 支持自定义路由规则和权重配置
- 提供模型性能监控和统计

## 使用场景
- 多模型环境中自动选择最优 LLM 处理请求
- 优化 AI 调用成本同时保证服务质量
- 构建高可用的多模型推理服务

## 依赖和前提条件
- Python 运行环境
- Bash/Shell 环境

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟡 Medium | 存在可疑 Prompt 模式 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
