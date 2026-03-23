# nas-master

> ASUSTOR NAS 硬件感知的混合 SMB+SSH 元数据抓取套件

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | nas-master |
| **作者** | afajohn |
| **ClawHub** | https://clawskills.sh/skills/afajohn-nas-master |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/afajohn/nas-master |
| **安全评级** | 🔴 High |

## 功能概述
- 递归扫描 NAS 所有文件夹（包括隐藏目录）获取元数据
- SSH 层：提取 RAID 状态、Btrfs 完整性、Linux 权限
- MySQL 数据库持久化存储元数据
- 硬件保护：CPU 限速 25%、GPU 内存保留
- PHP/AJAX 仪表板前端
- 严格只读安全策略

## 使用场景
- 全面扫描和索引 ASUSTOR NAS 文件系统
- 构建 NAS 文件元数据搜索和可视化平台

## 依赖和前提条件
- Python、PHP、MySQL、PowerShell、SSH
- NAS 访问凭证（SMB + SSH）
- 数据库密码
- XAMPP 环境

## 包含文件
- `SKILL.md` — 技能定义和完整架构说明
- `nas_engine.py` — 核心抓取引擎
- `setup_pro_db.sql` — 数据库初始化脚本
- `.env` — 环境配置（含示例凭证！）

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 通过 paramiko SSH 执行远程命令（cat /proc/mdstat、btrfs scrub status） |
| SEC-02 数据外泄 | 🟡 Medium | 文件元数据存储到 MySQL 数据库 |
| SEC-03 凭证获取 | 🔴 High | .env 文件包含明文 NAS 密码、SSH 密码、数据库密码；AutoAddPolicy 接受所有 SSH 主机 |
| SEC-04 供应链风险 | 🟡 Medium | paramiko、mysql-connector、psutil 依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 递归扫描所有文件（包括 .@metadata 等隐藏目录） |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🔴 High | SSH 远程执行系统命令；扫描整个文件系统；AutoAddPolicy 跳过主机验证 |
| SEC-08 持久化机制 | 🟡 Medium | MySQL 数据库持久化 |
| SEC-09 信息采集 | 🔴 High | 递归扫描 NAS 所有文件和隐藏目录；获取 RAID/Btrfs 系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码可审计，但 .env 含明文凭证是严重问题 |

**综合评级: 🔴 High**
**风险摘要:** SSH 远程命令执行、明文凭证存储、全盘文件系统扫描、跳过 SSH 主机验证

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
