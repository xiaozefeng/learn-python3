#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time,threading

# threading 是多线程高级模块，threading 是_thread 模块的封装
def loop():
    print('thread %s is running... ' % threading.current_thread().name)
    n = 0
    while n<5:
        n = n+1
        print('thread %s >>> %s '% (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended '% threading.current_thread().name)

print('thread %s ended '% threading.current_thread().name)
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended '% threading.current_thread().name)

