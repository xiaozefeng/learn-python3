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
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY,name VARCHAR(20))')
# 插入数据
cursor.execute('INSERT INTO user(id,name) VALUES (\'1\',\'jack\')')
cursor.close()
conn.commit()
conn.close()

# 查询
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM user WHERE id = ?', '1')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
