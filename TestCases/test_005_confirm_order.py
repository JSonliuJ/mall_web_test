# -- encoding: utf-8 --
# @time:    	2022/10/14 22:54
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import sys

from PageObjects.login_page import LoginPage

local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import yaml
import pytest
from Common.file_path import TestDatas_path

order_file = os.path.join(TestDatas_path, 'order.yaml')
params_file = os.path.join(TestDatas_path, 'test_params.yaml')

with open(order_file, 'r', encoding='utf-8') as f1:
    order = yaml.safe_load(f1)
f1.close()
with open(params_file, 'r', encoding='utf-8') as f2:
    params = yaml.safe_load(f2)
f2.close()

class TestCofirmOrder():
    @pytest.mark.confirm_order_success
    @pytest.mark.parametrize(['goods_name', 'img_url', 'expected'], params['test_confirm_order_successful'])
    def test_confirm_order_successful(self, login,goods_name, img_url, expected):
        # 测试步骤
        driver = login
        page = LoginPage(driver)
        page._test_params['goods_name'] = goods_name
        page._test_params['img_url'] = img_url
        page._test_params['expected'] = expected
        page.steps(order, page)
