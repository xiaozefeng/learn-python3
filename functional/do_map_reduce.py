#!/usr/bin/env python3
# -*- conding: utf-8 -*-
from functools import reduce

# map(func,list) 对list中的每一个元素使用func方法
L = [1,2,3,4,5,6]
def f(x):
    return x * x

r = map(f,L)
for x in r:
    print(x)

# reduce(func,list) func接收2个参数, 类似 func(func(list[0],list[1]),list[2])
def fn(x,y):
    return x+y

r = reduce(fn,L)
print('使用reduce...')
print(r)

# 要把序列[1, 3, 5, 7, 9]变换成整数13579
L = [1,3,5,7,9]
def fn1(x,y):
    return x*10+y

r = reduce(fn1,L)
print(r)

# 整理成str2int函数
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))

r = str2int('765343')
print(r)

# 使用lambda 简化 str2int 函数
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int1(s):
    return reduce(lambda x,y: x * 10 +y , map(char2num,s))

r = str2int1('1212251')
print('lambda版本的str2int 结果',r)

# 练习
# 把用户输入的不规范的英文名字，变为首字母大写
names = ['jack','rose','lucy']
def capitalize(s):
    return s[0].upper()+s[1:]

r = map(capitalize,names)
for x in r:
    print(x)

## 求和函数
def my_sum(x,y):
    return x+y

def prod(L):
    return reduce(my_sum,L)

print(prod([1,3,5,7,9]))









