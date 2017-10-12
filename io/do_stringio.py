# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

# read from StringIO
f = StringIO('水面细生风，菱歌慢慢声， 客亭临小市， 灯火夜妆明')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
