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

> 每日笔记模板。基于 [Journal](../journal/README.md) 工作流。

## 🎯 Today's Goals

- [ ]
- [ ]
- [ ]

## 🎌 日语过关卡

> 判定标准：✅ 过关 = 当日自测错 ≤1；🔶 保底 = ≥5 分钟复习即算打卡；❌ 未过 = 错 ≥2，明日优先复测。错项累计 ≥3 次的，同步到[学习计划](../topics/languages/japanese/kana-plan.md)的错项登记。非日语学习日可删除本区块。

| 项目 | 自测内容 / 链接 | 今日结果 |
|:---|:---|:---|
| 自测 · 认读 | （当期认读材料链接） | 错 ____ 个（错项：____） |
| 自测 · 听写 | （当期听写材料 / 音频来源） | 错 ____ 个（错项：____） |
| 自测 · 默写 | （当期默写材料链接） | 错 ____ 个（错项：____） |
| 自测 · 例词通读 | （当期例词 / 朗读材料链接） | 错 ____ 个（错项：____） |

- [ ] 复习打卡：当期复习材料（如[五十音闪卡](../topics/languages/japanese/kana-cards.md)到期卡；≥5 分钟保底也算），用时 ____ 分钟
- **今日判定**（填一个）：✅ 过关（错 ≤1）／ 🔶 保底 ／ ❌ 未过（错 ≥2，明日复测：____）

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

> 主动建立链接，让笔记之间形成网络；用相对路径 Markdown 链接（如 `[五十音计划](../topics/languages/japanese/kana-plan.md)`），不要用 wikilink

- [示例：五十音计划](../topics/languages/japanese/kana-plan.md) —— 换成今日相关笔记
-

## ✅ Tomorrow's Plan

- [ ]
- [ ]

---

> `Foam: Open Daily Note` 会用本模板自动在 `journal/daily/` 创建当天笔记（路径由上方 `foam_template.filepath` 决定，`${FOAM_DATE_*}` 变量自动展开）。
> 手动复制本文件时，把 `${FOAM_DATE_*}` 替换为当天日期即可。
> 模板文件位置：`templates/daily-note.md`
