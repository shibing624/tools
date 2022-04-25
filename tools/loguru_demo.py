# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from loguru import logger
trace = logger.add('runtime_{time}.log', rotation="500 MB")
# trace = logger.add('runtime.log')
logger.debug('this is a debug message')
logger.remove(trace)
logger.debug('this is another debug message')

logger.add('runtime_{time}.log', rotation='1 week') # 每周一创建新日志
logger.add('runtime_{time}.log', rotation='00:00') # 每天凌晨创建新日志
logger.add('runtime.log', retention='10 days') # 保留10天的日志，旧的日志会被删除