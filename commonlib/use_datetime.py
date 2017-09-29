#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print(now)

# 自定义时间
dt = datetime(2017, 9, 29, 9, 54, 30)
print('自定义时间', dt)

# 获取timestamp
print(dt.timestamp())

# Java 的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
t = 1429417200.0
dt = datetime.fromtimestamp(t)  # 本地时间
print(dt)

# 本地时间做转换，没有时区的概念, 比如我现在电脑是北京时间，那么和UTC时区差8个小时
utc_dt = datetime.utcfromtimestamp(t)  # utc时间
print(utc_dt)

# str 转换成 datetime
cday = datetime.strptime('2017-09-29 09:58:11', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime 加减 需要导入 timedelta
print(now + timedelta(hours=2))
print(now + timedelta(days=2))
print(now + timedelta(days=1, hours=12))
