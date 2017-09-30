#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 读文件
with open('/Users/xiaozefeng/Desktop/domain.xml', 'r') as f:
    for line in f.readlines():
        print(line.strip())

# 写文件
with open('/Users/xiaozefeng/Desktop/test.txt', 'w', encoding='utf-8') as f:
    f.write('Hello Python3')

print('写入文件成功')
