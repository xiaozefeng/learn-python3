#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器
import functools

def log(func):
    @functools.wraps(func)
    def wrapper( *args, **kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-09-27')

now()

# 自定义内容日志
def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call')
            print('%s %s():'% (text,func.__name__))
            print('end call')
            return func(*args,**kw)
        return wrapper
    return decorator

@logger('execute')
def log_now():
    print('2017-09-27')

log_now()
