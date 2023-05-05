# -*- coding: utf-8 -*-
# @Time : 2023/3/26 22:30
# @Author : yangyang
# @File : 2222/ClientSliderVerificationPage.py
import json
import os
import cv2
import time
import random
import requests
import numpy as np
from selenium import webdriver
from base.ClientLoginBase import LoginBase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config.driver_config import DriverConfig
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ClientSliderVerificationPage():

    def onload_save_img(self, url, file_path):
        '''
        直接访问url加载图片并保存
        @param url: 图片url
        @param file_path: 图片保存地址
        @return:
        '''
        # 加载图片地址
        r1 = requests.get(url)
        # 打开文件路径
        with open(file_path, 'wb') as f:
            # wb存为二进制文件
            f.write(r1.content)

    def get_slide_locus(self, distance):
        '''
        获取滑动点，以列表形式输出
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

    def get_element_slide_distance(self, slider_ele, background_ele, correct=0):
        """
        根据传入滑块，和背景的节点，计算滑块的距离
        该方法只能计算 滑块和背景图都是一张完整图片的场景，
        如果背景图是通过多张小图拼接起来的背景图，
        该方法不适用，请使用get_image_slide_distance这个方法
        :param slider_ele: 滑块图片的节点
        :type slider_ele: WebElement
        :param background_ele: 背景图的节点
        :type background_ele:WebElement
        :param correct:滑块缺口截图的修正值，默认为0,调试截图是否正确的情况下才会用
        :type: int
        :return: 背景图缺口位置的X轴坐标位置（缺口图片左边界位置）
        """
        # 获取验证码的图片
        slider_url = slider_ele.get_attribute("src")
        background_url = background_ele.get_attribute("src")
        # 下载验证码背景图,滑动图片
        slider = "picture/slider.jpg"
        background = "picture/background.jpg"
        ClientSliderVerificationPage().onload_save_img(slider_url, slider)
        ClientSliderVerificationPage().onload_save_img(background_url, background)
        # 读取进行色度图片，转换为numpy中的数组类型数据，
        slider_pic = cv2.imread(slider, 0)
        print(slider_pic)
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

    def slide_verification(self, driver, slide_element, distance):
        """
        滑动滑块进行验证
        :param driver: driver对象
        :type driver:webdriver.Chrome
        :param slide_element: 滑块的元组
        :type slider_ele: WebElement
        :param distance:  滑动的距离
        :type: int
        :return:
        """
        # 获取滑动前页面的url地址
        # start_url = driver.current_url
        print("需要滑动的距离为：", distance)
        # 根据滑动距离生成滑动轨迹
        locus = self.get_slide_locus(distance)
        print("生成的滑动轨迹为:{}，轨迹的距离之和为{}".format(locus, distance))
        # 按下鼠标左键
        ActionChains(driver).click_and_hold(slide_element).perform()
        time.sleep(0.1)
        # 遍历轨迹进行滑动
        for loc in locus:
            # time.sleep(0.01)
            ActionChains(driver).move_by_offset(loc, random.randint(-5, 5)).perform()
            ActionChains(driver).context_click(slide_element)
        # 释放鼠标
        time.sleep(0.3)
        # ActionChains(driver).move_to_element_with_offset(to_element=slide_element, xoffset=22, yoffset=random.randint(-5, 5)).perform()
        ActionChains(driver).release(on_element=slide_element).perform()
        time.sleep(2)

    def get_3_ele(self, driver):
        '''
        切换到滑动图片框架中，返回图框，背景图，滑块三个元素
        @param browser:
        @return:
        '''
        # 4、模拟滑动验证
        # 4.1切换到滑动验证码的iframe中
        tcaptcha = driver.find_element('xpath', LoginBase().sliderVerificationIframeXpath())
        driver.switch_to.frame(tcaptcha)
        # 4.2 获取滑动相关的元素
        # 选择拖动滑块的节点
        drag_ele = driver.find_element('xpath', LoginBase().sliderButtonXpath())
        # 获取滑块图片的节点
        slideBlock_ele = driver.find_element('xpath', LoginBase().sliderPicXpath())
        # 获取缺口背景图片节点
        slideBg_ele = driver.find_element('xpath', LoginBase().sliderBackPicXpath())
        return drag_ele, slideBlock_ele, slideBg_ele

    def move_slider(self, driver, drag_ele, slideBlock_ele, slideBg_ele):
        '''
        移动滑块，滑动验证
        @param browser:
        @param drag_ele:
        @param slideBlock_ele:
        @param slideBg_ele:
        @return:
        '''
        # 4.3计算滑动距离
        sc = ClientSliderVerificationPage()
        distance = sc.get_element_slide_distance(slideBlock_ele, slideBg_ele)
        # 滑动距离误差校正，滑动距离*图片在网页上显示的缩放比-滑块相对的初始位置
        print("校正前的滑动距离", distance)
        # distance = distance * (280 / 680) - 22
        distance = distance * (280 / 680) + 6
        print("校正后的滑动距离", distance)
        # 4.4、进行滑动
        sc.slide_verification(driver, drag_ele, distance)
        # try:
        #     if driver.find_element('xpath', LoginBase().errorSliderWarning()):
        #         raise Exception('滑动失败，继续滑动')
        #         sc.slide_verification(driver, drag_ele, distance)



    def switch_to_frame(self, driver):
        '''
        切换进入滑块验证框架内
        @param driver: 驱动
        @return:
        '''
        driver.switch_to.frame(driver.find_element('xpath', LoginBase().sliderVerificationIframeXpath()))
