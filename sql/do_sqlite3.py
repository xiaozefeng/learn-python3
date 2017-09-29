#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# SQLite的特点是轻量级、可嵌入，但不能承受高并发访问
# 连接数据库
# 如果test.db 不存在会在当前目录创建
conn = sqlite3.connect('test.db')

# 创建一个Cursor游标
cursor = conn.cursor()
# 执行sql
cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
# 插入数据
cursor.execute('insert into user(id,name) values (\'1\',\'jack\')')
cursor.close()
conn.commit()
conn.close()

# 查询
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id = ?','1')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

