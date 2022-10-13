# -- encoding: utf-8 --
# @time:    	2021/10/12 15:48
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
import os
import sys
local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)

import pytest
from Common.base_page import BasePage



from Common.file_path import TestDatas_path
import os
import yaml
yaml_file= os.path.join(TestDatas_path,'login_yaml.yaml')
print(yaml_file)
with open(yaml_file,'r',encoding='utf-8') as f:
    data = yaml.safe_load(f)

@pytest.mark.usefixtures("driver")
@pytest.mark.key_word_driver
class TestKeyWord():
    def test_keyword(self,driver):
        # 测试步骤
        page = BasePage(driver)
        self.driver = driver
        steps = data['test_login']['steps']
        print(steps)
        for step in steps:
            method_name = step['action']
            params = step['params']
            method = getattr(page, method_name)
            method(**params)