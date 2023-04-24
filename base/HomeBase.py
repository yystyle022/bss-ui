# -*- coding=utf-8 -*-
# @Time : 2023/3/17 16:50
# @Author : yangyang
# @File : UI/HomeBase.py

class HomeBase:

    def loginButtonXpath(self):
        '''
        首页登录xpath
        @return:
        '''
        return "//a[contains(text(),'登录')]"

    def registerButtonXpath(self):
        '''
        首页注册xpath
        @return:
        '''
        return "//a[contains(text(),'注册')]"
