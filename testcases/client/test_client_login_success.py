# -*- coding: utf-8 -*-
# @Time : 2023/3/26 21:41
# @Author : yangyang
# @File : 2222/test_client_login_success.py


import allure
from common.playwrightFunction import client_login, client_login_fail, client_login_fail_username_no_exist


@allure.feature('测试登录官网')
@allure.title('测试登录官网成功')
def test_login_client_success(chromium_browser):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    #     context = browser.new_context(no_viewport=True)
    #     page = context.new_page()
    client_login(chromium_browser)


@allure.feature('测试登录官网')
@allure.title('测试登录官网-密码错误')
def test_login_client_password_mistake(chromium_browser):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    #     context = browser.new_context(no_viewport=True)
    #     page = context.new_page()
    client_login_fail(chromium_browser)


@allure.feature('测试登录官网')
@allure.title('测试登录官网-账号不存在')
def test_login_client_username_no_exist(chromium_browser):
    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    #     context = browser.new_context(no_viewport=True)
    #     page = context.new_page()
    client_login_fail_username_no_exist(chromium_browser)
