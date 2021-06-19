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


excel_path = os.path.join(os.path.dirname(__file__), '../test_data/test_data.xlsx')
# print(excel_path)

wb = xlrd.open_workbook(excel_path)   # 创建工作簿对象
sheet = wb.sheet_by_index(0)          # 创建表格对象
# cell_value = sheet.cell_value(3, 2)   # 直接取值  行列下标从0开始   row col
# cell_value = sheet.cell_value(0, 0)
# print(cell_value)
# cell_value = sheet.cell_value(1, 0)
# print(cell_value)
# cell_value = sheet.cell_value(2, 0)   # 对于合并的左上角收个单元格会返回真实值
# print(cell_value)

# 2,0 3,0 4,0 学习Python编程


# 处理方式：xlrd
merged = sheet.merged_cells       # 返回一个列表   起始行，结束行，起始列，结束列

# 逻辑：凡是在merged_cells属性范围内的单元格 它的值都要等于左上角首个单元格的值
row_index = 3
col_index = 0
for (rlow, rhigh, clow, chigh) in merged:        # 遍历表格中所有单元格位置信息
    if (row_index >= rlow and row_index < rhigh):      # 行主表判断   1<=3<5
        if (col_index >= clow and col_index < chigh):
            cell_value = sheet.cell_value(rlow, clow)
# print(cell_value)


def get_merged_cell_value(row_index, col_index):
    '''
    既能获取普通单元格，又能获取合并单元格
    :param row_index:
    :param col_index:
    :return:
    '''


    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有单元格位置信息
        if (row_index >= rlow and row_index < rhigh):  # 行主表判断   1<=3<5
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                break     # 防止循环去进行判断出现值覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index, col_index)
    return cell_value

print(get_merged_cell_value(4, 0))
print(merged)
