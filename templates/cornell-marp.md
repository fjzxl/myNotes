---
marp: true
theme: default
paginate: true
size: 16:9
title: 康奈尔笔记 · Marp 版
---

<!-- _class: lead -->

# 📒 Cornell × Marp

**康奈尔笔记的幻灯片版**

把笔记做成可演示的幻灯片，保留两栏版式

📚 配套：[[cornell-note]]、[[../../topics/tools/marp-guide]]

---

## ✨ 设计思路

传统康奈尔笔记是**纸面两栏**版式（左 30% 线索 / 右 70% 笔记 / 底总结）。

幻灯片版本：
- 整页用 **CSS Grid 30/70** 分栏
- 顶部一行作为"标题"
- 每张幻灯片 = 一个康奈尔"行"
- 总结**单独成页**（用 `_class` 切换布局）

---

## 🎨 核心 CSS

```css
section.cornell-row {
  display: grid;
  grid-template-columns: 30% 70%;
  gap: 1rem;
  text-align: left;
  font-size: 22px;
}

section.cornell-row .cues {
  border-right: 2px solid #888;
  padding-right: 0.5rem;
  background: rgba(255, 165, 0, 0.05);
}

section.cornell-row .notes {
  padding-left: 0.5rem;
}

section.cornell-summary {
  text-align: left;
  background: rgba(34, 197, 94, 0.05);
  border: 2px solid #16a34a;
  border-radius: 8px;
  padding: 1rem;
}
```

---

## 📋 完整模板

复制下面内容到一个新 `.md` 文件：

````markdown
---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section.cornell-row {
    display: grid;
    grid-template-columns: 30% 70%;
    gap: 1rem;
    text-align: left;
  }
  section.cornell-row .cues {
    border-right: 2px solid #888;
    padding-right: 0.5rem;
    background: rgba(255,165,0,0.05);
  }
  section.cornell-row .notes {
    padding-left: 0.5rem;
  }
  section.cornell-summary {
    text-align: left;
    background: rgba(34,197,94,0.05);
    border: 2px solid #16a34a;
    border-radius: 8px;
    padding: 1rem;
  }
---

<!-- _class: cornell-row -->

<div class="cues">

### 🔑 线索

- 概念 1
- 概念 2
- 关键问题
- 定义
- 对比

</div>

<div class="notes">

### 📝 笔记

- 要点 1：详细展开
- 要点 2：详细展开
- 公式：`f(x) = ...`
- 例题：

  ```
  题目 → 解答
  ```

</div>

---

<!-- _class: cornell-row -->

<div class="cues">

### 🔑 线索（第二行）

- 概念 3
- 疑问

</div>

<div class="notes">

### 📝 笔记（第二行）

- ...

</div>

---

<!-- _class: cornell-summary -->

### 📋 总结（24h 内必填）

- **整页核心**：
- **关键概念**：
- **待深入**：

````

---

## 🧪 实战示例：AM-GM 不等式

下面是一个**完整可运行**的 Cornell × Marp 示例（直接复制保存为 `.md` 即可）。

````markdown
---
marp: true
theme: default
size: 16:9
paginate: true
style: |
  section.cornell-row {
    display: grid;
    grid-template-columns: 30% 70%;
    gap: 1rem;
    text-align: left;
    font-size: 20px;
  }
  section.cornell-row .cues {
    border-right: 2px solid #888;
    padding-right: 0.5rem;
    background: rgba(255,165,0,0.05);
  }
  section.cornell-row .notes {
    padding-left: 0.5rem;
  }
  section.cornell-summary {
    text-align: left;
    background: rgba(34,197,94,0.05);
    border: 2px solid #16a34a;
    border-radius: 8px;
    padding: 1rem;
    font-size: 22px;
  }
---

<!-- _class: cornell-row -->

<div class="cues">

### 🔑 线索

- **AM-GM**
- 非负实数
- 算术 ≥ 几何
- 等号条件

</div>

<div class="notes">

### 📝 AM-GM 不等式

> 对任意非负实数 $a_1, a_2, \ldots, a_n$：

$$\frac{a_1 + a_2 + \cdots + a_n}{n} \geq \sqrt[n]{a_1 a_2 \cdots a_n}$$

**等号条件**：所有 $a_i$ 相等

</div>

---

<!-- _class: cornell-row -->

<div class="cues">

### 🔑 线索

- 前向归纳
- 基例 $n=2$
- Cauchy 思路

</div>

<div class="notes">

### 📝 证明思路（前向归纳）

1. **基例 $n=2$**：$(\sqrt{a_1} - \sqrt{a_2})^2 \geq 0$
2. **前向步**：$n \to 2n$（分组）
3. **后向步**：$2^k \to 2^k - 1$（补元素）

详见：[[../../math/inequalities#均值不等式]]

</div>

---

<!-- _class: cornell-summary -->

### 📋 总结

- **核心**：算术平均 ≥ 几何平均
- **关键点**：等号当且仅当所有数相等
- **应用**：最值证明、不等式链的起点
- **配套笔记**：[[../../math/inequalities]]

````

---

## 🚀 导出

```bash
# 导 PDF
marp am-gm-cornell.md --pdf

# 导 HTML（保留交互）
marp am-gm-cornell.md --html

# 导 PPTX
marp am-gm-cornell.md --pptx
```

---

## 💡 进阶用法

### 1. 标题页用 lead 风格

```markdown
<!-- _class: lead -->

# 课程主题

## 副标题
```

### 2. 加背景图

```markdown
<!-- _backgroundColor: "#1a1a2e" -->
<!-- _color: white -->

# 章节封面
```

### 3. 分章节用大写罗马数字

```markdown
# Ⅰ. 引入

---

# Ⅱ. 主体

---

# Ⅲ. 总结
```

### 4. 加分页符（章节间）

```markdown
---

# 下一章
```

---

## ⚖️ Cornell × Marp 的适用场景

| 场景 | 用 Cornell 笔记 | 用 Cornell × Marp |
|------|---------------|------------------|
| 课堂笔记 | ✅ | ❌ 太花哨 |
| 读书笔记 | ✅ | ❌ |
| 自己复盘 | ✅ | ⚠️ 偶尔 |
| **分享给同学/汇报** | ❌ | ✅ |
| **考研复习讲解** | ❌ | ✅ |
| **会议展示** | ❌ | ✅ |

> **结论**：Cornell 笔记是"输入"，Cornell × Marp 是"输出"。

---

## 📚 相关资源

- [[cornell-note]] —— 标准康奈尔笔记模板（HTML + CSS 版）
- [[../../topics/tools/marp-guide]] —— Marp 完整使用指南
- [[../../topics/programming/Java/slides/Servlet-lifecycle]] —— Marp 幻灯片实战示例
