import os
import pytest

if __name__ == '__main__':
    # pytest主函数
    pytest.main(
        ['-s', '-vs', '--reruns=2', './testcases', '-n=2', '--capture=sys', '--alluredir=./result/',
         '--html=./result/report.html', '--self-contained-html'])
    # 直接执行allure服务
    # os.system('allure serve ./result/')
    # 生成report报告文件
    os.system('{} generate {} -o ./report/ --clean'.format(
        #os.path.join(r'D:\python3.10.10\Scripts\allure-2.13.2\bin\allure.bat'),
        os.path.join(r'D:\python3.8\Scripts\allure-2.13.2\bin\allure.bat'),
        os.path.join(os.getcwd(), 'result')))
