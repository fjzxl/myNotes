---
title: Foam 使用指南
tags:
  - knowledge-management
  - vscode
  - markdown
  - tools
aliases:
  - Foam 知识库搭建
  - Foam Guide
---

# Foam 使用指南：搭建类 Obsidian 知识库

> 一份面向 VS Code 用户的 Foam 完整手册。读完你就能用 Foam 搭建起一个与 Obsidian 体验相近、但完全本地化、可编程的知识管理系统。

---

## 目录

1. [什么是 Foam](#1-什么是-foam)
2. [与 Obsidian 的对比](#2-与-obsidian-的对比)
3. [安装与初始化](#3-安装与初始化)
4. [核心概念](#4-核心概念)
5. [基础功能实战](#5-基础功能实战)
6. [进阶配置](#6-进阶配置)
7. [推荐目录结构](#7-推荐目录结构)
8. [日常工作流](#8-日常工作流)
9. [搭配扩展推荐](#9-搭配扩展推荐)
10. [常见问题 FAQ](#10-常见问题-faq)

---

## 1. 什么是 Foam

**Foam** 是一款基于 VS Code 的个人知识管理扩展，灵感来自 **Roam Research**。它把一组 Markdown 文件组织成一个互联的知识网络，核心理念是：

- **Markdown 是事实标准**：所有内容都是纯 `.md` 文件，不绑定任何专有格式
- **双链（Bidirectional Links）**：用 `[[wikilinks]]` 创建笔记间的双向引用
- **图谱视图**：可视化所有笔记及其连接关系
- **本地优先**：所有数据存在你自己的文件系统里，不依赖任何云服务
- **可编程**：因为是 VS Code 扩展，可以搭配任何 VS Code 插件、脚本、Git 工作流

一句话总结：**Foam = VS Code + Markdown + Roam 思想**。

---

## 2. 与 Obsidian 的对比

| 维度 | Obsidian | Foam |
|------|----------|------|
| 平台 | 独立桌面/移动 App | VS Code 插件 |
| 编辑器 | 自带 Markdown 编辑器 | VS Code 编辑器（可装任意 Markdown 扩展） |
| 文件格式 | 纯 Markdown | 纯 Markdown（兼容 Obsidian） |
| 双向链接 | ✅ `[[wikilink]]` | ✅ `[[wikilink]]` |
| 反向链接 | ✅ | ✅ |
| 图谱视图 | ✅ | ✅（基于本地服务） |
| 每日笔记 | ✅ | ✅ |
| 标签 | ✅ | ✅ |
| 插件生态 | 强大的社区插件 | 复用 VS Code 全部扩展 |
| 移动端 | ✅ iOS/Android | ❌（需借助其他方式） |
| 同步 | Obsidian Sync / 第三方 | Git / iCloud / Dropbox / 任何文件同步 |
| 学习成本 | 低（开箱即用） | 中（需要熟悉 VS Code） |
| 价格 | 个人免费 / 商业付费 | 完全免费 |
| 适合人群 | 不想折腾、追求完整体验 | 程序员、VS Code 重度用户、喜欢 DIY |

**结论**：如果你已经深度使用 VS Code、想要一个可编程、可版本控制的笔记系统，Foam 是更好的选择；如果你更看重开箱即用和移动端，Obsidian 更合适。

两者**文件格式完全兼容**，可以随时迁移。

---

## 3. 安装与初始化

### 3.1 安装前置条件

- VS Code 1.85+
- （可选）Node.js 18+，用于部分高级功能（如 `[[graph]]` 本地服务）

### 3.2 安装 Foam 扩展

1. 打开 VS Code
2. 按 `Ctrl+Shift+X` 打开扩展面板
3. 搜索 `Foam`（作者：Foam），点击安装
   - 或直接访问 [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode)

### 3.3 推荐同时安装的官方扩展包

Foam 团队推荐一并安装：

- **Markdown All in One** — 快捷键、目录、数学公式、粘贴图片等
- **Markdown Preview Enhanced** — 强大的 Markdown 实时预览
- **vscode-pdf** — PDF 查看（用于配合 Foam 的 PDF 注释功能，可选）

### 3.4 初始化知识库

Foam 没有"项目"概念，**任何包含 Markdown 文件的目录都是 Foam 知识库**。

```powershell
# 新建知识库目录
mkdir D:\notes\myKnowledge
cd D:\notes\myKnowledge

# 用 VS Code 打开
code .
```

在 VS Code 中：

1. `Ctrl+Shift+P` 打开命令面板
2. 输入 `Foam: Open Graph` 或 `Foam: Show Welcome`
3. 出现欢迎页即代表初始化完成

### 3.5 推荐配置 Git

笔记是宝贵的个人资产，强烈建议用 Git 进行版本管理：

```powershell
cd D:\notes\myKnowledge
git init
# 创建 .gitignore
"node_modules/`n.DS_Store`n.vscode/`n" | Out-File -Encoding utf8 .gitignore
git add .
git commit -m "init: foam knowledge base"
```

可以选择性推送到 GitHub 私有仓库，实现免费的云端备份 + 多设备同步。

---

## 4. 核心概念

### 4.1 Wikilink（双链）

在 Markdown 中用 `[[]]` 包裹笔记名，即可创建指向另一篇笔记的链接：

```markdown
我今天读了 [[深度学习]] 的相关材料。
也可以这样链接：[[深度学习|深度学习笔记]] （显示自定义文本）
指向章节：[[深度学习#反向传播]]
```

**关键点**：

- 链接的笔记**不必事先存在**——Foam 会自动识别并标记为"未创建"
- 未创建的链接在 Foam 称为 **placeholder / orphan candidate**
- 点击 `[[未创建的笔记]]`，Foam 会提示创建

### 4.2 Backlinks（反向链接）

任何笔记 A 引用了笔记 B，Foam 都会在 B 底部自动生成反向链接面板：

```markdown
# 深度学习

正文内容...

## Backlinks
<!-- 该区域由 Foam 自动维护 -->
```

切换到 Markdown 预览（`Ctrl+K V`）即可看到完整的反向链接列表。

### 4.3 Tags（标签）

Foam 支持两种标签：

**1. Frontmatter 标签**（YAML 头部）：
```markdown
---
tags:
  - ai
  - machine-learning
---

# 笔记内容
```

**2. 行内标签**（`#` 开头，需用空格或行首区分）：
```markdown
正文 #ai 内容 #机器学习
```

### 4.4 Graph（图谱）

`Ctrl+Shift+P` → `Foam: Open Graph`，会在浏览器中打开一个本地服务（默认 `http://localhost:3000`），可视化所有笔记及其连接：

- 节点 = 笔记
- 边 = 链接关系
- 颜色 = 标签或孤立节点

**图谱筛选**：
- `tag:xxx` 只看某标签的笔记
- `ORPHANS:true` 只看孤立笔记（没有入链/出链）
- 组合：`tag:project AND ORPHANS:false`

### 4.5 Daily Notes（每日笔记）

`Ctrl+Shift+P` → `Foam: Open Daily Note`，自动打开/创建今天的日记。默认路径与命名可在 `settings.json` 配置（见 6.2）。

### 4.6 Placeholders（占位符）

任何被引用但还没创建的笔记都是 placeholder。Foam 提供命令快速管理：

- `Foam: Show Orphaned Notes` — 列出所有未创建引用
- `Foam: Create Note From Placeholder` — 批量创建

---

## 5. 基础功能实战

### 5.1 创建笔记

**方式一**：直接新建 `.md` 文件
```powershell
ni "深度学习.md" -ItemType File
```

**方式二**：在任意 Markdown 中输入 `[[新笔记]]`，然后：
- `Ctrl+Shift+P` → `Foam: Create Note From Placeholder`
- 或点击提示中的 "Create"

### 5.2 链接、跳转、重命名

- **跳转**：`Ctrl+Click`（或 `F12`）跳转到链接目标
- **跟随光标**：`Alt+Click` 预览链接内容
- **重命名**：`F2` 重命名笔记——Foam 会**自动更新所有引用此笔记的 wikilink**（这是 Foam 最强特性之一）

### 5.3 自动补全

在 Markdown 中输入 `[[`，Foam 会弹出当前知识库内所有笔记的搜索框，支持模糊匹配。无需记忆笔记名。

### 5.4 引用块（Block References）

Foam 支持引用具体段落（需开启实验性功能）：

```markdown
某段内容 ^block-id

在另一篇笔记中引用：
![[深度学习#^block-id]]
```

启用方式：VS Code 设置 → 搜索 `foam.links` → 开启 `Include block references`。
**注意**：此特性与 Obsidian 略有差异，复杂场景建议先验证。

### 5.5 搜索

- **VS Code 原生**：`Ctrl+Shift+F` 全文检索（支持正则）
- **Foam 增强**：`Ctrl+Shift+P` → `Foam: Search Notes`（带标签筛选的专用搜索）

---

## 6. 进阶配置

### 6.1 `settings.json` 关键配置

打开 `Ctrl+,` → 右上角打开 JSON，加入：

```jsonc
{
  // Foam 核心
  "foam.edit.linkReferenceDefinitions": "withoutBrackets",
  "foam.files.attachmentExtensions": ["png", "jpg", "jpeg", "gif", "svg", "pdf"],

  // Markdown 增强
  "markdown.preview.fontSize": 14,
  "editor.minimap.enabled": false,

  // 推荐搭配
  "files.autoSave": "afterDelay",
  "editor.wordWrap": "on",
  "editor.bracketPairColorization.enabled": true
}
```

### 6.2 每日笔记配置

```jsonc
{
  "foam.openDailyNote.dateFormat": "YYYY-MM-DD",
  "foam.openDailyNote.filename": "journal/daily/{date}.md",
  "foam.openDailyNote.title": "{date}",
  "foam.openDailyNote.template": {
    "title": "每日笔记",
    "content": [
      "## 📅 {date} ({dayOfWeek})",
      "",
      "### 🎯 今日目标",
      "- [ ] ",
      "",
      "### 📝 今日记录",
      "",
      "### 💡 灵感 & 想法",
      "",
      "### 📚 今日链接",
      ""
    ]
  }
}
```

### 6.3 笔记模板（Templates）

推荐安装 **YAML-Template** 或使用 Foam 自带的 snippet：

`.vscode/foam.code-snippets`：

```jsonc
{
  "Zettelkasten Note": {
    "prefix": "zk",
    "body": [
      "# ${TM_FILENAME_BASE}",
      "",
      "> 创建时间：$CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE",
      "> 状态：🌱 种子笔记",
      "",
      "## 核心观点",
      "",
      "## 引用与依据",
      "",
      "## 链接",
      "- 上游：",
      "- 下游："
    ],
    "description": "Zettelkasten 卡片笔记模板"
  }
}
```

使用：在新文件输入 `zk` → Tab。

### 6.4 配置 Graph 过滤

`.vscode/foam.graph.json`（可选）：

```jsonc
{
  "groups": [
    {
      "label": "📚 知识库",
      "query": "tag:knowledge OR tag:tech",
      "color": "#4fc3f7"
    },
    {
      "label": "📅 日记",
      "query": "tag:daily",
      "color": "#81c784"
    }
  ]
}
```

---

## 7. 推荐目录结构

Foam 没有强制的目录约定，下面是几个成熟的方案：

### 7.1 PARA 方法（推荐新手）

```
myKnowledge/
├── 0-Inbox/          # 临时收集
├── 1-Projects/       # 有明确目标的项目
├── 2-Areas/          # 持续关注的领域
├── 3-Resources/      # 参考资料
├── 4-Archive/        # 已归档
└── journal/
    └── daily/        # 每日笔记
```

### 7.2 Zettelkasten（推荐深度使用）

```
myKnowledge/
├── 0-inbox/                  # 闪念
├── 1-literature-notes/       # 文献笔记（自己的话复述）
├── 2-permanent-notes/        # 永久笔记（核心）
├── 3-mocs/                   # Maps of Content 索引页
├── 4-projects/               # 项目
├── 5-archive/
└── journal/
    └── daily/
```

**MOC（Map of Content）** 是 Zettelkasten 的核心：用一篇笔记作为某个主题的目录，把所有相关永久笔记聚合起来。

示例 `3-mocs/深度学习 MOC.md`：
```markdown
# 深度学习 MOC

## 基础
- [[神经元]]
- [[激活函数]]
- [[反向传播]]

## 进阶
- [[CNN]]
- [[RNN]]
- [[Transformer]]

## 实践
- [[PyTorch 入门]]
- [[训练技巧]]
```

### 7.3 混合方案（推荐大多数用户）

```
myKnowledge/
├── inbox/                # 临时收集
├── journal/              # 每日笔记
│   └── daily/
├── notes/                # 核心知识笔记（无层级扁平）
├── projects/             # 项目相关
├── resources/            # 引用资料
├── templates/            # 模板
└── attachments/          # 图片、PDF 等
```

**核心思想**：核心笔记扁平化存放（依赖 wikilink 而不是目录树），用 MOC 聚合。

---

## 8. 日常工作流

### 8.1 早晨（5 分钟）

1. 打开 VS Code
2. `Ctrl+Shift+P` → `Foam: Open Daily Note` 打开今日笔记
3. 写下今天的目标

### 8.2 日常记录（随时）

- 看到好文章 → 丢进 `inbox/`
- 灵光一现 → `Ctrl+Shift+P` → `Foam: New Note`（快捷键 `Ctrl+Alt+N`）
- 引用已有内容 → 用 `[[]]` 创建连接

### 8.3 周末整理（30-60 分钟）

1. `Foam: Show Orphaned Notes` — 找出尚未建立的引用，决定是否创建
2. `Foam: Open Graph` — 看图谱，识别孤立笔记
3. 把 inbox 里的临时笔记转成永久笔记
4. 更新 MOC

### 8.4 复习循环

- **每日**：翻翻今日笔记，回顾链接的旧笔记
- **每周**：浏览图谱，补充缺失的连接
- **每月**：重写最常用的 MOC

---

## 9. 搭配扩展推荐

### 9.1 必装

| 扩展 | 作用 |
|------|------|
| Markdown All in One | 快捷键、目录、自动完成 |
| Markdown Preview Enhanced | 强大预览 + Pandoc 支持 |
| GitLens | Git 增强（谁在何时改了什么） |
| Code Spell Checker | 英文拼写检查 |

### 9.2 锦上添花

| 扩展 | 作用 |
|------|------|
| Foam（已装） | 知识管理核心 |
| TODO Highlight | 高亮 TODO 关键字 |
| Paste Image | 截图直接粘贴进笔记 |
| Auto-Open Markdown Preview | 边写边看 |
| Tag Autocomplete | 标签自动补全 |

### 9.3 进阶（程序员向）

| 扩展 | 作用 |
|------|------|
| Draw.io Integration | 在 Markdown 里画架构图 |
| Mermaid Markdown Syntax Highlighting | 流程图、时序图 |
| Jupyter | 在笔记里运行 Python 代码 |
| Quarto | 把笔记发布成网页/PDF/书 |

---

## 10. 常见问题 FAQ

### Q1：Foam 和 Obsidian 冲突吗？

**不冲突**。两者都是读写标准 Markdown，可以同时打开同一个目录。建议方案：

- 主力用 Foam（VS Code）
- 移动端用 Obsidian（iOS/Android）

### Q2：笔记能加密吗？

Foam 本身不提供加密，但因为你掌控文件，可以用：
- **VeraCrypt** 加密整个目录
- **git-crypt** 加密敏感文件
- **7-Zip** 加密压缩备份

### Q3：怎么同步到多设备？

任何能同步文件夹的工具都可以：
- **Git + GitHub 私有仓库**（推荐，有版本控制）
- **iCloud / OneDrive / Dropbox**（简单但无版本控制）
- **Syncthing**（P2P 私密同步）

注意避免多个设备同时编辑同一文件，会产生冲突。

### Q4：图谱打不开？

`Foam: Open Graph` 依赖 Node.js 本地服务。检查：

```powershell
node --version  # 应该 >= 18
```

如果还是不行，尝试：
1. `Ctrl+Shift+P` → `Foam: Kill Graph Server`，然后重新打开
2. 检查端口 3000/3001 是否被占用

### Q5：如何把 Obsidian 笔记迁移到 Foam？

直接复制 Markdown 文件夹即可。需要注意：

- Obsidian 的 `![[file]]` 嵌入语法 Foam 部分支持
- Obsidian 的 Canvas 文件（`.canvas`）Foam 不能识别
- 标签语法兼容
- Frontmatter 兼容

### Q6：Foam 停止维护了吗？

截至 2024 年，Foam 社区版由志愿者维护，更新节奏变慢但核心功能稳定。重要更新请关注 [GitHub 仓库](https://github.com/foambubble/foam)。

如果需要更活跃的维护，可考虑：
- **foam-community** 分支
- 自行 fork 改造

### Q7：如何在 Foam 里画图？

两种方案：

1. **Mermaid**（原生 Markdown 支持）：
   ````markdown
   ```mermaid
   graph LR
     A[笔记A] --> B[笔记B]
     B --> C[笔记C]
   ```
   ````

2. **Draw.io**：安装 `Draw.io Integration` 扩展，编辑 `.drawio` 文件，导出 SVG/PNG 嵌入笔记。

### Q8：怎么把笔记发布成博客/网站？

推荐用 **Quarto** 或 **Obsidian Publish 的开源替代**：

- [Quarto](https://quarto.org/) — 科学文档发布
- [Jekyll](https://jekyllrb.com/) + [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) 主题
- [Astro](https://astro.build/) + [Foam 模板](https://github.com/foambubble/foam-template)

---

## 附录：Foam 常用快捷键速查

| 操作 | 快捷键 / 命令 |
|------|---------------|
| 打开每日笔记 | `Ctrl+Shift+P` → `Foam: Open Daily Note` |
| 新建笔记 | `Ctrl+Shift+P` → `Foam: New Note` |
| 打开图谱 | `Ctrl+Shift+P` → `Foam: Open Graph` |
| 跳转到链接 | `F12` 或 `Ctrl+Click` |
| 重命名笔记（自动更新所有引用） | `F2` |
| 显示孤立笔记 | `Ctrl+Shift+P` → `Foam: Show Orphaned Notes` |
| 显示反向链接 | 切换到 Markdown 预览（`Ctrl+K V`） |
| 复制 wikilink | `Ctrl+Shift+P` → `Foam: Copy Wikilink To Current Note` |
| 跳到当前笔记的目录 | `Ctrl+Shift+P` → `Foam: Reveal Current Note In Explorer` |

---

## 参考资源

- **官方文档**：[foam.visualstudio.com](https://foambubble.github.io/foam/)
- **GitHub 仓库**：[github.com/foambubble/foam](https://github.com/foambubble/foam)
- **YouTube 教程**：搜索 "Foam VS Code tutorial"
- **Reddit 社区**：r/FoamNotes
- **示例知识库**：[github.com/foambubble/foam-template](https://github.com/foambubble/foam-template)

---

## 相关链接

> 在 Foam / Obsidian 中可点击跳转，标准 Markdown 渲染器会显示为纯文本。

### 本仓库相关

- [[tools]] — 顶层工具索引（VS Code 快捷键、Markdown 工具）
- [[Developing/tools/foam|foam]] — Foam 工具索引（本文档的入口页）
- [[Developing/markdown_dev|markdown_dev]] — Markdown 写作环境配置（Foam 强依赖的 Markdown 工具链）
- [[Developing/tools/vscode|vscode]] — VS Code 基础与插件清单
- [[README]] — 仓库结构总览

### 概念关联

- [[双向链接]]（占位笔记，可后续创建）
- [[Zettelkasten]]（占位笔记，可后续创建）
- [[知识图谱]]（占位笔记，可后续创建）
- [[PARA 方法]]（占位笔记，可后续创建）

### 外部资源

- [Foam 官方文档](https://foambubble.github.io/foam/)
- [Foam GitHub](https://github.com/foambubble/foam)
- [Foam 模板仓库](https://github.com/foambubble/foam-template)

---

> **作者注**：本指南基于 Foam 0.20+ 撰写。Foam 处于持续演进中，部分实验性功能（Block References、AI 集成等）可能随版本变化，请以官方文档为准。
