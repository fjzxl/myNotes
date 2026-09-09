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
GRANT all privileges ON databasename.* TO 'username'@'%';
USE mysql;
update user set user.Host='%'where user.User='username';
FLUSH PRIVILEGES;
```

## 创建表

```sql
CREATE TABLE IF NOT EXISTS table_name (
    column1 datatype COMMENT comment,
    column2 datatype COMMENT comment,
    ...,
    PRIMARY KEY (`id`),
) ENGINE = INNODB charset = utf8mb4 COMMENT comment;
```

## 插入数据

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```