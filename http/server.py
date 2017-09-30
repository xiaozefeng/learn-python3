#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

# 导入自己写的application函数
from hello import application

# 创建一个服务器
httpd = make_server('', 8080, application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()
