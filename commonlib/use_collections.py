# -*- coding: utf-8 -*-

from collections import namedtuple

Point = namedtuple('Point',['x', 'y'])
p = Point(1, 2)
print('Point: ', p.x, p.y)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)



from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['a'] = 'abc'
print('dd["a"]', dd['a'])
print('dd["b"]', dd['b'])


from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1
print(c)
