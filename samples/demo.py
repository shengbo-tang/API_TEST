#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 19:03
=================================================="""

# a = {'one': 1, 'two': 2, 'three': 3}
# a['one'] = 3.2
# a.setdefault('four', 4)
# a.setdefault('one', 3.3)
# print(a)

list_a = [
    {'用例编号': 'case01', '用例名称': 'setp_01', '是否执行': '是', '测试用例步骤': 'step01'},
    {'用例编号': 'case02', '用例名称': 'setp_02', '是否执行': '是', '测试用例步骤': 'step01'},
    {'用例编号': 'case02', '用例名称': 'setp_03', '是否执行': '是', '测试用例步骤': 'step02'},
    {'用例编号': 'case03', '用例名称': 'setp_04', '是否执行': '是', '测试用例步骤': 'step01'},
    {'用例编号': 'case03', '用例名称': 'setp_05', '是否执行': '是', '测试用例步骤': 'step02'}
]
case_dict = {}

# for i in list_a:
#     case_list.setdefault("case_info", []).append(i)
# print(case_list)

for i in list_a:
    case_dict.setdefault(i["用例编号"], []).append(i)
print(case_dict)


case_list = []
for k, v in case_dict.items():
    case_dict = {}
    case_dict["case_name"] = k
    case_dict["case_info"] = v
    case_list.append(case_dict)

for c in case_list:
    print(c)

# 字典转列表





# all_case_list = []
# for i in list_a:
    # all_case = {}
    # case_list.setdefault(i['用例编号'], []).append(i)
#     all_case["case_name"] = i['用例编号']
#     all_case["case_info"] = case_list[i['用例编号']]
#     all_case_list.append(all_case)
# print(all_case_list)