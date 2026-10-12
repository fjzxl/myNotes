---
title: vscode
tags:
  - tools
created: 2026-09-10
updated: 2026-10-11
---
# vscode

Language Server提供了诸如自动补全、定义跳转、代码格式化等与编程语言相关的功能。
Language Server Protocol(LSP)是编辑器/IDE与语言服务器之间的一种协议，通过JSON-RPC传输。
Debug Adapter Protocol基于JSON的协议，抽象了开发工具与调试工具之间的通信。

Ubuntu下将vscode作为默认editor

```shell
xdg-mime default code.desktop text/plain
```

```shell
sudo update-alternatives --set editor /usr/bin/code
```

## 插件

material icon theme、one dark pro、prettier、vscode-pigments、auto rename tag

## 设置

visual studio code的所有内容几乎都可以被设置。

**两种不同范围的设置。**

- 用户设置(User Settings)：这是一个全局范围的设置，会应用到所有的visual studio code实例中。
- 工作区设置(Workspace Settings)：设置保存在相应的工作区，只会对相应的工作区生效。工作区设置会覆盖用户设置。

**用户设置的settings.json位置**

- windows："%APPDATA%\Code\User\settings.json"
- linux: "$HOME/.config/Code/User/settings.json"

**语言特定的设定** \
ctrl+shift+p打开命令面板输入Preferences:Configure Language Specific Settings

**只能通过用户设置进行定义** \
git.path
terminal.integrated.shell.linux
terminal.integrated.shellArgs.linux
terminal.integrated.shell.osx
terminal.integrated.shellArgs.osx
terminal.integrated.shell.windows
terminal.integrated.shellArgs.windows
terminal.external.linuxExec
terminal.external.osxExec
terminal.external.windowsExec

## 快捷键

以下均为 Windows/Linux 默认键位（macOS 大致对应把 Ctrl 换成 Cmd）。命令面板（ctrl+shift+p 或 F1）能执行 VS Code 的一切命令，记不住的快捷键都可以在这里输入命令名完成。

### 命令面板与快速跳转

ctrl+p 文件跳转（按文件名快速打开）
ctrl+shift+o 跳转到文件中的符号
ctrl+T 查看工作区中的所有符号
ctrl+g 跳转到文件中的某一行
ctrl+shift+\ 在匹配括号之间进行跳转
alt+left/right 在不同的编辑位置（跳转历史）之间后退/前进
ctrl+tab / ctrl+shift+tab 在所有打开的文件之间循环切换

ctrl+p 打开的输入框还支持其它前缀，直接输入即可切换模式：

| 前缀 | 作用           | 示例             |
| ---- | -------------- | ---------------- |
| 无   | 按文件名打开   | kana.md          |
| :    | 跳到某一行     | :128             |
| @    | 当前文件的符号 | @快捷键          |
| #    | 工作区符号     | #多光标          |
| >    | 执行命令       | >toggle zen mode |

### 编辑

ctrl+x 剪切当前行（未选中内容时）
ctrl+c 复制当前行（未选中内容时）
alt+↑/↓ 把当前行向上或向下移动；shift+alt+↑/↓ 向上/向下复制当前行
ctrl+shift+k 删除当前行
ctrl+enter 在下方插入一个新行（光标停在原地）；ctrl+shift+enter 在上方插入
ctrl+/ 切换行注释；shift+alt+A 切换块注释
ctrl+] / ctrl+[ 增加/减少缩进
ctrl+L 选中当前行，再按一次向下扩展一行
shift+alt+→ / shift+alt+← 智能扩展/收缩选中范围
ctrl+Home / ctrl+End 跳到文件开头/结尾
alt+Z 切换自动换行
shift+alt+F 格式化整个文档；ctrl+k ctrl+f 只格式化选中部分
ctrl+Z / ctrl+Y 撤销 / 重做

### 查找与替换

ctrl+F 当前文件查找；ctrl+H 当前文件替换
ctrl+shift+F 跨文件搜索；ctrl+shift+H 跨文件替换
F3 / shift+F3 查找下一个 / 上一个
查找面板内：alt+C / alt+R / alt+W 分别切换区分大小写、正则表达式、全字匹配
alt+Enter 选中所有匹配项（进入多光标状态，配合批量编辑）

### 多光标

alt+click：按住alt键，然后单击鼠标左键，就能增加一个新的光标
ctrl+alt+down：在当前光标下方新增一个光标
ctrl+alt+up：在当前光标上方新增一个光标
ctrl+D：第一次按下ctrl+d，会选择当前光标处的单词。再按一次ctrl+d，会在下一个相同单词的位置添加一个新的光标。
ctrl+shift+L：会在当前光标处的单词所有出现的位置，都添加新的光标。
ctrl+U 撤销上一次光标操作（多光标加多了、加错了，按它逐步回退）

列选择：shift+alt，然后把光标拖至右下角，完成了对文字的列选择。也可以用 ctrl+shift+alt+方向键 进行纯键盘的列选择。

### 代码导航与重构

F12 跳转到定义
alt+F12 在当前页查看定义（peek）
ctrl+alt+click 可以把定义所在的文件在另一侧打开
shift+F12 查看引用；shift+alt+F12 查看一个符号的所有引用
ctrl+F12 跳转到一个符号的相应实现
F2 重命名符号
ctrl+. 快速修复

### 界面、窗口与面板

ctrl+B 显示/隐藏侧边栏
ctrl+J 显示/隐藏底部面板
ctrl+, 打开设置
F11 切换全屏模式；ctrl+k z 进入/退出 zen mode
ctrl+shift+E / ctrl+shift+F / ctrl+shift+G / ctrl+shift+X / ctrl+shift+D 分别聚焦资源管理器、搜索、源代码管理、扩展、调试面板
ctrl+k ctrl+t 切换颜色主题；ctrl+k ctrl+s 打开键盘快捷键设置

### 编辑器与标签页

ctrl+\ 将当前编辑器分为两个
当打开多个编辑器，可以通过ctrl+1，2，3，4来在不同窗口切换
按住alt同时单击资源管理器的文件，可在侧边打开该文件
ctrl+N 新建文件；ctrl+O 打开文件
ctrl+shift+N 新建一个窗口
ctrl+W 关闭当前编辑器（标签页）；关闭整个窗口用 alt+F4
ctrl+shift+T 重新打开刚关闭的编辑器
ctrl+PgUp / ctrl+PgDn 切换到上一个/下一个标签页
ctrl+k w 关闭所有打开的编辑器

### 错误与警告

ctrl+shift+M 调出PROBLEMS面板，显示所有的错误和警告
F8或shift+F8 在当前文件的错误和警告之间循环跳转

### 调试

F5 启动/继续调试；shift+F5 停止调试
F9 切换断点
F10 单步跳过
F11 单步进入（调试时；非调试状态下 F11 是切换全屏）
shift+F11 单步跳出

### 终端

ctrl+` 打开/关闭集成终端
ctrl+shift+` 新建一个终端；ctrl+shift+5 将终端分屏
当焦点在集成终端时，不同系统下的复制与粘贴快捷键是不同的
Linux：ctrl+shift+c和ctrl+shift+v
Windows: ctrl+c和ctrl+v

### Markdown 预览

ctrl+shift+V 打开预览；ctrl+K V 在侧边打开预览，边写边看，适合本仓库的 Foam 笔记

### 实战案例

1. 批量修改当前文件中的同一个词：光标放在单词上，ctrl+D 逐个添加选中，或 ctrl+shift+L 一次全选，然后直接输入新名字。比查找替换更直观，可以边看边改。
2. 跨文件批量替换：ctrl+shift+H 打开替换面板，例如把全仓库的 `console.log` 换成 `logger.debug`，逐个确认后全部替换；只想先看看分布就按 ctrl+shift+F。
3. 安全重命名变量/函数：F2 是语义级重命名，所有引用同步更新，不会误伤字符串和注释里的同名文本。
4. 列选择统一加前缀：按住 shift+alt 向下拖出纵向光标，一次性给多行加 `//`、`- ` 或 `> ` 前缀，例如把几行普通文本变成 Markdown 列表或引用。
5. 用正则提取全部标题：ctrl+F 打开查找，alt+R 开启正则，输入 `^#+ `，alt+Enter 全选匹配，ctrl+C 复制，即得到全文标题列表，可以直接粘贴成目录。
6. 快速修掉报错：F8 跳到第一个错误，ctrl+. 查看快速修复（自动导包、拼写纠正等），应用后再按 F8 去下一个。
7. 光标加多了不用重来：按 ctrl+U 逐步撤销多余的光标，保留已经改好的部分。

自定义snippets：ctrl+shift+p 输入 snippets（Preferences: Configure User Snippets）

## Task

Task可以被用来运行脚本或启动一个进程。Task被配置在.vscode文件夹的tasks.json文件中。
Task只能被配置在有文件夹打开的项目中。

在顶部菜单栏中选择Terminal->Configure Tasks。然后选择Create tasks.json file from template，选择others。
task定义
label：在用户界面展示的Task标签
type：Task的类型，分为shell和process

- shell：作为shell命令运行
- process：作为进程运行
command：真正执行的命令
windows：Windows中的特定属性。相应的属性会在Windows中覆盖默认的属性定义。
group：定义Task属于哪一个组。
presentation：定义用户界面如何处理Task的输出。always表示集成终端在Task每次运行时都会展示其输出，new表示Task每次运行后都会创建一个新的集成终端并输出。
options：定义cwd(当前工作目录)、env(环境变量)和shell值。
runOptions：定义Task何时运行及如何运行。

预定义变量

| 变量名                     | 含义                                              |
| -------------------------- | ------------------------------------------------- |
| ${workspaceFolder}         | 在Visual Studio Code中打开的文件夹的完整路径      |
| ${workspaceFolderBasename} | 在Visual Studio Code中打开的文件夹名              |
| ${file}                    | 当前打开的文件的完整路径                          |
| ${relativeFile}            | 当前打开的文件相对workspaceFolder的路径           |
| ${relativeFileDirname}     | 当前打开的文件的文件夹的相对workspaceFolder的路径 |
| ${fileBasename}            | 当前打开的文件的文件名                            |
| ${fileBasenameNoExtension} | 当前打开的文件的文件名，不含扩展名                |
| ${fileDirname}             | 当前打开的文件的文件夹的完整路径                  |
| ${fileExtname}             | 当前打开的文件的扩展名                            |
| ${cwd}                     | Task启动时的工作目录                              |
| ${lineNumber}              | 当前光标所在的行号                                |
| ${selectedText}            | 当前打开的文件中选中的文本                        |
| ${execPath}                | Visual Studio Code可执行文件的完整路径            |
| ${defaultBuildTask}        | 默认的Build Task的名字                            |

环境变量 ${env: Name}

launch.json
launch.json定义了调试器需要的配置。

| 属性                   | 含义                                                                         | 必须 |
| ---------------------- | ---------------------------------------------------------------------------- | ---- |
| type                   | 调试器类型                                                                   | 必须 |
| request                | 调试的模式，launch，启动程序并调试。attach，将程序附加到一个正在运行的程序中 | 必须 |
| name                   | 调试配置的名字                                                               | 必须 |
| presentation           | 使用order、group和hidden属性来定义调试配置的显示。                           | 可选 |
| preLaunchTask          | 定义在调试之前要运行的任务                                                   | 可选 |
| postDebugTask          | 定义在调试结束时运行的任务                                                   | 可选 |
| internalConsoleOptions | 定义调试控制台的显示                                                         | 可选 |
| serverReadyAction      | 设置在调试时自动在浏览器中打开URL                                            | 可选 |

大多数调试器支持的属性
program：要运行的可执行文件或源代码的路径。
args：要传递给program的参数。
env：环境变量。
cwd：调试器的工作目录。默认值是${workspaceFolder}
port：要附加到的进程的端口。
stopOnEntry：是否在程序人口进行断点。
console：指定程序输出的位置

- internalConsole：Visual Studio Code的调试控制台。
- integratedTerminal：Visual Studio Code的集成终端
- externalTerminal：系统的终端。

多目标调试
通过compound属性可以配置多目标调试

调试jupyter notebook
调试jupyter notebook，首先把jupyter notebook文件导出为python。然后调试python文件。
