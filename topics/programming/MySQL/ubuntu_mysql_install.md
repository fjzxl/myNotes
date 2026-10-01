---
title: 安装mysql
tags:
  - programming
  - mysql
created: 2026-09-10
updated: 2026-09-10
---
# 安装mysql

```shell
sudo apt info -a mysql-server-8.0
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
USE mysql;
update user set user.Host='%'where user.User='username';
FLUSH PRIVILEGES;
```

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
