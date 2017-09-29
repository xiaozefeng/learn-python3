#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',db='foo')
cur = conn.cursor()
cur.execute("SELECT * FROM TB_INFOR_JOB")
for r in cur.fetchall():
           print(r)
           #cur.close()
conn.close()

