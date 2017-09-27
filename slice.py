#!/usr/bin/env python3
#-*- coding: utf-8 -*-
L  = ['Michael','Sarah','Tracy','Bob','Jack']
# 从索引0开始取到索引3
print(L[0:3])
# 跟上面一样
print(L[:3])

# 生成0-99的list
L1 = list(range(100))
print(L1)

print(L1[:10])
# 取倒数10位
print(L1[-10:])

# 前10位每隔2取一位
print(L1[:10:2])

# 所有数，每隔5位取一位
print(L1[::5])

# 复制一个list
print(L1[:])

# tuple 和字符串也可以支持切片操作，只是切片后还是原来的类型
print((1,2,3)[:])
print('abcd'[::2])

