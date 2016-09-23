#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-23 09:51:00
# @Author  : jerry.liangj@qq.com

import redis

DB_HOST = '127.0.0.1'
DB_PORT = 6379
DB_INDEX = 0

redis_db = redis.Redis(host=DB_HOST, port=DB_PORT, db=DB_INDEX)