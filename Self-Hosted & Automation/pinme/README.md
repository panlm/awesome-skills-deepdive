# pinme

> 一键将静态网站部署到 IPFS 网络

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | pinme |
| **作者** | ntlx |
| **ClawHub** | https://clawskills.sh/skills/ntlx-pinme |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/ntlx/pinme |
| **安全评级** | 🟡 Medium |

## 功能概述
- 零配置前端部署到 IPFS
- 自动检测静态目录（dist/build/out/public）
- 预览 URL 生成（pinme.eth.limo）
- CAR 文件导入导出
- 自定义域名绑定（Plus 计划）
- 上传历史和文件管理

## 使用场景
- 将前端构建产物部署到 IPFS 去中心化网络
- 获取静态网站的永久预览链接

## 依赖和前提条件
- Node.js 16.13.0+
- `pinme` CLI（npm 全局安装）
- 可选：AppKey（认证）

## 包含文件
- `SKILL.md` — 技能定义和完整命令参考
- `_meta.json` — 元数据

## 安全状态 (ClawHub)
| 来源 | 评级 |
|---|---|
| VirusTotal | 🟡 Suspicious |
| OpenClaw | 🟡 Suspicious |

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 通过 pinme CLI 操作 |
| SEC-02 数据外泄 | 🟡 Medium | 上传文件到 IPFS 网络（公开不可逆） |
| SEC-03 凭证获取 | 🟢 Safe | 可选的 AppKey |
| SEC-04 供应链风险 | 🟡 Medium | npm 包依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 不修改本地文件 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 prompt 操作 |
| SEC-07 越权操作 | 🟢 Safe | 用户主动操作 |
| SEC-08 持久化机制 | 🟡 Medium | IPFS 上的内容理论上永久存在 |
| SEC-09 信息采集 | 🟢 Safe | 不采集信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 纯 SKILL.md 文档 |

**综合评级: 🟡 Medium**
**风险摘要:** 将文件上传到 IPFS 公开网络，内容上传后不可撤回

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23
