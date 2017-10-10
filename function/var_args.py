# -*- coding: utf-8 -*-

# 可变长参数
def hello(greeting, *args):
    if(len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting,', '.join(args)))


hello('Hi')
hello('Hi','jack')

names = ('rose','lucy')
hello('Hello',*names)
