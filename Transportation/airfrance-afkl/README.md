# Air France - KLM

> 通过法航-荷航开放数据 API 追踪航班状态、获取实时航班信息

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Air France - KLM |
| **作者** | iclems |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/iclems-airfrance-afkl |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/iclems/airfrance-afkl |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询法航和荷航航班的实时状态信息
- 获取航班延误、取消和登机口变更通知
- 查看航班时刻表和历史准点率
- 支持按航班号或航线查询
- 获取航班详细信息（机型、航站楼等）

## 使用场景
- 追踪即将起飞的法航航班实时状态
- 查询巴黎到阿姆斯特丹航线的当日航班列表
- 检查特定航班的延误情况和预计到达时间

## 依赖和前提条件
- API Key（法航-荷航开放数据平台）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟡 Medium | 涉及定时或后台任务 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，3 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
