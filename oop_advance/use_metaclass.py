# -*- coding: utf-8 -*-


# metaclass 是创建类，所以必须从type 类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add(5)
L.add('End')
print(L)
