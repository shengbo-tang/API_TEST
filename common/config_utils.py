#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 20:35
=================================================="""
import configparser


class ConfigUtils:
    def __init__(self, config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding='utf-8')

    def read_value(self, section, key):
        value = self.cfg.get(section, key)
        return value