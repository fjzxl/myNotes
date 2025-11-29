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

zen mode：ctrl+k z
ctrl+,
ctrl+B
ctrl+shift+p或F1
ctrl+p 文件跳转
ctrl+tab
ctrl+shift+tab
ctrl+shift+p snippets
ctrl+shift+o 跳转到文件中的符号
ctrl+g 跳转到文件中的某一行
ctrl+\\ 将当前编辑器分为两个
按住alt同时单击资源管理器的文件
当打开多个编辑器，可以通过ctrl+1，2，3，4来在不同窗口切换
ctrl+shift+\\ 在匹配括号之间进行跳转
ctrl+shift+N 新建一个窗口
ctrl+W 关闭当前窗口
ctrl+x 剪切当前行
ctrl+c 复制当前行
alt+↑/↓ 把当前行的内容向上或向下复制
ctrl+shift+k 删除当前行
F12 跳转到定义
alt+F12 在当前页查看定义
shift+F12 查看引用
shift+alt+F12 查看一个符号的所有引用
ctrl+F12 跳转到一个符号的相应实现
F2 重命名符号
ctrl+. 快速修复
F11 切换全屏模式
ctrl+N 新建文件
ctrl+O 打开文件
ctrl+shift+O 跳转到文件中的不同符号
ctrl+T 查看工作区中的所有符号
ctrl+\`打开终端
ctrl+alt+click 可以把定义所在的文件在另一侧打开


### 多光标
alt+click：按住alt键，然后单击鼠标右键，就能增加一个新的光标
ctrl+alt+down：在当前光标下方新增一个光标
ctrl+alt+up：在当前光标上方新增一个光标
ctrl+D：第一次按下ctrl+d，会选择当前光标处的单词。再按一次ctrl+d，会在下一个相同单词的位置添加一个新的光标。
ctrl+shift+L：会在当前光标处的单词所有出现的位置，都添加新的光标。

列选择：shift+alt，然后把光标拖至右下角，完成了对文字的列选择。

当焦点在集成终端时，不同系统下的复制与粘贴快捷键是不同的
Linux：ctrl+shift+c和ctrl+shift+v
Windows: ctrl+c和ctrl+v

文件导航
ctrl+tab：就能看到所有打开的文件/
alt+left/right：可以在不同的编辑位置进行跳转。

错误与警告
ctrl+shift+M 调出PROBLEMS面板，显示所有的错误和警告
F8或shift+F8 在当前文件的错误和警告之间循环跳转

自定义snippets

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

