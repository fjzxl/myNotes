---
title: VS Code C/C++ 环境配置
tags:
  - programming
  - cpp
created: 2026-09-10
updated: 2026-10-10
---
# VS Code C/C++ 环境配置

> 目标：在 VS Code 里获得 C/C++ 的**编辑（跳转/补全）+ 一键构建 + 断点调试**三件套。前提：先装好工具链（`gcc`/`g++`，Windows 用 MinGW-w64 或 MSYS2，或直接在 WSL/远程 Linux 里开发），并用 `gcc --version` 验证可用。构建原理见 [[topics/programming/cplusplus/into|C 入门]]。

## 1. 扩展选择

| 扩展 | 特点 | 适合 |
|------|------|------|
| **C/C++**（ms-vscode.cpptools，微软官方） | 自带调试器（cppdbg），配置简单，补全够用 | 入门首选 |
| clangd | 补全/跳转/重构更快更准，走 `compile_commands.json` | 大型项目进阶 |

入门建议：只装 **C/C++** 一个，够用且少踩坑；以后项目大了再换 clangd（注意它与 cpptools 的补全会打架，需禁用后者智能感知）。

## 2. 三层配置各管什么

```
.vscode/
├── tasks.json      # 构建任务：按什么命令编译（Ctrl+Shift+B 触发）
├── launch.json     # 调试配置：怎么运行 + 挂调试器（F5 触发）
└── c_cpp_properties.json  # 智能感知：头文件路径、C 标准（只影响编辑器，不影响编译）
```

**关键认知**：智能感知和真正编译是两条线。`c_cpp_properties.json` 配错了只影响红线误报；`tasks.json` 里的命令才是真编译。头文件找不到时先分清是哪条线的问题。

## 3. tasks.json：一键构建

命令面板（`Ctrl+Shift+P`）→ *Tasks: Configure Task* → *使用模板创建* → 选 g++/gcc 生成骨架，改成：

```jsonc
{
  // tasks.json —— JSONC 格式，允许注释
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build C",
      "type": "shell",
      "command": "gcc",
      "args": [
        "-Wall", "-Wextra", "-g", "-std=c17",
        "${file}",
        "-o", "${fileDirname}/${fileBasenameNoExtension}"
      ],
      "group": { "kind": "build", "isDefault": true },  // Ctrl+Shift+B 直接触发
      "problemMatcher": ["$gcc"]   // 把编译报错解析成可点击的问题列表
    }
  ]
}
```

- `"isDefault": true` 让 `Ctrl+Shift+B` 免选择直接构建当前文件。
- `$gcc` problemMatcher 把 stderr 里的文件:行号变成点击可跳转——排错效率的关键。
- 多文件项目：把 `${file}` 换成 `*.c` 通配或写成 make 任务（`"command": "make"`）。

## 4. launch.json：断点调试

先确保构建带 `-g`，然后 F5 → 选 *C++ (GDB/LLDB)*：

```jsonc
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "调试当前文件",
      "type": "cppdbg",
      "request": "launch",
      "program": "${fileDirname}/${fileBasenameNoExtension}",  // 调试的可执行文件（不是源码！）
      "args": [],                    // 命令行参数写这里
      "stopAtEntry": false,
      "cwd": "${fileDirname}",
      "environment": [],
      "externalConsole": false,      // true 会弹独立终端窗口
      "MIMode": "gdb"                // Windows/MinGW 也是 gdb；macOS 换 lldb
    }
  ]
}
```

调试器快捷键：`F9` 断点、`F5` 继续、`F10` 单步跳过（不进函数）、`F11` 步入（进函数）、`Shift+F11` 跳出。左侧 WATCH 面板可随时加表达式；DEBUG CONSOLE 里 `p arr@5` 能把数组按 5 个元素展开（gdb 语法）。

## 5. c_cpp_properties.json：智能感知

`Ctrl+Shift+P` → *C/C++: Edit Configurations (UI)* 图形化配置，等价于：

```jsonc
{
  "configurations": [
    {
      "name": "Linux",
      "includePath": ["${workspaceFolder}/**", "/usr/include"],
      "compilerPath": "/usr/bin/gcc",
      "cStandard": "c17",
      "intelliSenseMode": "gcc-x64"
    }
  ]
}
```

includePath 加自建头文件目录后，`#include "myheader.h"` 不再标红。

## 6. 常见问题速查

| 现象 | 原因与解法 |
|------|-----------|
| 终端里 `gcc` 找不到 | 工具链不在 PATH；Windows 常见，把 MinGW 的 `bin` 加入系统 PATH 后**重启 VS Code** |
| 能跑但断点是空心圆 | 编译没带 `-g`，或 `program` 路径指向了旧的可执行文件 |
| 头文件标红但能编译 | 智能感知配置问题：`includePath` 补上目录即可，不影响构建 |
| 调试一闪而过 | `program` 指向了源文件而不是可执行文件 |
| 中文乱码 | Windows 控制台默认 GBK：源码存 UTF-8 时加 `system("chcp 65001")` 或统一用 GBK 编码源文件 |

## 相关链接

- [[topics/programming/cplusplus/into]] —— 编译四阶段与 gcc/make（本篇的前置）
- [[topics/tools/VSCode]] —— VS Code 基础与插件清单
- [[notes/MOC - programming]] —— 编程知识地图
