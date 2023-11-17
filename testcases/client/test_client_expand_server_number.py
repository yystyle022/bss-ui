# -*- coding=utf-8 -*-
# @Time : 2023/9/20 10:00
# @Author : yangyang
# @File : bss-ui/test_client_expand_server_number.py
import allure
from base.ClientHomeBase import HomeBase
from common.playwrightFunction import client_login, write_log_to_allure, screenshot_to_allure, expand_server_number


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌测试浏览器---实例列表扩容差分账号,扩容成功')
def test_instance_list_expand_server_number_chromium_browser(chromium_browser):
    client_login(chromium_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        chromium_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(chromium_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        chromium_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(chromium_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        chromium_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(chromium_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        chromium_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(chromium_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(chromium_browser)


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌测试浏览器---实例列表扩容差分账号,扩容1000个，扩容成功')
def test_instance_list_expand_1000_server_number_chromium_browser(chromium_browser):
    client_login(chromium_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        chromium_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(chromium_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        chromium_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(chromium_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        chromium_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(chromium_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        chromium_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(chromium_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(chromium_browser, sums='1000')


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌正式浏览器---实例列表扩容差分账号,扩容成功')
def test_instance_list_expand_server_number_chrome_browser(chrome_browser):
    client_login(chrome_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        chrome_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(chrome_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        chrome_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(chrome_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        chrome_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(chrome_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        chrome_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(chrome_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(chrome_browser)


@allure.feature('扩容差分账号测试用例')
@allure.title('谷歌正式浏览器---实例列表扩容差分账号,扩容1000个，扩容成功')
def test_instance_list_expand_1000_server_number_chrome_browser(chrome_browser):
    client_login(chrome_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        chrome_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(chrome_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        chrome_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(chrome_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        chrome_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(chrome_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        chrome_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(chrome_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(chrome_browser, sums='1000')


@allure.feature('扩容差分账号测试用例')
@allure.title('微软edge浏览器---实例列表扩容差分账号,扩容成功')
def test_instance_list_expand_server_number_edge_browser(edge_browser):
    client_login(edge_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        edge_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(edge_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        edge_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(edge_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        edge_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(edge_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        edge_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(edge_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(edge_browser)


@allure.feature('扩容差分账号测试用例')
@allure.title('微软edge浏览器---实例列表扩容差分账号,扩容1000个，扩容成功')
def test_instance_list_expand_1000_server_number_edge_browser(edge_browser):
    client_login(edge_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        edge_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(edge_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        edge_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(edge_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        edge_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(edge_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        edge_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(edge_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(edge_browser, sums='1000')


@allure.feature('扩容差分账号测试用例')
@allure.title('火狐浏览器---实例列表扩容差分账号,扩容成功')
def test_instance_list_expand_server_number_firefox_browser(firefox_browser):
    client_login(firefox_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        firefox_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(firefox_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        firefox_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(firefox_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        firefox_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(firefox_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        firefox_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(firefox_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(firefox_browser)


@allure.feature('扩容差分账号测试用例')
@allure.title('火狐浏览器---实例列表扩容差分账号,扩容1000个，扩容成功')
def test_instance_list_expand_1000_server_number_firefox_browser(firefox_browser):
    client_login(firefox_browser)

    with allure.step('点击首页右上角控制台按钮，进入控制台页面'):
        firefox_browser.click(HomeBase().consoleXpath())
        write_log_to_allure('点击首页右上角控制台按钮，进入控制台页面')
        screenshot_to_allure(firefox_browser, '进入控制台页面成功')

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        firefox_browser.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(firefox_browser, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        firefox_browser.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(firefox_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        firefox_browser.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(firefox_browser, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

    expand_server_number(firefox_browser, sums='1000')
