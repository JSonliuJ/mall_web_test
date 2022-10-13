# -- encoding: utf-8 --
# @time:    	2021/10/11 12:57
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import sys
local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import pytest
from TestDatas import login_datas as LD
from Common.my_log import MyLog

# pip install pyyaml
logger = MyLog()

class TestLogin():
    # TestCase中不能写__init__
    # @classmethod
    # def setUpClass(cls):
    #     #通过excel读取本功能当中需要的所有测试数
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass
        # cls.driver.quit()
    def setUp(self):
        pass
    # def tearDown(self):
    #     '''后置'''
    #     pass
        # 正常用例 -登录成功

    @pytest.mark.smoke
    @pytest.mark.usefixtures("access_web")
    @pytest.mark.usefixtures("refresh_page")
    @pytest.mark.parametrize("data", LD.success_data)
    def test_username_login(self,access_web,data):
        access_web[1].login(data["user"], data["password"])
        expected = data['expected']
        actual = access_web[1].get_user(expected)
        try:
            assert expected == actual
            access_web[1].login_out(expected)
        except Exception as e:
            logger.error(e)
            raise e

    @pytest.mark.login
    @pytest.mark.parametrize("data", LD.phone_data)  # 参数化，把LD.phone_data的测试数据交给自定义参数名为data的参数
    def test_username_login_error(self,access_web,data):
        access_web[1].login(data["user"], data["password"])
        # 断言 登录页面 提示：请输入正确手机号
        # 对别文件内容与期望值是否相等
        assert (access_web[1].get_error_msg(), data["expected"])

if __name__ == '__main__':
    # tl = TestLogin()
    # tl.test_username_login()
    pass