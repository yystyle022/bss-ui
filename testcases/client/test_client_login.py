# -*- coding: utf-8 -*-
# @Time : 2023/3/26 21:41
# @Author : yangyang
# @File : 2222/test_client_login.py


import allure
from playwright.sync_api import sync_playwright
from common.playwrightFunction import client_login

@allure.feature('测试登录官网')
@allure.title('测试登录官网')
def test_login_client():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        client_login(page)
