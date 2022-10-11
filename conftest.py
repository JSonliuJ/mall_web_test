# —— coding :utf-8 ——
# @time:    2020/10/7 21:01
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    conftest.py
import pytest

@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['zh_cn']