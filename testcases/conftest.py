# -*- coding: utf-8 -*-
# @Time : 2023/3/27 21:12
# @Author : yangyang
# @File : 2222/conftest.py
import os
import yaml
import pytest
from config.driver_config import DriverConfig
from common.report_add_img import add_img_to_report
from playwright.sync_api import sync_playwright

current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@pytest.fixture()
def driver():
    '''
    返回驱动
    @return:
    '''
    driver = DriverConfig().chrome_driver_config()
    yield driver
    driver.quit()


@pytest.fixture()
def chromium_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture()
def chrome_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(channel="chrome", headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture()
def edge_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(channel="msedge", headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture()
def firefox_browser():
    playwright = sync_playwright().start()
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080}, )
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture()
def url():
    '''
    获取登录url
    @return:
    '''
    with open(current_path + r'\config\environment.yaml') as f:
        environment = yaml.load(f.read(), Loader=yaml.FullLoader)
        return environment['url']


@pytest.fixture
def managementUrl():
    '''
    获取管理端url
    @return:
    '''
    with open(current_path + r'\config\environment.yaml') as f:
        environment = yaml.load(f.read(), Loader=yaml.FullLoader)
        return environment['managementUrl']


@pytest.fixture()
def username():
    '''
    获取用户名
    @return:
    '''
    with open(current_path + r'\config\environment.yaml') as f:
        environment = yaml.load(f.read(), Loader=yaml.FullLoader)
        return environment['user']['yangyang1']['username']


@pytest.fixture
def managementUser():
    '''
    获取管理端用户名
    @return:
    '''
    with open(current_path + r'\config\environment.yaml') as f:
        environment = yaml.load(f.read(), Loader=yaml.FullLoader)
        return environment['management']['test1']['username']


@pytest.fixture()
def password():
    '''
    获取密码
    @return:
    '''
    with open(current_path + r'\config\environment.yaml') as f:
        environment = yaml.load(f.read(), Loader=yaml.FullLoader)
        return environment['user']['yangyang1']['password']


@pytest.fixture()
def managementPwd():
    '''
    获取管理端密码
    @return:
    '''
    with open(current_path + r'\config\environment.yaml') as f:
        environment = yaml.load(f.read(), Loader=yaml.FullLoader)
        return environment['management']['test1']['password']

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item):
#     '''
#     收集测试结果函数
#     @param item:测试用例
#     @param call:测试步骤
#     @return:
#     '''
#     # 返回用例执行后的result对象,是块内存位置
#     outcomes = yield
#     # 从result的内存位置中拿出测试报告
#     report = outcomes.get_result()
#     # 拿出测试用例注释
#     report.description = str(item.function.__doc__)
#     # 拿到测试报告中的步骤
#     if report.when == 'call':
#         # 判断步骤是否失败
#         if report.failed:
#             # 截图
#             add_img_to_report(driver=driver().get_driver, step_name='失败截图', need_sleep=False)
