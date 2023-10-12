# -*- coding=utf-8 -*-
# @Time : 2023/9/19 15:46
# @Author : yangyang
# @File : bss-ui/test_client_purchase_server_number.py

import allure
from time import sleep
from base.ClientHomeBase import HomeBase
from playwright.sync_api import sync_playwright
from base.ClientConsoleBase import ClientConsoleBase
from base.ClientLiQingDetailsBase import ClientLiQingDetailsBase
from common.playwrightFunction import client_login, write_log_to_allure, screenshot_to_allure, assert_element_exist, purchase_server_number


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买手动激活、手动绑定方式的厘清账号')
def test_fontpage_purchase_liqing_manualactive_manualbind(chrome_browser):
    page = chrome_browser
    client_login(page)
    with allure.step('点击首页厘清购买按钮，进入厘清页面'):
        page.click(HomeBase().liqingHomePageTitleXpath())
        write_log_to_allure('鼠标移动到厘清icon上，点击后展示出厘清购买按钮')
        screenshot_to_allure(page, '鼠标移动到厘清icon上，点击后展示出厘清购买按钮')
        sleep(0.5)
        page.click(HomeBase().liqingHomePagePurchaseButtonXpath())
        write_log_to_allure('点击购买按钮进入详情厘清详情页面')
        screenshot_to_allure(page, '点击购买按钮进入详情厘清详情页面')

    with allure.step('验证是否进入厘清详情页面'):
        assert_element_exist(page, ClientLiQingDetailsBase().manualActiveMethodXpath())
        write_log_to_allure('验证是否进入厘清详情页面，查看页面是否存在手动激活元素，手动激活元素存在，页面进入成功')
        screenshot_to_allure(page, '验证是否进入厘清详情页面')

    purchase_server_number(page, active=2, bind=2, duration=2, sums="5")


@allure.feature('购买差分账号测试用例')
@allure.title('官网首页购买自动激活、自动绑定方式的厘清账号')
def test_fontpage_purchase_liqing_autoactive_autobind(chrome_browser):
    page = chrome_browser
    client_login(page)
    with allure.step('点击首页厘清购买按钮，进入厘清页面'):
        page.click(HomeBase().liqingHomePageTitleXpath())
        write_log_to_allure('鼠标移动到厘清icon上，点击后展示出厘清购买按钮')
        screenshot_to_allure(page, '鼠标移动到厘清icon上，点击后展示出厘清购买按钮')
        sleep(0.5)
        page.click(HomeBase().liqingHomePagePurchaseButtonXpath())
        write_log_to_allure('点击购买按钮进入详情厘清详情页面')
        screenshot_to_allure(page, '点击购买按钮进入详情厘清详情页面')

    with allure.step('验证是否进入厘清详情页面'):
        assert_element_exist(page, ClientLiQingDetailsBase().manualActiveMethodXpath())
        write_log_to_allure('验证是否进入厘清详情页面，查看页面是否存在手动激活元素，手动激活元素存在，页面进入成功')
        screenshot_to_allure(page, '验证是否进入厘清详情页面')

    purchase_server_number(page, duration=1, sums="3")


@allure.feature('购买差分账号测试用例')
@allure.title('控制台购买手动激活、手动绑定方式的厘清账号')
def test_console_purchase_liqing_manualactive_manualbind(chrome_browser):
    page = chrome_browser
    client_login(page)
    with allure.step('点击首页左上角控制台按钮，进入控制台页面'):
        page.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页左上角控制台按钮，进入控制台页面')
        screenshot_to_allure(page, '进入控制台页面成功')

    with allure.step('点击厘米级购买账号按钮，进入厘清详情页面'):
        page.click(ClientConsoleBase().purchaseCmAccountButtonXpath())
        write_log_to_allure('点击厘米级购买账号按钮，进入厘清详情页面')
        screenshot_to_allure(page, '进入厘清详情页面成功')

    purchase_server_number(page, active=2, bind=2, duration=2, sums="4")


@allure.feature('购买差分账号测试用例')
@allure.title('控制台购买自动激活、自动绑定方式的厘清账号')
def test_console_purchase_liqing_autoactive_autobind(chrome_browser):
    page = chrome_browser
    client_login(page)
    with allure.step('点击首页左上角控制台按钮，进入控制台页面'):
        page.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页左上角控制台按钮，进入控制台页面')
        screenshot_to_allure(page, '进入控制台页面成功')

    with allure.step('点击厘米级购买账号按钮，进入厘清详情页面'):
        page.click(ClientConsoleBase().purchaseCmAccountButtonXpath())
        write_log_to_allure('点击厘米级购买账号按钮，进入厘清详情页面')
        screenshot_to_allure(page, '进入厘清详情页面成功')

    purchase_server_number(page, duration=2, sums="6")
