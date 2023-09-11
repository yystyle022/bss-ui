# -*- coding: utf-8 -*-
# @Time : 2023/3/26 21:41
# @Author : yangyang
# @File : 2222/test_login.py


import allure
from page.LoginPage import LoginPage



@allure.feature('客户端登录验证')
class TestLogin():
    @allure.story('登录客户端')
    @allure.description('登录客户端')
    def test_login(self, driver, url, username, password):
        '''
        登录
        @param driver:
        @param url:
        @param username:
        @param password:
        @return:
        '''
        with allure.step('登录'):
            LoginPage().login(driver, url, username, password)


