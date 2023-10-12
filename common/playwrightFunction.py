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

clientUsername = "18322369885"
clientPassword = "YANGyang022"
clientURL = "https://bss-front-uat.sixents.com"
clientUsername1 = "18322369889"
clientPassword1 = "YANGyang0223"
managementURL = "https://bss-backend-uat.sixents.com"
managementUsername = "test"
managementPassword = "liufenceshi123"
managementUsername1 = "testss"
managementPassword1 = "$Nbiud8po23%yf*FK"
expandInstanceId = "9871572"


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
    allure.attach(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  {text}', name='runlog', attachment_type=allure.attachment_type.TEXT)


def assert_element_exist(page, element):
    '''
    登录成功断言
    @param page:
    @param element:
    @return:
    '''
    sleep(1)
    assert page.locator(element).count() > 0, f'页面元素：{element}不存在,请检查页面/元素是否加载成功'


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


def client_login_fail(page):
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
        page.fill('//input[@placeholder="请输入密码"]', clientPassword1)
        write_log_to_allure(f'输入密码:{clientPassword1}')
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

    with allure.step('验证是否登录失败'):
        assert_element_exist(page, "//span[text()='密码错误！']")
        write_log_to_allure('验证是否登录失败')
        screenshot_to_allure(page, '验证是否登录失败')


def client_login_fail_username_no_exist(page):
    with allure.step('打开官网进入首页'):
        page.goto(clientURL)
        write_log_to_allure(f'打开官网{clientURL},进入首页成功')
        screenshot_to_allure(page, '打开官网进入首页')

    with allure.step('点击登录按钮'):
        page.click('//a[contains(text(),"登录")]')
        write_log_to_allure('点击页面左上角登录按钮，进入登录页面成功')
        screenshot_to_allure(page, '点击登录按钮进入登录页面')

    with allure.step('输入用户名'):
        page.fill('//input[@placeholder="请输入账号或手机号码"]', clientUsername1)
        write_log_to_allure(f'输入用户名:{clientUsername1}')
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

    with allure.step('验证是否登录失败,提示账号不存在'):
        assert_element_exist(page, "//span[text()='账号不存在！']")
        write_log_to_allure('验证是否登录失败,提示账号不存在')
        screenshot_to_allure(page, '验证是否登录失败,提示账号不存在')


def management_login_success(page):
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


def management_login_fail_password_mistake(page):
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
        page.fill("//input[@placeholder='密码']", managementPassword1)
        write_log_to_allure(f'输入用密码：{managementPassword1}')
        screenshot_to_allure(page, '输入密码')

    with allure.step('点击登录按钮'):
        page.click('//button[@type="submit"]')
        write_log_to_allure('点击登录按钮,进行登录')
        screenshot_to_allure(page, '点击登录按钮')
        sleep(2)

    with allure.step('验证是否登录失败-密码错误'):
        assert_element_exist(page, "//span[text()='密码错误！']")
        write_log_to_allure('验证页面是否包含密码错误元素，元素存在，登录失败')
        screenshot_to_allure(page, '验证是否登录失败-密码错误')


def management_login_fail_server_number_no_exist(page):
    '''
    登录管理端失败-账号不存在
    @param page:
    @return:
    '''
    with allure.step('打开管理端官网进入登录页'):
        page.goto(managementURL)
        write_log_to_allure(f'打开管理端官网:{managementURL},进入登录页面')
        screenshot_to_allure(page, '打开官网进入首页')

    with allure.step('输入用户名'):
        page.fill("//input[@placeholder='账号或手机号']", managementUsername1)
        write_log_to_allure(f'输入用户名：{managementUsername1}')
        screenshot_to_allure(page, '输入用户名')

    with allure.step('输入密码'):
        page.fill("//input[@placeholder='密码']", managementPassword1)
        write_log_to_allure(f'输入用密码：{managementPassword1}')
        screenshot_to_allure(page, '输入密码')

    with allure.step('点击登录按钮'):
        page.click('//button[@type="submit"]')
        write_log_to_allure('点击登录按钮,进行登录')
        screenshot_to_allure(page, '点击登录按钮')
        sleep(2)

    with allure.step('验证是否登录失败-账号不存在'):
        assert_element_exist(page, "//span[text()='该账号不存在 ']")
        write_log_to_allure('验证页面是否包含账号不存在元素，元素存在，登录失败')
        screenshot_to_allure(page, '验证是否登录失败-账号不存在')


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


def expand_server_number(page, instanceId='9871524', duration=2, sums='5'):
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
            page.click("//span[text()='天']")
            write_log_to_allure('选择购买时长为1天，选择成功')
        elif duration == 2:
            page.click("//span[text()='个月']")
            write_log_to_allure('选择购买时长为1个月，选择成功')
        elif duration == 3:
            page.click("//span[text()='年']")
            write_log_to_allure('选择购买时长为1年，选择成功')
        screenshot_to_allure(page, '购买时长选择成功')

    with allure.step('填写扩容数量'):
        page.fill("//input", sums)
        write_log_to_allure(f'输入的扩容数量为:{sums}')
        screenshot_to_allure(page, f'输入的扩容数量为:{sums}')

    with allure.step('点击提交扩容按钮，进入提交订单页面'):
        page.click("text=提交扩容")
        write_log_to_allure('点击提交扩容按钮，进入提交订单页面')
        screenshot_to_allure(page, '点击提交扩容按钮，进入提交订单页面')
        sleep(2)

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

    with allure.step('前往控制台页面'):
        page.click("//button[2]")
        write_log_to_allure('点击返回控制台按钮，进入控制台页面')
        screenshot_to_allure(page, '点击返回控制台按钮，进入控制台页面')
        sleep(2)

    with allure.step('点击控制台页面左侧导航栏服务号管理菜单'):
        page.click("//span[text()='服务号管理']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理菜单')
        screenshot_to_allure(page, '点击控制台页面左侧导航栏服务号管理菜单')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务'):
        page.click("//span[text()='厘米级服务']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务')
        screenshot_to_allure(page, '点击控制台页面左侧导航栏服务号管理-厘米级服务')

    with allure.step('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例'):
        page.click("//span[text()='实例']")
        write_log_to_allure('点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')
        screenshot_to_allure(page, '点击控制台页面左侧导航栏服务号管理-厘米级服务-实例')

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
        number1 = page.query_selector("//td[text()='9871524']/following-sibling::td[7]").text_content()
        write_log_to_allure(f'实例下的差分账号数量为：{number1}')
        print(f"扩容后的差分账号数量为：{number1}")

    assert int(number1) == int(number) + int(sums)


def click_step(page, describe, position, sleepTime: int = 0):
    '''
    点击步骤
    @param page:
    @param describe:
    @param position:
    @param sleepTime:
    @return:
    '''
    with allure.step(describe):
        page.click(position)
        write_log_to_allure(describe)
        screenshot_to_allure(page, describe)
        if sleepTime:
            sleep(sleepTime)


def fill_step(page, describe, position, number, sleepTime: int = 0):
    '''
    输入框输入数据步骤
    @param page:
    @param position:
    @param sums:
    @param sleepTime:
    @return:
    '''
    with allure.step(describe):
        page.fill(position, number)
        write_log_to_allure(describe)
        screenshot_to_allure(page, describe)
        if sleepTime:
            sleep(sleepTime)


def assert_step(page, describe, element):
    '''
    断言元素是否存在
    @param page:
    @param describe:
    @param element:
    @return:
    '''
    with allure.step(describe):
        assert_element_exist(page, element)
        write_log_to_allure(describe)
        screenshot_to_allure(page, describe)


def go_to_online_order_application_page(page, model: str = '1', where: str = '2'):
    '''
    线下订单申请进入不同类型的订单页面
    @param page:
    @param model: 模式  1：通用模式   2：累计模式
    @param where: 页面  1：新购页面   2：扩容页面   3：续费页面   4：试用转正式页面
    @return: 无返回
    '''
    management_login_success(page)
    click_step(page=page, describe='点击首页左侧导航栏【服务产品管理】，弹出下拉列表', position="//span[text()='服务产品管理']")
    click_step(page=page, describe='点击首页左侧导航栏【线下订单申请】，进入线下订单列表页面', position="//span[text()='线下订单申请']")
    click_step(page=page, describe='点击页面【新增申请】button，进入线下订单申请页面', position="//span[text()='新增申请']")
    if model == '1':
        click_step(page=page, describe='选择页面通用模式类型，进入通用模式线下订单申请页面', position="//div[text()='通用模式']")
    elif model == '2':
        click_step(page=page, describe='选择页面通用模式类型，进入累计模式线下订单申请页面', position="//div[text()='累计模式']")
    if where == '1':
        click_step(page=page, describe='选择订单类型，订单类型为新购', position="//span[text()=' 新购 ']")
    elif where == '2':
        click_step(page=page, describe='选择订单类型，订单类型为扩容', position="//span[text()=' 扩容 ']")
    elif where == '3':
        click_step(page=page, describe='选择订单类型，订单类型为续费', position="//span[text()=' 续费 ']")
    elif where == '4':
        click_step(page=page, describe='选择订单类型，订单类型为试用转正式', position="//span[text()=' 试用转正式 ']")


def select_product_type(page, type):
    '''
    选择产品类型
    @param page: 驱动
    @param type: 类型   1：厘清  2：分明  3：星璨
    @return:
    '''
    click_step(page=page, describe='点击页面服务产品选择框，弹出服务产品下拉选择列表', position="//div[text()='请选择']")
    if type == '1':
        click_step(page=page, describe='选择产品类型为厘清', position="//li[text()=' 厘清/Locate-CM ']")
    elif type == '2':
        click_step(page=page, describe='选择产品类型为分明', position="//li[text()=' 分明/Locate-DM ']")
    elif type == '3':
        click_step(page=page, describe='选择产品类型为星璨', position="//li[text()=' 星璨/Orion ']")


def select_test_period(page, testPeriod):
    '''
    选择是否具有测试期
    @param page: 驱动
    @param testPeriod:   True:具备测试期  False：不具备测试期
    @return:
    '''
    if testPeriod == False:
        click_step(page=page, describe='选择不需要测试激活', position="//span[text()=' 否 ']")
    elif testPeriod == True:
        click_step(page=page, describe='选择需要测试激活', position="//span[text()=' 是 ']")
        fill_step(page=page, describe='输入测试期时长为5天', position="//span[text()='天']/..//input", number='5')


def select_link_method(page, link):
    '''
    选择链接方式
    @param page: 驱动
    @param link: 链接方式  1：ntrip或SDK  2：ntrip  3：SDK
    @return:
    '''
    if link == '1':
        click_step(page=page, describe='选择连接方式为ntrip', position="//span[text()=' ntrip或SDK ']")
    elif link == '2':
        click_step(page=page, describe='选择连接方式为ntrip', position="//span[text()=' ntrip ']")
    elif link == '3':
        click_step(page=page, describe='选择连接方式为SDK', position="//span[text()=' SDK ']")


def select_active_method(page, active):
    '''
    选择激活方式
    @param page: 驱动
    @param active: 1：自动激活  2：手动激活
    @return:
    '''
    if active == '1':
        click_step(page=page, describe='选择激活方式为自动激活', position="//span[text()=' 自动激活 ']")
    elif active == '2':
        click_step(page=page, describe='选择激活方式为手动激活', position="//span[text()=' 手动激活 ']")


def select_bind_method(page, bind):
    '''
    选择绑定方法
    @param page:驱动
    @param bind:绑定方法 1：自动绑定  2：手动绑定
    @return:
    '''
    if bind == '1':
        click_step(page=page, describe='选择绑定方式为自动绑定', position="//span[text()=' 自动绑定 ']")
    elif bind == '2':
        click_step(page=page, describe='选择绑定方式为手动绑定', position="//span[text()=' 手动绑定 ']")


def select_active_time(page, time):
    '''
    选择激活时点
    @param page: 驱动
    @param time: 激活时点 1：非实时激活  2：实时激活  3：在截止日期前激活
    @return:
    '''
    if time == '1':
        click_step(page=page, describe='选择激活时点为非实时激活', position="//span[text()=' 非实时激活 ']")
    elif time == '2':
        click_step(page=page, describe='选择激活时点为实时激活', position="//span[text()=' 实时激活 ']")
    elif time == '3':
        click_step(page=page, describe='选择激活时点为在截止日期前激活', position="//span[text()=' 在截止日期前激活 ']")
        click_step(page=page, describe='点击日期选择框弹出日期选择页面', position="//span[text()=' 在截止日期前激活 ']//input")
        click_step(page=page, describe='选择截止日期为今天', position="//a[text()='今天']")


def select_purchase_duration(page, durationType, duration):
    '''
    填写购买时长
    @param page:
    @param durationType:
    @param duration:
    @return:
    '''
    click_step(page=page, describe='点击购买时长单位，弹出购买时长单位选择列表', position="//div[text()=' 年 ']")
    if durationType == '1':
        click_step(page=page, describe='选择购买时长单位为 年', position="//li[text()=' 年 ']")
        fill_step(page=page, describe=f'输入购买时长为：{duration}年', position="//label[text()='购买时长']/../following-sibling::div//input", number=duration)
    elif durationType == '2':
        click_step(page=page, describe='选择购买时长单位为 月', position="//li[text()=' 月 ']")
        fill_step(page=page, describe=f'输入购买时长为：{duration}月', position="//label[text()='购买时长']/../following-sibling::div//input", number=duration)
    elif durationType == '3':
        click_step(page=page, describe='选择购买时长单位为 天', position="//li[text()=' 天 ']")
        fill_step(page=page, describe=f'输入购买时长为：{duration}天', position="//label[text()='购买时长']/../following-sibling::div//input", number=duration)


def online_order_application_new_purchase_common_model(page,
                                                       CustomerNumber: str = '71268',
                                                       ServiceProduct: str = '1',
                                                       TestActive: bool = False,
                                                       LinkMethod: str = '1',
                                                       ActiveMethod: str = '1',
                                                       BindMethod: str = '1',
                                                       ActiveTime: str = '1',
                                                       PurchaseSums: str = '10',
                                                       PurchaseDurationType: str = '1',
                                                       PurchaseDuration: str = '1',
                                                       PurchasePrice: str = '1.8'
                                                       ):
    '''

    @param page: 浏览器驱动
    @param CustomerNumber:客户编号  默认：71268
    @param ServiceProduct:服务产品  1：厘清  2：分明  3：星璨
    @param TestActive:是否测试激活  True:测试激活  False:非测试激活
    @param LinkMethod:链接方式  1：ntrip或SDK  2：ntrip  3：SDK
    @param ActiveMethod:激活方法  1：自动激活  2：手动激活
    @param BindMethod:绑定方法  1：自动绑定  2：手动绑定
    @param ActiveTime:激活时点  1：非实时激活  2：实时激活  3：在截止日期前激活
    @param PurchaseSums:购买数量
    @param PurchaseDurationUnit:购买时长单位  1：天  2：月  3：年
    @param PurchaseDuration:购买时长
    @param PurchasePrice:购买价格
    @return:No return
    '''
    # 进入通用模式新购页面
    go_to_online_order_application_page(page)
    # 填写用户编号
    fill_step(page=page, describe=f'输入的用户编号为：{CustomerNumber}', position="//input[@id='userId']", number=CustomerNumber)
    # 选择产品类型
    select_product_type(page=page, type=ServiceProduct)
    # 选择测试期
    select_test_period(page=page, testPeriod=TestActive)
    # 选择链接方式
    select_link_method(page=page, link=LinkMethod)
    # 选择激活方式
    select_active_method(page=page, active=ActiveMethod)
    # 选择绑定方式
    select_bind_method(page=page, bind=BindMethod)
    # 选择激活时点
    select_active_time(page=page, time=ActiveTime)
    # 填写购买数量
    fill_step(page=page, describe=f'输入购买账号数量为：{PurchaseSums}个', position="//label[text()='购买数量']/../following-sibling::div//input", number=PurchaseSums)
    # 填写购买时长
    select_purchase_duration(page=page, durationType=PurchaseDurationType, duration=PurchaseDuration)
    # 输入购买价格
    fill_step(page=page, describe=f'输入购买价格为：{PurchasePrice}', position="//label[text()='购买价格']/../following-sibling::div//input", number=PurchasePrice)
    # 选择线下合同时间
    click_step(page=page, describe='点击线下合同时间的日期选择框弹出日期选择页面', position="//label[text()='线下合同时间']/../following-sibling::div//input")
    click_step(page=page, describe='选择截止日期为今天', position="//a[text()='今天']")
    # 输入销售人员名称
    fill_step(page=page, describe=f'输入销售人员名称为：yy测试', position="//label[text()='销售人员']/../following-sibling::div//input", number='yy测试')
    # 输入销售人员电话
    fill_step(page=page, describe=f'输入销售人员电话为：18322369885', position="//label[text()='销售人员电话']/../following-sibling::div//input", number='18322369885')
    # 输入备注
    fill_step(page=page, describe=f'输入备注信息为：这是UI测试申请', position="//textarea", number='这是UI测试申请')
    # 选择账号类型为内部测试账号
    click_step(page=page, describe='选择账号类型为内部测试账号', position="//span[text()=' 内部测试账号 ']")
    # 点击提交按钮
    click_step(page=page, describe='点击提交按钮，提交新购申请', position="//span[text()='提 交']")
    click_step(page=page, describe='点击确定提交申请', position="//span[text()='确 定']")
    # 获取订单号
    OrderNumber = page.query_selector("//tbody/tr[1]/td[1]").text_content()
    write_log_to_allure(f'线下订单申请的订单号为：{OrderNumber}')
    print(f"申请单编号为：{OrderNumber}")
    return OrderNumber


def online_order_application_expand_common_model(page,
                                                 CustomerNumber: str = '71268',
                                                 ServiceProduct: str = '1',
                                                 TestActive: bool = False,
                                                 ActiveTime: str = '1',
                                                 ExpandInstanceId: str = expandInstanceId,
                                                 PurchaseSums: str = '10',
                                                 PurchaseDurationType: str = '1',
                                                 PurchaseDuration: str = '1',
                                                 PurchasePrice: str = '1.7'
                                                 ):
    go_to_online_order_application_page(page, model='1', where='2')
    # 填写用户编号
    fill_step(page=page, describe=f'输入的用户编号为：{CustomerNumber}', position="//input[@id='userId']", number=CustomerNumber)
    # 选择产品类型
    select_product_type(page=page, type=ServiceProduct)
    # 选择测试期
    select_test_period(page=page, testPeriod=TestActive)
    # 选择激活时点
    select_active_time(page=page, time=ActiveTime)
    # 填写需要扩容的实例Id
    fill_step(page=page, describe=f'输入扩容实例：{ExpandInstanceId}', position="//input[@placeholder='请输入扩容的实例ID']", number=ExpandInstanceId)
    # 填写购买数量
    fill_step(page=page, describe=f'输入购买账号数量为：{PurchaseSums}个', position="//label[text()='购买数量']/../following-sibling::div//input", number=PurchaseSums)
    # 填写购买时长
    select_purchase_duration(page=page, durationType=PurchaseDurationType, duration=PurchaseDuration)
    # 输入购买价格
    fill_step(page=page, describe=f'输入购买价格为：{PurchasePrice}', position="//label[text()='购买价格']/../following-sibling::div//input", number=PurchasePrice)
    # 选择线下合同时间
    click_step(page=page, describe='点击线下合同时间的日期选择框弹出日期选择页面', position="//label[text()='线下合同时间']/../following-sibling::div//input")
    click_step(page=page, describe='选择截止日期为今天', position="//a[text()='今天']")
    # 输入销售人员名称
    fill_step(page=page, describe=f'输入销售人员名称为：yy测试', position="//label[text()='销售人员']/../following-sibling::div//input", number='yy测试')
    # 输入销售人员电话
    fill_step(page=page, describe=f'输入销售人员电话为：18322369885', position="//label[text()='销售人员电话']/../following-sibling::div//input", number='18322369885')
    # 输入备注
    fill_step(page=page, describe=f'输入备注信息为：这是UI测试申请-扩容订单', position="//textarea", number='这是UI测试申请')
    # 选择账号类型为内部测试账号
    click_step(page=page, describe='选择账号类型为内部测试账号', position="//span[text()=' 内部测试账号 ']")
    # 点击提交按钮
    click_step(page=page, describe='点击提交按钮，提交新购申请', position="//span[text()='提 交']")
    click_step(page=page, describe='点击确定提交申请', position="//span[text()='确 定']")
    # 获取订单号
    OrderNumber = page.query_selector("//tbody/tr[1]/td[1]").text_content()
    write_log_to_allure(f'线下订单申请的订单号为：{OrderNumber}')
    print(f"申请单编号为：{OrderNumber}")
    return OrderNumber


def review_online_order_application(page, OrderNumber):
    '''
    线下订单审核
    @param page:
    @param OrderNumber: 订单号
    @return:
    '''
    click_step(page=page, describe='点击首页左侧导航栏【财务管理】，弹出下拉列表', position="//span[text()='财务管理']")
    click_step(page=page, describe='点击首页左侧导航栏【线下订单审核】，进入线下订单审核页面', position="//span[text()='线下订单审核']")
    click_step(page=page, describe='点击搜索条件进行搜索条件切换', position="//div[@title='用户编号']")
    click_step(page=page, describe='切换搜索条件为申请单编号查询', position="//li[text()=' 申请单编号 ']")
    fill_step(page=page, describe=f'输入查询的申请单编号为：{OrderNumber}', position="//input[@placeholder='请输入']", number=OrderNumber)
    click_step(page=page, describe='点击查询按钮查询申请单', position="//span[text()='查 询']")
    click_step(page=page, describe=f'点击申请单列表编号为：{OrderNumber}的申请单详情按钮，进入详情页面', position="//a[text()=' 详情 ']")
    fill_step(page=page, describe='输入审核备注信息：UI测试订单', position="//textarea", number='UI测试订单')
    click_step(page=page, describe=f'点击提交按钮', position="//span[text()='提 交']")
    assert_step(page=page, describe='查看【操作成功】toast提示是否存在', element="//span[text()='操作成功']")
