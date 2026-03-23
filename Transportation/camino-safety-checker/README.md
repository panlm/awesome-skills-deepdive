# Safety Checker for a location

> 使用 Camino AI 查找 24 小时营业场所、照明区域、交通站点和警察局等安全地点

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Safety Checker for a location |
| **作者** | james-southendsolutions |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/james-southendsolutions-camino-safety-checker |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/james-southendsolutions/camino-safety-checker |
| **安全评级** | 🟡 Medium |

## 功能概述
- 查找附近 24 小时营业的商户和场所
- 定位照明良好的公共区域
- 搜索最近的交通站点和警察局
- 提供安全路线建议

## 使用场景
- 深夜在陌生城市查找附近安全的公共场所
- 规划夜间步行的安全路线

## 依赖和前提条件
- API Key（Camino AI）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟡 Medium**
**风险摘要:** 存在 2 项高风险，2 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
