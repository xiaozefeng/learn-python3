# -*- coding: utf-8 -*-

from collections import Iterable, Iterator

def g():
    yield 1
    yield 2
    yield 3


print('Iterable? [1,2,3]:', isinstance([1,2,3], Iterable))
print('Iterable? "abc" :', isinstance('abc',Iterable))
print('Iterable? 123', isinstance(123, Iterable))
print('Iterable? g()', isinstance(g(), Iterable))

print('Iterator? [1,2,3]:', isinstance([1,2,3], Iterator))
print('Iterator? iter([1,2,3]) :', isinstance(iter([1,2,3]), Iterator))
print('Iterator? "abc" :', isinstance('abc', Iterator))
print('Iterator? 123 :', isinstance(123, Iterator))
print('Iterator? g(): ', isinstance(g(), Iterator))


# iter list:
print('for x in [1,2,3,4,5]:')
for x in [1,2,3,4,5]:
    print(x)

print('for x in iter([1,2,3,4,5]:)')
for x in iter([1,2,3,4,5]):
    print(x)



# use next
print('use next():')
it = iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# iter dict
print('iter dict')
d = {'a':1, 'b':2, 'c':3}

print('iter key:',d)
for k in d.keys():
    print('k=',k)

print('iter values: ',d)
for v in d.values():
    print('v= ',v)

print('iter item:',d)
for k,v in d.items():
    print('%s => %s' %(k,v))


# iter list with index
print("iter enumerate(['A','B','C']):")
for i,value in enumerate(['A','B','C']):
    print(i,value)


# iter complex list
print('iter [(1,1),(2,4),(3,9)]')
for x, y in [(1,1), (2,4), (3,9)]:
    print(x,y)
