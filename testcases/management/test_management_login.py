# -*- coding=utf-8 -*-
# @Time : 2023/4/26 10:40
# @Author : yangyang
# @File : bss-ui/test_management_login.py

import allure
from page.LoginPage import LoginPage
from common.playwrightFunction import management_login


# @allure.feature('管理端登录验证')
# class TestManagementLogin():
#
#
#     @allure.story('登录管理端')
#     @allure.description('登录管理端')
#     def test_login_management(self, driver, managementUrl, managementUser, managementPwd):
#         '''
#         管理端登录
#         @param driver:
#         @return:
#         '''
#         with allure.step('登录'):
#             LoginPage().login_management(driver, managementUrl, managementUser, managementPwd)

@allure.title('登录管理端测试')
@allure.description('登录管理端')
def test_login_management():
    management_login()
