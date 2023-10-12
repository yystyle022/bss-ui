# -*- coding=utf-8 -*-
# @Time : 2023/10/7 17:25
# @Author : yangyang
# @File : bss-ui/test_management_online_order_application_new_purchase.py
import allure
from common.playwrightFunction import online_order_application_new_purchase_common_model, review_online_order_application


@allure.feature('管理端线下订单申请-新购')
@allure.title('管理端线下订单申请---新购自动激活自动绑定无测试期非实时激活账号---谷歌测试浏览器')
def test_online_order_application_new_purchase_chromium_browser(chromium_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请
    orderNumber = online_order_application_new_purchase_common_model(chromium_browser)
    # 财务审核
    review_online_order_application(chromium_browser, orderNumber)


@allure.feature('管理端线下订单申请-新购')
@allure.title('管理端线下订单申请-新购自动激活自动绑定无测试期非实时激活账号---谷歌正式浏览器')
def test_online_order_application_new_purchase_chrome_browser(chrome_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    orderNumber = online_order_application_new_purchase_common_model(chrome_browser)
    review_online_order_application(chrome_browser, orderNumber)


@allure.feature('管理端线下订单申请-新购')
@allure.title('管理端线下订单申请-新购自动激活自动绑定无测试期非实时激活账号---微软Edge浏览器')
def test_online_order_application_new_purchase_edge_browser(edge_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    orderNumber = online_order_application_new_purchase_common_model(edge_browser)
    review_online_order_application(edge_browser, orderNumber)


@allure.feature('管理端线下订单申请-新购')
@allure.title('管理端线下订单申请-新购自动激活自动绑定无测试期非实时激活账号---火狐浏览器')
def test_online_order_application_new_purchase_firefox_browser(firefox_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    orderNumber = online_order_application_new_purchase_common_model(firefox_browser)
    review_online_order_application(firefox_browser, orderNumber)
