#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/19 13:53
=================================================="""

import os
import xlrd
from common.excel_utils import ExcelUtile

excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
excelUtile = ExcelUtile(excel_path, "Sheet1")
# print(excelUtile.get_merged_cell_value(8, 0))
sheet_list = []
for row in range(1, excelUtile.get_row_count()):
    row_dict = {}
    row_dict["事件"] = excelUtile.get_merged_cell_value(row, 0)
    row_dict["步骤序号"] = excelUtile.get_merged_cell_value(row, 1)
    row_dict["步骤操作"] = excelUtile.get_merged_cell_value(row, 2)
    row_dict["完成情况"] = excelUtile.get_merged_cell_value(row, 3)
    sheet_list.append(row_dict)

for row in sheet_list:
    print(row)


all_data_list = []
first_row = excelUtile.sheet.row(0)
print(first_row)
for row in range(1, excelUtile.get_row_count()):
    row_dict = {}
    for col in range(0, excelUtile.get_col_count()):
        row_dict[first_row[col].value] = excelUtile.get_merged_cell_value(row, col)
    all_data_list.append(row_dict)
for row in all_data_list:
    print(row)