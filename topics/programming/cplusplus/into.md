---
title: C 入门：从源码到可执行文件
tags:
  - programming
  - cpp
created: 2026-09-10
updated: 2026-10-10
---
# C 入门：从源码到可执行文件

> C/C++ 学习的第一课不是语法，而是搞清楚**源文件是怎么变成可执行文件的**。理解这条流水线，后面遇到链接错误、undefined reference、头文件包含问题都有据可查。

## 1. 编译四阶段

```
hello.c → [预处理器 cpp] → hello.i → [编译器 cc1] → hello.s → [汇编器 as] → hello.o → [链接器 ld] → hello
          (文本替换)                 (生成汇编)               (生成机器码)                (拼装符号)
```

| 阶段 | 做什么 | 产物 | gcc 停在该阶段的选项 |
|------|--------|------|---------------------|
| 预处理（Preprocess） | 展开 `#include`、替换宏 `#define`、处理条件编译 `#if` | `.i`（仍是 C 文本） | `gcc -E hello.c -o hello.i` |
| 编译（Compile） | 词法/语法分析、优化，翻译成汇编 | `.s` | `gcc -S hello.c` |
| 汇编（Assemble） | 汇编翻译成机器指令，得到**目标文件** | `.o` | `gcc -c hello.c` |
| 链接（Link） | 合并多个 `.o` 与库，解析符号地址 | 可执行文件 | `gcc hello.o -o hello`（默认全做） |

验证产物类型：`file hello.i`（文本）、`file hello.o`（ELF relocatable）、`file hello`（ELF executable）。

**为什么要知道这些**：

- 报 `undefined reference to 'foo'` → 链接阶段问题：没提供定义所在的目标文件/库，或函数签名不一致。
- 报 `No such file or directory`（`#include`）→ 预处理阶段问题：头文件搜索路径不对。
- 宏展开的结果不符合预期 → 用 `gcc -E` 直接看展开后的文本，最快定位。
- 多文件项目改了 `a.c` 只需 `gcc -c a.c` 再重新链接，不必重编全部——这就是 make 存在的意义。

## 2. gcc 常用选项

| 选项 | 作用 |
|------|------|
| `-o <name>` | 指定输出文件名 |
| `-Wall -Wextra` | 打开常用警告（**默认应常开**） |
| `-g` | 带调试信息，配合 gdb / VS Code 调试 |
| `-O0 / -O2` | 不优化 / 常用优化（学习期用 `-O0`，发布用 `-O2`） |
| `-I<dir>` | 追加头文件搜索目录 |
| `-L<dir> -l<name>` | 追加库目录 / 链接库（`-lm` 链数学库） |
| `-std=c17` | 指定语言标准（C 用 c17，C++ 编译器是 `g++`，如 `-std=c++17`） |

注意：`.c` 文件用 `gcc`，`.cpp` 用 `g++`；混链 C++ 时最后一步链接用 `g++`（它会自动带上 C++ 标准库）。

## 3. make：增量构建

项目一大，手动敲命令既慢又容易漏。make 根据**文件时间戳**判断哪些目标需要重建，只做必要的事。

```makefile
# Makefile —— 注意：命令行必须以 Tab 开头（不是空格）
CC      = gcc
CFLAGS  = -Wall -Wextra -g -std=c17
TARGET  = app
OBJS    = main.o utils.o

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
```

- 规则三要素：`目标: 依赖` + 命令行。依赖比目标新（或目标不存在）才执行命令。
- `%.o: %.c` 是模式规则；`$<` = 第一个依赖，`$@` = 目标。
- 常用命令：`make`（构建第一个目标）、`make clean`、`make -j4`（并行构建）。
- 排错第一反应：报 `missing separator` → 十有八九是用了空格代替 Tab。

## 4. 第一个程序的结构

```c
#include <stdio.h>   /* 预处理指令：把标准输入输出的声明搬进来 */

int main(void) {     /* 程序入口，返回 int 作为进程退出码 */
    printf("hello, c\n");
    return 0;        /* 0 表示成功 */
}
```

编译运行：`gcc -Wall main.c -o main && ./main`；查看退出码 `echo $?`。

## 5. 学习路线建议

1. 本篇：构建流水线 + gcc + make（工具面）
2. 语言核心：类型、运算符、控制流、函数、数组与字符串
3. 指针与内存模型（C 的灵魂，画内存图学）
4. 结构体、文件 I/O、多文件组织（头文件怎么写）
5. 动手项目：简易 shell / 数据结构实现

## 相关链接

- [[topics/programming/cplusplus/vscodec]] —— 用 VS Code 写 C/C++：环境配置、构建与调试
- [[topics/programming/Linux/linux-kernel-4.9-build]] —— 大型 C 项目的构建实例（内核编译）
- [[notes/MOC - programming]] —— 编程知识地图
