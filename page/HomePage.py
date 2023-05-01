# -*- coding=utf-8 -*-
# @Time : 2023/3/17 16:51
# @Author : yangyang
# @File : UI/HomePage.py

from base.ClientHomeBase import HomeBase


class HomePage():

    def click_login_button(self, driver):
        '''
        点击首页登录按钮
        @param driver: 驱动
        @return:
        '''
        loginButtonXpath = HomeBase().loginButtonXpath()
        driver.find_element('xpath', loginButtonXpath).click()

    def click_register_button(self, driver):
        '''
        点击首页注册按钮
        @param driver: 驱动
        @return:
        '''
        registerButtonXpath = HomeBase().registerButtonXpath()
        driver.find_element('xpath', registerButtonXpath)
