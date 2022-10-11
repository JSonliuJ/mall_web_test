# -- encoding: utf-8 --
# @time:    	2020/10/11 21:13
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
# 需要验证码
from selenium.webdriver.common.by import By


class RegisterLocators:
    '''验证手机号'''
    # 手机号输入框
    mobile_input = (By.XPATH, '//input[@placeholder="请输入手机号"]')
    # 验证码按钮
    code_button = (By.XPATH, '//a[text()="获取验证码"]')
    # 验证码输入框
    code_input = (By.XPATH, '//input[@placeholder="请输入验证码"]')
    # 下一步按钮
    next_step_btn = (By.XPATH, '//span[text()="下一步"]')

    '''填写账号信息'''
    # 用户名输入框
    set_account_input = (By.XPATH, '//input[@placeholder="请您设置账号"]')
    set_pwd_input = (By.XPATH, '//input[@placeholder="请您设置密码"]')
    confirm_pwd_input = (By.XPATH, '//input[@placeholder="再次输入密码"]')
    account_next_button = (By.XPATH, '//span[text()="下一步"]')

    # 错误信息
    page_error_msg = (By.XPATH,'//div[@class="error-text"]')
    alert_err_msg = (By.XPATH,'//div[@role="alert"]/p[@class="el-message__content"]')