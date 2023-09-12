# -*- coding=utf-8 -*-
# @Time : 2023/4/26 11:01
# @Author : yangyang
# @File : bss-ui/demo.py
from page.LoginPage import LoginPage
from page.ClientLiQingDetailPage import ClientLiQingDetailPage
from config.driver_config import DriverConfig
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def chrome_driver_config():
    '''
    谷歌浏览器驱动
    @return:返回谷歌浏览器驱动
    '''
    # global driver
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    # 无头模式
    # options.add_argument('--headless')
    # 设置窗口大小
    # options.add_argument("window-size=1920,1080")
    # 设置最大化窗口
    options.add_argument("--start-maximized")
    # 解决卡顿
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sanbox')
    options.add_argument('--disable-dev-shm-usage')
    # 增加浏览器型号
    # options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36')
    # 解决selenium无法访问https的问题
    options.add_argument('--allow-insecure-localhost')
    # 处理SSL证书错误问题
    options.add_argument('--ignore-ssl-errors')
    # 无痕模式
    options.add_argument('--incognito')
    # 去除chrome正受到自动测试软件的控制
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("detach", True)
    # 忽略无用的日志
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    # 实例化浏览器驱动
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(url=r'https://registry.npmmirror.com/-/binary/chromedriver',
                                            latest_release_url=r'https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE',
                                            cache_valid_range=30).install()), options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # 隐性等待时间
    driver.implicitly_wait(4)
    # 删除所有的cookies
    driver.delete_all_cookies()
    # 最大化窗口
    driver.maximize_window()
    return driver

if __name__ == '__main__':
    driver = chrome_driver_config()
    url = "https://bss-front-uat.sixents.com"
    username = 'test'
    password = 'liufentest123'
    duration = 1
    active = 1
    bind = 1
    sum = 1

    LoginPage().login(driver, url, username, password)
    ClientLiQingDetailPage().purchaseLiQing(driver, active, bind, duration, sum)

