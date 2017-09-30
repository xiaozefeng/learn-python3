#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip 和 port
s.bind(('127.0.0.1', 9999))
# 监听5个客户端
s.listen(5)
print('Watting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s' % (sock, addr))
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
