# MUKI Fingerprint (MUKI 资产指纹识别)

> 红队侦察用的 MUKI 资产指纹识别工具，支持主动/被动指纹识别

## 📖 描述

MUKI 是一款面向红队作战的主动资产指纹识别工具。它使用 30,000+ 被动签名和 300+ 主动探测规则，帮助安全研究人员从混乱的 C 类网段和大规模资产列表中快速定位脆弱系统。

## ✨ 功能特点

- **被动指纹识别**: 30,000+ 被动签名库
- **主动探测**: 300+ 主动探测规则
- **目录扫描**: 检测暴露的管理面板和配置文件
- **敏感信息提取**: 从 HTTP 响应中提取凭据和 API 密钥
- **WAF/CMS 检测**: 识别防火墙和内容管理系统类型
- **代理支持**: 支持 HTTP 和 SOCKS5 代理
- **多种输出格式**: JSON、CSV、HTML

## ⚠️ 重要提示

**使用此工具前必须获得目标系统所有者的书面授权！**

## 🚀 使用方法

### 安装
```bash
clawhub install admin4giter/muki-fingerprint
```

### 前置要求
- Linux amd64 系统
- 对目标系统的网络访问
- 目标系统所有者的明确书面授权

### 基本命令
```bash
# 扫描单个 URL
muki -u https://target.com

# 从文件扫描多个 URL
muki -l targets.txt

# 使用代理扫描
muki -u https://target.com -p socks5://127.0.0.1:1080

# 禁用特定模块
muki -u https://target.com -A -N  # 无主动探测，无目录扫描
```

### 使用场景
- 渗透测试前的服务版本映射
- 发现暴露的管理面板和配置文件
- 大范围 IP 检测 WAF 和 CMS 类型
- HTTP 响应中的凭据泄露检测
- 从子域名列表构建资产清单

## 🔒 安全评估

| 项目 | 状态 |
|------|------|
| ClawHub 页面 | [查看](https://clawskills.sh/skills/admin4giter-muki-fingerprint) |
| GitHub 源码 | [查看](https://github.com/openclaw/skills/tree/main/skills/admin4giter/muki-fingerprint) |
| 安全状态 | ⚠️ 待验证 (Suspicious) |
| 注意 | 仅限授权渗透测试使用 |

## 📚 附加资源

- [ClawSkills 页面](https://clawskills.sh/skills/admin4giter-muki-fingerprint)
- [GitHub 源码仓库](https://github.com/openclaw/skills/tree/main/skills/admin4giter/muki-fingerprint)
- [MUKI 项目](https://github.com/yingfff123/MUKI)
- 作者: @admin4giter
