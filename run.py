import os
import pytest

pytest.main(
    ['-s', './testcases', '--capture=sys', '--alluredir=./result/', '--html=./result/report.html',
     '--self-contained-html'])
# 直接执行allure服务
# os.system('allure serve ./result/')
# 生成report报告文件
os.system('{} generate {} -o ./report/ --clean'.format(
    os.path.join(r'D:\Software\python\Lib\site-packages\allure-2.13.2\bin\allure.bat'),
    os.path.join(os.getcwd(), 'result')))
