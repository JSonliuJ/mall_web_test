# —— coding :utf-8 ——
# @time:    2020/10/7 20:59
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    indexpage_locators.py
from selenium.webdriver.common.by import By
# 头部导航栏
from selenium.webdriver.common.by import By
class IndexPageLocator:
    '''头部导航栏'''
    # 搜索框
    head_search_input = (By.XPATH,'//div[@class="head-scroll"]//input[@placeholder="请输入商品名称"]')
    # 登陆按钮
    # 点击登录
    login_btn = (By.XPATH, '//a[text()="登录"]')
    # 注册按钮
    register_btn = (By.XPATH,'//a[text()="注册"]')
    # 我的订单按钮
    # 个人中心按钮
    # 购物车按钮

    '''主体栏'''
    # 商品列表按钮
    # 新品推荐按钮
    # 限时特惠按钮
    # 优惠团购按钮
    # 秒杀专场按钮
    # 领券中心按钮
    # 搜索框
    home_search_input = (By.XPATH, '//div[@class="home-search"]//input[@placeholder="请输入商品名称"]')
    # 搜索按钮
    home_search_button = ('xpath', '//div[@class="home-search"]//input[@value="搜索"]')
    # 点击商品
    home_goods_img = ('xpath', '//div[@class="goods-img"]')
    # 购物车图标

