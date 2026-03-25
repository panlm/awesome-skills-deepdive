# 🌐 Agent Browser — AI 代理无头浏览器自动化

## 描述

Agent Browser 是一个专为 AI 代理优化的无头浏览器自动化 CLI 工具。通过可访问性树快照和基于 ref 的元素选择，实现确定性的网页交互，避免了 CSS 选择器和 XPath 的脆弱性。

## 功能特点

- **Ref 元素选择**：从可访问性树快照中提取稳定的 ref（如 @e2, @e3），用于确定性地定位交互元素
- **会话隔离**：支持多个独立的浏览器会话同时运行
- **认证状态保存**：可保存登录状态，避免重复认证
- **网络拦截**：支持 mock API 响应，用于自动化测试
- **JSON 输出**：快照输出 JSON 格式，便于程序解析

## 使用方法

```bash
# 安装
npm install -g agent-browser

# 基本工作流
agent-browser open https://example.com
agent-browser snapshot -i --json
agent-browser click @e2
agent-browser fill @e3 "text"
```

### 适用场景

- 自动化多步骤 Web 表单提交
- 运行并发的管理员和用户浏览器会话进行测试
- 抓取需要 JavaScript 执行的动态单页应用
- 复用保存的登录状态跳过重复认证

## 安全评估

- **VirusTotal**: ⚠️ 未验证
- **OpenClaw**: ⚠️ 未验证
- **风险说明**: 需安装全局 npm 包 `agent-browser`，具备完整浏览器自动化能力

## 附加资源

- [GitHub 源码](https://github.com/openclaw/skills/tree/main/skills/matrixy/agent-browser-clawdbot)
- [ClawHub 页面](https://clawskills.sh/skills/matrixy-agent-browser-clawdbot)
- [agent-browser 项目主页](https://github.com/vercel-labs/agent-browser)
