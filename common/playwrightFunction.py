# -*- coding=utf-8 -*-
# @Time : 2023/9/19 9:36
# @Author : yangyang
# @File : bss-ui/playwrightFunction.py
# -*- coding=utf-8 -*-
# @Time : 2023/9/18 14:26
# @Author : yangyang
# @File : playwright/test.py
import os
import cv2
import allure
import requests
import numpy as np
from time import sleep
from datetime import datetime
from playwright.sync_api import sync_playwright
from base.ClientLiQingDetailsBase import ClientLiQingDetailsBase

clientURL = "https://bss-front-uat.sixents.com"
clientUsername = "18322369885"
clientPassword = "YANGyang022"
managementURL = "https://bss-backend-uat.sixents.com"
managementUsername = "sixents"
managementPassword = "$Nbiud8po23%yf*F"
currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def dragbox_location(page):
    dragbox_bounding = page.frame_locator("//iframe[@id='tcaptcha_iframe']").locator("//img[@id = 'slideBlock']").bounding_box()
    if dragbox_bounding is not None and dragbox_bounding["x"] > 20:
        return dragbox_bounding


def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)


def download_images(page, image_name, frame_xpath, image_xpath, save_directory):
    frame = page.frame_locator(frame_xpath)
    if not frame:
        print("Frame not found for the given XPath.")
        return
    # 定位图片images
    images = frame.locator(image_xpath)
    if not images:
        print("No images found for the given XPath.")
        return
    # 创建图片文件夹
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    # 获取图片下载src
    src = images.get_attribute('src')
    if src:
        image_filename = f'{image_name}.jpg'  # 根据需求修改文件名
        image_save_path = os.path.join(save_directory, image_filename)
        download_image(src, image_save_path)
        print(f'Downloaded image to: {image_save_path}')


def get_slide_distance():
    '''
    获取未补偿前的滑动距离
    @return:
    '''
    slider = "picture/slider.jpg"
    background = "picture/background.jpg"
    slider_pic = cv2.imread(slider, 0)
    background_pic = cv2.imread(background, 0)
    # 获取缺口图数组的形状 -->缺口图的宽和高
    width, height = slider_pic.shape[::-1]
    # 将处理之后的图片另存
    slider01 = "picture/slider01.jpg"
    background_01 = "picture/background01.jpg"
    cv2.imwrite(background_01, background_pic)
    cv2.imwrite(slider01, slider_pic)
    # 读取另存的滑块图
    slider_pic = cv2.imread(slider01)
    # 进行色彩转换
    slider_pic = cv2.cvtColor(slider_pic, cv2.COLOR_BGR2GRAY)
    # 获取色差的绝对值
    slider_pic = abs(255 - slider_pic)
    # 保存图片
    cv2.imwrite(slider01, slider_pic)
    # 读取滑块
    slider_pic = cv2.imread(slider01)
    # 读取背景图
    background_pic = cv2.imread(background_01)
    # 比较两张图的重叠区域
    result = cv2.matchTemplate(slider_pic, background_pic, cv2.TM_CCOEFF_NORMED)
    # 获取图片的缺口位置
    top, left = np.unravel_index(result.argmax(), result.shape)
    # 背景图中的图片缺口坐标位置
    print("当前滑块的缺口位置：", (left, top, left + width, top + height))
    return left


def get_slide_locus(distance):
    '''
    获取滑块的滑动点，以列表形式输出
    @param distance: 计算出的滑动距离
    @return: 返回滑动点的列表
    '''
    distance += 8
    v = 0
    m = 0.312
    # 保存0.3内的位移
    tracks = []
    current = 0
    mid = distance * 4 / 5
    # 判断每次滑动后的距离是否小于滑动距离
    while current <= distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0 * m + 0.5 * a * (m ** 2)
        current += s
        tracks.append(round(s))
        v = v0 + a * m
    return tracks


def screenshot_to_allure(page, name):
    '''
    截图放入allure测试报告
    @param page:
    @param path:
    @param name:
    @return:
    '''
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    path = f'../result/{name}.png'
    sleep(1)
    page.screenshot(timeout=5000, path=path)
    allure.attach.file(path, name=name, attachment_type=allure.attachment_type.PNG)


def write_log_to_allure(text):
    '''
    写入日志到allure测试报告
    @param text:
    @return:
    '''
    allure.attach(f'{currentTime}  {text}', name='runlog', attachment_type=allure.attachment_type.TEXT)


def assert_element_exist(page, element):
    '''
    登录成功断言
    @param page:
    @param element:
    @return:
    '''
    assert page.locator(element).count() > 0, '页面进入失败'


def client_login(page):
    '''
    登录官网
    @param page:
    @return:
    '''
    with allure.step('打开官网进入首页'):
        page.goto(clientURL)
        write_log_to_allure(f'打开官网{clientURL},进入首页成功')
        screenshot_to_allure(page, '打开官网进入首页')

    with allure.step('点击登录按钮'):
        page.click('//a[contains(text(),"登录")]')
        write_log_to_allure('点击页面左上角登录按钮，进入登录页面成功')
        screenshot_to_allure(page, '点击登录按钮进入登录页面')

    with allure.step('输入用户名'):
        page.fill('//input[@placeholder="请输入账号或手机号码"]', clientUsername)
        write_log_to_allure(f'输入用户名:{clientUsername}')
        screenshot_to_allure(page, '输入用户名')

    with allure.step('输入密码'):
        page.fill('//input[@placeholder="请输入密码"]', clientPassword)
        write_log_to_allure(f'输入密码:{clientPassword}')
        screenshot_to_allure(page, '输入密码')

    with allure.step('点击登录按钮'):
        page.click('//button[@type="submit"]')
        write_log_to_allure(f'点击页面登录按钮，进行登录')
        screenshot_to_allure(page, '点击登录按钮')
        sleep(1)

    with allure.step('获取登录页面滑块验证信息'):
        download_images(page, image_name="slider", frame_xpath="//iframe[@id='tcaptcha_iframe']", image_xpath="//img[@id='slideBlock']", save_directory='picture')
        download_images(page, image_name="background", frame_xpath="//iframe[@id='tcaptcha_iframe']", image_xpath="//img[@id='slideBg']", save_directory='picture')
        write_log_to_allure('下载滑块图片成功')
        position = dragbox_location(page)
        x = position['x'] + position['width'] / 2
        y = position['y'] + position['height'] / 2
        write_log_to_allure(f'开始计算滑块的中心点位置坐标，X坐标为：{x},Y坐标为：{y}')
        distance = get_slide_locus(get_slide_distance() * (280 / 680) + 6)
        write_log_to_allure(f'开始计算滑块滑动数据，滑动的距离列表为{distance}')

    with allure.step('滑动滑块验证'):
        page.mouse.move(x, y)
        page.mouse.down()
        sleep(0.2)
        for i in distance:
            x = x + i
            page.mouse.move(x, y)
        page.mouse.up()
        write_log_to_allure('开始移动滑块进行验证')
        screenshot_to_allure(page, '滑动滑块验证')
        sleep(2)

    with allure.step('验证是否登录成功'):
        assert_element_exist(page, "//a[contains(text(),'控制台')]")
        write_log_to_allure('控制台元素存在，登录成功，进入首页')
        screenshot_to_allure(page, '验证是否登录成功')


def management_login(page):
    '''
    登录管理端
    @param page:
    @return:
    '''
    with allure.step('打开管理端官网进入登录页'):
        page.goto(managementURL)
        write_log_to_allure(f'打开管理端官网:{managementURL},进入登录页面')
        screenshot_to_allure(page, '打开官网进入首页')

    with allure.step('输入用户名'):
        page.fill("//input[@placeholder='账号或手机号']", managementUsername)
        write_log_to_allure(f'输入用户名：{managementUsername}')
        screenshot_to_allure(page, '输入用户名')

    with allure.step('输入密码'):
        page.fill("//input[@placeholder='密码']", managementPassword)
        write_log_to_allure(f'输入用密码：{managementPassword}')
        screenshot_to_allure(page, '输入密码')

    with allure.step('点击登录按钮'):
        page.click('//button[@type="submit"]')
        write_log_to_allure('点击登录按钮,进行登录')
        screenshot_to_allure(page, '点击登录按钮')
        sleep(2)

    with allure.step('验证是否登录成功'):
        assert_element_exist(page, "//span[text()='首页']")
        write_log_to_allure('验证页面是否包含首页元素，首页元素存在，登录成功')
        screenshot_to_allure(page, '验证是否登录成功')


def purchase_server_number(page, active: int = 1, bind: int = 1, duration: int = 1, sums: str = "1"):
    '''
    购买差分账号
    @param page:page驱动
    @param active:激活方式
    @param bind:绑定方式
    @param duration:购买时长
    @param sums:购买数量
    @return:
    '''
    with allure.step('选择页面购买时长'):
        if duration == 1:
            page.click(ClientLiQingDetailsBase().purchaseDurationOneDayXpath())
            write_log_to_allure('选择购买时长为1天，选择成功')
        elif duration == 2:
            page.click(ClientLiQingDetailsBase().purchaseDurationOneMonthXpath())
            write_log_to_allure('选择购买时长为1个月，选择成功')
        elif duration == 3:
            page.click(ClientLiQingDetailsBase().purchaseDurationOneYearXpath())
            write_log_to_allure('选择购买时长为1年，选择成功')
        screenshot_to_allure(page, '购买时长选择成功')

    with allure.step('选择差分账号激活方式'):
        if active == 1:
            page.click(ClientLiQingDetailsBase().autoActiveMethodXpath())
            write_log_to_allure('选择自动激活方式成功')
        elif active == 2:
            page.click(ClientLiQingDetailsBase().manualActiveMethodXpath())
            write_log_to_allure('选择手动激活方式成功')
        screenshot_to_allure(page, '选择差分账号激活方式成功')

    with allure.step('选择差分账号绑定方式'):
        if bind == 1:
            page.click(ClientLiQingDetailsBase().autoBindMethodXpath())
            write_log_to_allure('选择自动激活方式成功')
        elif bind == 2:
            page.click(ClientLiQingDetailsBase().manualBindMethodXpath())
            write_log_to_allure('选择手动激活方式成功')
        screenshot_to_allure(page, '选择差分账号绑定方式成功')

    with allure.step('填写差分账号购买数量'):
        page.click(ClientLiQingDetailsBase().purchaseSumXpath())
        page.fill(ClientLiQingDetailsBase().purchaseSumXpath(), sums)
        write_log_to_allure(f'填写购买的差分账号数量，购买数量为{sums}，数量填写成功')
        screenshot_to_allure(page, '填写差分账号购买数量')

    with allure.step('点击立即购买'):
        page.click(ClientLiQingDetailsBase().purchaseButtonXpath())
        write_log_to_allure('点击立即购买按钮')
        screenshot_to_allure(page, '点击立即购买按钮')
        sleep(1)

    with allure.step('点击提交订单按钮，进入确认支付页面'):
        page.click(ClientLiQingDetailsBase().submitOrderButtonXpath())
        write_log_to_allure('点击提交订单按钮，进入确认支付页面')
        screenshot_to_allure(page, '点击提交订单按钮，进入确认支付页面')
        sleep(1)

    with allure.step('点击确认支付按钮，支付订单成功'):
        page.click('text=确认支付')
        write_log_to_allure('点击确认支付按钮，支付订单成功')
        screenshot_to_allure(page, '点击确认支付按钮，支付订单成功')
        sleep(1)

    with allure.step('判断是否支付成功'):
        assert_element_exist(page, ClientLiQingDetailsBase().paySuccessIdentificationXpath())
        write_log_to_allure('支付成功')
        screenshot_to_allure(page, '判断是否支付成功')


def expand_server_number(page, instanceId='9871524', duration=1, sums='5'):
    '''
    扩容差分账号
    @param page:
    @param instanceId: 实例Id
    @param duration: 扩容时长
    @param sums: 扩容数量
    @return:
    '''
    with allure.step('实例id输入框输入需要扩容的实例Id'):
        page.fill("//input[@placeholder='请输入']", instanceId)
        write_log_to_allure(f'输入实例Id:{instanceId}')
        screenshot_to_allure(page, f'输入实例Id:{instanceId}')

    with allure.step('点击查询按钮进行实例查询'):
        page.click("//button[1]")
        write_log_to_allure('点击查询按钮进行查询')
        screenshot_to_allure(page, '点击查询按钮进行查询')
        sleep(2)

    with allure.step('获取扩容前实例下差分账号个数'):
        number = page.query_selector("//td[text()='9871524']/following-sibling::td[7]").text_content()
        write_log_to_allure(f'实例下的差分账号数量为：{number}')

    with allure.step('点击实例的扩容按钮，进入扩容详情页面'):
        page.click("//a[text()='扩容']")
        write_log_to_allure('点击实例的扩容按钮，进入扩容详情页面')
        screenshot_to_allure(page, '点击实例的扩容按钮，进入扩容详情页面')
        sleep(2)


    with allure.step('扩容页面选择购买时长'):
        if duration == 1:
            page.click(ClientLiQingDetailsBase().purchaseDurationOneDayXpath())
            write_log_to_allure('选择购买时长为1天，选择成功')
        elif duration == 2:
            page.click(ClientLiQingDetailsBase().purchaseDurationOneMonthXpath())
            write_log_to_allure('选择购买时长为1个月，选择成功')
        elif duration == 3:
            page.click(ClientLiQingDetailsBase().purchaseDurationOneYearXpath())
            write_log_to_allure('选择购买时长为1年，选择成功')
        screenshot_to_allure(page, '购买时长选择成功')
