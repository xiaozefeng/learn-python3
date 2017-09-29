#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple, deque, defaultdict

# 用namedtuple 生成一个表示坐标的数据类型
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('p= %s p.x = %s p.y = %s' % (p, p.x, p.y))
print(isinstance(p, Point))
print(isinstance(p, tuple))

# 用namedtuple 生成一个用来表示
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('y')
print(q)

# defaultdict key不存在时返回一个默认值
dd = defaultdict(lambda: 'N/A')
dd['k'] = 'abc'
print(dd['k'])
print(dd['k1'])
