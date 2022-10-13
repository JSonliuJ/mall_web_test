# -- encoding: utf-8 --
# @time:    	2022/10/11 22:29
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com

user_data = [
    {"user": "random_str", "password": "random_str"},
    # {"user": "xxA", "password": "123456abc"},  # 用户名长度为3
    # {"user": "xxA$", "password": "123456abc"},  # 用户名包含特殊字符
    # {"user": "abc123456789ABCDF", "password": "123456abc"},  # 用户名长度大于16位
    # {"user": "abc123456789ABCDF", "password": "123456abc"},
]
iphone_data = [
    {"iphone": "185932987971", "code": "请输入正确的手机号"},  # 手机号大于11位，
    {"iphone": "1859329879", "code": "请输入正确的手机号"},  # 手机号小于11位
    {"iphone": "18593298797", "code": "","error_msg":"该手机号已注册，无法重新注册"}, # 已注册的手机号
    {"iphone": "18593298797", "code": "","error_msg":"该手机号已注册，无法重新注册"}  # 验证码为空
]
