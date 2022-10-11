# —— coding :utf-8 ——
# @time:    2020/10/7 21:01
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    login_page.py


from PageLocators.indexpage_locators import IndexPageLocator as iloc
from PageLocators.loginpage_locators import LoginPageLocator as loc

from Common.base_page import BasePage
from TestDatas.Common_datas import Config as cf

class LoginPage(BasePage):
    '''登录页面类'''
    # 登录操作
    def login(self, username, password):
        # 输入用户名
        # 输入密码
        # 点击登录
        doc = "登录页面_登录信息"
        # 输入网址
        self.open_url(cf.web_login_url)
        # 点击登录按钮
        self.click_element(iloc.login_btn,doc)
        # 输入用户名
        self.input_text(username, loc.username_input_locator,doc)
        # 输入密码
        self.input_text(password,loc.password_input_locator,doc)
        # 确认登录
        self.click_element(loc.confirm_login_locator,doc)

    # 获取错误提示信息 ----登录区域
    def get_error_msg(self):
        doc = "登录页面_获取登录区域错误提示信息"
        # self.wait_eleVisible(loc.error_msg_locator,doc=doc)
        return self.get_element_text(loc.error_msg_locator,doc)

    def get_user(self,username):
        """获取登录后的用户名"""
        username = loc.user_name[1].replace('#username#',username)
        loc_user_name = ('xpath',username)
        doc = "登录页面_获取登陆成功用户信息"
        return self.get_element_text(loc_user_name,doc)

if __name__ == '__main__':
    from selenium import webdriver
    d = webdriver.Chrome()
    d.implicitly_wait(5)
    d.maximize_window()
    lp = LoginPage(d)
    lp.login('17778063407','123456')
