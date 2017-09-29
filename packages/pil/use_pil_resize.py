#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image

# 打开一个图片文件
im = Image.open('test.jpg')

w,h = im.size
print('Original image size: %sx%s'% (w,h))

# 缩放到50%
im.thumbnail((w//2,h//2))
print('Resize image to: %sx%s'%(w//2,h//2))
im.save('thumbnail.jpg','jpeg')
