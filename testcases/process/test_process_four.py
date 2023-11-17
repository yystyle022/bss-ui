# -*- coding=utf-8 -*-
# @Time : 2023/10/20 14:10
# @Author : yangyang
# @File : bss-ui/test_process_four.py

import allure
import random
from common.userstestok import sdk_send_gga
from common.client_playwright_function import serach_instance_AK_AS, get_server_number_password, manual_active_server_number, manual_bind_server_number
from common.playwrightFunction import online_order_application_new_purchase_common_model, review_online_order_application, get_server_number, write_log_to_allure


@allure.feature('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用')
@allure.title('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用---谷歌正式浏览器')
def test_process_four_chrome_browser(chrome_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,手动激活手动绑定
    OrderNumber = online_order_application_new_purchase_common_model(chrome_browser, ActiveMethod='2', BindMethod='2', PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(chrome_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(chrome_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(chrome_browser, servernumber=ServerNumber)
    # 手动激活差分账号成功
    assert manual_active_server_number(chrome_browser, ServerNumber) == True
    # 手动绑定差分账号成功
    assert manual_bind_server_number(chrome_browser, ServerNumber) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用')
@allure.title('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用---谷歌测试浏览器')
def test_process_four_chromium_browser(chromium_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,手动激活手动绑定
    OrderNumber = online_order_application_new_purchase_common_model(chromium_browser, ActiveMethod='2', BindMethod='2', PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(chromium_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(chromium_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(chromium_browser, servernumber=ServerNumber)
    # 手动激活差分账号成功
    assert manual_active_server_number(chromium_browser, ServerNumber) == True
    # 手动绑定差分账号成功
    assert manual_bind_server_number(chromium_browser, ServerNumber) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用')
@allure.title('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用---微软Edge浏览器')
def test_process_four_edge_browser(edge_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,手动激活手动绑定
    OrderNumber = online_order_application_new_purchase_common_model(edge_browser, ActiveMethod='2', BindMethod='2', PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(edge_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(edge_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(edge_browser, servernumber=ServerNumber)
    # 手动激活差分账号成功
    assert manual_active_server_number(edge_browser, ServerNumber) == True
    # 手动绑定差分账号成功
    assert manual_bind_server_number(edge_browser, ServerNumber) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用')
@allure.title('管理端新购 ntrip或sdk 手动激活手动绑定 非实时激活 的正式账号 可以正常sdk登录使用---火狐浏览器')
def test_process_four_firefox_browser(firefox_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请,手动激活手动绑定
    OrderNumber = online_order_application_new_purchase_common_model(firefox_browser, ActiveMethod='2', BindMethod='2', PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(firefox_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(firefox_browser, ReviewOrderNumber=OrderNumber))
    # 获取差分账号密码
    PassWord = get_server_number_password(firefox_browser, servernumber=ServerNumber)
    # 手动激活差分账号成功
    assert manual_active_server_number(firefox_browser, ServerNumber) == True
    # 手动绑定差分账号成功
    assert manual_bind_server_number(firefox_browser, ServerNumber) == True
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(ServerNumber, PassWord) == True, '差分账号不可用'
