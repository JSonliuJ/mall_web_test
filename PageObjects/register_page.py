# -- encoding: utf-8 --
# @time:    	2020/10/11 22:19
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import time

import allure
from Common.base_page import BasePage
from TestDatas.Common_datas import Config as cf
from PageLocators.indexpage_locators import IndexPageLocator as iloc
from PageLocators.register_locators import RegisterLocators as loc
from Common.mysql_handle import MySQLHandler
import faker
import random
import string

class RegisterPage(BasePage):

    def load(self):
        self.open_url(cf.web_login_url)

    def validate_mobile(self, iphone):
        # 1.输入手机号
        doc = '注册页面_验证手机号'
        self.click_element(iloc.register_btn)
        self.input_text(iphone, loc.mobile_input, doc)
        # 2. 点击获取验证码按钮
        self.click_element(loc.code_button, doc)
        # 3. 数据库获取验证码
        # 4. 查询数据库，获取验证码
        db = MySQLHandler(**cf.db)
        print(iphone,type(iphone))
        sql = "SELECT mobile_code FROM tz_sms_log WHERE user_phone = %s ORDER BY rec_date DESC" % iphone
        code = db.select_sql(sql)[0]
        # print("code",code)
        db.close()
        # 5. 输入验证码
        self.input_text(code, loc.code_input, doc)
        # 6. 点击下一步按钮
        self.click_element(loc.next_step_btn, doc)

    def fill_account_info(self, user, password):
        doc = '注册页面_填写账号信息'
        # 1.填写账号
        isExist = self.ele_isExist(loc.set_account_input)
        if isExist:
            self.input_text(user, loc.set_account_input, doc)
        # 2. 填写密码
        self.input_text(password, loc.set_pwd_input, doc)
        # 3.确认密码
        self.input_text(password, loc.confirm_pwd_input, doc)
        # 4. 点击下一步
        self.click_element(loc.account_next_button, doc, doc)

    def generate_iphone_account(self,n):
        fk = faker.Faker(locale=['zh_CN'])
        iphone = fk.phone_number()
        str_list = ('').join([random.choice(string.digits + string.ascii_letters) for i in range(n)])
        return iphone,str_list

    def finish_register(self):
        pass
