# —— coding :utf-8 ——
# @time:    2020/10/7 21:03
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    login_datas.py
# 正常用例 -登录成功
success_data = [{"user":"17778063xxx","password":"123456","expected":"zhangsan"},
                {"user":"1a2b","password":"abcd","expected":"1a2b"}
                ]

# 异常用例 - 错误的手机号格式(大于11位、小于11位、为空、不在号码段)
phone_data = [
    {"user":"18593298797","password":"abcd","expected":"请输入正确手机号"},  # 小于11位
    {"user":"185932987977","password":"abcd","expected":"请输入正确手机号"}, #大于11位
    {"user":"","password":"abcd","expected":"账号为4~16位字母、数字或下划线"},  # 手机号为空
    {"user":"118593298797","password":"abcd","expected":"请输入正确手机号"}, # 不在手机号频段
    {"user":"17788063407","password":"abcd","expected":"请输入正确手机号"},  # 手机号没有注册
    {"user": "1a2", "password": "abcd", "expected": "账号为4~16位字母、数字或下划线"}, # 账号3位数
    {"user": "1a2b$", "password": "abcd", "expected": "账号为4~16位字母、数字或下划线"},# 账号包含字符
    {"user": "12345678912345671", "password": "abcd", "expected": "账号为4~16位字母、数字或下划线"} # 密码17位
]
