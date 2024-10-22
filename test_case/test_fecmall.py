#Author: Sanmu
#CreatTime: 2024/10/22
#Descriptior: 描述
import allure
import pytest

from conf.set_conf import write_conf, read_conf
from test_case.conftest import read_yaml

@allure.epic('实现fecmall所有接口测试')
@allure.feature('基于access-token实现接口关联')
class TestFecamll:
    @allure.title('实现登录验证')
    @pytest.mark.parametrize('data',read_yaml('./data/data.yaml'))
    def test_login(self,test_api,data):
        with allure.step('1、发起post请求'):
            res = test_api.do_post(**data['login']).json()
        with allure.step('2、打印响应结果'):
            print(res)
        with allure.step('3、对响应结果校验'):
            expected = 'success'
            test_api.assert_text(expected,res,'status')
        with allure.step('4、提取access-tooken'):
            token = test_api.get_text(res,'access-token')
            write_conf('header','access-token',token)

    @allure.title('获取多语言部分的配置列表')
    @pytest.mark.parametrize('data', read_yaml('./data/data.yaml'))
    def test_languages(self,test_api,api_clean,data):
        with allure.step('1、发起get请求'):
            token = read_conf('header','access-token')
            data['languages']['headers']['access-token'] = token
            res = test_api.do_get(**data['languages']).json()
        with allure.step('2、打印响应结果'):
            print(res)
        with allure.step('3、对响应结果校验'):
            expected = 'fetch all languages success'
            test_api.assert_text(expected,res,'message')


