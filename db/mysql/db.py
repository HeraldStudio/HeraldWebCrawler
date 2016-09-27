#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-23 09:51:00
# @Author  : jerry.liangj@qq.com

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PWD = '084358'
DB_NAME = 'herald_webservice'

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME), echo=False,pool_size=500, pool_recycle=100)

mysql_db = scoped_session(sessionmaker(bind=engine,autocommit=False,autoflush=True,expire_on_commit=False))