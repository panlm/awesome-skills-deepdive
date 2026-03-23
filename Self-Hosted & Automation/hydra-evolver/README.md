# hydra-evolver

> Proxmox 原生编排技能，将家庭实验室变为自愈 AI 集群

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | hydra-evolver |
| **作者** | spamtylor |
| **ClawHub** | https://clawskills.sh/skills/spamtylor-hydra-evolver |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/spamtylor/hydra-evolver |
| **安全评级** | 🔴 High |

## 功能概述
- 自动扫描网络发现新节点（TCP 端口扫描）
- 向 Windows/Mac/Linux 节点注入 OpenClaw Agent
- Proxmox 虚拟化遥测和 VM 管理
- 自我进化循环：分析项目文件并提出修复方案
- 一键配置新硬件（Docker + OpenClaw + Tailscale）
- ZeroLeaks 强化防护

## 使用场景
- 自动管理家庭实验室的分布式 AI agent 集群
- 新硬件上线后自动部署 Docker/Tailscale/OpenClaw

## 依赖和前提条件
- Python 3、Docker、PM2
- Proxmox Token（PVE_TOKEN_ID、PVE_TOKEN_SECRET）

## 包含文件
- `SKILL.md` — 技能定义
- `scripts/provision.sh` — 新硬件一键部署脚本
- `scripts/scan.py` — 网络节点扫描
- `scripts/evolve.py` — 自我进化分析
- `package.json` — 依赖配置

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | provision.sh 执行 `curl ... | sh` 安装 Docker；执行 apt-get、usermod |
| SEC-02 数据外泄 | 🟡 Medium | 扫描结果输出到 JSON，无直接外发 |
| SEC-03 凭证获取 | 🔴 High | 需要 Proxmox API Token（PVE_TOKEN_ID/SECRET）；provision.sh 需 sudo 权限 |
| SEC-04 供应链风险 | 🔴 High | `curl -fsSL https://get.docker.com | sh` 和 `curl https://get.volta.sh | bash` 下载执行远程脚本 |
| SEC-05 文件系统篡改 | 🔴 High | 安装 Docker、Node.js、Tailscale、OpenClaw 到系统目录 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🔴 High | 需要 sudo/root 权限；可管理 Proxmox VM；可修改系统配置 |
| SEC-08 持久化机制 | 🔴 High | 安装系统服务（Docker、Tailscale）；使用 PM2 持久化进程 |
| SEC-09 信息采集 | 🔴 High | TCP 端口扫描网络中的节点（SSH:22、OpenClaw:18789） |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可审计 |

**综合评级: 🔴 High**
**风险摘要:** 具有系统级权限的基础设施编排工具，下载执行远程脚本、安装系统服务、扫描网络、管理 VM

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
