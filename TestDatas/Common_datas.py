# —— coding :utf-8 ——
# @time:    2020/10/7 21:02
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    Common_datas.py
# 全局 --系统访问地址 --登录链接
class Config:
    db = dict(
        host = '47.113.180.81',
        port = 3306,
        user = 'lemon',
        password = 'lemon123',
        database = 'yami_shops'
    )

    web_login_url = "http://mall.lemonban.com:3344"