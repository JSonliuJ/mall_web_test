# —— coding :utf-8 ——
# @time:    2020/10/7 21:00
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    loginpage_locators.py

from selenium.webdriver.common.by import By
class LoginPageLocator:
    ''''元素定位类'''
    # 输入用户名
    username_input_locator = (By.XPATH, '//input[@placeholder="请输入手机号/用户名"]')
    # 输入密码
    password_input_locator = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 确认登录
    confirm_login_locator = (By.XPATH, '//a[@class="login-button"]')
    # 错误信息
    error_msg_locator = (By.XPATH, '//div[@class="error"]')
    # 用户名信息
    user_name = ('xpath', f'//a[text()="#username#"]')
    # 退出登陆按钮
    logout_btn = ('xpath', f'//span[@class="link-select"]/a[text()="退出登录"]')
