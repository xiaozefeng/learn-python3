#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 协程，又称微线程，纤程。英文名Coroutine。


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] consuming %s' % n)
        r = '200 OK'


def produce(c):
    # 启动生成器
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
