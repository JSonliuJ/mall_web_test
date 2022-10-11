# —— coding :utf-8 ——
# @time:    2020/10/7 21:00
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    index_page.py

import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators import indexpage_locators as loc
class IndexPage:
    def __init__(self,driver):
        self.driver = driver
    def isExist_logout_ele(self):
        # 等待5s，元素没有出现 //a[@href="/Index/logout.html"]
        # 如果存在返回True，如果不存在，返回False
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[@href="/Index/logout.html"]')))
            return True
        except:
            return False

    # 选标操作 --默认选第一个 = 元素定位的时候，过滤掉不可以投的标
    def click_first_bid(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.bid_button))
        self.driver.find_element(*loc.bid_button).click()
    # 随机选一个标 //*[text()="抢投标"]
    def click_bid_by_random(self):
        # 找到所有符合的标
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.bid_button))
        eles = self.driver.find_elements(*loc.bid_button)
        # 随机数
        index = random.randint(0,len(eles)-1)
        eles[index].click()