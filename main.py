#!/usr/bin/python

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


engine = create_engine('mysql+pymysql://root:Thunder#123@localhost:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(id='1', name='Bob')

session.add(new_user)

session.commit()

session.close()

session = DBSession()

try:
    user = session.query(User).filter(User.id == '1').one()
    print('type:{0}'.format(type(user)))
    print("name:{0}".format(user.name))
except Exception as error:
    print("Don't find msg")
session.close()
