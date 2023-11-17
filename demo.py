# -*- coding=utf-8 -*-
# @Time : 2023/4/26 11:01
# @Author : yangyang
# @File : bss-ui/demo.py

# from playwright.sync_api import sync_playwright
# from common.playwrightFunction import browser
from datetime import datetime, timedelta
from sqlite3 import Date

from dateutil.relativedelta import relativedelta
from common.playwrightFunction import client_login

# def browsers(sss):
#     browser = sss.chromium.launch(headless=False, args=["--start-maximized"])
#     context = browser.new_context(no_viewport=True)
#     page = context.new_page()
#     return page
#
#
# if __name__ == '__main__':
#     with sync_playwright() as p:
#         page = browsers(p)
#         page.goto("https://bss-front-uat.sixents.com")
#         page.click('//a[contains(text(),"登录")]')
#         page.fill('//input[@placeholder="请输入账号或手机号码"]', "18322369885")
#         page.fill('//input[@placeholder="请输入密码"]', "YANGyang022")
#         page.click('//button[@type="submit"]')
#
# page = browser()
# page.goto("https://bss-front-uat.sixents.com")
# page.click('//a[contains(text(),"登录")]')
# page.fill('//input[@placeholder="请输入账号或手机号码"]', "18322369885")
# page.fill('//input[@placeholder="请输入密码"]', "YANGyang022")
# page.click('//button[@type="submit"]')
# sleep(5)
# times = "2023-10-23 14:43:31"
# oo = "2023-10-23 14:41:30"
# print((datetime.strptime(times, "%Y-%m-%d %H:%M:%S") + timeplus).replace(hour=23, minute=59, second=59))
# print(datetime.strptime(times, "%Y-%m-%d %H:%M:%S").replace(hour=23, minute=59, second=59))
# TruthActiveTime = datetime.strptime(times, "%Y-%m-%d %H:%M:%S").replace(microsecond=0, second=0)
# ss = datetime.strptime(oo, "%Y-%m-%d %H:%M:%S").replace(microsecond=0, second=0)
# if TruthActiveTime == ss:
#     print()
# else:
#     NotADirectoryError
print(Date.now())