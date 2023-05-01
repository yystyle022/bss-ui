# -*- coding: utf-8 -*-
# @Time : 2023/3/14 21:51
# @Author : yangyang
# @File : UI/LoginPage.py


import allure
from time import sleep
from page.HomePage import HomePage
from page.ObjectMap import ObjectMap
from base.ClientLoginBase import LoginBase
from logs.log_config import log
from page.SliderVerificationPage import SliderVerificationPage
from common.report_add_img import add_img_to_report


class LoginPage():

    def login_input_value(self, driver, input_placeholder, input_value):
        '''
        登录页面输入框内输入内容
        @param driver: 驱动
        @param input_placeholder: 输入框
        @param input_value: 输入框内的值
        @return:
        '''
        driver.find_element('xpath', LoginBase().loginInputXpath(input_placeholder)).send_keys(input_value)

    def click_sumbit_button(self, driver):
        '''
        点击登录按钮
        @param driver: 驱动
        @return:
        '''
        driver.find_element('xpath', LoginBase().submitButtonXpath()).click()

    def GetUrl(self, driver, url):
        '''
        打开网址进入首页
        @param driver: 驱动
        @param url: 地址
        @return:
        '''
        return driver.get(url)

    def assert_login_success(self, driver):
        '''
        验证是否登陆成功
        @param driver:
        @return:
        '''
        successLoginXpath = LoginBase().loginSuccessXpath()
        assert ObjectMap().element_appear(driver, locateType='xpath', locateValue=successLoginXpath,
                                          timeout=5), "未进入首页，登录失败"

    def assert_management_login_success(self, driver):
        '''
        验证管理端登录成功
        @param driver:
        @return:
        '''
        managementSuccessLoginXpath = LoginBase().managementLoginSuccessXpath()
        assert ObjectMap().element_appear(driver, locateType='xpath', locateValue=managementSuccessLoginXpath,
                                          timeout=5),"未进入首页，登录失败"

    def login(self, driver, url, username, password):
        '''
        登录客户端
        @param driver:
        @param user:
        @return:
        '''
        with allure.step('打开网址，进入首页'):
            self.GetUrl(driver, url)
            log.info('打开网址:' + url + ',进入首页')
            add_img_to_report(driver, '打开网址')
        with allure.step('点击登录，进入登录页面'):
            HomePage().click_login_button(driver)
            log.info('点击首页登录按钮，进入账号密码输入页面')
            add_img_to_report(driver, '点击首页登录按钮，进入账号密码输入页面')
        with allure.step('输入账号密码'):
            self.login_input_value(driver, '请输入账号或手机号码', username)
            self.login_input_value(driver, '请输入密码', password)
            log.info('输入用户名:{},输入密码{}'.format(username, password))
            add_img_to_report(driver, '输入账号密码')
        with allure.step('点击登录按钮'):
            self.click_sumbit_button(driver)
            log.info('点击登录按钮')
            add_img_to_report(driver, '点击登录按钮')
            sleep(3)
        with allure.step('滑动滑块验证'):
            elements_3 = SliderVerificationPage().get_3_ele(driver)
            SliderVerificationPage().move_slider(driver, *elements_3)
            log.info('滑动滑块验证')
            add_img_to_report(driver, '滑动滑块进行验证')
            self.assert_login_success(driver)

    def login_management(self, driver, managementUrl, managementUser, managementPwd):
        '''
        登录管理端
        @param driver:
        @param managementUrl:
        @param managementUser:
        @param managementPwd:
        @return:
        '''
        with allure.step('打开网址，进入首页'):
            self.GetUrl(driver, managementUrl)
            log.info('打开网址:' + managementUrl + ',进入首页')
            add_img_to_report(driver, '打开网址')
        with allure.step('输入账号密码'):
            self.login_input_value(driver, '账号或手机号', managementUser)
            self.login_input_value(driver, '密码', managementPwd)
            log.info('输入用户名:{},输入密码{}'.format(managementUser, managementPwd))
            add_img_to_report(driver, '输入账号密码')
        with allure.step('点击登录按钮'):
            self.click_sumbit_button(driver)
            log.info('点击登录按钮')
            add_img_to_report(driver, '点击登录按钮')
            sleep(3)
            self.assert_management_login_success(driver)
