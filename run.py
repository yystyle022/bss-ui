import os
import shutil
import pytest
from time import sleep

# 删除老的测试结果
os.chdir(os.path.dirname(os.path.realpath(__file__)))
if os.path.exists('./result/'):
    shutil.rmtree('./result/')
if os.path.exists('./logs/log'):
    shutil.rmtree('./logs/log')

# pytest主函数
pytest.main(['-s', '-vs', '--reruns=2', './testcases', '-n=2', '--capture=sys', '--alluredir=./result/', '--html=./result/report.html', '--self-contained-html'])
# 直接执行allure服务
# os.system('allure serve ./result/')

# 生成report报告文件
# os.system('{} generate {} -o ./report/ --clean'.format(
#     # os.path.join(r'D:\python3.10.10\Scripts\allure-2.13.2\bin\allure.bat')git ,
#     os.path.join(r'D:\python3.8\Scripts\allure-2.13.2\bin\allure.bat'),
#     os.path.join(os.getcwd(), 'result')))
