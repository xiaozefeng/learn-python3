#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import json
# 序列化
d = dict(name='jack',age=20,score=88)
with open('dump.txt','wb') as f:
    pickle.dump(d,f)
    print('序列号成功')

# 反序列化
with open('dump.txt','rb') as f:
    d = pickle.load(f)
    print('反序列化结果',d)

# 转换成json
r = json.dumps(d)
print('转换成json =',r)

# 从json 转换成 dict
d = json.loads(r)
print('从josn字符串转换成dict = ',d)

# 序列化对象
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('jack',18,99)
json_str = json.dumps(s,default=(lambda obj: obj.__dict__))
print('对象转换成json = ',json_str)

# json 转换成对象
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s1 = json.loads(json_str,object_hook=dict2student)
print('json字符串转换成对象',s1)

















