#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
m = Image.open('/Users/xiaozefeng/Desktop/test.jpg')
print(m.format,m.size,m.mode)
m.thumbnail((200,100))
m.save('/Users/xiaozefeng/Desktop/thumb.jpg','JPEG')
