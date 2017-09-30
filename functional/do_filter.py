#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 过滤器
L = [x for x in range(21)]
r = filter(lambda n: n % 2 == 1, L)
for x in r:
    print(x)
