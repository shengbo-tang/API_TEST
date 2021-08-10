#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@IDE    ：PyCharm
@Author ：shengbo.tang
@Email  : t975426031@163.com
@Date   ：2021/7/3 23:27
=================================================="""

import requests
import ast
from common.logcalconfig_utils import local_config


class RequestsUtils:

    def __init__(self):
        self.hosts = local_config.URL
        self.headers = {"Content-Type": "application/json;charset=utf-8"}
        self.session = requests.Session()

    def get(self, get_infos):
        url = self.hosts + get_infos["请求地址"]
        print(url)
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_infos["请求参数(get)"])
                                    )
        response.encoding = response.apparent_encoding
        print(response.text)
        result = {
            'code': 0,     # 请求成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.json()
        }
        return result

    def post(self, get_infos):
        url = self.hosts + get_infos["请求地址"]
        response = self.session.post(url=url,
                                     headers=self.headers,
                                     params={"access_token": "47_OT4z6u65f1oJGIrqlUTPC4hG06moJsx0m_6ytLEeLJC6UCC1_-foHbJR1b03R92gp1Y21MWQlbpR410pu-PU2scwz1PKPgNYSPeteNPTX2QLgAp1nRnEsSPGouInsUBAs_aDUqn08P8dDpbSIIOeAIAXXD"},
                                     # params=ast.literal_eval(get_infos["请求参数(get)"]),
                                     data=get_infos["提交数据（post）"]
                                     )
        response.encoding = response.apparent_encoding
        print(response.text)
        result = {
            'code': 0,     # 请求成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.json()
        }
        return result


if __name__ == '__main__':
    # get_infos = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在', '期望结果': 'access_token,expires_in', '测试结果': ''}
    # RequestsUtils().get(get_infos)
    post_infos = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":100}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}', '测试结果': ''}
    RequestsUtils().post(post_infos)

