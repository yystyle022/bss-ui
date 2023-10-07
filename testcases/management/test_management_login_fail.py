# -*- coding=utf-8 -*-
# @Time : 2023/9/21 15:32
# @Author : yangyang
# @File : bss-ui/test_management_login_fail.py
import allure
from common.playwrightFunction import management_login_fail_password_mistake,management_login_fail_server_number_no_exist


# @allure.feature('管理端登录失败测试用例-密码错误')
# @allure.title('测试登录管理端-谷歌测试浏览器')
# def test_management_login_fail_password_mistake_chromium_browser(chromium_browser):
#     management_login_fail_password_mistake(chromium_browser)


# @allure.feature('管理端登录失败测试用例-密码错误')
# @allure.title('测试登录管理端-谷歌正式浏览器')
# def test_management_login_fail_password_mistake_chrome_browser(chrome_browser):
#     management_login_fail_password_mistake(chrome_browser)
#
#
# @allure.feature('管理端登录失败测试用例-密码错误')
# @allure.title('测试登录管理端-微软Edge浏览器')
# def test_management_login_fail_password_mistake_edge_browser(edge_browser):
#     management_login_fail_password_mistake(edge_browser)
#
#
# @allure.feature('管理端登录失败测试用例-密码错误')
# @allure.title('测试登录管理端-火狐浏览器')
# def test_management_login_fail_password_mistake_firefox_browser(firefox_browser):
#     management_login_fail_password_mistake(firefox_browser)


@allure.feature('管理端登录失败测试用例-账号不存在')
@allure.title('测试登录管理端-谷歌测试浏览器')
def test_management_login_fail_server_number_no_exist_chromium_browser(chromium_browser):
    management_login_fail_server_number_no_exist(chromium_browser)


@allure.feature('管理端登录失败测试用例-账号不存在')
@allure.title('测试登录管理端-谷歌正式浏览器')
def test_management_login_fail_server_number_no_exist_chrome_browser(chrome_browser):
    management_login_fail_server_number_no_exist(chrome_browser)


@allure.feature('管理端登录失败测试用例-账号不存在')
@allure.title('测试登录管理端-微软Edge浏览器')
def test_management_login_fail_server_number_no_exist_edge_browser(edge_browser):
    management_login_fail_server_number_no_exist(edge_browser)


@allure.feature('管理端登录失败测试用例-账号不存在')
@allure.title('测试登录管理端-火狐浏览器')
def test_management_login_fail_server_number_no_exist_firefox_browser(firefox_browser):
    management_login_fail_server_number_no_exist(firefox_browser)
