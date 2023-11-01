# -*-coding:utf-8-*-
# @Time    :2023/10/3014:37
# @Author  :jzw
# @Email   :1615573929@qq.com
# @File    :run.py
# @Software:PyCharm

import HTMLTestRunnerNew
from ceshi import *

suite=unittest.defaultTestLoader.discover(".",pattern="ceshi.py")
with open("reports.html","wb+") as f:
    runner=HTMLTestRunnerNew.HTMLTestRunner(f,2,title="测试报告",description="login reports",tester="JZW")
    runner.run(suite)