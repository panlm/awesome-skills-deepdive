# PagerKit — SwiftUI 高级分页导航库

> PagerKit 专家指导技能，一个用于高级可定制分页导航的 SwiftUI 库。

## 标题和描述

**名称**: PagerKit  
**作者**: szpakkamil (Kamil Szpak)  
**版本**: 1.0.1  
**Slug**: `szpakkamil-pagerkit`

PagerKit 是一个强大的 SwiftUI 库，用于创建高度可定制的跨平台分页导航。此技能提供从基础使用、动态页面生成到高级页面指示器定制、事件处理和最佳实践的全面指导。

## 功能特点

### 核心能力
- 📱 **跨平台支持**: iOS 14.0+, iPadOS 14.0+, macOS 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 10.0+
- 🎨 **高度可定制**: 丰富的修饰符 API 用于定制页面指示器、导航方向、事件处理等
- 🏗️ **声明式 UI**: 使用 `PKPageBuilder` 和 `ForEach` 进行声明式页面构建
- 🔄 **动态页面**: 支持从数据集合动态生成页面

### 主要组件
| 组件 | 说明 |
|------|------|
| `PKPagesView` | 主分页容器，支持全局修饰符 |
| `PKPage` | 单个页面内容定义 |
| `PKPageBuilder` | 声明式内容构建器 |
| `ForEach` | 从集合动态生成页面 |

### 页面指示器定制
- 🎯 自定义颜色（活动/非活动状态）
- 🖼️ 自定义图片（全局或每页独立）
- 📐 背景样式（minimal、prominent、automatic）
- ↕️ 布局方向（水平/垂直）
- 📍 位置和间距调整
- 👁️ 显示/隐藏控制

### 事件处理
- 📊 绑定当前页面索引
- 🔄 手动/自动页面切换回调
- ➡️ 页面过渡方向检测
- ⏰ 过渡开始/结束事件

## 使用方法/示例

### 安装（Swift Package Manager）
在 Xcode 中: **File > Add Package Dependency** → `https://github.com/SzpakKamil/PagerKit.git`

### 基本分页设置
```swift
import PagerKit

PKPagesView {
    PKPage { Text("Page A").font(.title) }
    PKPage { Text("Page B").font(.title) }
    PKPage { Text("Page C").font(.title) }
}
.pkCurrentPageIndex(index: $currentPage)
.pkPageNavigationOrientation(.horizontal)
```

### 从数据动态生成页面
```swift
struct Item: Identifiable {
    let id = UUID()
    let title: String
}

let items = [Item(title: "Item 1"), Item(title: "Item 2")]

PKPagesView {
    ForEach(items) { item in
        PKPage { Text(item.title) }
            .pkPageFooter { Text("Footer for \(item.title)") }
    }
}
```

### 自定义页面指示器
```swift
.pkPageControlIndicatorBackgroundStyle(.prominent)
.pkPageControlIndicatorTintColor(.gray)
.pkPageControlIndicatorCurrentIndicatorTintColor(.blue)
```

### 页面切换事件处理
```swift
.pkOnManualPageChange { currentIndex, direction in
    print("用户导航到第 \(currentIndex) 页，方向: \(direction)")
}
.pkOnTransitionEnd { previous, current in
    print("从第 \(previous) 页过渡到第 \(current) 页")
}
```

## 安全评估

| 检查项 | 评级 | 发现 |
|---|---|---|
| SEC-01 命令执行 | ✅ 无风险 | 纯 SwiftUI 库指导，不执行命令 |
| SEC-02 数据外泄 | ✅ 无风险 | 无网络请求或数据传输 |
| SEC-03 凭证获取 | ✅ 无风险 | 不涉及凭证 |
| SEC-04 供应链风险 | ✅ 低风险 | SPM 依赖，来自作者官方仓库 |
| SEC-05 文件系统篡改 | ✅ 无风险 | 纯 UI 库，不涉及文件操作 |
| SEC-06 Prompt 注入 | ✅ 无风险 | 纯技术文档，无 prompt 注入风险 |
| SEC-07 越权操作 | ✅ 无风险 | UI 组件库，无特殊权限需求 |
| SEC-08 持久化机制 | ✅ 无风险 | 无持久化 |
| SEC-09 信息采集 | ✅ 无风险 | 不采集任何信息 |
| SEC-10 混淆/反分析 | ✅ 无风险 | 代码完全开源透明 |

**综合评级: ✅ 安全** — 这是一个纯 SwiftUI UI 库的文档指导技能，不涉及任何系统操作、网络请求或数据处理，安全性极高。

## 附加资源列表

- 📦 ClawSkills 页面: https://clawskills.sh/skills/szpakkamil-pagerkit
- 🔗 GitHub 源码: https://github.com/clawdbot/skills/tree/main/skills/szpakkamil/pagerkit
- 📖 官方文档: https://documentation.kamilszpak.com/documentation/pagerkit/
- 🌐 项目网站: https://kamilszpak.com/pl/pagerkit
- 📦 SPM 仓库: https://github.com/SzpakKamil/PagerKit.git
- 📄 技能文件: `SKILL.md`, `_meta.json`, `references/ForEach.md`, `references/PKPage.md`, `references/PKPageBuilder.md`, `references/PKPageControlBackgroundStyle.md`, `references/PKPageControlDirection.md`, `references/PKPageDirection.md`, `references/PKPagesView.md`, `references/PagerKit.md`, `references/_index.md`

---
> 本文档由 awesome-skills-deepdive 自动生成 | 2026-03-25
