#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 19:25
=================================================="""

import os
from common.excel_utils import ExcelUtile
from common import config
from common.logcalconfig_utils import local_config

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '..', local_config.CASE_DATA_PATH)


class TestdataUtile:
    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtile(test_data_path, "Sheet1").get_sheet_data_by_dict()

    def __get_testcase_data_dict(self):
        test_case_dict = {}
        for row_data in self.test_data:
            test_case_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return test_case_dict

    def def_testcase_data_list(self):
        testcase_list = []
        for k, v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict["case_name"] = k
            one_case_dict["case_indo"] = v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__ == '__main__':
    testdataUtils = TestdataUtile()
    for i in testdataUtils.def_testcase_data_list():
        print(i)
