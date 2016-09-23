#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-23 09:51:00
# @Author  : jerry.liangj@qq.com

import logging
import os


def getLogger(name):
	handlers = {
		logging.INFO : "/var/log/%s/info.log" % name,
		logging.ERROR : "/var/log/%s/error.log" % name
	}
	# logging format
	formater = logging.Formatter('%(asctime)-4s %(message)s')
	# logger format identified by name
	logger = logging.getLogger(name)
	logger.setLevel(logging.INFO)

	logLeverls = handlers.keys()
	for level in logLeverls:
		path = os.path.abspath(handlers[level])
		handlers[level] = logging.FileHandler(path)
		handlers[level].setFormatter(formater)
		handlers[level].setLevel(level)
		logger.addHandler(handlers[level])

	return logger

