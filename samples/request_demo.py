#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/6/23 21:15
=================================================="""

import requests

host = 'https://api.weixin.qq.com'
# 获取token
params = {
    'grant_type': 'client_credential',
    'appid': 'wxb65f74721700c2ef',
    'secret': 'eb377f14338431395adfde77e5ff5aee'
}
res = requests.get(url=host + '/cgi-bin/token', params=params)
token_id = res.json()['access_token']

# 创建一个标签
get_params = {
    'access_token': token_id
}
post_params = '{"tag": {"name": "newdream012"}}'

headers = {
    'content_type': 'application/json'
}

res01 = requests.post(url=host + '/cgi-bin/tags/create',
                      params=get_params,
                      headers=headers,
                      data=post_params)
print(res01.json())
