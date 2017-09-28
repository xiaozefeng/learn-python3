#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
# 多平台通用的多进程写法
def run_proc(name):
    print('run child process %s (%s)...' % (name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
