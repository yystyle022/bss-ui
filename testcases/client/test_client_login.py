# -*- coding: utf-8 -*-
# @Time : 2023/3/26 21:41
# @Author : yangyang
# @File : 2222/test_client_login.py


import allure
from page.LoginPage import LoginPage
from common.playwrightFunction import client_login



@allure.title('官网登录测试')
@allure.description('登录客户端')
def test_login():
    client_login()
