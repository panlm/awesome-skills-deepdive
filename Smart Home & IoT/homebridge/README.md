# 🏠 Homebridge — 智能家居设备控制

## 描述

通过 Homebridge Config UI X 的 REST API 控制 HomeKit 兼容的智能家居设备。支持列出配件、开关控制、亮度调节、颜色设置、温控器控制和风扇管理。

## 功能特点

- **设备发现**：按房间或类型列出所有智能配件
- **灯光控制**：开关、亮度调节、颜色设定
- **温控器**：设定目标温度和模式
- **风扇控制**：调节风速和开关
- **批量操作**：一次关闭房间内所有灯光
- **REST API**：基于 Homebridge Config UI X 的标准 REST 接口

## 使用方法

### 前提条件

1. Homebridge 已安装且 Config UI X 正在运行
2. 配置凭证文件 `~/.clawdbot/credentials/homebridge.json`：

```json
{
  "url": "https://homebridge.local:8581",
  "username": "admin",
  "password": "your-password"
}
```

### 基本操作

```bash
# 获取认证令牌
TOKEN=$(curl -s -X POST "${HOMEBRIDGE_URL}/api/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"password"}' \
  | jq -r '.access_token')

# 列出所有配件
curl -s "${HOMEBRIDGE_URL}/api/accessories" \
  -H "Authorization: Bearer ${TOKEN}"
```

## 安全评估

- **VirusTotal**: ⚠️ 未验证
- **OpenClaw**: ⚠️ 未验证
- **风险说明**: 需要 Homebridge 管理凭证；可控制物理智能家居设备

## 附加资源

- [GitHub 源码](https://github.com/openclaw/skills/tree/main/skills/jiasenl/clawdbot-skill-homebridge)
- [ClawHub 页面](https://clawskills.sh/skills/jiasenl-clawdbot-skill-homebridge)
- [Homebridge 项目](https://github.com/homebridge/homebridge-config-ui-x)
