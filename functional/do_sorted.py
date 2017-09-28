#!/usr/bin/env python3
# -*- conding: utf-8 -*-
# 排序函数
r = sorted([36, 5, -12, 9, -21])
print(r)

r = sorted([36, 5, -12, 9, -21],key=abs)
print(r)

r = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(r)

# 练习 按照名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 根据明天排序
r = sorted(L,key=(lambda t: t[0]))
print('按照名字自然顺序排序',r)
# 根据成绩排序 (倒叙)
r = sorted(L,key=(lambda t: t[1]),reverse=True)
print('按照成绩倒序排序',r)
