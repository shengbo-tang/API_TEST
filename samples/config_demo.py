#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 20:26
=================================================="""
import os
import configparser


config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')
cfg = configparser.ConfigParser()
cfg.read(config_path, encoding='utf-8')
print(cfg.get('default', 'URL'))