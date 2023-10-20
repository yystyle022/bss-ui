# -*- coding=utf-8 -*-
# @Time : 2023/10/12 9:40
# @Author : yangyang
# @File : bss-ui/test_management_online_order_application_expand.py
import allure
from common.playwrightFunction import online_order_application_expand_common_model, review_online_order_application


@allure.feature('管理端线下订单申请-扩容')
@allure.title('管理端线下订单申请---扩容自动激活自动绑定无测试期非实时激活账号---谷歌测试浏览器')
def test_online_order_application_expand_chromium_browser(chromium_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请
    orderNumber = online_order_application_expand_common_model(chromium_browser)
    # 财务审核
    review_online_order_application(chromium_browser, orderNumber)


@allure.feature('管理端线下订单申请-扩容')
@allure.title('管理端线下订单申请---扩容自动激活自动绑定无测试期非实时激活账号---谷歌浏览器')
def test_online_order_application_expand_chrome_browser(chrome_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请
    orderNumber = online_order_application_expand_common_model(chrome_browser)
    # 财务审核
    review_online_order_application(chrome_browser, orderNumber)


@allure.feature('管理端线下订单申请-扩容')
@allure.title('管理端线下订单申请---扩容自动激活自动绑定无测试期非实时激活账号---微软Edge浏览器')
def test_online_order_application_expand_edge_browser(edge_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请
    orderNumber = online_order_application_expand_common_model(edge_browser)
    # 财务审核
    review_online_order_application(edge_browser, orderNumber)


@allure.feature('管理端线下订单申请-扩容')
@allure.title('管理端线下订单申请---扩容自动激活自动绑定无测试期非实时激活账号---火狐浏览器')
def test_online_order_application_expand_firefox_browser(firefox_browser):
    '''
    线下订单申请测试用例---新购
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请
    orderNumber = online_order_application_expand_common_model(firefox_browser)
    # 财务审核
    review_online_order_application(firefox_browser, orderNumber)
