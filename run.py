# import HTMLTestRunner
import os
import sys
local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(local_path)
import pytest
import time

from Common.file_path import *


# 实例化套件对象
# s = unittest.TestSuite()
# # 1. 实例化TestLoader对象
# loader = unittest.TestLoader()
# # 2. 使用discover找到一个目录下所有测试用例
# s.addTests(loader.discover(TestCases_path))
# fp = open(reports_path + 'autoTest_report.html', 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(
#     stream=fp,
#     title='单元测试报告',
#     description='web自动化单元测试报告',
# )
# runner.run(s)

day_ts = time.strftime("%Y%m%d%H%M%S",time.localtime())
# 运行方式2
pytest.main([
             # "-m register",
             "--html={0}/{1}_report.html".format(reports_path,day_ts),
             "--junitxml={0}/{1}_report.xml".format(reports_path,day_ts)],
             # "--alluredir={0}".format(allure_reports_path)]
             # "--reruns","2","--reruns-delay","5"]
)
# pytest.main()
