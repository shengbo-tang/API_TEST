#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/8/10 19:03
=================================================="""

import requests

response = requests.get('http://www.hnxmxit.com/')
response.encoding = response.apparent_encoding
print(response.text)
