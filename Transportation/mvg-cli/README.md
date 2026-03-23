# Mvg

> 慕尼黑公共交通（MVG）查询和 S-Bahn 实时追踪

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Mvg |
| **作者** | lars147 |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/lars147-mvg-cli |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/lars147/mvg-cli |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查询慕尼黑 MVG 公共交通出发时间
- S-Bahn 列车实时位置追踪
- 获取地铁、公交、电车时刻信息
- 站点搜索和换乘方案

## 使用场景
- 查看慕尼黑 Marienplatz 站的下一班地铁
- 追踪 S-Bahn 列车的实时位置和延误情况

## 依赖和前提条件
- Node.js / npm

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🟡 Medium | 需要 API 密钥或令牌 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 1 项高风险，4 项中风险。数据外泄：大量外部数据传输

> 本文档由 awesome-skills-deepdive skill 自动生成
