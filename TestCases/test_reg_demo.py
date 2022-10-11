# -- encoding: utf-8 --
# @time:    	2020/10/12 1:43
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
from Common.mysql_handle import MySQLHandler
import pytest
@pytest.mark.skip
@pytest.mark.usefixtures('new_mobile')
def test_demo(new_mobile):
    from TestDatas.Common_datas import Config as cf
    my_db = MySQLHandler(**cf.db)
    sql = "SELECT mobile_code FROM tz_sms_log WHERE user_phone = %s ORDER BY rec_date DESC" % new_mobile
    code = my_db.select_sql(sql)
    print("code", code)
    my_db.close()