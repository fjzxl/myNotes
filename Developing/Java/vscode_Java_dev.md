# 本地Java devlepment

- [本地Java devlepment](#本地java-devlepment)
  - [download Java and set up environment](#download-java-and-set-up-environment)
    - [执行命令](#执行命令)
    - [更改.bashrc，配置环境变量](#更改bashrc配置环境变量)
    - [执行命令，查看是否安装成功](#执行命令查看是否安装成功)
  - [donwload maven and setup environment](#donwload-maven-and-setup-environment)
    - [更改.bashrc，配置环境变量](#更改bashrc配置环境变量-1)
    - [修改maven的conf下settings.xml设置](#修改maven的conf下settingsxml设置)
  - [vscode setup](#vscode-setup)

## download Java and set up environment

### 执行命令

```shell
tar -zxvf 
```

### 更改.bashrc，配置环境变量

```bash
export JAVA_HOME_8=/home/clarence/software/java/jdk1.8.0_451
export JAVA_HOME_21=/home/clarence/software/java/jdk-21.0.7
export JAVA_HOME=${JAVA_HOME_21}
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:${PATH}
```

### 执行命令，查看是否安装成功

```shell
java -version
```

## donwload maven and setup environment

### 更改.bashrc，配置环境变量

```bash
export M2_HOME=/home/clarence/software/maven/apache-maven-3.9.11
export MAVEN_HOME=${M2_HOME}
export MAVEN_BIN=${M2_HOME}/bin/
export PATH=${MAVEN_HOME}:${MAVEN_BIN}:${PATH}
```

### 修改maven的conf下settings.xml设置

```xml
<localRepository>/home/clarence/repos/m2</localRepository>
<mirros>
    <mirror>
      <id>aliyun</id>
      <mirrorOf>*</mirrorOf>
      <name>aliyun Maven</name>
      <url>https://maven.aliyun.com/repository/public/</url>
    </mirror>
</mirros>
```

## vscode setup

ctrl+shift+p settings

```json
{
    "editor.fontSize": 20,
    "editor.minimap.sectionHeaderFontSize": 18,
    "debug.console.fontSize": 18,
    "terminal.integrated.fontSize": 18,
    "scm.inputFontSize": 18,
    "chat.editor.fontSize": 18,
    "markdown.preview.fontSize": 18,
    "java.configuration.runtimes": [
        {
            "name": "JavaSE-21",
            "path": "/home/clarence/software/java/jdk-21.0.7",
            "default": true
        },
        {
            "name": "JavaSE-1.8",
            "path": "/home/clarence/software/java/jdk1.8.0_451",
            "default": false
        },
    ],
    "java.jdt.ls.java.home": "/home/clarence/software/java/jdk-21.0.7",
    "maven.executable.path": "/home/clarence/software/maven/apache-maven-3.9.11/bin/mvn",
    "maven.settingsFile": "/home/clarence/software/maven/apache-maven-3.9.11/conf/settings.xml",
    "java.configuration.maven.userSettings": "/home/clarence/software/maven/apache-maven-3.9.11/conf/settings.xml",
    "java.maven.downloadSources": true,
    "maven.terminal.useJavaHome": true,
    "java.configuration.maven.globalSettings": "/home/clarence/software/maven/apache-maven-3.9.11/conf/settings.xml",
}
```
