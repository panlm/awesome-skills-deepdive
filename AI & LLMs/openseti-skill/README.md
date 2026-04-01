# OpenSETI

> 分布式 SETI 扫描器，贡献算力分析 Breakthrough Listen 射电望远镜真实数据，发现异常可获得代币奖励

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | OpenSETI |
| **作者** | synergysize |
| **类目** | AI & LLMs |
| **ClawHub** | https://clawskills.sh/skills/synergysize-openseti-skill |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/synergysize/openseti-skill |
| **安全评级** | 🟡 Medium |

## 功能概述
- 连接 Breakthrough Listen 射电望远镜真实数据进行分析
- 类似 SETI@home 的分布式计算项目
- 分析发现异常信号可获得代币奖励
- 支持注册 Solana 钱包参与挖矿
- 贡献 GPU/CPU 算力进行信号搜索
- 参与寻找地外智慧生命的全球科学项目

## 使用场景
- 利用闲置计算资源参与 SETI 分布式信号扫描
- 搭建自动化的外星信号检测节点
- 通过贡献算力获取 OpenSETI 代币奖励

## 依赖和前提条件
- Solana 钱包地址
- GPU 或 CPU 计算资源
- 网络连接

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，2 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
