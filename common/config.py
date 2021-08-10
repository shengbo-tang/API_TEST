#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 20:38
=================================================="""
import os
from common.config_utils import ConfigUtils


config_path = os.path.join(os.path.dirname(__file__), '..', 'config/config.ini')

configUtils = ConfigUtils(config_path)
URL = configUtils.read_value('default', 'URL')
CASE_DATA_PATH = configUtils.read_value('Path', 'CASE_DATA_PATH')
