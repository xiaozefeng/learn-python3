# -*- coding: utf-8 -*-

import sqlite3

# 连接SQLite数据库
# 如果数据库文件不存在，会在当前目录创建
conn = sqlite3.connect('test.db')

# 创建一个Cursor
cursor = conn.cursor()

# 执行一条sql
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')

# 继续执行一条SQL语句，插入一条记录
cursor.execute('insert into user(id, name) values("1","Jack")')

# 通过rowcount 获取插入的行数
print('rowcount = ', cursor.rowcount)

# 关闭Cursor
cursor.close()
# 提交事务
conn.commit()
conn.close

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id = ?',  '1')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
