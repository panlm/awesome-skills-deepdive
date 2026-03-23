# ipinfo

> 使用 ipinfo.io API 进行 IP 地理位置查询

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | ipinfo |
| **作者** | tiagom101 |
| **ClawHub** | https://clawskills.sh/skills/tiagom101-ipinfo |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/tiagom101/ipinfo |
| **安全评级** | 🟢 Low |

## 功能概述
- IP 地理位置查询（城市、地区、国家、邮编）
- 获取当前主机公网 IP
- 时区和坐标信息
- ASN/组织信息
- 免费层 5 万次/月，可选 token 提升限额
- 支持 jq 提取特定字段

## 使用场景
- IP 地址地理定位
- 网络分析和安全审查
- 用户地理分布分析

## 依赖和前提条件
- curl
- `IPINFO_TOKEN` 环境变量（可选）

## 包含文件
| 文件 | 说明 |
|---|---|
| SKILL.md | 主指令文件，API 使用指南 |
| _meta.json | 元数据 |

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 仅使用 curl 调用 API |
| SEC-02 数据外泄 | 🟢 Safe | 向 ipinfo.io 发送 IP 查询，属预期功能 |
| SEC-03 凭证获取 | 🟢 Safe | 可选 token 从环境变量读取 |
| SEC-04 供应链风险 | 🟢 Safe | 仅依赖 ipinfo.io 官方 API |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件写入 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无动态 prompt |
| SEC-07 越权操作 | 🟢 Safe | 无超范围操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化 |
| SEC-09 信息采集 | 🟡 Medium | 可查询任意 IP 的地理位置信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 代码清晰可读 |

**综合评级: 🟢 Low**
**风险摘要:** 标准的 IP 地理定位工具，功能单一，安全性良好

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
