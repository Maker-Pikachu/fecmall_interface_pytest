# Author: Sanmu
# CreatTime: 2024/10/22
# Descriptior: 描述
import requests
from jsonpath import jsonpath

from conf.set_conf import read_conf


class APiKeys:
    def __init__(self, env):
        self.env = env
    def do_get(self,path,headers=None,params=None, **kwargs):
        url = self.set_url(path)
        return requests.get(url=url, headers=headers, params=params, **kwargs)
    def do_post(self,path,headers=None,data=None, **kwargs):
        url = self.set_url(path)
        return requests.post(url=url, headers=headers, json=data, **kwargs)

    #获取响应文本
    def get_text(self,res,key):
        values = jsonpath(res, f'$..{key}')
        #对结果二次封装
        if values:
            if len(values) == 1:
                return values[0]
            else:
                return values
        else:
            return '找不到值'

    #校验判断
    def assert_text(self,expected,res,key):
        reality = self.get_text(res,key)
        assert str(expected) == str(reality),f'''
            期望值：{expected},
            实际值：{reality},
            断言结果：{expected} != {reality}，断言失败！
        '''
    
    #拼接url
    def set_url(self,path):
        url = read_conf(self.env, 'HOST')
        if path:
            url = url + path
        return url

