import allure
from logs.log_config import log
from page.HomePage import HomePage
from page.LoginPage import LoginPage
from common.report_add_img import add_img_to_report


@allure.feature('客户端购买厘清账号')
class TestPurchaseLiqing():
    @allure.story('首页购买厘清账号，验证账号是否购买成功')
    @allure.description('首页购买厘清账号')
    def test_purchase_liqing_for_homepage(self, driver, url, username, password, active=1, bind=1, duration=1, sum=1):
        with allure.step('登录官网进入首页'):
            LoginPage().login(driver, url, username, password)
        with allure.step('点击首页厘清立即购买进入详情页面'):
            HomePage().move_to_liqing_title(driver)
            HomePage().click_liqing_homepage_purchase_button(driver)
            log.info('点击首页厘清立即购买进入详情页面')
            add_img_to_report(driver, '点击首页厘清立即购买进入详情页面')
        with allure.step('选择购买厘清账号种类'):
            if active == 1:
