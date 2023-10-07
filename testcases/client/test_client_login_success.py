# -*- coding: utf-8 -*-
# @Time : 2023/3/26 21:41
# @Author : yangyang
# @File : 2222/test_client_login_success.py


import allure
from playwright.sync_api import sync_playwright
from common.playwrightFunction import client_login, client_login_fail, client_login_fail_username_no_exist


@allure.feature('测试登录官网')
@allure.title('测试登录官网成功')
def test_login_client_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        client_login(page)


@allure.feature('测试登录官网')
@allure.title('测试登录官网-密码错误')
def test_login_client_password_mistake():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        client_login_fail(page)


@allure.feature('测试登录官网')
@allure.title('测试登录官网-账号不存在')
def test_login_client_username_no_exist():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        client_login_fail_username_no_exist(page)
