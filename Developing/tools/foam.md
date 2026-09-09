# Foam

> VS Code 上的 Roam 式个人知识管理扩展。**所有内容都是纯 Markdown 文件**，靠 `[[wikilink]]` 建立双向连接。

## 完整文档

主文档见 [[foam-knowledge-base-guide]] —— 包含安装、配置、目录结构、工作流、与 Obsidian 对比、FAQ。

## 一句话总结

> **Foam = VS Code + Markdown + Roam 思想**

## 核心特性速查

- **[[wikilink]]** —— 双向链接，引用不存在的笔记会自动标记
- **Backlinks** —— 切换 Markdown 预览（`Ctrl+K V`）即可看到反向链接
- **Graph** —— `Ctrl+Shift+P` → `Foam: Open Graph`，本地浏览器看图谱
- **Daily Notes** —— 每日自动生成/打开
- **F2 自动重命名** —— 重命名笔记时自动更新所有引用

## 相关链接

- [[tools]] —— 顶层工具索引（含 VS Code 快捷键）
- [[markdown_dev]] —— Markdown 写作环境配置（Foam 强依赖的 Markdown 工具链）
- [[vscode]] —— VS Code 基础与插件清单
- [[README]] —— 仓库结构总览

## 与本仓库的集成

本仓库 `D:\notes\myNotes` 完全可以作为 Foam 知识库使用：

1. 在 VS Code 打开本目录：`code .`
2. 安装 [Foam 扩展](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode)
3. `Ctrl+Shift+P` → `Foam: Open Graph` 即可看到所有笔记的关系图

## 推荐搭配扩展

- Markdown All in One
- Markdown Preview Enhanced
- Paste Image
- Code Spell Checker

详见 [[foam-knowledge-base-guide#9-搭配扩展推荐]]。
