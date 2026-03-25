# 🍳 Anova Oven — 精准烤箱和低温烹饪控制

## 描述

通过 WiFi WebSocket API 控制 Anova 精准烤箱（APO）和精准低温烹饪器（APC）。支持启动烹饪模式（低温烹饪、烘烤、蒸汽）、设定温度、监控状态和远程停止烹饪。

## 功能特点

- **多设备支持**：同时控制精准烤箱和精准低温烹饪器
- **多种烹饪模式**：低温烹饪（sous vide）、烘烤、蒸汽等
- **精准温度控制**：精确设定温度、加热元件、风扇速度和探针温度
- **远程监控**：实时查看设备状态和烹饪进度
- **远程控制**：远程启动和停止烹饪
- **WebSocket API**：通过 Anova 云端 WebSocket 接口通信

## 使用方法

### 前提条件

1. 从 Anova App 获取个人访问令牌（More → Developer → Personal Access Tokens）
2. 安装 Python 依赖：`pip3 install websockets`
3. 设备已连接 WiFi 并绑定 Anova 账户

### 基本操作

```bash
# 存储令牌
mkdir -p ~/.config/anova
echo "anova-your-token" > ~/.config/anova/token

# 查看设备列表
python3 scripts/anova.py list

# 启动低温烹饪
python3 scripts/anova.py start --device DEVICE_ID --mode sous_vide --temp 135
```

## 安全评估

- **VirusTotal**: ⚠️ 未验证
- **OpenClaw**: ⚠️ 未验证
- **风险说明**: 需要 Anova 个人访问令牌；通过云端 API 控制物理设备

## 附加资源

- [GitHub 源码](https://github.com/openclaw/skills/tree/main/skills/dodeja/anova-skill)
- [ClawHub 页面](https://clawskills.sh/skills/dodeja-anova-skill)
- [原始 README](./ORIGINAL_README.md)
