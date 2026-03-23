# clauditor

> Clawdbot 代理的防篡改审计看门狗，使用 HMAC 链式日志检测可疑活动

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | clauditor |
| **作者** | apollostreetcompany |
| **ClawHub** | https://clawskills.sh/skills/apollostreetcompany-clauditor |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/apollostreetcompany/clauditor |
| **安全评级** | 🔴 High |

## 功能概述
- 独立 sysaudit 守护进程（伪装服务名）
- HMAC 链式追加日志
- 基于规则的异常检测（外泄/注入/持久化/篡改）
- 命令基线和首次执行标记
- 孤儿进程检测
- 交互式安装向导

## 使用场景
- 监控 Clawdbot 代理的文件系统活动
- 生成安全摘要报告
- 检测潜在的数据外泄和凭证访问

## 依赖和前提条件
Rust (cargo), systemd, Linux

## 包含文件
- `AGENTS.md`
- `Cargo.toml`
- `ORIGINAL_README.md`
- `SKILL.md`
- `_meta.json`
- `crates/alerter/Cargo.toml`
- `crates/alerter/src/lib.rs`
- `crates/clauditor-cli/Cargo.toml`
- `crates/clauditor-cli/src/main.rs`
- `crates/collector/Cargo.toml`
- `crates/collector/src/lib.rs`
- `crates/collector/src/privileged.rs`
- `crates/detector/Cargo.toml`
- `crates/detector/src/baseline.rs`
- `crates/detector/src/lib.rs`
- `crates/detector/src/rules.rs`
- `crates/detector/src/sensitive.rs`
- `crates/detector/src/sequence.rs`
- `crates/schema/Cargo.toml`
- `crates/schema/src/lib.rs`
- `crates/writer/Cargo.toml`
- `crates/writer/src/lib.rs`
- `wizard/install.sh`
- `wizard/wizard.sh`

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🔴 High | 安装系统级守护进程，需要 root 权限 |
| SEC-02 数据外泄 | 🟢 Safe | 设计目的就是检测外泄，自身不外发数据 |
| SEC-03 凭证获取 | 🟡 Medium | HMAC 密钥存储在 /etc/sysaudit/key |
| SEC-04 供应链风险 | 🟡 Medium | 需要编译 Rust 代码 |
| SEC-05 文件系统篡改 | 🔴 High | 创建系统用户、写入 /etc/sysaudit 和 /var/lib/.sysd/.audit |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 注入风险 |
| SEC-07 越权操作 | 🔴 High | 需要 root 权限安装系统服务 |
| SEC-08 持久化机制 | 🔴 High | 安装 systemd 服务（伪装名 systemd-journaldd） |
| SEC-09 信息采集 | 🔴 High | 监控所有文件系统执行活动（FAN_OPEN_EXEC） |
| SEC-10 混淆/反分析 | 🟡 Medium | 服务名伪装为 systemd-journaldd 可能引起混淆 |

**综合评级: 🔴 High**
**风险摘要:** 安装系统级监控守护进程，需 root 权限，服务名伪装；虽然目的是安全监控，但权限极高

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
