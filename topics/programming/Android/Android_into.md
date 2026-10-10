---
title: Android 入门
tags:
  - programming
  - android
created: 2026-09-10
updated: 2026-10-10
---
# Android 入门

> 目标：建立 Android 开发的整体图景——平台是什么、应用由什么组成、怎么跑起第一个项目。实操记录基于 Ubuntu + Android Studio。

## 1. 平台概览

Android 是基于 Linux 内核的移动操作系统，应用层开发几乎都跑在 **Java/Kotlin 虚拟机（ART）** 上。自下而上分四层：

| 层 | 内容 | 开发者接触度 |
|----|------|------------|
| Linux 内核 | 驱动、进程/内存管理 | 几乎不碰（NDK/系统开发除外） |
| HAL / 原生库 | 相机、音频、OpenGL 等 C/C++ 库 | 偶尔通过 API 间接使用 |
| Android Runtime + 应用框架 | ART、四大组件、窗口、通知等系统服务 | **日常开发的主战场** |
| 应用层 | 自己写的 App | 全部 |

**开发语言**：新项目首选 **Kotlin**（Google 官方首选，语法现代、空安全）；Java 生态存量巨大依然完全可用。本文记录用的是 Java。

## 2. 应用由什么组成：四大组件

所有 Android 应用都是四大组件的组装，理解它们就理解了 Android 应用模型：

| 组件 | 是什么 | 典型场景 | 生命周期特点 |
|------|--------|---------|-------------|
| **Activity** | 一屏界面 | 登录页、设置页 | 用户可见/交互时活动；返回栈管理 |
| **Service** | 后台长任务 | 播放音乐、下载 | 无界面；前后台限制多 |
| **BroadcastReceiver** | 系统广播的接收器 | 监听开机、网络变化 | 收到即短命执行，不做长活 |
| **ContentProvider** | 跨应用数据接口 | 通讯录、相册供他 App 查询 | 标准化 CRUD 接口 |

组件需要在 **AndroidManifest.xml** 里**注册**才生效——这是 Android 与桌面程序的一大差异：系统通过 Manifest 知道你的应用有什么。

## 3. 开发环境：安装 Android Studio

Ubuntu 下：官网下载压缩包 → 解压 → 运行 `studio.sh`，一路 next 即可（首次会自动下载 SDK 平台与构建工具）。注意事项：

- 需要先装 JDK（新版 AS 一般自带 JetBrains Runtime，无需另配）。
- SDK 目录默认在 `~/Android/Sdk`；命令行工具要用到时把它加进 PATH。
- 模拟器需要 KVM 加速：确认 `egrep -c '(vmx|svm)' /proc/cpuinfo` 结果大于 0。

## 4. 第一个项目

新版 Android Studio 创建项目时选择 **No Activity**（空壳），然后可以选 Java 语言；再手动新建 Activity，选择 **Empty Views Activity** 模板。

为什么是"Empty **Views** Activity"：新版 Android 默认 UI 工具包是 **Jetpack Compose**（声明式 UI，Kotlin 专属，类似前端框架的写法），而传统方案是 **View 体系**（XML 布局 + Java/Kotlin 代码操作）。两条路线：

| | View 体系（传统） | Jetpack Compose（新） |
|---|---|---|
| UI 写法 | XML 布局 + `findViewById` / DataBinding | Kotlin 声明式函数（`@Composable`） |
| 语言 | Java / Kotlin | 仅 Kotlin |
| 学习资料 | 存量巨大 | 官方主推，新项目趋势 |

入门建议：用 Java 学就先走 View 体系把概念（生命周期、Intent、布局）跑通；之后转 Kotlin + Compose 的迁移成本主要在语法，不在概念。

## 5. AndroidManifest：主 Activity 声明

新建的 `MainActivity` 要在 `AndroidManifest.xml` 中声明为**主入口**：

```xml
<activity
    android:name=".MainActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />

        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

`<action android:name="android.intent.action.MAIN" />` 和 `<category android:name="android.intent.category.LAUNCHER" />` 表示 MainActivity 是这个项目的**主 Activity**——应用启动时首先启动的就是这个 Activity。

要点：

- 两者成对出现缺一不可：MAIN 说"我是入口"，LAUNCHER 说"我要出现在启动器（桌面图标）里"。
- `android:exported="true"`：允许被应用外启动。带 intent-filter 的入口 Activity 必须显式声明（Android 12 起强制）。
- `.MainActivity` 是包名的相对写法，等价于完整类名。

## 6. 项目结构速览

```
app/
├── src/main/
│   ├── java/…/MainActivity.java   # 代码
│   ├── res/
│   │   ├── layout/activity_main.xml  # 布局（View 体系）
│   │   ├── values/strings.xml        # 文案等资源
│   │   └── drawable/、mipmap/        # 图片资源
│   └── AndroidManifest.xml          # 应用清单（组件注册、权限）
├── build.gradle(.kts)              # 模块级构建配置与依赖
build.gradle / settings.gradle      # 项目级构建配置
```

资源通过 `R` 类引用（`R.layout.activity_main`、`R.string.app_name`），构建系统（Gradle）自动生成。

## 7. 学习路线建议

1. 跑通第一个项目（本篇）＋ 理解 Manifest
2. Activity 生命周期（onCreate → onStart → onResume…）与 Intent 跳转传参
3. 常用布局与控件（View 体系）或 Compose 基础
4. RecyclerView（列表，面试必问）与 Fragment
5. 网络请求（Retrofit）+ 数据持久化（Room/DataStore）
6. 做一个完整小应用（记账/待办），发布或侧载到真机

## 相关链接

- [[topics/programming/Java/spring/spring_intro]] —— Java 服务端生态对照
- [[topics/programming/Web/javascript]] —— 声明式 UI 思想在 Compose 中的对应
- [[notes/MOC - programming]] —— 编程知识地图
