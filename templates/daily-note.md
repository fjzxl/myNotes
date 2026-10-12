---
foam_template:
  name: Daily Note
  description: 每日笔记（Foam: Open Daily Note 自动创建到 journal/daily/YYYY-MM-DD.md）
  filepath: "/journal/daily/${FOAM_DATE_YEAR}-${FOAM_DATE_MONTH}-${FOAM_DATE_DATE}.md"
---
title: "${FOAM_DATE_YEAR}-${FOAM_DATE_MONTH}-${FOAM_DATE_DATE}"
tags:
  - daily-note
date: "${FOAM_DATE_YEAR}-${FOAM_DATE_MONTH}-${FOAM_DATE_DATE}"
day-of-week: ${FOAM_DATE_DAY_NAME}
---

# ${FOAM_DATE_YEAR}-${FOAM_DATE_MONTH}-${FOAM_DATE_DATE}（${FOAM_DATE_DAY_NAME}）

> 每日笔记模板。基于 [[journal/README|Journal]] 工作流。

## 🎯 Today's Goals

- [ ]
- [ ]
- [ ]

## 📝 Today's Log

### 上午
-

### 下午
-

### 晚上
-

## 💡 Insights & Ideas

-

## 🐛 Problems & Solutions

### Problem
-

### Solution
-

## 📚 Today's Links

> 主动建立 wikilink，让笔记之间形成网络

- [[]]
- [[]]

## ✅ Tomorrow's Plan

- [ ]
- [ ]

---

> `Foam: Open Daily Note` 会用本模板自动在 `journal/daily/` 创建当天笔记（路径由上方 `foam_template.filepath` 决定，`${FOAM_DATE_*}` 变量自动展开）。
> 手动复制本文件时，把 `${FOAM_DATE_*}` 替换为当天日期即可。
> 模板文件位置：`templates/daily-note.md`
