#!/usr/bin/env python3
# -*- conding: utf-8 -*-

#生成器 生成列表、列表元素按照某种算法生成、一边循环一遍计算的机制
# 语法
g = (x * x for x in range(10))
print(g)

# 使用循环遍历generator
for x in g:
    print(x)

# 使用函数实现裴波那契函数
def fib(max):
    n, a, b = 0, 0 ,1
    while n< max:
        print(b)
        a, b = b, a+b
        n = n+1
    return 'done'
print('使用函数打印裴波那契序列')
fib(6)


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

f = fib1(6)
print('使用generator打印裴波那契序列')
for x in fib1(6):
    print(x)
