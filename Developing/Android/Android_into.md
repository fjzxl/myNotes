# Android

## 安装Android Studio

Ubunut下
解压然后next即可

## 第一个项目

新版Android Studio选择创建 No Activity,可以选择Java语言。
然后新建Activity选择Empty Views Activity。
新版android使用了Jetpack Compose。

在Android-Manifest.xml中

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

\<action android:name="android.intent.action.MAIN" />和\<category android:name="android.intent.category.LAUNCHER" />表示MainAcitivity是这个项目的主Activity，首先启动的就算这个Activity。
