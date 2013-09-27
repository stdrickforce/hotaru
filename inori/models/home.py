# -*- coding: utf-8 -*-

from inori.settings import mysql_settings

from sqlalchemy import create_engine
master_url = ("mysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**mysql_settings))
engine = create_engine(master_url)

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
)

from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base()

from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)


class Tweet(DeclarativeBase):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, default=0)
    content = Column(String(200), default=u"")
    created_at = Column(DateTime)

    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class Blog(DeclarativeBase):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, default=0)
    blog_category_name = Column(String(20), default=u"")
    title = Column(String(50), default=u"")
    content = Column(Text, default=u"")
    created_at = Column(DateTime)


class BlogCategory(DeclarativeBase):
    __tablename__ = 'blog_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), default=u"")

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    DeclarativeBase.metadata.create_all(engine)
