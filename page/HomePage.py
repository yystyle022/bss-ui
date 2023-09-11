# -*- coding=utf-8 -*-
# @Time : 2023/3/17 16:51
# @Author : yangyang
# @File : UI/HomePage.py
from selenium.webdriver import ActionChains
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

    def move_to_liqing_title(self,driver):
        '''
        移动鼠标指针到厘清的标题上
        @param driver:
        @return:
        '''
        #获取标题
        liqingHomePageTitleXpath = HomeBase().liqingHomePageTitleXpath()
        liqingHomePageTitle = driver.find_element('xpath', liqingHomePageTitleXpath)
        #获取鼠标指针事件
        actions = ActionChains(driver)
        #移动鼠标指针到标题上
        actions.move_to_element(liqingHomePageTitle)
        #执行操作
        actions.perform()


    def click_liqing_homepage_purchase_button(self,driver):
        '''
        点击厘清的立即购买按钮
        @param driver:
        @return:
        '''
        liqingHomePagePurchaseButtonXpath = HomeBase().liqingHomePagePurchaseButtonXpath()
        driver.find_element('xpath', liqingHomePagePurchaseButtonXpath).click()




