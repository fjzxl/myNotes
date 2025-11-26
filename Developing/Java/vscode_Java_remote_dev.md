# 远程Java devlepment

- [远程Java devlepment](#远程java-devlepment)
  - [download Java and set up environment in remote server](#download-java-and-set-up-environment-in-remote-server)
  - [donwload maven and setup environment](#donwload-maven-and-setup-environment)
  - [vscode setup](#vscode-setup)
    - [首先在本地机器安装Remote Development](#首先在本地机器安装remote-development)
    - [配置ssh remote](#配置ssh-remote)
    - [在远程服务器安装插件](#在远程服务器安装插件)
    - [远程服务器配置](#远程服务器配置)
  - [download tomcat and unzip](#download-tomcat-and-unzip)
    - [目录结构](#目录结构)
  - [安装插件](#安装插件)

## download Java and set up environment in remote server

参考本地配置，在远程服务器配置
[java 环境下载配置](/Developing/Java/vscode_Java_dev.md#download-java-and-set-up-environment)

## donwload maven and setup environment

参考本地配置，在远程服务器配置
[maven 环境配置](/Developing/Java/vscode_Java_dev.md#donwload-maven-and-setup-environment)

## vscode setup

### 首先在本地机器安装Remote Development

![安装 Remote Development 插件](/Source/pics/developing/remote_development_plugin.png)

### 配置ssh remote

![配置 ssh remote](/Source//pics/developing/add_remote.png)

打开remote
![打开 remote](/Source/pics/developing/open_remote.png)

等待remote vscode server安装
![等待 remote scode server安装](/Source/pics/developing/download_vscode_server.png)

### 在远程服务器安装插件

![在远程服务器安装插件](/Source/pics/developing/add_plugins_for_ssh.png)

### 远程服务器配置

![远程服务器配置](/Source/pics/developing/remote_settings.png)

## download tomcat and unzip

下载tomcat并解压即可

在bin目录下启动startup.sh即可

配置在conf中，其中server.xml可以配置端口等信息。如果出现乱码，可以修改logging.properties

### 目录结构

- bin：用来存放Tomcat服务器的可执行程序，主要有两大类，一类是以.sh结尾的（linux命令），另一类是以.bat结尾的（windows命令）。比如：启动和关闭 tomcat 的 bat 文件
- conf：用来存放Tomcat服务器的配置文件
  - server.xml可以设置端口号、设置域名或IP、默认加载的项目、请求编码、最大线程并发数等
  - web.xml可以设置tomcat支持的文件类型
  - context.xml可以用来配置数据源之类的
  - tomcat-users.xml用来配置管理tomcat的用户与权限
- lib：主要用来存放tomcat运行需要加载的jar包
- logs：用来存放Tomcat服务器运行时输出的日志信息
- temp：用来存放Tomcat服务器运行时产生的临时数据
- webapps：用来存放Tomcat服务器部署的工程，比如tomcat中自带一些项目。比如我们访问的 <http://localhost:8080/> 对应的页面，就是tomcat自带的ROOT项目。当然，可以项目放在webapps下。
- work：是Tomcat工作时的目录，用来存放Tomcat运行时jsp被访问后翻译为Servlet的源码和编译后的文件

## 安装插件

