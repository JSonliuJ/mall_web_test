# —— coding :utf-8 ——
# @time:    2020/10/7 21:01
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    conftest.py
from selenium import webdriver
from PageObjects.login_page import LoginPage
import pytest
import faker
driver = None


# 声明是一个fixture
@pytest.fixture()
def access_web():
    global driver
    # 前置操作
    print("所有用例执行之前，setup整个测试类执行一次")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    # driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)  # 分割线：返回值
    # yield driver
    # 后置操作
    print("所有用例执行完成，tearDown整个测试类执行一次")
    driver.quit()

@pytest.fixture()
def refresh_page():
    # 前置操作
    yield
    # 后置操作
    driver.refresh()

@pytest.fixture()
def driver():
    global d
    d = webdriver.Chrome()
    d.implicitly_wait(5)
    d.maximize_window()
    yield d
    d.quit()

@pytest.fixture()
def driver_refresh():
    # 前置操作
    yield
    # 后置操作
    d.refresh()

@pytest.fixture()
def new_mobile():
    fk = faker.Faker(locale=['zh_CN'])
    return fk.phone_number()

@pytest.fixture()
def login(driver):
    """下单夹具. 浏览器，  po 模式当中 login"""
    # TODO: 配置文件
    # home = HomePage(driver)
    # home.login('yuze', '1234')
    lg = LoginPage(driver)
    lg.login('1a2b','abcd')
    return driver
