# WPS Office 自动化技能

> WPS Office 自动化技能，支持文档创建、Markdown 转换和图文混排布局。

## 标题和描述

**名称**: wps-office  
**作者**: lilei0311 (MaxStorm Team)  
**版本**: 1.3.0  
**许可证**: MIT  
**Slug**: `lilei0311-wps-skill`

WPS Office 自动化操作 Skill，支持本地文档操作和 WPS 365 云端协作功能。可自动创建 Word、Excel、PPT 文档，进行 Markdown 与 Office 格式的双向转换，以及实现图文混排布局。

## 功能特点

### 本地文档操作（无需凭证）
- 📄 创建 Word、Excel、PPT 文档
- 📂 打开和列出已有文档
- 🔄 支持 MD ↔ Word/RTF/HTML 格式转换
- 📦 批量转换文档格式

### Markdown 转换功能
- 📝 MD ↔ Word（完整版，支持标题、列表、表格、代码块）
- 📊 MD ↔ Excel（表格转工作表，列表转数据）
- 🎬 MD ↔ PPT（标题转幻灯片）
- 🖼️ MD 含图片转 Word

### 图片处理与图文混排
- **Word**: 插入图片、图片网格、图文混排（左图右文、右图左文等）
- **PPT**: 幻灯片图片插入、4种图文混排布局
- **Excel**: 单元格图片插入和图文混排
- 🎨 图片尺寸调整、批量压缩

### WPS 365 云端功能（需凭证）
- 智能表单、智能文档、多维表格
- 流程图创建和导出
- 思维导图创建和导出

## 使用方法/示例

### 安装依赖
```bash
pip install requests pyautogui pyperclip Pillow
```

### 基本使用
```bash
# 创建 Word 文档
python scripts/main.py create type=writer filename=报告.docx

# Markdown 转 Word
python3 scripts/main.py md_to_docx file=文档.md output=文档.docx title="我的文档"

# Markdown 转 PPT
python3 scripts/main.py md_to_pptx file=汇报.md output=汇报.pptx title="项目汇报"

# Word 图文混排
python3 scripts/main.py create_text_image_layout text="说明文字" image=图片.png layout=left output=图文.docx
```

### 配置文件 (config.json)
```json
{
  "default_save_path": "~/Documents/WPS",
  "wps_path": "",
  "app_id": "",
  "app_secret": ""
}
```

## 安全评估

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | ⚠️ 中风险 | 使用 `subprocess` 调用 WPS 应用程序；使用 `pyautogui` 模拟键盘输入 |
| SEC-02 数据外泄 | ⚠️ 中风险 | WPS 365 API 调用涉及外部数据传输（HTTPS 加密） |
| SEC-03 凭证获取 | ⚠️ 中风险 | 需要 WPS 开放平台的 `app_id` 和 `app_secret`，存储在明文配置文件中 |
| SEC-04 供应链风险 | ⚠️ 低风险 | 依赖 `requests`, `pyautogui`, `pyperclip`, `Pillow` 等第三方库 |
| SEC-05 文件系统篡改 | ⚠️ 中风险 | 创建、打开和修改文件，需确保在受信任环境使用 |
| SEC-06 Prompt 注入 | ✅ 低风险 | 未见明显 prompt 注入风险 |
| SEC-07 越权操作 | ⚠️ 中风险 | macOS 需授予辅助功能权限；GUI 自动化可能与当前活动窗口交互 |
| SEC-08 持久化机制 | ✅ 低风险 | 无明显持久化机制 |
| SEC-09 信息采集 | ⚠️ 低风险 | 可列出文档目录文件 |
| SEC-10 混淆/反分析 | ✅ 低风险 | 代码开源，无混淆 |

**综合评级: ⚠️ 中等风险** — GUI 自动化和凭证明文存储是主要风险点。建议首次在沙盒环境中测试，审查 `scripts/main.py` 源码。

## 附加资源列表

- 📦 ClawSkills 页面: https://clawskills.sh/skills/lilei0311-wps-skill
- 🔗 GitHub 源码: https://github.com/clawdbot/skills/tree/main/skills/lilei0311/wps-skill
- 📖 WPS 开放平台: https://open.wps.cn
- 📄 技能文件: `SKILL.md`, `_meta.json`, `config.json`, `skill.json`, `scripts/main.py`, `scripts/md_converter.py`, `scripts/excel_converter.py`, `scripts/image_handler.py`, `scripts/ppt_converter.py`, `test/test_excel.md`, `test/test_md.md`, `test/test_ppt.md`, `test/test_image.py`

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-25
