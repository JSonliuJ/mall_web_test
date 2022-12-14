# —— coding :utf-8 ——
# @time:    2020/10/7 21:01
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    conftest.py
import time

from selenium import webdriver
from PageObjects.login_page import LoginPage
import pytest
import faker

'''
共享机制，将前后置（如实例化driver、打开浏览器、刷新浏览器、关闭浏览器）放到conftest.py文件，
# 不需要导入文件，在对应的测试类、测试方法定义中传入即可
'''


# 声明是一个fixture
@pytest.fixture()
def access_web():
    global dr
    # 前置操作
    print("所有用例执行之前，setup整个测试类执行一次")
    dr = webdriver.Chrome()
    dr.implicitly_wait(5)
    dr.maximize_window()
    lg = LoginPage(dr)
    yield (dr, lg)  # 分割线：返回值
    # yield driver
    # 后置操作
    print("所有用例执行完成，tearDown整个测试类执行一次")
    dr.quit()


@pytest.fixture()
def refresh_page():
    # 前置操作
    yield
    # 后置操作
    dr.refresh()


@pytest.fixture()
def driver():
    global d
    d = webdriver.Chrome()
    d.implicitly_wait(5)
    d.maximize_window()
    yield d
    d.quit()


# @pytest.fixture()
# def driver_refresh():
#     # 前置操作
#     yield
#     # 后置操作
#     d.refresh()


@pytest.fixture()
def login(driver): # 调用fixture时一定要在定义函数中传入driver，否则报错
    """下单夹具. 浏览器，  po 模式当中 login"""
    lg = LoginPage(driver)
    lg.login('1a2b','abcd')
    time.sleep(10)
    return driver


@pytest.fixture()
def new_mobile():
    fk = faker.Faker(locale=['zh_CN'])
    return fk.phone_number()
