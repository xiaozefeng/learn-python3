# -*- coding: utf-8 -*-

import functools

# @functools.wraps(func) 的作用是把func的属性都拷贝给 这个注解所修饰的function
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper


@log
def now():
    print('2017-10-11')


now()


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s()' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@logger('DEBUG')
def today():
    print('2017-10-11')


today()
print(today.__name__)
