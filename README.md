# myNotes · 知识库

> 基于 **Zettelkasten + PARA 混合方法** 的个人知识库。VS Code + Foam 双链管理，所有内容为纯 Markdown，**所有文件名英文**。

## 设计原则

- **4 大主题**：`programming` / `ai` / `math` / `history`
- **`tools` 提升为一级主题**（与编程/AI 并列）
- **5 个 MOC（Map of Content）** 索引页放在 `notes/`
- **附件独立**：所有图片/PDF/代码片段放在 `attachments/`，与笔记体系解耦
- **空目录有 stub README**：每个空目录都放了一个 `README.md` 引导说明
- **本地优先 + Git 版本控制**：单仓库跨设备同步

## 目录结构

```
myNotes/
│
├── inbox/                          # 闪念、临时收集（有 stub README）
├── journal/                        # 笔记日志（有 stub README）
│   ├── README.md
│   └── daily/                      # 每日笔记（有 stub README）
│
├── topics/                         # 主题知识（5 个一级主题）
│   ├── programming/                # 编程
│   │   ├── Java/  cplusplus/  Web/  Android/  Linux/  MySQL/
│   ├── ai/                         # AI
│   │   ├── Claude Code.md
│   │   ├── MoE.md
│   │   └── note.md
│   ├── math/                       # 数学（考研数一）
│   │   └── inequalities.md         # 不等式专题
│   ├── history/                    # 历史（待填充，有 stub README）
│   └── tools/                      # 工具笔记（与编程/AI 并列）
│       ├── VSCode.md
│       ├── Foam.md
│       ├── foam-knowledge-base-guide.md
│       ├── Markdown.md
│       └── Shortcuts.md
│
├── notes/                          # Zettelkasten 永久笔记 + MOC
│   ├── MOC - programming.md
│   ├── MOC - ai.md
│   ├── MOC - math.md
│   └── MOC - history.md
│
├── projects/                       # 当前项目（有 stub README）
├── resources/                      # 引用资料、skills 速查
│   └── skills.md
│
├── templates/                      # 笔记模板
│   ├── README.md
│   └── daily-note.md               # 每日笔记模板
│
├── archive/                        # 归档
│   └── old-structure/              # 2026-09 重构前的旧目录
│
├── attachments/                    # 附件独立王国
│   ├── images/
│   │   ├── programming/            # Java/ + Linux/ + vscode-remote-dev/
│   │   ├── ai/                     # 待填充（有 stub README）
│   │   ├── history/                # 待填充（有 stub README）
│   │   └── math/                   # 待填充（有 stub README）
│   ├── pdfs/                       # 待填充（有 stub README）
│   └── code-snippets/              # 待填充（有 stub README）
│
├── .claude/                        # Claude 配置
├── .vscode/                        # VS Code 工作区配置
│   ├── settings.json               # UTF-8 + LF + PowerShell 终端
│   └── extensions.json             # 推荐扩展列表（含 Tip of the Day）
│
├── .gitignore
└── README.md
```

## 主题与导航

| 主题 | MOC 索引 | 主题 README | 状态 |
|------|---------|------------|------|
| 编程 | [[notes/MOC - programming]] | `topics/programming/` | ✅ 有内容 |
| AI | [[notes/MOC - ai]] | `topics/ai/` | ✅ 有内容 |
| 数学 | [[notes/MOC - math]] | `topics/math/` | 🔨 起步中（考研数一） |
| 历史 | [[notes/MOC - history]] | [[topics/history/README]] | ⏳ 待填充 |
| 工具 | [[topics/tools/Shortcuts]] | `topics/tools/` | ✅ 工具速查 |

## 推荐工具

- **VS Code** —— 主力编辑器
- **Foam** —— 双向链接知识管理（见 [[topics/tools/foam-knowledge-base-guide]]）
- **Tip of the Day** —— 启动时右下角弹快捷键提示
- **Git** —— 版本控制 + 多设备同步

## ⚙️ 配置

> 所有配置都在 `.vscode/` 下，**重启 VS Code 后生效**。

### 配置文件总览

| 文件 | 作用 |
|------|------|
| `.vscode/settings.json` | 工作区设置（编码/行尾/终端/Foam/Tip） |
| `.vscode/extensions.json` | 推荐扩展（打开工作区时提示安装） |
| `.vscode/foam.code-snippets` | 笔记模板快捷片段（键入 prefix + Tab） |
| `templates/*.md` | Foam 完整模板（Ctrl+Shift+P → "Foam: Create Note from Template"） |
| `.gitignore` | Git 忽略规则 |

### `.vscode/settings.json` 关键配置

#### 📁 文件：强制 UTF-8 + LF

```json
{
  "files.encoding": "utf8",              // 新建文件默认 UTF-8
  "files.eol": "\n",                     // 新建文件默认 LF
  "files.autoGuessEncoding": false,      // 不自动猜编码（避免乱码）
  "files.insertFinalNewline": true,      // 末尾自动加 LF
  "files.trimFinalNewlines": true,       // 去尾部多余 LF
  "files.trimTrailingWhitespace": true   // 去尾部空白
}
```

#### 🖥️ 终端：PowerShell 强制 UTF-8（解决中文乱码）

```json
{
  "terminal.integrated.profiles.windows": {
    "PowerShell (UTF-8)": {
      "source": "PowerShell",
      "args": [
        "-NoExit",
        "-Command",
        "$OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; chcp 65001 | Out-Null"
      ]
    }
  },
  "terminal.integrated.defaultProfile.windows": "PowerShell (UTF-8)"
}
```

> **不生效？** 手动在新终端跑 `chcp 65001` 或升级到 PowerShell 7（`winget install Microsoft.PowerShell`）。

#### 🔔 Tip of the Day：启动弹快捷键

```json
{
  "tipOfTheDay.enabled": true,
  "tipOfTheDay.showOnStartup": true,         // 启动时弹
  "tipOfTheDay.startupHourLocal": 8,         // 8 点后才弹（避免凌晨）
  "tipOfTheDay.language": "zh",              // 中文提示
  "tipOfTheDay.operatingSystem": "auto"      // 自动检测 OS
}
```

手动触发：`Ctrl+Alt+T`

#### 🧠 Foam 模板目录

```json
{
  "foam.templates.folderPath": "./templates",  // 模板源目录
  "foam.templates.snippetPrefix": "tpl",       // 列表触发前缀
  "foam.templates.dateFormat": "YYYY-MM-DD"    // 模板 {{date}} 格式
}
```

使用：
- `Ctrl+Shift+P` → `Foam: Create Note from Template`（列表）
- 或键入 `tpl` + Tab（弹列表）

#### 📝 Markdown 智能补全

```json
{
  "[markdown]": {
    "files.encoding": "utf8",
    "files.eol": "\n"
  }
}
```

### `.vscode/extensions.json` 推荐扩展

打开工作区时，VS Code 会提示安装这些扩展：

| 扩展 ID | 作用 |
|---------|------|
| `WrecklessEngineer.tip-of-the-day` | 启动时弹快捷键提示 |
| `foam.foam-vscode` | 双向链接知识管理 |
| `yzhang.markdown-all-in-one` | 目录、快捷键、数学公式 |
| `shd101wyy.markdown-preview-enhanced` | **强大 Markdown 预览**（Cornell 模板依赖） |
| `marp-team.marp-vscode` | **Marp：Markdown → PPT / PDF / HTML**（可选） |
| `eamodio.gitlens` | Git 增强 |
| `streetsidesoftware.code-spell-checker` | 英文拼写检查 |
| `ms-python.python` | Python 支持 |

### 🎨 模板渲染依赖

| 模板 | 渲染方式 | 必需扩展 |
|------|---------|---------|
| `daily-note` | 纯 Markdown | 无 |
| **`cornell-note`** | **HTML + 内联 CSS**（两栏版式） | **`shd101wyy.markdown-preview-enhanced`** |
| `permanent-note` | 纯 Markdown | 无 |
| `literature-note` | 纯 Markdown | 无 |
| `moc` | 纯 Markdown | 无 |
| `project` | 纯 Markdown | 无 |
| `code-snippet` | 纯 Markdown | 无 |

> Cornell 笔记的精髓是**真正的两栏版式**（左线索 / 右笔记 / 底总结），纯 Markdown 表格无法做到。
> 因此本模板采用 **HTML `<div>` + CSS Grid** 实现，**必须用 Markdown Preview Enhanced 预览**才能看到效果。

### 🖨️ 导 PDF / HTML / 幻灯片

#### 方案 A：Marp 导 PPT / PDF（适合做展示）

```powershell
# 1. 安装 Marp CLI（一次性）
npm install -g @marp-team/marp-cli

# 2. 在 .md 文件顶部加 Marp frontmatter：
#    ---
#    marp: true
#    theme: default
#    ---

# 3. 命令行导 PDF
marp templates/cornell-note.md --pdf
```

VS Code 里：装了 `marp-team.marp-vscode` 扩展后，**Marp 面板**（上方工具栏）可直接预览幻灯片 / 导 PDF。

#### 方案 B：Markdown Preview Enhanced 导 PDF（适合单页笔记）

```powershell
# 1. 在 VS Code 打开 .md 文件
# 2. Ctrl+Shift+P → "Markdown Preview Enhanced: Open Preview"
# 3. 预览界面右上角 ⋯ → "Chrome (Puppeteer) PDF"
```

会自动用 Chromium 渲染当前笔记（含 HTML/CSS）并导出 PDF。

### 📊 Marp 完整使用指南

详见 [[topics/tools/marp-guide]] —— 包含 4 个实战示例（算法讲解 / 考研数学 / 康奈尔笔记 / 带背景图）、Frontmatter 详解、主题自定义、批量导出等。

### `.vscode/foam.code-snippets` 快捷片段

在任何 `.md` 文件里输入 prefix 然后按 **Tab**：

| 输入 | 用途 | 对应完整模板 |
|------|------|--------------|
| `daily` + Tab | 每日笔记骨架 | `templates/daily-note.md` |
| `cornell` + Tab | **康奈尔笔记骨架（3 区：线索/笔记/总结）** | `templates/cornell-note.md` |
| `perm` + Tab | Zettelkasten 永久笔记骨架 | `templates/permanent-note.md` |
| `lit` + Tab | 文献笔记骨架 | `templates/literature-note.md` |
| `moc` + Tab | MOC 索引页骨架 | `templates/moc.md` |
| `proj` + Tab | 项目笔记骨架 | `templates/project.md` |
| `code` + Tab | 代码片段骨架 | `templates/code-snippet.md` |
| `wl` + Tab | `[[target\|display]]` 快速插入 | — |
| `fm` + Tab | YAML Frontmatter 头部 | — |

> **快捷片段**（VS Code 原生）只给骨架；**完整模板**（Foam）含详细字段。

### `templates/` 完整模板清单

| 模板 | 用途 | 大小 |
|------|------|------|
| `daily-note.md` | 每日笔记（PARA 1） | 621B |
| **`cornell-note.md`** | **康奈尔笔记（3 区：线索 / 笔记 / 总结）** | **2.2KB** |
| `permanent-note.md` | **Zettelkasten 永久笔记（核心）** | 882B |
| `literature-note.md` | 读书/读文章 | 1.0KB |
| `moc.md` | 主题索引页 | 994B |
| `project.md` | 项目跟踪 | 986B |
| `code-snippet.md` | 重用代码 | 560B |
| `README.md` | 模板目录说明 | 1.7KB |

详见 [[templates/README]]。

### 完整工作流

```
1. 早上开 VS Code
   ↓
2. Ctrl+Shift+P → "Foam: Open Daily Note"  (打开/创建今日笔记)
   ↓
3. 输入 daily + Tab → 展开骨架
   ↓
4. 边写边用 perm/lit/proj 插入其他笔记的骨架
   ↓
5. 用 wl + Tab 快速插入 [[wikilink]]
   ↓
6. 写完保存，Foam 自动建立反向链接
   ↓
7. 周末整理：用 moc 模板新建/更新 MOC 索引
```

## 重建历史

- **2026-09-09 第一次重构**：从旧 `Developing/AI/Source` 结构重构为 PARA + Zettelkasten 混合结构
  - 4 大主题提取到 `topics/` 一级
  - 工具笔记提升为 `topics/tools/`
  - 附件统一到 `attachments/`
  - 所有文本文件转 UTF-8 + LF
  - 旧目录归档到 `archive/old-structure/`

- **2026-09-09 完善**：英文文件名 + stub README
  - 中文文件名改为英文：`不等式.md` → `inequalities.md`、`内核-4.9编译.md` → `linux-kernel-4.9-build.md`
  - 11 个空目录添加 stub `README.md` 引导说明
  - 图片目录压缩：去除冗余的 `developing/` 层级，重新组织为 `Java/`、`Linux/`、`vscode-remote-dev/`
  - 创建每日笔记模板 `templates/daily-note.md`
  - 为 inequalities.md、linux-kernel-4.9-build.md 添加 Frontmatter

- **2026-09-09 模板 + MOC 完善**：
  - 新增 5 个核心模板：`permanent-note` / `literature-note` / `moc` / `project` / `code-snippet`
  - 重写 4 个 MOC，加 wikilink 索引和 Foam 查询语法
  - 35 个 MOC 内 wikilink 全部有效

- **2026-09-09 配置体系化**：
  - 新增 `.vscode/foam.code-snippets`（8 个原生 snippet）
  - 在 `.vscode/settings.json` 配置 Foam 模板目录
  - **本节** README 详细文档化所有配置

- **2026-09-09 增加康奈尔笔记模板**：
  - 新增 `templates/cornell-note.md`（2.2KB）—— 经典的 3 区笔记法：线索栏 / 笔记栏 / 总结
  - 在 `.vscode/foam.code-snippets` 加 `cornell` + Tab 快捷片段
  - 更新 templates/README.md 和主 README 索引

- **2026-09-09 Cornell 模板升级为 HTML 版式 + Marp 导出**：
  - 重写 `cornell-note.md` 用 HTML `<div>` + CSS Grid 实现真正的两栏版式
  - 必需依赖：Markdown Preview Enhanced（已在推荐列表）
  - 新增 `marp-team.marp-vscode` 到推荐扩展（导 PDF/PPT/HTML）
  - README 新增"模板渲染依赖"和"导 PDF/HTML/幻灯片"两个子节

- **2026-09-09 新增 Marp 完整使用指南**：
  - 新建 `topics/tools/marp-guide.md`（12.8KB / 10 节 / 4 个实战示例）
  - 覆盖：基础语法、Frontmatter、主题、KaTeX、CLI 导出、批量处理、8 个 FAQ
  - 在 Shortcuts.md、MOC - programming.md、README.md 添加链接

- **2026-09-10 三个 Marp 实战成果**：
  - ① **Marp 幻灯片实战**：`topics/programming/Java/slides/Servlet-lifecycle.md`（6.5KB，11 张幻灯片，含代码/表格/ASCII 时序图）
  - ② **Cornell × Marp 混合模板**：`templates/cornell-marp.md`（5.5KB，含完整 CSS + AM-GM 实战示例）
  - ③ **5 分钟录屏脚本**：`topics/tools/marp-screencast-script.md`（8KB，5 节时间轴 + 录制清单 + 发布建议）
  - 更新 MOC、Mar p guide、templates README 引用
