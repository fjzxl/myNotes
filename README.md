# myNotes · 知识库

> 基于 **Zettelkasten + PARA 混合方法** 的个人知识库。VS Code + Foam 双链管理，所有内容为纯 Markdown，**所有文件名英文**。

## 设计原则

- **4 大主题**：`programming` / `ai` / `math` / `history`
- **`tools` 提升为一级主题**（与编程/AI 并列）
- **`exams` 考试备考一级主题**：软考等备考大纲、真题与论文练习
- **`languages` 语言学习一级主题**：日语等外语学习大纲与语料（兴趣驱动，考试仅作阶段自测）
- **6 个 MOC（Map of Content）** 索引页放在 `notes/`（编程 / AI / 数学 / 历史 / 考试备考 / 语言学习）；工具主题以 [Shortcuts](topics/tools/Shortcuts.md) 为速查入口
- **附件独立**：图片/代码片段等附件放在 `attachments/`，与笔记体系解耦（大体积教材 PDF 例外，见 `.gitignore` 说明）
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
├── topics/                         # 主题知识（7 个一级主题）
│   ├── programming/                # 编程
│   │   ├── Java/  cplusplus/  Web/  Android/  Linux/  MySQL/
│   ├── ai/                         # AI
│   │   ├── Claude Code.md
│   │   ├── MoE.md
│   │   └── ml-booklist.md          # 机器学习书单与 16 周计划
│   ├── math/                       # 数学（考研数一）
│   │   ├── inequalities.md         # 不等式专题总览（依赖图 · 15 条一览表 · 口诀速记）
│   │   ├── inequalities/           # 不等式章节笔记（01-basics ~ 06-exercises 六章）
│   │   ├── functions-and-bounds.md # 界与函数（高数起点）
│   │   ├── calculus.md             # 高等数学总览（章节导航）
│   │   └── calculus/               # 高数章节笔记（02-03-sequence-function-limits.md 等）
│   ├── history/                    # 历史（待填充，有 stub README）
│   ├── exams/                      # 考试备考（软考等）
│   │   ├── README.md
│   │   └── ruankao/                # 软考
│   │       ├── system-architect.md   # 系统架构设计师备考大纲
│   │       └── essay-sample-seckill.md # 论文范文：秒杀系统
│   ├── languages/                  # 语言学习（兴趣向，考试仅作自测）
│   │   ├── README.md
│   │   └── japanese/               # 日语
│   │       ├── syllabus.md         # 日语学习大纲（标日 + JLPT 分级）
│   │       ├── kana.md             # 五十音笔记（总表 / 全表共通规律 / 发音 / 辨析）
│   │       ├── kana-cards.md       # 五十音闪卡（235 张，Q::A 牌组）
│   │       ├── kana-plan.md        # 五十音三周每日计划
│   │       └── kana-*-row.md       # 逐行笔记全 10 行（a/ka/sa/ta/na/ha/ma/ya/ra/wa，拨音 ん 并入 wa 篇）
│   └── tools/                      # 工具笔记（与编程/AI 并列）
│       ├── README.md               # 工具索引（入口）
│       ├── VSCode.md
│       ├── Foam.md
│       ├── foam-knowledge-base-guide.md
│       ├── Markdown.md
│       ├── Shortcuts.md
│       ├── marp-guide.md           # Marp 完整使用指南
│       └── marp-screencast-script.md  # Marp 5 分钟录屏脚本
│
├── notes/                          # Zettelkasten 永久笔记 + MOC
│   ├── MOC - programming.md
│   ├── MOC - ai.md
│   ├── MOC - math.md
│   ├── MOC - history.md
│   ├── MOC - exams.md
│   └── MOC - languages.md
│
├── projects/                       # 当前项目（有 stub README）
├── resources/                      # 引用资料、skills 速查
│   └── skills.md
│
├── templates/                      # 笔记模板（12 个）
│   ├── README.md
│   ├── daily-note.md               # 每日笔记
│   ├── cornell-note.md             # 康奈尔笔记（HTML 两栏版式）
│   ├── cornell-marp.md             # 康奈尔 × Marp（笔记转幻灯片）
│   ├── book-note.md                # 读书笔记（整本书沉淀）
│   ├── book-chapter.md             # 章节阅读与主动回忆
│   ├── skill-learning.md           # 技能学习计划与验收
│   ├── practice-log.md             # 练习、纠错与复测
│   ├── permanent-note.md           # Zettelkasten 永久笔记
│   ├── literature-note.md          # 文献笔记
│   ├── moc.md                      # MOC 索引页
│   ├── project.md                  # 项目跟踪
│   └── code-snippet.md             # 代码片段
│
├── archive/                        # 归档（有 stub README，当前无归档内容）
│
├── check.py                        # 仓库唯一检查入口：文件名规范 + 链接/格式
├── .checkallow                     # 文件名 kebab-case 例外名单（check.py 读取）
├── scripts/                        # 仓库工具
│   └── check_notes.py              # 链接/格式校验库（由 check.py 调用）
├── tests/
│   └── test_check.py               # 回归测试：python -m unittest discover -s tests
│
├── attachments/                    # 附件独立王国
│   ├── images/
│   │   ├── programming/            # Java/ + Linux/ + vscode-remote-dev/
│   │   ├── ai/                     # 待填充（有 stub README）
│   │   ├── history/                # 待填充（有 stub README）
│   │   ├── languages/              # japanese/（五十音讲义挂图）
│   │   └── math/                   # inequalities/（不等式专题插图 × 20）+ curves/（参数方程·极坐标常见曲线 × 8）
│   ├── pdfs/                       # 待填充（有 stub README）
│   └── code-snippets/              # 待填充（有 stub README）
│
├── .claude/                        # Claude 配置
├── .vscode/                        # VS Code 工作区配置
│   ├── settings.json               # UTF-8 + LF + PowerShell 终端
│   └── extensions.json             # 推荐扩展列表（含 Tip of the Day）
│
├── .gitignore
├── .gitattributes                # 锁定 UTF-8 + LF 行尾（跨设备克隆不跑偏）
├── .zcodeignore
└── README.md
```

## 主题与导航

| 主题 | MOC 索引 | 主题 README | 状态 |
|------|---------|------------|------|
| 编程 | [MOC - programming](notes/MOC%20-%20programming.md) | `topics/programming/` | ✅ 有内容 |
| AI | [MOC - ai](notes/MOC%20-%20ai.md) | `topics/ai/` | ✅ 有内容 |
| 数学 | [MOC - math](notes/MOC%20-%20math.md) | `topics/math/` | 🔨 起步中（考研数一） |
| 历史 | [MOC - history](notes/MOC%20-%20history.md) | [README](topics/history/README.md) | ⏳ 待填充 |
| 考试备考 | [MOC - exams](notes/MOC%20-%20exams.md) | [README](topics/exams/README.md) | 🔨 起步中（软考架构师） |
| 语言学习 | [MOC - languages](notes/MOC%20-%20languages.md) | [README](topics/languages/README.md) | 🔰 起步中（日语·兴趣向） |
| 工具 | [Shortcuts](topics/tools/Shortcuts.md) | [README](topics/tools/README.md) | ✅ 工具速查 |

## 推荐工具

- **VS Code** —— 主力编辑器
- **Foam** —— 双向链接知识管理（见 [foam-knowledge-base-guide](topics/tools/foam-knowledge-base-guide.md)）
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
| `templates/*.md` | Foam 完整模板（Ctrl+Shift+P → "Foam: Create New Note From Template"） |
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
  // 模板目录（默认 .foam/templates；指到 templates/ 即可复用本仓库模板）
  "foam.templates.folder": "templates"
}
```

使用：
- `Ctrl+Shift+P` → `Foam: Create New Note From Template`，从列表选择模板
- 模板中的 `$FOAM_TITLE`、`$FOAM_DATE_*` 等 Foam 变量会自动展开；`{{...}}` 字段需手动填写
- 快速骨架走本地 snippets：`daily` / `cornell` / `perm` 等 + Tab

#### 🗓️ Foam 每日笔记目录

```json
{
  // "Foam: Open Daily Note" 的落盘位置（Foam 已标记弃用该设置，0.44 仍生效）
  "foam.openDailyNote.directory": "journal/daily"
}
```

> 新版 Foam 改由 `templates/daily-note.md` 模板的 `foam_template.filepath` 决定每日笔记路径——本仓库模板已配置同一位置，升级后行为不变。`输入 daily + Tab` 的手动骨架流程仍可用于补写过去的日期。

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
| **`cornell-marp`** | **HTML + Marp**（笔记转幻灯片） | **`marp-team.marp-vscode`（或 Marp CLI）** |
| `book-note` | 纯 Markdown | 无 |
| `book-chapter` | 纯 Markdown | 无 |
| `skill-learning` | 纯 Markdown | 无 |
| `practice-log` | 纯 Markdown | 无 |
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

# 3. 命令行导 PDF（cornell-marp 才是 Marp 文档）
marp templates/cornell-marp.md --pdf
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

详见 [marp-guide](topics/tools/marp-guide.md) —— 包含 4 个实战示例（算法讲解 / 考研数学 / 康奈尔笔记 / 带背景图）、Frontmatter 详解、主题自定义、批量导出等。

### `.vscode/foam.code-snippets` 快捷片段

在任何 `.md` 文件里输入 prefix 然后按 **Tab**：

| 输入 | 用途 | 对应完整模板 |
|------|------|--------------|
| `daily` + Tab | 每日笔记骨架 | `templates/daily-note.md` |
| `jp` + Tab | 日语过关卡（可单独插入） | — |
| `cornell` + Tab | **康奈尔笔记骨架（3 区：线索/笔记/总结）** | `templates/cornell-note.md` |
| `perm` + Tab | Zettelkasten 永久笔记骨架 | `templates/permanent-note.md` |
| `lit` + Tab | 文献笔记骨架 | `templates/literature-note.md` |
| `book` + Tab | **读书笔记骨架（整本书沉淀）** | `templates/book-note.md` |
| `chapter` + Tab | 章节阅读与主动回忆 | `templates/book-chapter.md` |
| `skill` + Tab | 技能学习计划与验收 | `templates/skill-learning.md` |
| `practice` + Tab | 单次练习、纠错与复测 | `templates/practice-log.md` |
| `moc` + Tab | MOC 索引页骨架 | `templates/moc.md` |
| `proj` + Tab | 项目笔记骨架 | `templates/project.md` |
| `code` + Tab | 代码片段骨架 | `templates/code-snippet.md` |
| `wl` + Tab | `[显示文字](相对路径.md)` 快速插入笔记链接 | — |
| `fm` + Tab | YAML Frontmatter 头部 | — |

> **快捷片段**（VS Code 原生）只给骨架；**完整模板**（Foam）含详细字段。

### `templates/` 完整模板清单

| 模板 | 用途 |
|------|------|
| `daily-note.md` | 每日笔记（PARA 1） |
| **`cornell-note.md`** | **康奈尔笔记（3 区：线索 / 笔记 / 总结）** |
| **`cornell-marp.md`** | **康奈尔 × Marp 混合（笔记转幻灯片）** |
| `book-note.md` | **读书笔记（整本书：总结/逐章/金句/行动）** |
| `book-chapter.md` | 章节阅读、论证分析与主动回忆 |
| `skill-learning.md` | 技能学习计划、能力拆解与验收 |
| `practice-log.md` | 单次练习、反馈、纠错与复测 |
| `permanent-note.md` | **Zettelkasten 永久笔记（核心）** |
| `literature-note.md` | 读书/读文章 |
| `moc.md` | 主题索引页 |
| `project.md` | 项目跟踪 |
| `code-snippet.md` | 重用代码 |
| `README.md` | 模板目录说明 |

详见 [README](templates/README.md)。

读书可用 [章节笔记](templates/book-chapter.md) 记录每次阅读，再汇总到 [整本书笔记](templates/book-note.md)；技能学习可用 [学习计划](templates/skill-learning.md) 定目标，配合 [练习记录](templates/practice-log.md) 持续练习、纠错和复测。

### 完整工作流

```
1. 早上开 VS Code
   ↓
2. Ctrl+Shift+P → "Foam: Open Today's Note"  (自动在 journal/daily/ 创建/打开今日笔记；默认快捷键 Alt+D)
   ↓
3. 在今日笔记里填目标与日志（daily-note 模板自动套用）
   ↓
4. 边写边用 perm/lit/proj 插入其他笔记的骨架
   ↓
5. 用 wl + Tab 快速插入笔记间的 Markdown 相对链接
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
  - ① **Marp 幻灯片实战**：`topics/programming/Java/slides/Servlet-lifecycle.md`（6.5KB，15 张幻灯片，含代码/表格/ASCII 时序图）
  - ② **Cornell × Marp 混合模板**：`templates/cornell-marp.md`（5.5KB，含完整 CSS + AM-GM 实战示例）
  - ③ **5 分钟录屏脚本**：`topics/tools/marp-screencast-script.md`（8KB，5 节时间轴 + 录制清单 + 发布建议）
  - 更新 MOC、marp-guide、templates README 引用

- **2026-09-17 ~ 09-19 不等式专题大扩充 + book-note 模板**：
  - `topics/math/inequalities.md` 扩充至 1657 行：高阶不等式（Young / Hölder / 权方和 / Minkowski）、多视角理解（向量·矩阵·几何·物理）、应用（指数/对数/三角/积分）
  - 新增 20 张几何插图，统一放 `attachments/images/math/inequalities/`
  - 新增 `templates/book-note.md` 读书笔记模板 + `book` + Tab 快捷片段

- **2026-09-30 链接与目录同步**：
  - 全库 wikilink 统一为工作区根相对路径：修复 `templates/cornell-marp`、`Java/slides/Servlet-lifecycle`、`marp-screencast-script`、`marp-guide`、`Foam` 中的 `../` 相对链接与裸文件名链接
  - README 目录结构 / 模板清单 / snippet 表与实际文件同步
  - `attachments/images/math/README.md` 更新为实际结构（inequalities/ × 20）
  - MOC - math / MOC - programming 更新索引与更新记录

- **2026-09-30 TypeScript 笔记体系**：
  - 补全 `topics/programming/Web/typescript/intro.md`（26 行骨架 → 1100+ 行完整入门教程）
  - 新增 `topics/programming/Web/typescript/type-system.md`（进阶篇：结构化类型、型变、条件类型、infer、递归、类型体操）
  - 新增 `topics/programming/Web/typescript/interface.md`（对照 JavaScript 解释接口契约的用途与边界）
  - 笔记间互链成网：javascript / es6 / intro / interface / type-system 按学习顺序互相导航，MOC 收录全部
  - 三篇笔记的全部类型示例经 tsc 5.9 `--strict` 实测校验；据此修正 satisfies 字符串字面量拓宽的描述、示例类型 `Range` 与 DOM 全局类型重名、结构化示例中多余属性检查的表述等 3 处问题

- **2026-10-01 结构优化 + 全库校验修复**：
  - 拆分超长教程：`javascript.md`（9600+ 行 → 总览导航页 + 8 章笔记）、`css.md`（5100+ 行 → 总览导航页 + 10 阶段笔记），总览保留学习路线/图谱/附录并新增章节导航，章节笔记互相链接前后章
  - 全库主题笔记补齐 frontmatter（title / tags / created / updated，共 26 篇）
  - 新增 `scripts/check_notes.py`：校验 wikilink / Markdown 链接锚点 / 图片目标 / frontmatter / 代码围栏配对 / 表格列数 / 编码与行尾
  - 依据外部审阅报告集中修复：Foam 工作流说明按官方文档校正（`foam.templates.folder`、`Foam: Create New Note From Template`、`Foam: Show Graph`、Backlinks 面板、每日笔记配置）、Marp 示例可运行化（cornell-marp 两示例补 `---` 与分页、marp-guide 嵌套围栏与颜色值加引号）、Servlet/JavaScript/ES6 示例缺陷、MoE 与不等式等概念表述，共 30+ 处

- **2026-10-02 新增考试备考主题**：
  - 新建 `topics/exams/`（含 stub README）与 `ruankao/system-architect.md`：软考系统架构设计师备考大纲，重点覆盖论文写作模块（素材卡 / 六段模板 / 真题矩阵 / 3 周冲刺节奏）
  - 新增 `notes/MOC - exams.md` 索引，README 目录结构与主题表同步

- **2026-10-08 新增语言学习主题**：
  - 新建 `topics/languages/`（含 README）与 `japanese/syllabus.md`：日语学习大纲（兴趣向——看懂动漫/游戏；零基础、每天约 20 分钟；标日教材 × JLPT N5→N3 分级里程碑，事实联网核实）
  - 新增 `notes/MOC - languages.md` 索引，README 目录结构与主题表同步

- **2026-10-09 数学起点笔记 + 五十音闪卡 + 链接巡检**：
  - 新增 `topics/math/functions-and-bounds.md`（界与函数：确界理论 · 函数四性质 · 初等函数 · 参数方程 · 极坐标 · 图形变换），挂入 MOC - math 与不等式专题导航
  - 新增 `topics/languages/japanese/kana-cards.md`（五十音闪卡 235 张，`Q :: A` 行内牌组，建卡进度对齐三周计划），kana / kana-plan / kana-a-row / MOC - languages 全链路互链
  - 链接巡检：`resources/skills.md` 接入「推荐工具」；MOC - math / MOC - programming 回链 [笔记编撰计划](projects/note-writing-plan.md)（原为单向）；目录树 math / languages 分支与实际文件同步

- **2026-10-10 内容补全批次（附带优化任务落地 + 数学推进）**：
  - 新增 `topics/programming/Web/html.md`（HTML 基础：结构、语义化、表单、无障碍），补齐前端三件套入口；es6.md 与 JS 教程第 6 章互加交叉引用明确分工
  - 空壳笔记扩充：`ai/Claude Code.md`（Agent 编程心得）、`cplusplus/into.md`（编译四阶段 + make）、`cplusplus/vscodec.md`（VS Code C/C++ 三层配置）、`Android/Android_into.md`（平台架构 + 四大组件）；`ai/note.md` 闪念移入 `inbox/innovation-flash.md`
  - 数学：新增 `topics/math/calculus.md`（高数总览）与 `topics/math/calculus/02-03-sequence-function-limits.md`（数列与函数极限长文）；`inequalities.md` 新增「口诀速记」（总纲三句 · 十五条口诀表 · 均值链专记 · 选工具顺口溜）与「分层习题」13 题（附提示与详解）
  - 各 MOC 与 `projects/note-writing-plan.md`（附带优化任务勾选、进度更新）同步；目录树 ai / math 分支同步

- **2026-10-11 全库审计修复（内容正确性 + 工具文档 + 仓库工程）**：
  - **数学**：`functions-and-bounds.md` 判别法的符号结论写反（$(0,1)$ 内应为同号、$(1,\infty)$ 内应为异号），已修正并与同句单调性结论对齐；`inequalities.md` 全 1889 行 + 13 道分层习题逐题验算无误
  - **日语**：`kana.md` 清音 44→**46**、わ行新音 3→**2**（を 读 o）、发音表 `つ/づ` 分行（原文把 `ぢ` 和 `つ` 排成一行）、促音出现位置补全（漏 う行前 / 拗音前 / 词首）、外来词音节补 `ヴァ/ヴィ/ヴェ/ヴォ/ツィ`
  - **工具文档**：`foam-knowledge-base-guide.md` 按 foam-vscode **0.46.0** 的 `package.json` 逐条核对——修正非法枚举值 `withoutBrackets`→`withoutExtensions`、`attachmentExtensions` 数组→空格分隔字符串、VS Code 要求 1.85→1.110+、删除「图谱依赖本地服务 / 需装 Node.js」的自相矛盾表述、替换 6 条已不存在的命令（`Show Welcome` / `Create Note From Placeholder` / `Search Notes` / `New Note` / `Copy Wikilink To Current Note` / `Reveal Current Note In Explorer`）、反向链接改到 Connections 视图、图谱分组配置改到 `foam.graph.views`；`marp-guide.md` 片段动画改为原生 fragmented list（原文的 `section.active` 是永不命中的死代码）、Mermaid 改用围栏代码块；`marp-screencast-script.md` 修正 `math: katex` 的位置（全局指令必须在顶部 frontmatter）与「导出后自动打开 PDF」；`VSCode.md` Alt+Click 改回左键
  - **结构一致性**：新增 `topics/tools/README.md` 工具索引并补齐 [README](topics/tools/README.md)；`Shortcuts` 与 `foam-guide` 收进 MOC - programming（工具笔记此前 5/7 有归属、2 篇无索引）；`kana-a-row` 收进 MOC - languages；`typescript/interface.md` 补 `updated`；README 目录树补 `essay-sample-seckill.md` / `.gitattributes` / `.zcodeignore`
  - **仓库工程**：新增 `.gitattributes` 锁定 UTF-8 + LF（此前 Windows `core.autocrlf=true` 且无该文件，克隆后会整体转 CRLF）；`.gitignore` 放行 `.vscode/foam.code-snippets`（settings.json 含机器相关路径，仍保持本地）；`check_notes.py` 清掉两处死代码并把 `updated` 纳入 frontmatter 必检项

- **2026-10-11 五十音图笔记补充**：
  - 新增**逐行笔记全 10 行**（`kana-a-row` ~ `kana-wa-row`，新增 9 篇；拨音 `ん` 并入わ行篇，与计划 10-20 的分组一致），每篇含速览表（段 / 平假名 / 片假名 / 罗马字 / 笔画 / 字源）、发音要点、笔顺、易混辨析、例词试读与自测清单，按每日计划日推进
  - `kana.md` 新增 **§9 全表共通规律**：行序口诀与六组记忆法（合计 46 音的推导）、辅音发音部位对照、「一拍」度量衡（拗音 1 拍 / 促音无声占 1 拍 / 长音加 1 拍）、**全表 8 个不按字母直拼的读音**（し・ち・つ・ふ・じ・ぢ・ず・づ）、平片笔顺共通规则、三个不属于行的特例（拨音 ん / 小写 ゃゅょ / 历史假名 ゐ ゑ）；原「自测与验收」顺延为 §10
  - 逐行笔记的 46 组「假名 ↔ 片假名 ↔ 罗马字」三元组已用脚本对拍标准五十音图：**46/46 全覆盖、0 错配**；新笔记统一标注「页码待对照教材补」，未编造任何教材页码
  - 索引同步：`kana.md` 关联区、`notes/MOC - languages`、`topics/languages/README.md`、README 目录树均收录新笔记；逐行笔记之间的「上一行 / 下一行」已双向互链

- **2026-10-11 不等式专题拆分为 hub + 章节笔记**：
  - `topics/math/inequalities.md`（2026 行）按学习阶段拆分：总览（依赖图 · 15 条一览表 · 目录）与口诀速记留在 hub，证明 / 多视角 / 应用 / 习题分居 `topics/math/inequalities/` 六章——`01-basics`（三角 · AM-GM · 排序 · 切比雪夫）、`02-core-tools`（柯西-施瓦茨含 Lagrange 恒等式附录 · 伯努利 · 琴生含凸函数判定附录 · Nesbitt 含 Titu 引理附录）、`03-advanced`（Young → Hölder → 权方和 / Minkowski）、`04-multiview`（多视角理解）、`05-applications`（七个场景 · 指对 · 三角 · 积分四件套 · 题型速查）、`06-exercises`（A/B/C 分层习题 + 答案详解）
  - 174 个文内锚点链接按「锚点 → 所在章」映射自动改写为跨文件 wikilink（总览表内用相对 Markdown 链接，避开表格内 `\|` 转义）；章节按 javascript/css 章节惯例「第 N / 6 章 · 上一章 · 下一章」互链、章尾 ↩ 返回总览
  - 外部引用同步：`templates/cornell-marp.md` 带锚点链接改指 `01-basics`；AGENTS.md hub 范例清单、README 目录树、MOC - math 描述与更新记录更新；`check_notes.py` 103 文件 0 error

- **2026-10-12 文档巡检修正**：
  - AGENTS.md 与 `templates/README.md` 更正 `.vscode/foam.code-snippets` 状态（已被 .gitignore 放行、暂未提交，原文误写为「被 Git 忽略」）
  - MOC - math / MOC - programming 的 `updated` 同步为 2026-10-11；MOC - programming 补录当日「核心笔记」收录 Shortcuts 与 foam-knowledge-base-guide 的更新条目
  - `archive/` 补 stub README，兑现「空目录有 stub README」约定
  - AGENTS.md 附件约定补「大体积教材 PDF 留在主题目录本地保存（gitignore）」例外，呼应 `.gitignore` 注释里的引用

- **2026-10-12 优化落地批次**：
  - **软考真题矩阵补全**：2025.5 试题四（论 AI 在测试用例生成中的应用）与 2026.5 整行（向量数据库 / 高并发 / 六边形架构 / 多模态大模型测试）按考生回忆版联网核实补入，矩阵扩为机考后四场，「高频方向」新增 AI 应用一类
  - **五十音页码补注**：9 篇逐行笔记的「页码待对照」占位按教材 PDF 逐页核实补全；发现入门单元实际至 **p.2–16**（p.17 为「基本单元 上」分隔页），kana / kana-plan / languages README 的 p.2–17 引用一并更正
  - **daily note 流程落地**：`.vscode/settings.json` 配 `foam.openDailyNote.directory: journal/daily`；`templates/daily-note.md` 升级为 Foam 原生模板（`foam_template.filepath`，新版 Foam 的接管机制）；播种首篇 `journal/daily/2026-10-12.md`（五十音 Day 1 任务）
  - **Zettelkasten 启动**：「交付即提取」约定写入 AGENTS.md（每篇计划内长文交付时提取 3–5 张原子卡）；MOC - math 补不等式六章直达导航，Ch1 挂首批 3 张原子卡（夹逼准则 / 单调有界定理 / 两个重要极限）；MOC - math 10-11 拆分条目补记原行数 1657
  - **README 推荐工具**撤下 `resources/skills` 速查（3 行裸列表与「科研技能清单」宣传不符；文件保留待扩写后再上线）

- **2026-10-12 锚点链接修复（Foam 跳转失效）**：
  - 症状：点击 hub 里的「实际场景」等锚点链接，Foam 提示**创建笔记**而非跳转。根因：拆分不等式专题时生成的 174 个 `[[路径#锚点]]` 式 wikilink——`#` 锚点 wikilink 的 Foam 解析跨版本不可靠（本地 VS Code 0.44.6 / VSCodium 0.46.0 均受影响；官方文档认可该语法但要求锚点为标题原文，而库内锚点为 GitHub slug）
  - 修复：全库 **114 处**锚点 wikilink 批量转为官方认可的 Markdown 锚点链接 `[文字](相对路径.md#锚点)`（不等式 hub + 六章 111 处、Foam.md、marp-guide.md 同文锚点、cornell-marp.md 手动 1 处）；锚点 slug 不变，VS Code 预览 / Foam / GitHub 三端原生跳转
  - 防再发：`check_notes.py` 新增规则——散文区出现 `[[..#..]]` 记 **error**；AGENTS.md 链接规范补「锚点一律用 Markdown 链接」条目；foam-knowledge-base-guide §4.1 补该坑说明

- **2026-10-13 journal 十月回填**：
  - 依据 git 提交历史与更新日志补记 `journal/daily/2026-10-01` ~ `2026-10-11` 与 `2026-10-13`（每日一篇，均标注「回填」，含提交时间、当日主线与相关笔记互链；日记间前后日成链）
  - `journal/daily/2026-10-12.md` 空白记录填充（全天主线回填 + 晚间三笔提交与深夜锚点修复批次）
  - 新建 `journal/weekly/2026-W40.md` 首篇周复盘（计划 W1 三线产出对照 + 反思 + W41 展望），兑现 journal README 的周日复盘节奏

- **2026-10-13 wikilink 全库停用（五十音笔记链接点击失效）**：
  - 症状：`journal/daily/2026-10-12.md` 里的五十音笔记 wikilink（`[[topics/languages/japanese/kana|五十音笔记]]` 等）点击不跳转；会话开始时 git status 出现的 `journal/daily/topics/` 未跟踪目录即为 Foam 把未解析链接按「当前笔记目录 + 目标路径」创建笔记的产物
  - 修复：全库 **760 处** wikilink 批量转为相对路径 Markdown 链接 `[文字](相对路径.md)`（107 个文件；空格 `%20` 编码；表格内转换顺带消除了 `\|` 转义问题）；`templates/` 占位与 foam-guide「概念关联」4 条占位（转纯文本）除外
  - 防再发：`check_notes.py` 规则升级——任何非模板 `[[...]]` wikilink 记 **error**；AGENTS.md 链接规范改为「笔记间链接一律 Markdown 相对链接」；`templates/daily-note.md` 与 `.vscode/foam.code-snippets` 的 `[[]]` 骨架同步替换

- **2026-10-13 journal 调整（删旧排新）**：
  - 删除 10-12 之前的回填日记（`journal/daily/2026-10-01` ~ `2026-10-11`）与 `journal/weekly/2026-W40.md` 周复盘；journal 现存 `2026-10-12` 起的实况与预排日记
  - 预排 `journal/daily/2026-10-14` ~ `2026-10-31` 共 18 篇：按五十音三周计划逐日排程（Day 3 ~ Day 20，さ行 → 拗音 → 周复习 → 综合自测 → 10-31 验收），目标清单、相关笔记链接（Markdown 相对链接）与前后日导航齐备；10-12 / 10-13 的失效前后日链接已同步修正

- **2026-10-13 根目录检查入口 `check.py`**：
  - 新增仓库根目录 `python check.py`（可带路径参数只查指定文件）：先跑**文件名规范**（仅 warning，不影响退出码——空格 / 大写 / 下划线 / 非 ASCII 的 kebab-case 风格提示、`journal/daily/` 日期命名、`.md` 扩展名大小写），再复用 `scripts/check_notes.py` 跑**链接与格式**（error 影响退出码）
  - 链接规则单一事实源仍在 `scripts/check_notes.py`，`check.py` 通过 import 复用，不另维护一份
- **2026-10-13 检查器加固：路径统一 + 回归测试**：
  - **路径统一归一化**：所有参数先经 `check_notes.normalize()` 归为仓库相对 posix 路径（相对 cwd 或绝对皆可），豁免判断、报错定位、链接解析只用归一化路径；越界 / 不存在 / 显式传入非 `.md` / 未匹配到任何 `.md` 均以退出码 2 报错（不再出现“0 文件却显示通过”）
  - **文件名例外名单外置**：`.checkallow`（每行一个仓库相对路径）取代 `check.py` 里的硬编码集合，存量 `MOC - *.md`、`Claude Code.md` 等 20 项在此维护，全库检查 0 文件名 warning；非 ASCII / 空格对**所有**文件（含 PDF、附件）提示
  - **链接检查修复**：`<路径>` 目标此前被 `URL_RE` 的 `^<` 整体跳过（死代码），现纳入校验；链接目标按磁盘实际大小写核对（Windows 不区分大小写，GitHub 区分，避免本地通过而线上 404）；逃逸仓库的目标改报“指向仓库外”
  - **健壮性 / 性能**：UTF-8 BOM 自动剥离（不再误报缺 frontmatter）；重复标题生成 GitHub 式锚点 `foo`/`foo-1`；行内代码按等长反引号对剥离（支持 `` `` `` 与 `|`）、代码围栏支持 `~~~` 且字符须配对；`collect()` 单次遍历、`run_files()` 复用已展开列表、锚点与目录列表按需缓存
  - **回归测试**：`tests/test_check.py`（标准库 `unittest`，24 项）覆盖路径归一化、`<路径>` 校验、大小写核对、BOM、围栏、行内代码表格、U+FEFF、非 ASCII 文件名等；`python -m unittest discover -s tests` 全绿

- **2026-10-13 check.py 四项加固**：
  - 无参数运行改为**检查全库**（与运行目录无关；此前从仓库外运行误报「路径位于仓库之外」，从子目录运行只查子树）
  - `.checkallow` 坏条目（越出仓库 / 路径不存在）跳过并提示，不再崩溃
  - 检查自动跳过 `git check-ignore` 命中的本地文件（`-z` 传参避免 CJK / 空格路径被引号转义；git 不可用时退化为不过滤）——三本本地教材 PDF 的命名警告随之消失
  - 同文档锚点 `(#slug)` 纳入校验（对本文标题核对，缺失记 warning）；全库 136 处既有同文档锚点全部通过

- **2026-10-13 不等式专题：用户改版核查 + 初学者优化**：
  - 核查用户当日修改（hub 入门路径/符号表/编号对照、各章「三问」导读、切比雪夫配对作差法证明、协方差扩写）：配对作差恒等式与协方差三种表述经 `fractions.Fraction` 精确算术 200 组随机对拍通过，协方差例子（5/3 与 -5/3）复核无误，全部「三问」陈述与取等条件核对正确，链接 0 error
  - `05-applications.md`：新增篇首「本篇路线」（五节导航）与「七个场景速览」表（场景 → 生活问题 → 工具，含文内锚点）；对数不等式推论补推导提示（上/下界各自来源、严格版由等号条件得到）
  - hub：删除与「章节导航」重复的「目录」块（其链接已由总览表「详见」列覆盖），「章节导航」补第七部分（口诀）条目，页眉「章节导航见文末」过时说法改为链接指向实际位置

- **2026-10-13 日语每日过关卡上线**：
  - 按用户选择（内嵌日记 / 弹性打卡 / 通用卡）设计「🎌 日语过关卡」区块：复习打卡（≥5 分钟保底）+ 自测四项错项登记 + 三级判定（✅ 错 ≤1 / 🔶 保底 / ❌ 错 ≥2 次日复测），错项累计 ≥3 次回流 kana-plan 登记——非五十音阶段同样适用
  - 批量插入 10-12 ~ 10-31 全部 20 篇冲刺日记（Goals 与 Log 之间）；`templates/daily-note.md` 与 `.vscode/foam.code-snippets` 的 `daily` 骨架同步携带，另加独立 `jp` + Tab 快速插入片段；kana-plan §5 补记录规则

- **2026-10-13 五十音逐行笔记「下一行」导航修复**：
  - 根因：十篇逐行笔记按 あ→わ 顺序创建，写作时「下一行」的目标笔记尚未存在，故只写成纯文本（笔记名放反引号），「上一行」当时已成文、是真链接；10-13 的 wikilink 批量转换只处理既有链接，这些纯文本保持原样，表现为「不能点击」
  - 修复：ka~ya 八篇的「下一行」统一转为 Markdown 链接（含学习日期与星期）；补上缺失的 ra→わ行 链接；末行 わ行 增加指向五十音笔记全表复习（10-21）的出口，十行导航链完整闭环

- **2026-10-13 过关卡自测链接列 + k8s 案例沉淀 + 当日日志补全**：
  - 「日语过关卡」升级三列（项目 / **自测内容·链接** / 今日结果）：20 篇冲刺日记逐日预填当日自测材料锚点（新学行日 → 行笔记 §1 速览 / §3 笔顺 / §5 例词 / §6 自测；周复习 → 总笔记全表；浊音拗音日 → §3；自测验收日 → §10 与计划 §4），锚点由 `check_notes.github_slug` 从真实标题计算并全量校验；模板与 `daily`/`jp` snippet 同步三列通用版
  - 新增 [calico-iptables-stale-rules](topics/programming/Linux/calico-iptables-stale-rules.md)（当日云主机重启后网络不通的排查与修复：现象 / 根因 / 排查命令 / `iptables -F` 与只删 `cali-` 链的替代方案 / 预防），MOC - programming 基础设施与工具两区收录
  - 2026-10-13 日志按用户口述补全（上午打通云主机至算力资源网络、下午 calico 修复链接主题笔记、晚上不等式核查优化）并整理 P&S 区块
  - 补充修订（同日晚）：按用户口述修正事实——重启范围为 ta-node2/ta-node3 两台、现象为 calico pods 报错 + ta-node2 CoreDNS 启动失败、`kubectl logs` 报 `:10250 no route to host`（apiserver→kubelet 入向被拦）；笔记重写为「集群背景 / 现象时间线 / 五步排查思路 / 根因 / 修复与替代 / 预防」，新增「模式识别」要点（`Error from server: Get "https://<node>:10250/..."` 即节点网络层问题）；实际修复为多台 `iptables -F` + 重启 calico（最小修复未做对照，已在笔记中注明）
  - 同日再补：按用户复盘问题（更快定位 / 更好修复 / 如何避免）重写三节——排查思路改为「错误语义判读表（no route to host / refused / timeout 分层）→ `-o wide` 节点映射 → `curl -k https://node:10250/healthz` 响应语义表 → iptables 计数器法 + firewalld 必查 → crictl 绕过 apiserver 取日志」；修复改为四级推荐顺序（排除 firewalld → 重启故障节点 calico-node 让 Felix 重写 → 定向删 cali- 链 → iptables -F 兜底）；预防补 firewalld 禁用、drain 标准流程、重启后体检清单、blackbox 探测
  - 同日三补：按用户实测路径完善——「本例实际路径（复盘）」记录 ping 通 / telnet·curl 10250 超时 / kubectl logs 报错的真实时间线与每步证明（ping 通 + TCP 超时 = 端口级选择性拦截；REJECT 与 DROP 并存 = 规则半成品，多次探测需记时间点）；「更优路径」把三连升级为三对照矩阵（健康节点 / 其他端口 22 / 本机）+ nc 超时探测 + tcpdump 双端同抓；新增「同类 k8s 网络问题通用排查框架」（四层定位 + 四类链路病根速查表）

- **2026-10-13 过关卡可勾选修复**：表格单元格里放不了可点击复选框（☐ 是普通字符），把「复习打卡」移出表格改为 `- [ ]` 任务项（VS Code 预览可直接点击勾选并写回源文件）、「今日判定」改为填空式（✅／🔶／❌ 填一个）；20 篇日记同步（10-12 用户已自行转换、10-13 保留已填的用时 5 分钟并预勾选），模板与 `daily`/`jp` snippet 同步

- **2026-10-15 全库内容审查与修复**：157 个 Markdown 文件在机械检查 0 error 的基础上逐篇精读（数学推导 python 实算、JS 例子 node 实测、技术事实对照官方源码/文档、日语对照教材与外部权威），修复确凿错误 61 处、存疑项 18 处（S11/S12 按用户要求保留）。要点：数学（04-multiview p-范数单调方向、squeeze 上界 n=1 失真）；日语（促音条件统一 か・さ・た・ぱ 行、长音例对与字源 さ=左、へ=蛇/ほんせん 删除更正、マ 笔顺、を 起笔说法删除、「7 个音」du→ぢ/づ 口径、MOC 同步）；编程（Servlet doGet/doPost 默认 405、Spring Web 模块 4 个与 portlet 5.0 移除、getBean id、Aware 阶段注脚、calico 先 -F 再 -X、gen_compile_commands.py 5.0、bear --、apt show、CSS circle() 基准与 transform 顺序、space-evenly 图示、颜色 148、lety→lett、let/const TDZ 口径、对象键 Symbol、BigInt/Symbol 章节、箭头函数提升格、16.7ms/50ms、SuppressedError 注）；AI/工具（Pile 链接描述、书单剑桥 6 本、Durrett 书名、Tong Zhang 单位、VS Code 终端设置 1.57/Exec 后缀、Jupyter 单元格调试、Foam: Open Today's Note 命令名（journal/README、daily-note 模板与工作流同步）、Marp highlight.js→Shiki、frontmatter 键序）；计划（短稿边界统一为 Ch1–Ch3+21–23、工程化 W21–W22 连续起步、报名窗口按 2026 上半年 3-23～31 对齐 W25 下半周～W26 初）；日记（10-12/14/15 打卡状态对齐）；模板/库元（cornell-marp 导出命令与分页符示例、daily-note frontmatter 合并进 foam_template 同块、attachments 图片改 Markdown 语法、archive 移动规则、foam-query 表述、README 目录树补 ml-booklist）；各文件 `updated` 与更新记录同步。
