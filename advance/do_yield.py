# -*- coding: utf-8 -*-

def each_ascii(s):
    for ch in s:
        yield ord(ch)
    return '%s chars' % len(s)

def yield_from(s):
    r = yield from each_ascii(s)
    print(r)


def main():
    for x in each_ascii('acb'):
        print(x)
    it = each_ascii('xyz')
    try:
        while True:
            print('next() =>',next(it))
    except StopIteration as s:
        print('exception => ',s.value)

    # using yield from in main() will change main() from function to generator
    # r = yield from each_ascii('hello')
    print('yield from =>')
    for ch in yield_from('hello'):
        pass


main()
