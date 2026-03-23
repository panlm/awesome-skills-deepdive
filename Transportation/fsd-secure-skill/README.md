# PolaBea

> 全自动驾驶 Agent（纯视觉方案），具备最高安全标准和冗余检查

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | PolaBea |
| **作者** | aadipapp |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/aadipapp-fsd-secure-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/aadipapp/fsd-secure-skill |
| **安全评级** | 🟢 Low |

## 功能概述
- 纯视觉（Camera-Only）自动驾驶方案
- 冗余检查机制确保行驶安全
- 实时环境感知和决策系统
- 遵循最高安全标准设计

## 使用场景
- 模拟纯视觉自动驾驶的决策流程
- 验证自动驾驶系统的安全冗余机制

## 依赖和前提条件
- Python、摄像头/视觉数据源

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。凭证获取：需要 API 密钥或令牌

> 本文档由 awesome-skills-deepdive skill 自动生成
