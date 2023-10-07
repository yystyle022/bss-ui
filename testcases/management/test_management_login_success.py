# -*- coding=utf-8 -*-
# @Time : 2023/4/26 10:40
# @Author : yangyang
# @File : bss-ui/test_management_login_success.py


import allure
from common.playwrightFunction import management_login_success


@allure.feature('管理端登录成功测试用例')
@allure.title('测试登录管理端-谷歌测试浏览器')
def test_login_management_success_chromium_browser(chromium_browser):
    management_login_success(chromium_browser)


@allure.feature('管理端登录成功测试用例')
@allure.title('测试登录管理端-谷歌正式浏览器')
def test_login_management_success_chrome_browser(chrome_browser):
    management_login_success(chrome_browser)


@allure.feature('管理端登录成功测试用例')
@allure.title('测试登录管理端-微软Edge浏览器')
def test_login_management_success_edge_browser(edge_browser):
    management_login_success(edge_browser)


@allure.feature('管理端登录成功测试用例')
@allure.title('测试登录管理端-火狐浏览器')
def test_login_management_success_firefox_browser(firefox_browser):
    management_login_success(firefox_browser)
