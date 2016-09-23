#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-23 09:51:00
# @Author  : jerry.liangj@qq.com

from sqlalchemy import Column, String, Integer
from db import engine,Base
from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

class CardCache(Base):
    __tablename__ = 'card'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096))
    date = Column(Integer, nullable=False)


class CookieCache(Base):
    __tablename__ = 'cookie'
    cardnum = Column(Integer, primary_key=True)
    cookie = Column(String(256), nullable=False)
    date = Column(Integer, nullable=False)

class ExamCache(Base):
    __tablename__ = 'exam'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096), nullable=False)
    date = Column(Integer, nullable=False)

class GpaCache(Base):
    __tablename__ = 'gpa'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096))
    date = Column(Integer, nullable=False)

class JWCCache(Base):
    __tablename__ = 'jwc'
    date = Column(Integer, primary_key=True)
    text = Column(String(10240), nullable=False)

class NicCache(Base):
    __tablename__ = 'nic'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(1024))
    date = Column(Integer, nullable=False)

class LectureCache(Base):
    __tablename__ = 'lecture'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096))
    date = Column(Integer, nullable=False)

class LibraryHotCache(Base):
    __tablename__ = 'library_hot'
    id = Column(Integer,primary_key=True)
    text = Column(String(4096), nullable=False)
    date = Column(Integer, nullable=False)

class ListLibraryCache(Base):
    __tablename__ = 'library_cache'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096))
    date = Column(Integer, nullable=False)

class PCCache(Base):
    __tablename__ = 'pc'
    date = Column(Integer, primary_key=True)
    text = Column(String(1023), nullable=False)
    lastdate = Column(Integer)

class PECache(Base):
    __tablename__ = 'pe'
    cardnum = Column(Integer, primary_key=True)
    count = Column(String(10), nullable=False)

    def __repr__(self):
        return '<PE (%s, %d)' % (self.cardnum, self.count)

class PeDetailCache(Base):
    __tablename__ = 'pedetail'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(2048))
    date = Column(Integer, nullable=False)

class PhylabCache(Base):
    __tablename__ = 'phylab'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096), nullable=False)
    date = Column(Integer, nullable=False)

class RoomCache(Base):
    __tablename__ = 'room'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096), nullable=False)
    date = Column(Integer, nullable=False)

class SRTPCache(Base):
    __tablename__ = 'srtp_cache'
    cardnum = Column(String(10), primary_key=True)
    text = Column(String(4096), nullable=False)
    date = Column(Integer, nullable=False)

class TiceCache(Base):
    __tablename__ = 'tice'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(4096), nullable=False)
    date = Column(Integer, nullable=False)

class UserDetail(Base):
    __tablename__ = 'user_detail'
    cardnum = Column(String(10), primary_key=True)
    schoolnum = Column(String(10), nullable=True)
    name = Column(String(50), nullable=False)
    sex = Column(String(10), nullable=True)
    nation = Column(String(50), nullable=True)
    room = Column(String(50), nullable=True)
    bed = Column(String(50), nullable=True)