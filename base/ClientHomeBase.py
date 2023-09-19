# -*- coding=utf-8 -*-
# @Time : 2023/3/17 16:50
# @Author : yangyang
# @File : UI/ClientHomeBase.py

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

    def liqingHomePageTitleXpath(self):
        '''
        首页厘清icon的xpath
        @return:
        '''
        return "//h5[text()='厘清/Locate-CM']"

    def liqingHomePagePurchaseButtonXpath(self):
        '''
        首页厘清购买按钮xpath
        @return:
        '''
        return "//h5[text()='厘清/Locate-CM']/..//span[text()='立即购买']"

    def consoleXpath(self):
        '''
        首页控制台xpath
        @return:
        '''
        return "//a[contains(text(),'控制台')]"
