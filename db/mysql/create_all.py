#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-23 09:51:00
# @Author  : jerry.liangj@qq.com


from model import *
from db import engine, Base

def main():
	try:
		print "##################start create table###################"
		Base.metadata.create_all(engine)
		print "##################create table complete################"
	except Exception,e:
		print "!!!!!!!!!!!!!!!!!create db occur error!!!!!!!!!!!!!!!!!"
		print str(e)

if __name__ == '__main__':
	main()

Base.metadata.create_all(engine)
