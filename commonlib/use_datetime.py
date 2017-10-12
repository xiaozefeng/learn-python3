# -*- coding: utf-8 -*-


from datetime import datetime, timedelta, timezone

# 获取当前的datetime
now = datetime.now()
print('now = ', now)
print('type(now)', type(now))


# 用指定日期时间创建datetime
dt = datetime(2017, 10, 12, 20,20)
print('dt = ',dt)

# 把datetime 转换成timestamp
print('datetime => timestamp', dt.timestamp())

# 把timestamp 转换成datetime
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))


# 从str 读取datetime
cday = datetime.strptime('2017-10-12 20:23:30', '%Y-%m-%d %H:%M:%S')

# 对日期进行加减
print('current datetime', cday)
print('current + 10 hours', cday + timedelta(hours=10))
print('current - 1 day', cday - timedelta(days=1))
print('current + 2.5 days', cday + timedelta(days=2, hours = 12))

# 把时间从UTC+0时区转换为UTC+8
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0.00 now=', utc_dt)
print('UTC+8.00 now=', utc8_dt)

