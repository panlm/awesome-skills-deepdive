# Image Ocr

> 图片文字识别（OCR）工具，从图像中提取文本

## 基本信息
| 项目 | 内容 |
|---|---|
| **名称** | Image Ocr |
| **作者** | xejrax |
| **类目** | PDF & Documents |
| **ClawHub** | https://clawskills.sh/skills/xejrax-image-ocr |
| **GitHub** | https://github.com/openclaw/skills/tree/main/skills/xejrax/image-ocr |
| **安全评级** | 🟢 Low |

## 功能概述
- 识别图片中的印刷体和手写文字
- 支持多种图片格式（JPG、PNG、BMP 等）
- 输出结构化的可编辑文本
- 支持多语言文字识别

## 使用场景
- 将扫描的纸质文档转换为可编辑的电子文本
- 从截图或照片中快速提取文字内容

## 依赖和前提条件
- Tesseract OCR

## 包含文件
- `README.md`
- `SKILL.md`
- `_meta.json`

## 详细安全审计
| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | 🟢 Safe | 无命令执行风险 |
| SEC-02 数据外泄 | 🟢 Safe | 无外部数据传输 |
| SEC-03 凭证获取 | 🟢 Safe | 无凭证需求 |
| SEC-04 供应链风险 | 🟢 Safe | 无外部依赖安装 |
| SEC-05 文件系统篡改 | 🟢 Safe | 无文件系统操作 |
| SEC-06 Prompt 注入 | 🟢 Safe | 无 Prompt 注入风险 |
| SEC-07 越权操作 | 🟡 Medium | 涉及权限相关操作 |
| SEC-08 持久化机制 | 🟢 Safe | 无持久化机制 |
| SEC-09 信息采集 | 🟢 Safe | 无信息采集 |
| SEC-10 混淆/反分析 | 🟢 Safe | 无混淆行为 |

**综合评级: 🟢 Low**
**风险摘要:** 1 项中风险。越权操作：涉及权限相关操作




---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-23