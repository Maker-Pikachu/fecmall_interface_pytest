# Author: Sanmu
# CreatTime: 2024/10/22
# Descriptior: 描述
import os

import pytest

if  __name__ == '__main__':
    pytest.main(['-sv','./test_case/test_fecmall.py','--alluredir=./allure-report'])
    os.system('allure generate ./allure-report/ -o ./report/allure-report/ --clean')