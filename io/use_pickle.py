# -*- coding: utf-8 -*-

import pickle

d = dict(name='jack', age=20, score=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)