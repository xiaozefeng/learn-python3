# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f  = lazy_sum(1,2,3,4,5,6,7,8,9)
f1  = lazy_sum(1,2,3,4,5,6,7,8,9)
print('f =',f)
print('f == f1 ? ', f == f1)
print('f() = ',f())


# why f2() f3() f4() returns 9, 9 ,9 rather that 1, 4, 9
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix bug
def fix_count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1,4):
        fs .append(f(i))
    return fs


f4, f5, f6 = fix_count()
print('fix count bug:')
print(f4())
print(f5())
print(f6())
