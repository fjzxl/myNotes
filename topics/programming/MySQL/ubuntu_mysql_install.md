---
title: 安装mysql
tags:
  - programming
  - programming/mysql
---
# 安装mysql

```shell
sudo apt show -a mysql-server-8.0
sudo apt install mysql-server-8.0
sudo mysql
```

## 创建数据库

```sql
CREATE DATABASE mydatabase
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;
CREATE USER username IDENTIFIED BY 'password';
GRANT all privileges ON mydatabase.* TO 'username'@'%';
FLUSH PRIVILEGES;
```

> 注：`CREATE USER username ...` 不写主机时默认创建的就是 `'username'@'%'`（任意主机可连），上面的 GRANT 已对 `'%'` 授权，**无需**再 `USE mysql; UPDATE user ...` 改 Host。直接改授权表是 MySQL 8 之前的旧教程做法，官方建议只用 `CREATE USER`/`GRANT`/`ALTER USER`。若用户当初是按 `'username'@'localhost'` 创建的，应 `DROP USER` 后按 `'%'` 重建，而不是 UPDATE 系统表。

## 创建表

```sql
-- 语法骨架：column1/column2 换成实际列名和类型，注释要用引号括起来
CREATE TABLE IF NOT EXISTS table_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    column1 VARCHAR(50) COMMENT '列说明',
    column2 INT COMMENT '列说明'
) ENGINE = INNODB charset = utf8mb4 COMMENT '表说明';
```

## 插入数据

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

---

## 相关笔记

本篇在图谱里的邻居——从这里可以走到相关主题，也能被别人走回来。

- [MOC - programming](../../../notes/MOC%20-%20programming.md)
- [Servlet（本库另一个后端栈组件，JDBC 那一层通常接在这里）](../Java/Servlet.md)
