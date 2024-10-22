# Author: Sanmu
# CreatTime: 2024/10/22
# Descriptior: 描述
import pathlib

import pytest
import yaml

from api_keys.api_keys import APiKeys

@pytest.fixture(scope='class')
def test_api():
    return APiKeys('TEST_ENV')
@pytest.fixture(scope='class')
def dev_api():
    return APiKeys('DEV_ENV')
@pytest.fixture(scope='class')
def api_clean(request):
    def api_finalizer():
        pass
    request.addfinalizer(api_finalizer)

def read_yaml(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data
