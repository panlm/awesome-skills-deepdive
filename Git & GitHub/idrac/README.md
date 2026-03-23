# iDRAC

> 通过 iDRAC Redfish API 监控和管理 Dell PowerEdge 服务器（支持 iDRAC 8/9）。

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | iDRAC |
| **作者** | eddygk |
| **版本** | - |
| **类目** | Git & GitHub |
| **ClawHub** | https://clawskills.sh/skills/eddygk-idrac |

## 功能概述
- 检查服务器硬件状态、健康状况和温度
- 查询 CPU、内存、存储/RAID 详细信息
- 监控系统传感器（风扇、电压、散热）
- 执行电源操作（状态查询、开机、关机、优雅关闭、强制重启）
- 检查 BIOS/固件版本和系统清单
- 查看系统事件日志（SEL）和生命周期控制器日志
- 获取硬件库存和序列号
- 支持三种凭证来源：1Password、文件、环境变量

## 使用场景
- 远程监控数据中心 Dell 服务器的运行状态和硬件健康
- 在无法物理接触服务器时执行远程电源操作和故障排查
- 定期巡检服务器固件版本和传感器数据

## 依赖和前提条件
- `curl`、`jq` 命令行工具
- 可选：1Password CLI（`op`）用于凭证管理
- 配置文件：`~/.config/idrac-skill/config`
- 凭证来源需配置 `IDRAC_IP` 和认证信息
- 支持 macOS 和 Linux

## 安全状态
## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟡 Medium | 存在命令执行相关引用 |
| SEC-02 数据外泄 | 🟡 Medium | 存在外部 API 调用 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。凭证获取：需要多种敏感凭证

---
> 本文档由 awesome-skills-deepdive skill 自动生成
