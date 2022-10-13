# -- encoding: utf-8 --
# @time:    	2022/10/11 23:00
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import sys
local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import string
import time
import pytest
import random
from PageObjects.register_page import RegisterPage
from TestDatas import register_datas as LD


@pytest.mark.usefixtures("driver")
@pytest.mark.usefixtures("driver_refresh")
@pytest.mark.usefixtures("new_mobile")
class TestRegister():
    # @classmethod
    # def setUpClass(cls):
    #     #通过excel读取本功能当中需要的所有测试数
    #     pass
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    # self.driver.quit()
    # def tearDown(self):
    #     '''后置'''
    #     pass
    # 正常用例 -登录成功
    @pytest.mark.register
    @pytest.mark.parametrize("data", LD.user_data)  # 参数化，把LD.user_data的测试数据交给自定义参数名为data的参数
    def test_user_register(self, driver, new_mobile, data):
        rp = RegisterPage(driver)
        rp.load()
        rp.validate_mobile(new_mobile)
        ran_str = ''.join([random.choice(string.digits+string.ascii_letters) for i in range(8)])
        data = rp.str_replace(data,'"random_str"','"%s"' % ran_str)
        rp.fill_account_info(data['user'], data['password'])
        time.sleep(5)
