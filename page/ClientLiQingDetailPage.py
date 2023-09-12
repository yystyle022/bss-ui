# -*- coding=utf-8 -*-
# @Time : 2023/9/11 10:38
# @Author : yangyang
# @File : bss-ui/ClientLiQingDetailPage.py
import allure
from time import sleep
from page.HomePage import HomePage
from page.ObjectMap import ObjectMap
from logs.log_config import log
from common.report_add_img import add_img_to_report
from base.ClientLiQingDetailsBase import ClientLiQingDetailsBase


class ClientLiQingDetailPage:
    '''
    厘清购买相关页面操作
    '''

    def choice_active_method(self, driver, active=1):
        '''
        选择激活方式
        @param driver:
        @param active:
        @return:
        '''
        if active == 2:
            driver.find_element('xpath', ClientLiQingDetailsBase().manualActiveMethodXpath()).click()

    def choice_bind_method(self, driver, bind=1):
        '''
        选择绑定方式
        @param driver:
        @param bind:
        @return:
        '''
        if bind == 2:
            driver.find_element('xpath', ClientLiQingDetailsBase().manualActiveMethodXpath()).click()

    def purchaseLiQing(self, driver, active, bind, duration, sum):
        '''
        购买厘清账号
        @return:
        '''
        with allure.step('选择购买时长'):
            if duration == 1:
                driver.find_element('xpath', ClientLiQingDetailsBase().purchaseDurationOneDayXpath()).click()
            elif duration == 2:
                driver.find_element('xpath', ClientLiQingDetailsBase().purchaseDurationOneMonthXpath()).click()
            elif duration == 3:
                driver.find_element('xpath', ClientLiQingDetailsBase().purchaseDurationOneYearXpath()).click()
            else:
                pass
            add_img_to_report(driver, '选择购买时长')
        with allure.step('选择激活方式'):
            if active == 2:
                driver.find_element('xpath', ClientLiQingDetailsBase().manualActiveMethodXpath()).click()
            else:
                pass
            add_img_to_report(driver, '选择激活方式')
        with allure.step('选择绑定方式'):
            if bind == 2:
                driver.find_element('xpath', ClientLiQingDetailsBase().manualActiveMethodXpath()).click()
            else:
                pass
            add_img_to_report(driver, '选择绑定方式')
        with allure.step('填写购买数量'):
            driver.find_element('xpath', ClientLiQingDetailsBase().purchaseSumXpath()).sendkeys(sum)
            add_img_to_report(driver, '填写购买数量')
        with allure.step('点击立即购买'):
            driver.find_element('xpath', ClientLiQingDetailsBase().purchaseButtonXpath()).click()
            add_img_to_report(driver, '点击立即购买进入提交订单页面')
        with allure.step('点击提交订单'):
            driver.find_element('xpath', ClientLiQingDetailsBase().submitOrderButtonXpath()).click()
            add_img_to_report(driver, '点击提交订单,进入确认支付页面')
        with allure.step('点击确认支付'):
            driver.find_element('xpath', ClientLiQingDetailsBase().confirmPaymentButtonXpath()).click()
            add_img_to_report(driver, '点击确认支付，进入支付成功页面')
        with allure.step('验证是否支付成功'):
            assert ObjectMap().element_appear(driver, locateType='xpath', locateValue=ClientLiQingDetailsBase().paySuccessIdentificationXpath(), timeout=5), "支付失败"
