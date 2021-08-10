#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 23:44
=================================================="""

import os
import logging
import time
from common.logcalconfig_utils import local_config


current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path, '..', local_config.LOG_PATH)


class LogUtils:
    def __init__(self, log_path=log_output_path):
        self.log_name = os.path.join(log_output_path, 'ApiTest_%s_%s.log' % (time.strftime('%Y_%m_%d'), time.strftime('%H-%M-%S')))
        self.logger = logging.getLogger("ApiTestLog")
        self.logger.setLevel(local_config.LOG_LEVEL)

        console_handler = logging.StreamHandler()     # 控制台输出
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')       # 文件输出
        formatter = logging.Formatter('[%(asctime)s] %(filename)s->(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        console_handler.close()          # 防止日志打印重复
        file_handler.close()             # 防止日志打印重复

    def get_logger(self):
        return self.logger


logger = LogUtils().get_logger()         # 防止日志打印重复


if __name__ == '__main__':
    logger.info('hello')