# -*- coding: utf-8 -*-

import types

def g():
    yield 1


print('type(123)', type(123))
print('type("123")', type('123'))
print('type(None)', type(None))
print('type(abs)', type(abs))
print('type(g())', type(g()))
