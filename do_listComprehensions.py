#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式 生成的是列表list 可以理解成头部的表达式就是循环中要做的动作
# 生成 [1x1, 2x2, 3x3, ..., 10x10]怎么做？
L=[]
for x in range(1,11):
    L.append(x*x)

# 使用列表生成式
result = [x * x for x in range(1,11) ]
print(result)


# 还可以加上判断
[x * x for x in range(1,11) if x %2 == 0]

# 还可以使用双层循环 三层或者三册以上就很少用到了
result = [m + n for m in 'ABC' for n in 'XYZ']

# 一些简单的例子
d = {'x':'A','y':'B','z':'C'}
result = [k+'='+v for k,v in d.items()]
print(result)

# 执行方法
print([s.lower() for s in 'ABC'])

# 练习
List = ['Hello','World',18,'Apple',None]
print([s.lower() for s in List if isinstance(s,str)])
