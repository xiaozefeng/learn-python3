# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User 对象
class User(Base):
    # 表名
    __tablename__ = 'account'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/taotao')

# 创建DBSession 类型
DBSession = sessionmaker(bind=engine)

# 创建session 对象
session = DBSession()

# 创建新的User对象
new_user = User(id='5', name='Bob')

# 添加到session
session.add(new_user)
session.commit()
session.close()

# 创建Session
session = DBSession()
# 创建Query 查询 filter是where条件， 最后调用one()返回一行，如果调用all()则返回所以行
user = session.query(User).filter(User.id=='5').one()
print('type= ',type(user))
print('name=', user.name)
session.close()
