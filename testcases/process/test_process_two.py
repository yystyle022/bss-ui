# -*- coding=utf-8 -*-
# @Time : 2023/10/18 9:40
# @Author : yangyang
# @File : bss-ui/test_process_two.py
# 管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用

import allure
import random
from common.userstestok import auth, sdk_send_gga
from common.client_playwright_function import serach_instance_AK_AS
from common.playwrightFunction import online_order_application_new_purchase_common_model, review_online_order_application, get_server_number, write_log_to_allure


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用---谷歌测试浏览器')
def test_process_two_chromium_browser(chromium_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk登录正常收发差分数据
    @param chromium_browser:
    @return:
    '''
    # 线下订单申请
    OrderNumber = online_order_application_new_purchase_common_model(chromium_browser, PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(chromium_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(chromium_browser, ReviewOrderNumber=OrderNumber))
    # 根据差分账号获取实例的AK和AS
    AKAS = serach_instance_AK_AS(chromium_browser, ServerNumber)
    AK = AKAS[0]
    AS = AKAS[1]
    # 接口进行鉴权
    with allure.step('进行接口鉴权'):
        authResponse = auth(AK, AS)
        serverNumber = authResponse[0]
        password = authResponse[1]
        write_log_to_allure(f'鉴权成功，接口返回的差分账号为：{serverNumber}  密码为：{password}')
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(serverNumber, password) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用---谷歌正式浏览器')
def test_process_two_chrome_browser(chrome_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk登录正常收发差分数据
    @param chrome_browser:
    @return:
    '''
    # 线下订单申请
    OrderNumber = online_order_application_new_purchase_common_model(chrome_browser, PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(chrome_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(chrome_browser, ReviewOrderNumber=OrderNumber))
    # 根据差分账号获取实例的AK和AS
    AKAS = serach_instance_AK_AS(chrome_browser, ServerNumber)
    AK = AKAS[0]
    AS = AKAS[1]
    # 接口进行鉴权
    with allure.step('进行接口鉴权'):
        authResponse = auth(AK, AS)
        serverNumber = authResponse[0]
        password = authResponse[1]
        write_log_to_allure(f'鉴权成功，接口返回的差分账号为：{serverNumber}  密码为：{password}')
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(serverNumber, password) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用---微软Edge浏览器')
def test_process_two_edge_browser(edge_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk登录正常收发差分数据
    @param edge_browser:
    @return:
    '''
    # 线下订单申请
    OrderNumber = online_order_application_new_purchase_common_model(edge_browser, PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(edge_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(edge_browser, ReviewOrderNumber=OrderNumber))
    # 根据差分账号获取实例的AK和AS
    AKAS = serach_instance_AK_AS(edge_browser, ServerNumber)
    AK = AKAS[0]
    AS = AKAS[1]
    # 接口进行鉴权
    with allure.step('进行接口鉴权'):
        authResponse = auth(AK, AS)
        serverNumber = authResponse[0]
        password = authResponse[1]
        write_log_to_allure(f'鉴权成功，接口返回的差分账号为：{serverNumber}  密码为：{password}')
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(serverNumber, password) == True, '差分账号不可用'


@allure.feature('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用')
@allure.title('管理端新购 ntrip或sdk 自动激活自动绑定 非实时激活 的正式账号 鉴权成功后 sdk可以正常登录使用---火狐浏览器')
def test_process_two_firefox_browser(firefox_browser):
    '''
    测试新购账号后，可以鉴权和登录，sdk登录正常收发差分数据
    @param firefox_browser:
    @return:
    '''
    # 线下订单申请
    OrderNumber = online_order_application_new_purchase_common_model(firefox_browser, PurchaseSums=f'{random.randint(1, 5)}')
    # 财务审核申请订单
    review_online_order_application(firefox_browser, OrderNumber)
    # 获取申请的差分账号
    ServerNumber = random.choice(get_server_number(firefox_browser, ReviewOrderNumber=OrderNumber))
    # 根据差分账号获取实例的AK和AS
    AKAS = serach_instance_AK_AS(firefox_browser, ServerNumber)
    AK = AKAS[0]
    AS = AKAS[1]
    # 接口进行鉴权
    with allure.step('进行接口鉴权'):
        authResponse = auth(AK, AS)
        serverNumber = authResponse[0]
        password = authResponse[1]
        write_log_to_allure(f'鉴权成功，接口返回的差分账号为：{serverNumber}  密码为：{password}')
    # 登录账号验证是否可用
    with allure.step('登录差分账号验证是否可用'):
        assert sdk_send_gga(serverNumber, password) == True, '差分账号不可用'
