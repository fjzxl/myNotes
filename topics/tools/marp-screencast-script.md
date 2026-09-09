---
title: Marp 录屏脚本
tags:
  - marp
  - screencast
  - tutorial
  - tools
---

# 🎬 录屏脚本：5 分钟学会 Marp

> **目标**：演示从零开始，用 Marp 把一份 Markdown 笔记导出成专业 PDF 演示文稿。
> **时长**：5 分钟
> **观众**：本知识库用户（已会 Markdown）
> **工具**：VS Code + Marp 扩展 + 终端

---

## 录制前准备

### 录屏工具（任选）

| 平台 | 推荐工具 |
|------|---------|
| **Windows** | OBS Studio（免费）/ Camtasia / Bandicam |
| **macOS** | QuickTime Player（自带）/ OBS Studio |
| **跨平台** | OBS Studio（首选，**完全免费**） |

### 录屏设置

- 分辨率：1920×1080（1080p）
- 帧率：30 fps
- 音频：麦克风（**单声道就够**）
- 格式：MP4（H.264 编码）

### 显示设置

- 字体放大到 **150%**（观众能看清）
- 关掉不相关通知
- 用 **深色主题**（代码更醒目）
- 终端字体：Cascadia Code / Consolas / Fira Code

### 推荐开场素材

- 浏览器打开：Marp 官方文档 https://marpit.marp.app/
- VS Code 打开：本知识库根目录 `D:\notes\myNotes`
- 终端打开：PowerShell（用之前配的 UTF-8 profile）

---

## 完整脚本（含时间轴、台词、操作）

### 🎬 0:00 - 0:30 开场（30s）

**画面**：黑屏淡入，显示标题

**字幕**：
```
Marp 5 分钟上手
Markdown → PDF 演示文稿
```

**台词**：
> "今天用 5 分钟演示一个超实用工具：Marp。它能让你用 Markdown 写出专业级演示文稿，最后导出 PDF。一份源文件，多端输出，可版本控制。"

---

### 🎬 0:30 - 1:00 第 1 步：环境准备（30s）

**画面**：VS Code 全屏

**操作**：

1. 按 `Ctrl+Shift+X` 打开扩展面板
2. 搜 `Marp` 安装
3. 打开终端（`Ctrl+`` ），运行：

```powershell
npm install -g @marp-team/marp-cli
```

**台词**：
> "先装两个东西：VS Code 的 Marp 扩展，编辑预览用；再装命令行工具 marp-cli，最后导 PDF 用。一行 npm 命令搞定。"

**字幕**：
```
两个组件：
1. marp-team.marp-vscode  (VS Code 扩展)
2. @marp-team/marp-cli     (命令行)
```

---

### 🎬 1:00 - 2:00 第 2 步：写第一张幻灯片（60s）

**画面**：VS Code，新建文件 `demo.md`

**操作**：

1. 输入以下内容（**实时打**，不要复制粘贴）：

```markdown
---
marp: true
theme: default
paginate: true
title: 我的第一次 Marp
---

# 你好 Marp

## Markdown 写 PPT

作者：MiniMax151938

---

# 第二页

- 简单
- 高效
- 可版本控制
```

2. 点击右上角 Marp 图标（一个礼物盒 🎁）打开预览

**台词**：
> "Marp 的语法超简单。文件开头三横线包起来的部分是 Frontmatter，告诉 Marp '这是幻灯片'。然后每两个 `---` 之间是一页。点击右上角的 Marp 图标看预览。"

**操作提示**：
- 输入 `marp: true` 时**故意慢一点**，让观众看清
- 按 `Ctrl+Shift+V` 也能开预览

---

### 🎬 2:00 - 3:00 第 3 步：加代码和图片（60s）

**画面**：VS Code + 浏览器（Marp 预览）

**操作**：

1. 继续编辑 `demo.md`，加代码块：

````markdown
---

# 代码示例

```python
def hello():
    print("Hello, Marp!")
```

````

2. 再加一张图片（用现有的）：

```markdown
---

# 图片

![width:500px](attachments/images/programming/Java/Servlet/Servlet-lifecircle.png)
```

3. 加数学公式（KaTeX）：

```markdown
---
math: katex
---

# 数学公式

行内：$E = mc^2$

块级：
$$
\int_0^1 x^2 dx = \frac{1}{3}
$$
```

**台词**：
> "Marp 支持所有标准 Markdown 语法，包括代码高亮、图片、数学公式 KaTeX。代码块和 Markdown 完全一样，图片用 `![width:500px]` 可以精确控制大小。"

---

### 🎬 3:00 - 4:00 第 4 步：换主题 + 自定义样式（60s）

**画面**：VS Code 演示主题切换

**操作**：

1. 把 Frontmatter 的 `theme: default` 改成 `theme: gaia`
2. 看预览变化（颜色变了）
3. 再改回 `default`，加自定义 CSS：

```markdown
---
marp: true
theme: default
style: |
  section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  h1 {
    text-align: center;
    color: yellow;
  }
---
```

4. 演示"封面页"局部指令：

```markdown
<!-- _class: lead -->

# 中心大标题
```

**台词**：
> "Marp 内置 3 个主题：default、gaia、uncover。觉得还不够，可以自己写 CSS 加 `style:` 字段直接覆盖。比如这里我用 CSS 渐变背景 + 黄色标题，立马变成企业级 PPT 风。"

---

### 🎬 4:00 - 4:30 第 5 步：导 PDF（30s）

**画面**：终端

**操作**：

1. 在终端运行：

```powershell
cd D:\notes\myNotes
marp demo.md --pdf
```

2. 等待 2-3 秒
3. 打开生成的 `demo.pdf`

**台词**：
> "最后一步，导出 PDF。一行命令搞定。导完会自动打开 PDF 文件。如果包含本地图片，加 `--allow-local-files` 标志。"

**操作提示**：
- 终端里用 `ls` 或 `Get-ChildItem` 显示 `demo.pdf` 已生成
- 双击打开 PDF 给观众看效果

---

### 🎬 4:30 - 5:00 收尾（30s）

**画面**：回到 VS Code 完整结构

**台词**：
> "回顾一下：Marp = Markdown 写 PPT。一份源文件、纯文本可 Git 控制、PDF/HTML/PPTX 多端输出。下次要做演示文稿，不用打开 PowerPoint，直接 Markdown 走起。完整的 Marp 指南在我知识库的 [[marp-guide]]，4 个实战示例直接抄作业。"

**字幕**：
```
📚 完整指南：[[marp-guide]]
🎯 Servlet 实战：[[../programming/Java/slides/Servlet-lifecycle]]
📐 Cornell × Marp：[[/templates/cornell-marp]]
```

**结束动画**：
- 渐黑
- 显示二维码或链接（如有博客/视频号）
- "完整版指南在评论区"

---

## 📋 录制检查清单

录之前确认：

- [ ] VS Code 已装 Marp 扩展
- [ ] `npm install -g @marp-team/marp-cli` 已运行
- [ ] 示例文件 `demo.md` 准备好（可以预先写好备用）
- [ ] 终端字体放大到能看清
- [ ] 通知全关
- [ ] 麦克风测试一遍
- [ ] OBS 录制区域设置好（1920×1080）

录完之后：

- [ ] 剪辑开头/结尾卡顿
- [ ] 字幕校对（自动生成的常错别字）
- [ ] 导出 H.264 / MP4 / 1080p
- [ ] 文件大小控制在 200MB 以内（上传友好）

---

## 🎯 进阶：录第 2 期（可选）

如果你想做更多 Marp 教程，可以录：

| 期数 | 主题 | 时长 |
|------|------|------|
| 第 1 期 | 基础（本文档） | 5 min |
| 第 2 期 | 自定义主题（写 theme.css） | 8 min |
| 第 3 期 | Cornell × Marp 混合 | 6 min |
| 第 4 期 | 演讲者备注 + 动画技巧 | 7 min |
| 第 5 期 | 批量导 PDF + GitHub Actions 自动发布 | 10 min |

---

## 📺 发布建议

| 平台 | 标题建议 | 标签 |
|------|---------|------|
| **B 站** | "5 分钟学会 Marp：用 Markdown 写 PPT" | #工具推荐 #程序员 #效率工具 |
| **YouTube** | "Marp in 5 Minutes: Markdown to PDF Slides" | #marp #markdown #productivity |
| **小红书** | "Markdown 写 PPT？5 分钟教程 | 程序员必备" | #工具分享 #效率 |
| **知乎** | "如何用 Markdown 写专业级演示文稿" | 工具 / 编程 |

---

## 🛠️ 录屏工具设置

### OBS Studio 快速配置

```
设置 > 视频：
  - 基础分辨率：1920x1080
  - 输出分辨率：1920x1080
  - FPS：30

设置 > 输出：
  - 输出模式：高级
  - 编码器：x264
  - 码率：8000 Kbps（高质量）或 4000 Kbps（普通）
  - 格式：MP4

场景：
  + 显示器捕获（全屏）
  + 音频输入捕获（麦克风）
  + 文字（标题水印，可选）
```

### 快捷键

- `Ctrl+F9` 开始录制
- `Ctrl+F9` 停止录制
- 录完自动保存到 `~/Videos`

---

## 📚 相关资源

- [[marp-guide]] —— Marp 完整使用指南
- [[templates/cornell-marp]] —— 康奈尔 × Marp 混合模板
- [[../programming/Java/slides/Servlet-lifecycle]] —— Marp 实战示例
- [Marp 官方文档](https://marpit.marp.app/) —— 主题、指令、API
- [OBS Studio 教程](https://obsproject.com/) —— 录屏/直播
