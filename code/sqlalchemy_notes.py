from sqlalchemy import Column, String, create_engine, Integer, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from datetime import date

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:12345@localhost:3306/test')


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)  # 项目名

    # 关系
    records = relationship("Record", backref="affair")  # backref 可以让自动生成另一侧的ref


class Child(Base):
    __tablename__ = 'child'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)


Base.metadata.create_all(engine)  # 建立所有表
DBSession = sessionmaker(bind=engine)
session = DBSession()  # 开启会话
