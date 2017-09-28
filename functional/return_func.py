#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回函数 闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
f1 = lazy_sum(1,3,5,7,9)
print('f == f1',f==f1)
print('f()执行结果'f())
