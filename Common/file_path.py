# —— coding :utf-8 ——
# @time:    2020/10/7 20:58
# @IDE:     webTest_frmewok_v2.0
# @Author:  jsonJie
# @Email:   810030907@qq.com
# @File:    file_path.py
import os

# base_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] 二选1
base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
print(base_path)
# 测试数据路径
TestDatas_path = os.path.join(base_path, 'TestDatas')

# 测试用例路径
TestCases_path = os.path.join(base_path, 'TestCases')

# 报告路径
reports_path = os.path.join(base_path, r'OutPuts\reports')
allure_reports_path = os.path.join(base_path,r'OutPuts\allure_reports')

# 截图路径
screenshots_path = os.path.join(base_path, r'OutPuts\screenshots')

# 日志路径
logs_path = os.path.join(base_path, r'OutPuts\logs')

# config_dir = os.path.join(base_path,'Config')

if __name__ == '__main__':
    print(logs_path)