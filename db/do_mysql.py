#coding: utf-8

import mysql.cursor

# change root password to yours:
conn = mysql.connector.connect(user='root', password='root', datbase='taotao')

cursor = conn.cursor()

# 创建 account
cursor.exectute('create table account (id varchar(20) primary key, name varchar(20)) ENGINE=InnoDB  DEFAULT CHARSET=utf8')

# 插入一行记录
cursor.execute('insert into account (id, name) values (%s, %s)', ('1', 'Jack'))
print('rowcount = ', cursor.rowcount)

# 提交事务
conn.commit()
cursor.close()

# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print(values)

# 关闭Cursor 和 Connection:
cursor.close()
conn.close()
