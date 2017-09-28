#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list tuple str map set 都是可迭代对象 Iterable
# generator 可以使用next(g) 调用的才是迭代器 Iterator
# Iterable 可以通过iter() 转换成Iterator ，Iterator 是惰性的
# for x in numbers 迭代
#遍历map
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('key=',key)

for k,v in d.items():
    print('k=%s,v=%s' % (k,v))

L = ['Apple','Mic','Alibaba']
for x in L:
    print(x)


