#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 正则表达式
# 基础知识 \d 表示一个数字 \w 一个字符 .表示任意 \s一个空格
# 量词 * 表示0或n  ?表示0或1  +表示1或n {n}表示n {n,m}表示n到m个
# ^以某某开头 $以某某结尾
import re
r = re.match(r'\d{3}\-\d{3,8}$','010-12345')
if r:
    print('OK')
else:
    print('false')


# 切割字符串
print('a b   c'.split(' '))

r = re.split(r'\s+','a b   c')
print(r)

r = re.split(r'[\s\,]+','a,b,c d')
print(r)


