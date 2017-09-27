#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ASCII 一个字节   Unicode 2个字节    UTF-8 一个或者3个字节
print('包含中文的str')

# ord()函数获取字符的整数表示  chr()将对应的整数转换成字符
print(ord('A')) # 65
print(ord('中')) # 20013

# 字符和字节的相互转换
'abc'.encode('ascii')
'abc'.encode('utf-8')
b'abc'.decode('utf-8')

# 字符串格式化
print('Hello ,%s' % 'World')
