# TfL London Transit

> 伦敦 TfL 公共交通——实时地铁到站、公交预测、线路状态和行程规划

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | TfL London Transit |
| **作者** | brianleach |
| **类目** | Transportation |
| **ClawHub** | https://clawskills.sh/skills/brianleach-tfl |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/brianleach/tfl |
| **安全评级** | 🔴 High |

## 功能概述
- 查询伦敦地铁（Tube）的实时到站时间
- 获取公交车到站预测和路线信息
- 查看所有线路的运行状态和延误信息
- 行程规划（包含地铁、公交、DLR、Elizabeth 线等）
- 获取服务中断和计划施工信息
- 支持 Oyster 和非接触式支付信息查询

## 使用场景
- 查看牛津街站接下来的中央线列车到达时间
- 检查北线（Northern Line）是否正常运行
- 规划从帕丁顿到希思罗机场的最优路线

## 依赖和前提条件
- Node.js / npm、API Key（TfL，免费注册）

## 安全状态
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🔴 High | 大量外部数据传输 |
| SEC-03 凭证获取 | 🔴 High | 需要多种敏感凭证 |
| SEC-04 供应链风险 | 🟡 Medium | 需要安装外部依赖 |
| SEC-05 文件系统篡改 | 🟡 Medium | 存在文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟢 Safe | 无越权风险 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟡 Medium | 读取环境变量或系统信息 |
| SEC-10 混淆/反分析 | 🟡 Medium | 使用编码/解码操作 |

**综合评级: 🔴 High**
**风险摘要:** 存在 2 项高风险，4 项中风险。数据外泄：大量外部数据传输；凭证获取：需要多种敏感凭证

> 本文档由 awesome-skills-deepdive skill 自动生成
