# -*- coding=utf-8 -*-
# @Time : 2023/10/13 14:36
# @Author : yangyang
# @File : bss-ui/client_playwright_function.py

import re
import allure
import random
from time import sleep
from base.ClientHomeBase import HomeBase
from base.ClientLeftNavigationBar import ClientLeftNavigationBar
from common.playwrightFunction import click_step, fill_step, write_log_to_allure, screenshot_to_allure, client_login


def manual_active_server_number(page, servernumber: str, productName: str = "1", type: str = '0'):
    '''
    手动激活差分账号
    @param page:
    @param instanceId:
    @param servernumber:
    @param productName:
    @return:
    '''
    if type == '1':
        click_step(page=page, describe='点击控制台左侧导航栏【服务号管理】', position=ClientLeftNavigationBar().accountManagementXpath())
        click_step(page=page, describe='点击控制台左侧导航栏【厘米级服务】', position=ClientLeftNavigationBar().accountCmXpath())
        click_step(page=page, describe='点击控制台左侧导航栏厘米级服务下的【正式账号】', position=ClientLeftNavigationBar().accountCmFormalNumberXpath())
    page.wait_for_selector("//span[text()='批量激活']")
    click_step(page=page, describe='点击产品名称弹出产品名称选择列表', position="//div[text()=' 厘清/Locate-CM ']")
    if productName == '1':
        click_step(page=page, describe='选择产品为：厘清', position="//li[text()=' 厘清/Locate-CM ']")
    elif productName == '2':
        click_step(page=page, describe='选择产品为：星璨', position="//li[text()=' 星璨/Orion ']")
    fill_step(page=page, describe='输入差分账号进行查询', position="//label[@title='差分账号']/../following-sibling::div//input", number=servernumber)
    click_step(page=page, describe='点击查询按钮进行查询差分账号', position="//span[text()='查 询']")
    page.wait_for_selector(f"//td[text()='{servernumber}']")
    click_step(page=page, describe='点击差分账号激活按钮进行激活', position=f"//td[text()='{servernumber}']/..//a[text()='激活']")
    sleep(3)
    ActiveTime = page.query_selector(f"//td[text()='{servernumber}']/..//td[10]").text_content()
    ExpireTime = page.query_selector(f"//td[text()='{servernumber}']/..//td[11]/span").text_content()
    if ActiveTime and ExpireTime:
        write_log_to_allure(f'差分账号{servernumber}激活成功，激活时间为:{ActiveTime},到期时间为：{ExpireTime}')
        screenshot_to_allure(page, name=f'差分账号{servernumber}激活成功截图')
        print(f'差分账号{servernumber}激活成功，激活时间为:{ActiveTime},到期时间为：{ExpireTime}')
        return True
    else:
        write_log_to_allure(f'差分账号{servernumber}激活失败，请重试')
        screenshot_to_allure(page, name=f'差分账号{servernumber}激活失败截图')
        print(f'差分账号{servernumber}激活失败截图')
        return False


def manual_bind_server_number(page, servernumber: str, productName: str = "1", type: str = '0'):
    '''
    手动绑定差分账号
    @param page: 驱动
    @param servernumber: 差分账号
    @param productName: 产品名称
    @param deviceType: 设备类型
    @param deviceId: 设备Id
    @return:
    '''
    deivceType = f"uiceshi{random.randint(20000, 30000)}"
    if type == '1':
        click_step(page=page, describe='点击控制台左侧导航栏【服务号管理】', position=ClientLeftNavigationBar().accountManagementXpath())
        click_step(page=page, describe='点击控制台左侧导航栏【厘米级服务】', position=ClientLeftNavigationBar().accountCmXpath())
        click_step(page=page, describe='点击控制台左侧导航栏厘米级服务下的【正式账号】', position=ClientLeftNavigationBar().accountCmFormalNumberXpath())
    page.wait_for_selector("//span[text()='批量激活']")
    click_step(page=page, describe='点击产品名称弹出产品名称选择列表', position="//div[text()=' 厘清/Locate-CM ']")
    if productName == '1':
        click_step(page=page, describe='选择产品为：厘清', position="//li[text()=' 厘清/Locate-CM ']")
    elif productName == '2':
        click_step(page=page, describe='选择产品为：星璨', position="//li[text()=' 星璨/Orion ']")
    fill_step(page=page, describe='输入差分账号进行查询', position="//label[@title='差分账号']/../following-sibling::div//input", number=servernumber)
    click_step(page=page, describe='点击查询按钮进行查询差分账号', position="//span[text()='查 询']")
    page.wait_for_selector(f"//td[text()='{servernumber}']")
    click_step(page=page, describe='点击账号列表下拉菜单按钮', position=f"//td[text()='{servernumber}']/..//span[@class='expand-icon']")
    click_step(page=page, describe='点击差分账号绑定按钮，弹出绑定设备弹窗', position=f"//td[text()='{servernumber}']/../following-sibling::tr//a[text()=' 绑定 ']")
    fill_step(page=page, describe=f'输入绑定的设备Id为：{deivceType}', position="//input[@placeholder='请输入ID/SN']", number=deivceType)
    fill_step(page=page, describe=f'输入绑定的设备类型为：{deivceType}', position="//input[@placeholder='请输入设备类型']", number=deivceType)
    click_step(page=page, describe='点击确定按钮提交绑定信息', position="//span[text()='确 定']")
    sleep(5)
    ServerNumberBindDeviceId = page.query_selector(f"//td[text()='{servernumber}']/../following-sibling::tr//span[text()=' 设备ID/SN: ']/following-sibling::span").text_content()
    ServerNumberBindDeviceType = page.query_selector(f"//td[text()='{servernumber}']/../following-sibling::tr//span[text()=' 设备类型： ']/following-sibling::span").text_content()
    if ServerNumberBindDeviceId == deivceType and ServerNumberBindDeviceType == deivceType:
        write_log_to_allure(f'差分账号{servernumber}绑定设备成功，绑定的设备类型为：{deivceType}，绑定的设备ID为：{deivceType}')
        screenshot_to_allure(page, name=f'差分账号{servernumber}绑定成功截图')
        print(f'差分账号{servernumber}绑定设备成功，绑定的设备类型为：{deivceType}，绑定的设备ID为：{deivceType}')
        return True
    else:
        write_log_to_allure(f'差分账号{servernumber}绑定设备失败，请重试')
        screenshot_to_allure(page, name=f'差分账号{servernumber}绑定设备失败截图')
        print(f'差分账号{servernumber}绑定失败')
        return False


def get_server_number_password(page, servernumber: str, productName: str = '1'):
    '''
    获取差分账号密码
    @param page: 驱动
    @param servernumber: 差分账号
    @param productName: 产品名称
    @return:
    '''
    # 登录官网成功
    client_login(page)
    click_step(page=page, describe='点击首页左上角控制台按钮，进入控制台页面', position=HomeBase().consoleXpath())
    click_step(page=page, describe='点击控制台页面左侧导航栏服务号管理菜单', position="//span[text()='服务号管理']")
    click_step(page=page, describe='点击控制台页面左侧导航栏服务号管理-厘米级服务', position="//span[text()='厘米级服务']")
    click_step(page=page, describe='点击控制台页面左侧导航栏服务号管理-厘米级服务-正式账号', position="//span[text()='正式账号']")
    page.wait_for_selector("//span[text()='批量激活']")
    click_step(page=page, describe='点击产品名称弹出产品名称选择列表', position="//div[text()=' 厘清/Locate-CM ']")
    if productName == '1':
        click_step(page=page, describe='选择产品为：厘清', position="//li[text()=' 厘清/Locate-CM ']")
    elif productName == '2':
        click_step(page=page, describe='选择产品为：星璨', position="//li[text()=' 星璨/Orion ']")
    fill_step(page=page, describe='输入差分账号进行查询', position="//label[@title='差分账号']/../following-sibling::div//input", number=servernumber)
    click_step(page=page, describe='点击查询按钮进行查询差分账号', position="//span[text()='查 询']")
    page.wait_for_selector(f"//td[text()='{servernumber}']")
    click_step(page=page, describe='点击查看按钮，查看差分账号密码', position=f"//td[text()='{servernumber}']/../td[6]/a[2]")
    password = page.query_selector("//div[@role='tooltip']").text_content()
    write_log_to_allure(f'差分账号{servernumber}密码为：{password}')
    screenshot_to_allure(page, name=f'差分账号{servernumber}密码为：{password},截图')
    print(f'差分账号{servernumber}密码为：{password}')
    return password


def serach_instance_AK_AS(page, servernumber, productName: str = '1'):
    '''
    根据差分账号查找实例
    @param serverNumber:
    @return:
    '''
    # 登录官网成功
    client_login(page)
    click_step(page=page, describe='点击首页左上角控制台按钮，进入控制台页面', position=HomeBase().consoleXpath())
    click_step(page=page, describe='点击控制台页面左侧导航栏服务号管理菜单', position="//span[text()='服务号管理']")
    click_step(page=page, describe='点击控制台页面左侧导航栏服务号管理-厘米级服务', position="//span[text()='厘米级服务']")
    click_step(page=page, describe='点击控制台页面左侧导航栏服务号管理-厘米级服务-正式账号', position="//span[text()='正式账号']")
    page.wait_for_selector("//span[text()='批量激活']")
    click_step(page=page, describe='点击产品名称弹出产品名称选择列表', position="//div[text()=' 厘清/Locate-CM ']")
    if productName == '1':
        click_step(page=page, describe='选择产品为：厘清', position="//li[text()=' 厘清/Locate-CM ']")
    elif productName == '2':
        click_step(page=page, describe='选择产品为：星璨', position="//li[text()=' 星璨/Orion ']")
    fill_step(page=page, describe='输入差分账号进行查询', position="//label[@title='差分账号']/../following-sibling::div//input", number=servernumber)
    click_step(page=page, describe='点击查询按钮进行查询差分账号', position="//span[text()='查 询']")
    page.wait_for_selector(f"//td[text()='{servernumber}']")
    with allure.step('获取差分账号的实例ID'):
        InstanceId = page.query_selector(f"//td[text()='{servernumber}']/../td[4]").text_content()
        write_log_to_allure(f'差分账号{servernumber}实例ID为：{InstanceId}')
        screenshot_to_allure(page, name=f'差分账号{servernumber}实例ID为：{InstanceId} 截图')
    click_step(page=page, describe='点击控制台页面左侧导航栏实例，返回实例查询页面', position="//span[text()='实例']")
    fill_step(page=page, describe='输入实例进行查询', position="//input", number=f"{InstanceId}")
    click_step(page=page, describe='点击查询按钮进行实例查询', position="//span[text()='查 询']")
    with allure.step('获取实例AK'):
        AK = re.sub(r"[^0-9]", "", page.query_selector(f"//td[text()='{InstanceId}']/../td[8]").text_content())
        write_log_to_allure(f'实例的AK为：{AK}')
        screenshot_to_allure(page, name=f'实例的AK截图')
    click_step(page=page, describe='点击AS查看按钮进行AS查看', position="//a[text()='查看']")
    with allure.step('获取实例AS'):
        AS = page.query_selector(f"//div[@role='tooltip']").text_content()
        write_log_to_allure(f'实例的AK为：{AS}')
        screenshot_to_allure(page, name=f'实例的AS截图')
    return AK, AS
