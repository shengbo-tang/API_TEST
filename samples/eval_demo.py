#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/7/24 12:05
=================================================="""

sum = eval("66+32")
print(sum)

print(eval("{'name':'linux','age':18}"))

print(eval("{'name':num,'age':33}", {"num": 18}))

age = 10
print(eval("{'name':'linux','age':age}", {"age": 18}, locals()))

eval("__import__('os').system('ls')")
