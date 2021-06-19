#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 23:31
=================================================="""
import logging


logger = logging.getLogger("logger")
logger.setLevel(10)           # 10, 20, 30, 40, 50
handler1 = logging.StreamHandler()   # 控制台
logger.setLevel(30)           # 10, 20, 30, 40, 50
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)

handler2 = logging.FileHandler('./test.log', 'a', encoding='utf-8')
handler2.setLevel(10)
handler2.setFormatter(formatter)
logger.addHandler(handler2)

logger.info('hello')