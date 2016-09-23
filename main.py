#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-23 09:51:00
# @Author  : jerry.liangj@qq.com


from db.redis.db import redis_db
from sqlalchemy.orm import scoped_session, sessionmaker
from db.mysql.db import engine
from db.mysql.model import *

from log import getLogger


def main():
	log = getLogger("webcrawler")
	# handler = {
	# 	'card': cardhandler,
	# 	'exam': examHandler,
	# 	'gpa': gpaHandler,
	# 	'lecture': lectureHandler,
	# 	'library': libraryHandler,
	# 	'jwc': jwcHandler,
	# 	'nic': nicHandler,
	# 	'pedetail': peDetailHandler,
	# 	'phylab': phylabHandler,
	# 	'room': roomHandler,
	# 	'srtp': srtpHandler,
	# 	'user': userHandler

	# }
	while True:
		api = redis_db.blpop("api")
		print api[1]
		

if __name__ == '__main__':
	main()
