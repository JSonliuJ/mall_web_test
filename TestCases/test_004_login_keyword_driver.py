# -- encoding: utf-8 --
# @time:    	2021/10/12 15:48
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import inspect
import json
import os
import sys

local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import yaml
import pytest
from Common.base_page import BasePage
from Common.file_path import TestDatas_path
from TestDatas.Common_datas import Config as cf

login_file = os.path.join(TestDatas_path, 'login_yaml.yaml')
params_file = os.path.join(TestDatas_path, 'test_params.yaml')

with open(login_file, 'r', encoding='utf-8') as f1:
    data = yaml.safe_load(f1)
f1.close()
with open(params_file, 'r', encoding='utf-8') as f2:
    params = yaml.safe_load(f2)
f2.close()


@pytest.mark.key_word_driver
class TestLoginKeyWordDriver():

    @pytest.mark.parametrize(['user', 'pwd', 'expected'], params['test_login_successful'])
    def test_login_successful(self, driver, user, pwd, expected):
        # 测试步骤
        page = BasePage(driver)
        self.driver = driver
        page._test_params['url'] = cf.web_login_url
        page._test_params['user'] = user
        page._test_params['pwd'] = pwd
        page._test_params['expected'] = expected
        page.steps(data,page)

    @pytest.mark.parametrize(['user', 'pwd', 'expected'], params['test_login_error'])
    def test_login_error(self, driver, user, pwd, expected):
        # 测试步骤
        page = BasePage(driver)
        self.driver = driver
        page._test_params['url'] = cf.web_login_url
        page._test_params['user'] = user
        page._test_params['pwd'] = pwd
        page._test_params['expected'] = expected
        page.steps(data, page)

# if __name__ == '__main__':
#     print(params)
